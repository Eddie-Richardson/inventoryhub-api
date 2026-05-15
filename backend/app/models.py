import datetime
from sqlalchemy import Integer, Column, String, Numeric, Date, DateTime
from sqlalchemy.dialects.oracle import NUMBER

from database import Base

class Asset(Base):
    __tablename__ = "assets"
    asset_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    sku = Column(String)
    category = Column(String)
    manufacturer = Column(String)
    model = Column(String)
    serial_number = Column(String, unique=True)
    status = Column(String)
    location = Column(String)
    timestamp = Column(DateTime)
    price = Column(Numeric)
    purchase_date = Column(Date)
    warranty_expiration = Column(Date)
    assigned_to = Column(String)
    condition = Column(String)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)