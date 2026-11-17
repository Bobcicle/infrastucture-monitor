from pydantic import BaseModel, ConfigDict, Field, IPvAnyAddress


class HostCreate(BaseModel):
    hostname: str = Field(min_length=1, max_length=255)
    ip_address: IPvAnyAddress
    operating_system: str = Field(min_length=1, max_length=100)


class HostResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    hostname: str
    ip_address: IPvAnyAddress
    operating_system: str
    status: str