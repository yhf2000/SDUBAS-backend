import re

privilege_dict = dict()
privilege_dict['/projects/'] = '新建项目'
privilege_dict['/projects/update/'] = '项目编辑'
privilege_dict['/projects/delete/'] = '项目删除'
privilege_dict['/projects/list'] = '项目查看'
privilege_dict['/projects/get/'] = '项目查看'
privilege_dict['/projects/contents/'] = '项目查看'
privilege_dict['/projects//contents/'] = '项目查看'
privilege_dict['/projects/credits/'] = '项目学分认定'
privilege_dict['/projects/submissions//contents/'] = '项目编辑'
privilege_dict['/projects/scores//contents/'] = '项目批阅'
privilege_dict['/projects/submit//contents/'] = '项目提交'
privilege_dict['/projects/members/'] = '项目批阅'
privilege_dict['/projects/progress/'] = '项目提交'
privilege_dict['/projects/score/'] = '项目提交'
privilege_dict['/projects/project/type'] = '项目查看'
privilege_dict['/projects/content/submission/'] = '项目提交'
privilege_dict['/projects/renew//content'] = '项目编辑'
privilege_dict['/projects/user/credits'] = '项目学分认定'
privilege_dict['/projects//user/score/all'] = '项目提交'
privilege_dict['/projects/user/credits/all'] = '项目学分认定'
privilege_dict['/projects/content///score/all'] = '项目批阅'
privilege_dict['/projects/delete_user_in_project///'] = '项目编辑'
privilege_dict['/projects/add_user_in_project/'] = '项目编辑'
privilege_dict['/resources/resource'] = '新建资源'
privilege_dict['/resources/resource/view'] = '资源查看'
privilege_dict['/resources/resource/'] = '资源修改'
privilege_dict['/resources/resource/get/'] = '资源查看'
privilege_dict['/resources/resource/apply/'] = '资源申请'
privilege_dict['/resources/resource/application/'] = '资源查看'
privilege_dict['/resources/resource/ifapply/'] = '资源审批'
privilege_dict['/resources/resource/approve/'] = '资源审批'
privilege_dict['/resources/resource///approve'] = '资源审批'
privilege_dict['/resources/resource///refuse'] = '资源审批'
privilege_dict['/resources/resource//delete'] = '资源删除'
privilege_dict['/resources/financial'] = '管理资金'
privilege_dict['/resources/financial//account'] = '管理资金'
privilege_dict['/resources/financial//amount'] = '管理资金'
privilege_dict['/resources/financial//accountbook'] = '查看资金'
privilege_dict['/resources/financial//delete'] = '管理资金'
privilege_dict['/resources/financial//'] = '管理资金'
privilege_dict['/resources/financial//revise'] = '管理资金'
privilege_dict['/resources/financial/search'] = '管理资金'
privilege_dict['/users/user_add'] = '新建用户'
privilege_dict['/users/user_add_batch'] = '新建用户'
privilege_dict['/users/user_view'] = '用户管理'
privilege_dict['/users/user_add'] = '添加用户'
privilege_dict['/users//user_delete'] = '用户管理'
privilege_dict['/users//user_ban'] = '用户管理'
privilege_dict['/users//user_relieve'] = '用户管理'
privilege_dict['/educations/school_add'] = '添加学校'
privilege_dict['/educations/school_view'] = '添加学校'
privilege_dict['/educations//school_delete'] = '学校管理'
privilege_dict['/educations//school_update'] = '学校管理'
privilege_dict['/educations/college_add'] = '添加学院'
privilege_dict['/educations//college_delete'] = '学院管理'
privilege_dict['/educations/college_view'] = '学院管理'
privilege_dict['/educations//college_update'] = '学员管理'
privilege_dict['/educations/major_add'] = '添加专业'
privilege_dict['/educations//major_delete'] = '专业管理'
privilege_dict['/educations/major_view'] = '专业管理'
privilege_dict['/educations//major_update'] = '专业管理'
privilege_dict['/educations/class_add'] = '添加班级'
privilege_dict['/educations//class_delete'] = '班级管理'
privilege_dict['/educations//class_update'] = '班级管理'
privilege_dict['/educations/class_view'] = '班级管理'
privilege_dict['/educations/user_add_education'] = '添加用户'
privilege_dict['/permissions/add_default_role_for_user'] = '添加用户'
