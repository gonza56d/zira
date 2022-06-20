from datetime import date, datetime, timedelta
from random import randint
from typing import List
from unittest import TestCase
from uuid import uuid4

from parameterized import parameterized

from zira.core.models import Daily, Period, Spending
from zira.core.models.currency import Decimal
from zira.tests.factory import Factory


class TestPeriodExamples(TestCase):

    def setUp(self):
        self.period_id = uuid4()
        self.today = date.today()

    def create_period(
        self,
        max_daily_spend: Decimal,
        current_days: int,
        dailies_spendings_amount: Decimal
    ) -> Period:

        dailies: List[Daily] = []
        daily_spending = dailies_spendings_amount / current_days

        for day in range(current_days):
            daily_id = uuid4()
            daily_date = date.today() - timedelta(days=day)
            spendings: List[Spending] = []

            spendings_quantity = randint(1, 6)
            for x in range(spendings_quantity):
                spendings.append(
                    Factory.spending(
                        time=datetime(
                            year=daily_date.year,
                            month=daily_date.month,
                            day=daily_date.day,
                            hour=datetime.now().hour + x,
                            minute=datetime.now().minute,
                            second=datetime.now().second
                        ),
                        daily_id=daily_id,
                        amount=daily_spending / spendings_quantity
                    )
                )

            dailies.append(
                Factory.daily(
                    id=daily_id,
                    date=daily_date,
                    period_id=self.period_id,
                    spendings=spendings
                )
            )

        date_from = date.today() - timedelta(days=current_days)
        date_to = date.today() + timedelta(days=current_days)
        total_days = (date_to - date_from).days + 1

        return Factory.period(
            id=self.period_id,
            date_from=date_from,
            date_to=date_to,
            budget=max_daily_spend * total_days,
            dailies=dailies
        )

    @parameterized.expand([
        (Decimal(1000.00), 5, Decimal(5500.50)),
        (Decimal(800.50), 8, Decimal(6150.30)),
        (Decimal(1250.00), 4, Decimal(500.00)),
    ])
    def test_period_current_balance(
        self,
        max_daily_spend: Decimal,
        current_days: int,
        dailies_spendings_amount: Decimal
    ):
        """
        Ensure that periods can calculate their balance properly.

        - Given a period with max_daily_spending=x.
        - When the days passed are y and its dailies have spent z.
        - Then the current balance is x*y-z.
        """
        expected_current_balance = (
            max_daily_spend
            * current_days
            - dailies_spendings_amount
        )

        period = self.create_period(
            max_daily_spend,
            current_days,
            dailies_spendings_amount
        )

        assert (
            period.rounded(period.current_balance)
            ==
            round(float(expected_current_balance), 2)
        )

    @parameterized.expand([
        (Decimal(1000.00), 5, Decimal(5500.50)),
        (Decimal(800.50), 8, Decimal(6150.30)),
        (Decimal(1250.00), 4, Decimal(500.00)),
    ])
    def test_period_dailies_spendings_amount(
        self,
        max_daily_spend: Decimal,
        current_days: int,
        dailies_spendings_amount: Decimal
    ):
        """
        Ensure that periods can calculate their total daily spends.

        - Given a period with n dailies.
        - When each daily has x of spending.
        - Then the period.dailies_spendings_amount is n*x.
        """
        expected_dailies_spendings_amount = dailies_spendings_amount

        period = self.create_period(
            max_daily_spend,
            current_days,
            dailies_spendings_amount
        )

        assert (
            period.rounded(period.dailies_spendings_amount)
            ==
            round(float(expected_dailies_spendings_amount), 2)
        )

    @parameterized.expand([
        (Decimal(1000.00), 5, Decimal(5500.50)),
        (Decimal(800.50), 8, Decimal(6150.30)),
        (Decimal(1250.00), 4, Decimal(500.00)),
    ])
    def test_max_daily_spend(
        self,
        max_daily_spend: Decimal,
        current_days: int,
        dailies_spendings_amount: Decimal
    ):
        """
        Ensure that periods can calculate the max to spend per day.

        - Given a period with y days of duration.
        - When the budget is x.
        - Then the max_daily_spend is x / y.
        """
        expected_max_daily_spend = max_daily_spend

        period = self.create_period(
            max_daily_spend, current_days, dailies_spendings_amount
        )

        assert (
            period.rounded(period.max_daily_spend)
            ==
            round(float(expected_max_daily_spend), 2)
        )
