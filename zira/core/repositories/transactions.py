from abc import ABC, abstractmethod
from uuid import UUID

from zira.core.models import Period


class PeriodRepository(ABC):

    @abstractmethod
    def get_current_by_user_id(self, user_id: UUID) -> Period:
        pass
