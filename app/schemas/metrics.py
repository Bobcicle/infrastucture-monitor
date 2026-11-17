from pydantic import BaseModel


class CpuMetrics(BaseModel):
    usage_percent: float
    logical_cores: int
    physical_cores: int | None


class MemoryMetrics(BaseModel):
    total: int
    available: int
    used: int
    usage_percent: float


class DiskMetrics(BaseModel):
    total: int
    used: int
    free: int
    usage_percent: float


class SystemMetrics(BaseModel):
    hostname: str
    operating_system: str
    platform: str
    uptime_seconds: float


class MetricsResponse(BaseModel):
    cpu: CpuMetrics
    memory: MemoryMetrics
    disk: DiskMetrics
    system: SystemMetrics