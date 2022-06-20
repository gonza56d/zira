from datetime import date, datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel


class Spending(BaseModel):

    id: UUID
    time: datetime
    amount: float
    daily_id: UUID


class Daily(BaseModel):

    id: UUID
    date: date
    period_id: UUID
    spendings: List[Spending]
    spendings_amount: float


class Period(BaseModel):

    id: UUID
    date_from: date
    date_to: date
    budget: float
    dailies: List[Daily]
    current_balance: float
    dailies_spendings_amount: float
    max_daily_spend: float
    total_days: int
    days_left: int
    current_days: int
    active: bool
