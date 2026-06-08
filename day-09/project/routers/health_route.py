from fastapi import APIRouter
from services.health import get_metrics
router = APIRouter()

@router.get("/health")
def fetch_metrics():
    try:
        metrics_data = get_metrics()
        return metrics_data
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )