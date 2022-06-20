from datetime import date, datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel

from zira.core.models import Period


class SpendingSchema(BaseModel):

    id: UUID
    time: datetime
    amount: float
    daily_id: UUID


class DailySchema(BaseModel):

    id: UUID
    date: date
    period_id: UUID
    spendings: List[SpendingSchema]
    spendings_amount: float


class PeriodSchema(BaseModel):

    id: UUID
    date_from: date
    date_to: date
    budget: float
    dailies: List[DailySchema]
    current_balance: float
    dailies_spendings_amount: float
    max_daily_spend: float
    total_days: int
    days_left: int
    current_days: int
    active: bool

    @staticmethod
    def dump(period: Period):
        return PeriodSchema(

        )
