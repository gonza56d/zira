from pydantic.dataclasses import dataclass as pydantic_dataclass

from zira.core.models import Daily, Period, Spending


DailySchema = pydantic_dataclass(Daily)
PeriodSchema = pydantic_dataclass(Period)
SpendingSchema = pydantic_dataclass(Spending)
