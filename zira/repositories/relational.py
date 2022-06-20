from uuid import UUID

from zira.core.models import Period
from zira.core.repositories.transactions import PeriodRepository


class PostgresPeriodRepository(PeriodRepository):

    def get_current_by_user_id(self, user_id: UUID) -> Period:
        pass
