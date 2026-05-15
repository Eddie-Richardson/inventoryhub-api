import datetime
from pydantic import BaseModel


class AssetBase(BaseModel):
    name: str
    sku: str
    category: str
    manufacturer: str
    model: str
    serial_number: str
    status: str
    location: str
    price: float
    purchase_date: datetime.date
    warranty_expiration: datetime.date
    assigned_to: str
    condition: str
    notes: str

class AssetCreate(AssetBase):
    pass

class AssetResponse(AssetBase):
    asset_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True

class AssetUpdate(BaseModel):
    name: str | None = None
    sku: str | None = None
    category: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    serial_number: str | None = None
    status: str | None = None
    location: str | None = None
    price: float | None = None
    purchase_date: datetime.date | None = None
    warranty_expiration: datetime.date | None = None
    assigned_to: str | None = None
    condition: str | None = None
    notes: str | None = None