import io
from celery import Celery
from fastapi import HTTPException
from minio import S3Error
from model.db import minio_client
from const import development_ip,redis_password
broker = f'redis://:{redis_password}@127.0.0.1:6379/10'  # 消息队列
backend = f'redis://:{redis_password}@127.0.0.1:6379/11'  # 存储结果
upload_file_app = Celery(
    'tasks',
    broker=broker,
    backend=backend,
)


# 上传文件的异步任务，通10
# 过输入对象键前缀，文件名，文件内容
@upload_file_app.task()
def upload_file(folder,filename,contents):
    try:
        object_prefix = folder  # 指定对象键前缀
        object_name = object_prefix + filename  # 构建对象键
        minio_client.put_object('main', object_name, io.BytesIO(contents), len(contents))  # 将文件内容上传到Minio存储桶中
    except S3Error as e:
        raise HTTPException(status_code=401, detail=f"Error: {e}")
