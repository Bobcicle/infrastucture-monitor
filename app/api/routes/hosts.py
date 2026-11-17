from fastapi import APIRouter, HTTPException, status

from app.schemas.host import HostCreate, HostResponse
from app.services import host_service


router = APIRouter(
    prefix="/hosts",
    tags=["Hosts"],
)


@router.post(
    "",
    response_model=HostResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_host(host_data: HostCreate):
    return host_service.create_host(host_data)


@router.get(
    "",
    response_model=list[HostResponse],
)
def list_hosts():
    return host_service.get_hosts()


@router.get(
    "/{host_id}",
    response_model=HostResponse,
)
def retrieve_host(host_id: int):
    host = host_service.get_host(host_id)

    if host is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Host not found",
        )

    return host


@router.delete(
    "/{host_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def remove_host(host_id: int):
    deleted = host_service.delete_host(host_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Host not found",
        )