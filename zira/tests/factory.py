from datetime import date, datetime, timedelta
from random import randint
from time import sleep
from uuid import uuid4

from zira.core.models import Daily, Period, Spending


class Factory:

    @staticmethod
    def period(**kwargs) -> Period:
        self_id = kwargs.get('id', uuid4())
        date_from = kwargs.get('date_from', date.today() - timedelta(days=6))
        date_to = kwargs.get('date_to', date.today() + timedelta(days=6))

        dailies = []
        for days in range((date_to - date_from).days + 1):
            daily_id = kwargs.get('daily_id', uuid4())
            _date = date(
                year=date_from.year,
                month=date_from.month,
                day=date_from.day + days
            )
            spendings = []
            for x in range(randint(1, 6)):
                spendings.append(Factory.spending(
                    daily_id=daily_id,
                    time=datetime.now() - timedelta(hours=x)
                ))
            dailies.append(Factory.daily(
                id=daily_id,
                date=_date,
                period_id=self_id,
                spendings=spendings
            ))

        return Period(
            id=self_id,
            date_from=date_from,
            date_to=date_to,
            budget=kwargs.get(
                'budget',
                float(f'{randint(10000, 100000)}.{randint(0, 99)}')
            ),
            dailies=kwargs.get('dailies', dailies),
            user_id=kwargs.get('user_id', uuid4())
        )

    @staticmethod
    def daily(**kwargs) -> Daily:
        self_id = kwargs.get('id', uuid4())
        self_date = kwargs.get('date', date.today())
        now = datetime.now()
        return Daily(
            id=self_id,
            date=self_date,
            period_id=kwargs.get('period_id', uuid4()),
            spendings=kwargs.get(
                'spendings',
                [
                    Factory.spending(
                        time=datetime(
                            year=self_date.year,
                            month=self_date.month,
                            day=self_date.day,
                            hour=now.hour,
                            minute=now.minute,
                            second=now.second
                        ),
                        daily_id=self_id
                    ) for x in range(6)
                ]
            )
        )

    @staticmethod
    def spending(**kwargs) -> Spending:
        return Spending(
            id=kwargs.get('id', uuid4()),
            time=kwargs.get('time', datetime.now()),
            amount=kwargs.get(
                'amount',
                float(f'{randint(1, 1000)}.{randint(0, 99)}')
            ),
            daily_id=kwargs.get('daily_id', uuid4())
        )
