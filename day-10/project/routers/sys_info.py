from fastapi import APIRouter, HTTPException
from services.about import get_info

router = APIRouter()

@router.get("/sysinfo",status_code=200)
def system_info():
    try:
        return get_info()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )
