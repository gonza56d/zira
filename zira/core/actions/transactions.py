from dataclasses import dataclass
from uuid import UUID


@dataclass
class GetUserCurrentPeriod:

    user_id: UUID
