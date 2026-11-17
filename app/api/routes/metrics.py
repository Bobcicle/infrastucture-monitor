from fastapi import APIRouter

from app.schemas.metrics import MetricsResponse
from app.services.metrics_service import collect_metrics


router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
)


@router.get(
    "",
    response_model=MetricsResponse,
)
def get_metrics():
    return collect_metrics()