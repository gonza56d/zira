from datetime import date, datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel

from zira.core.models.currency import Decimal


class Transaction:

    @staticmethod
    def rounded(number: Decimal) -> float:
        return round(float(number), 2)


class Spending(BaseModel, Transaction):

    id: UUID
    time: datetime
    amount: Decimal
    daily_id: UUID


class Daily(BaseModel, Transaction):

    id: UUID
    date: date
    period_id: UUID
    spendings: List[Spending]

    @property
    def spendings_amount(self) -> Decimal:
        amount = Decimal(0)
        for spending in self.spendings:
            amount += Decimal(spending.amount)
        return amount


class Period(BaseModel, Transaction):

    id: UUID
    date_from: date
    date_to: date
    budget: Decimal
    dailies: List[Daily]

    @property
    def current_balance(self) -> Decimal:
        return (
            self.max_daily_spend
            * self.current_days
            - self.dailies_spendings_amount
        )

    @property
    def dailies_spendings_amount(self) -> Decimal:
        amount = Decimal(0)
        for daily in self.dailies:
            amount += daily.spendings_amount
        return amount

    @property
    def max_daily_spend(self) -> Decimal:
        return self.budget / self.total_days

    @property
    def total_days(self) -> int:
        timedelta = self.date_to - self.date_from
        return timedelta.days + 1

    @property
    def days_left(self) -> int:
        timedelta = self.date_to - date.today()
        return timedelta.days + 1

    @property
    def current_days(self) -> int:
        timedelta = date.today() - self.date_from
        return timedelta.days

    @property
    def active(self) -> bool:
        return self.days_left >= 0
