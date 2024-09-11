from typing import Optional, List

from pydantic import BaseModel
from enum import Enum


class StatusEnum(Enum):
    SENT = "sent"
    PENDING = "pending"
    FAILED = "failed"


class NotificationRequest(BaseModel):
    current_price_bitcoin: float
    daily_percentage_change: float
    trading_volume: float
    day_high: float
    day_low: float
    email_ids: List[str]
    status: Optional[str] = "pending"
