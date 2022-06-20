from dataclasses import dataclass
from uuid import UUID


@dataclass
class GetUser:

    user_id: UUID
