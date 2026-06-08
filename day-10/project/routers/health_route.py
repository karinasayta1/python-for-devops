from fastapi import APIRouter,HTTPException
from services.health import get_health

router = APIRouter()

@router.get("/health",status_code=200)
def health_check(cpu_threshold: float= 50.0, mem_threshold: float = 50.0, disk_threshold: float = 50.0):
    try:
        return get_health(cpu_threshold, mem_threshold, disk_threshold)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )
