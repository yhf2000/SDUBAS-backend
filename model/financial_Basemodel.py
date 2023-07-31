from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, validator, constr


class ResourceAdd(BaseModel):  # 资源添加请求体
    Id: int = None
    name: constr(strip_whitespace=True, min_length=1)  # 字符串类型的字段，去除首尾空格，最小长度为1
    count: int = Field(..., gt=0)  # 整数类型的字段，必须大于0
    state: int = 1  # 是否可用，这部分不确定，应该自动填入1


class ResourceDelete(BaseModel):
    id: int = Field(..., gt=0)  # 整数类型的字段，必须大于0


class FinancialUpdate(BaseModel):  # 修改note时输入，可添加过滤条件
    note: str  # 输入即可


class FinancialAdd(BaseModel):  # 添加资金项目填入
    Id: int = None  # 整数类型的字段，默认为None
    name: str = Field(..., strip_whitespace=True, min_length=1)  # 字符串类型的字段，不能全为空格，长度至少为1
    note: str = None  # 文本类型的字段，默认为None


class AmountAdd(BaseModel):  # 添加流水填入
    finance_id: int = Field(..., gt=0)  # 非空整数类型的字段，要求大于零，其实可不需要，但是输入处理起来简单，所以尽量输入吧
    state: int = Field(..., ge=0, le=1)  # 整数类型的字段，要求为0或1
    amount: int = Field(..., gt=0)  # 整数类型的字段，要求大于零
    log_content: str  # 字符串类型的字段，默认为None
    log_file_id: int = None  # 整数类型的字段，默认为None


class pageRequest(BaseModel):
    pn: int = Field(..., gt=0)
    pg: int = Field(..., gt=0)


class page(BaseModel):  # 定义的分页类
    pageSize: int = Field(..., gt=0)
    pageNow: int = Field(..., gt=0)

    def offset(self):
        return (max(1, self.pageNow) - 1) * self.pageSize

    def limit(self):
        return self.pageSize


class pageResult(BaseModel):  # 分页结果类
    pageIndex: int
    pageSize: int
    totalNum: int
    rows: List


class resource_count_update(BaseModel):
    count: int = Field(..., gt=0)


class ApplyBody(BaseModel):
    id: int = Field(..., gt=0)
    count: int = Field(..., gt=0)
    begintime: datetime
    endtime: datetime