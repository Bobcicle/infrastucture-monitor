import platform
import socket
import time

import psutil

from app.schemas.metrics import (
    CpuMetrics,
    DiskMetrics,
    MemoryMetrics,
    MetricsResponse,
    SystemMetrics,
)


def get_cpu_metrics() -> CpuMetrics:
    return CpuMetrics(
        usage_percent=psutil.cpu_percent(interval=1),
        logical_cores=psutil.cpu_count(logical=True) or 0,
        physical_cores=psutil.cpu_count(logical=False),
    )


def get_memory_metrics() -> MemoryMetrics:
    memory = psutil.virtual_memory()

    return MemoryMetrics(
        total=memory.total,
        available=memory.available,
        used=memory.used,
        usage_percent=memory.percent,
    )


def get_disk_metrics() -> DiskMetrics:
    disk = psutil.disk_usage("/")

    return DiskMetrics(
        total=disk.total,
        used=disk.used,
        free=disk.free,
        usage_percent=disk.percent,
    )


def get_system_metrics() -> SystemMetrics:
    boot_time = psutil.boot_time()
    uptime = time.time() - boot_time

    return SystemMetrics(
        hostname=socket.gethostname(),
        operating_system=platform.system(),
        platform=platform.platform(),
        uptime_seconds=uptime,
    )


def collect_metrics() -> MetricsResponse:
    return MetricsResponse(
        cpu=get_cpu_metrics(),
        memory=get_memory_metrics(),
        disk=get_disk_metrics(),
        system=get_system_metrics(),
    )