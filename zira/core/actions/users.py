from uuid import UUID

from pydantic import BaseModel


class GetUser(BaseModel):

    user_id: UUID
