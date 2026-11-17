from app.schemas.host import HostCreate


hosts: dict[int, dict] = {}

next_host_id = 1


def create_host(host_data: HostCreate) -> dict:
    global next_host_id

    host = {
        "id": next_host_id,
        "hostname": host_data.hostname,
        "ip_address": str(host_data.ip_address),
        "operating_system": host_data.operating_system,
        "status": "unknown",
    }

    hosts[next_host_id] = host

    next_host_id += 1

    return host


def get_hosts() -> list[dict]:
    return list(hosts.values())


def get_host(host_id: int) -> dict | None:
    return hosts.get(host_id)


def delete_host(host_id: int) -> bool:
    return hosts.pop(host_id, None) is not None