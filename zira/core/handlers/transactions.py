from dataclasses import dataclass

from zira.core.actions.transactions import GetUserCurrentPeriod
from zira.core.models import Period


@dataclass
class GetUserCurrentPeriodHandler:

    def __call__(self, action: GetUserCurrentPeriod) -> Period:
        pass
