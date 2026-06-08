from fastapi import APIRouter
from services.list_s3 import list_s3_buckets
from services.list_instances import list_ec2_instances

router = APIRouter()
@router.get("/s3")
def list_s3():
    return list_s3_buckets()

@router.get("/ec2")
def list_ec2():
    return list_ec2_instances()