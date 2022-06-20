from dataclasses import dataclass

from zira.core.actions.transactions import GetUserCurrentPeriod
from zira.core.models import Period
from zira.core.repositories.transactions import PeriodRepository


@dataclass
class GetUserCurrentPeriodHandler:

    period_repo: PeriodRepository

    def __call__(self, action: GetUserCurrentPeriod) -> Period:
        period = self.period_repo.get_current_by_user_id(action.user_id)
        return period
