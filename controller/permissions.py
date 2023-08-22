from fastapi import APIRouter, Depends, FastAPI, Request, HTTPException
import json

import type.permissions
from service.permissions import roleModel
from utils.response import standard_response
from utils.auth_permission import auth_permission

permissions_router = APIRouter()


@permissions_router.post("/add")  # 创建角色
async def add(data: type.permissions.role_base, user=Depends(auth_permission)):
    db = roleModel()
    return {"new_role": db.get_role_info_by_id(db.create(data))}


@permissions_router.post("/delete")  # 删除角色
@standard_response
async def delete(data: str):
    db = roleModel()
    return {"status": db.delete(data)}


@permissions_router.post("/attribute_role")  # 分配用户角色
async def attribute_role(data: type.permissions.attribute_role_base):
    db = roleModel()
    return {"attribute_role": db.get_user_role_info_by_id(db.attribute_user_role(data))}


@permissions_router.post("/attribute_privilege")  # 为角色添加权限
@standard_response
async def attribute_privilege(data: type.permissions.attribute_privilege_base):
    db = roleModel()
    return {"status": db.attribute_privilege(data)}


@permissions_router.post("/test")
@standard_response
async def test(request: Request):
    db = roleModel()
    user_id = int(request.headers.get("user_id"))
    role_list = db.search_role_by_user(user_id)
    return {"role": role_list}


@permissions_router.post("/auth_privilege")  # 权限验证
@standard_response
async def auth_privilege(request: Request):
    db = roleModel()
    user_id = int(request.headers.get("user_id"))
    # user = auth_login(request)
    permission_key = request.url.path
    permission = None
    role_list = db.search_role_by_user(user_id)
    privilege_set = db.search_privilege_by_role(role_list)
    json_string = json.dumps(list(privilege_set))
    permission = db.check_permission(permission_key, privilege_set)
    if not permission:
        raise HTTPException(
            status_code=403,
            detail="No permission",
        )
    return {"privilege": json_string}


@permissions_router.post("/work_id")  # 返回业务id
@standard_response
async def return_work_id(request: Request):
    db = roleModel()
    user_id = int(request.headers.get("user_id"))
    role_list = db.search_role_by_user(user_id)
    work_list = db.search_work_by_role(role_list)
    json_string = json.dumps(work_list)
    return {"work_id": json_string}


@permissions_router.post("/search_service_id")  # 返回业务id
@standard_response
async def return_service_id(request: Request, data: type.permissions.Return_Service_Id):
    db = roleModel()
    user_id = int(request.headers.get("user_id"))
    permission_key = request.url.path
    permission = None
    role_list = db.search_role_by_user(user_id)
    service_id = db.search_service_id(role_list, data.service_type, data.name)
    return {"service_id": service_id}


@permissions_router.post("/search_user_id")  # 返回用户id
@standard_response
async def return_user_id(request: Request, data: type.permissions.Return_User_Id):
    db = roleModel()
    permission_key = request.url.path
    permission = None
    user_list = db.search_user_id_by_service(data.service_type, data.service_id)
    return {"user_id": user_list}
