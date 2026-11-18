from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.host import Host
from app.schemas.host import HostCreate


def create_host(db: Session, host_data: HostCreate) -> Host:
    host = Host(
        hostname=host_data.hostname,
        ip_address=str(host_data.ip_address),
        operating_system=host_data.operating_system,
        status="unknown",
    )

    db.add(host)
    db.commit()
    db.refresh(host)

    return host


def get_hosts(db: Session) -> list[Host]:
    statement = select(Host).order_by(Host.id)

    return list(db.scalars(statement).all())


def get_host(db: Session, host_id: int) -> Host | None:
    return db.get(Host, host_id)


def delete_host(db: Session, host_id: int) -> bool:
    host = db.get(Host, host_id)

    if host is None:
        return False

    db.delete(host)
    db.commit()

    return True