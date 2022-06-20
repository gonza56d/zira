from uuid import UUID

from pydantic import BaseModel


class GetUserCurrentPeriod(BaseModel):

    user_id: UUID
