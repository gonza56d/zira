from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from pymessagebus import CommandBus

from zira.containers import Container
from zira.core.actions.transactions import GetUserCurrentPeriod
from zira.core.models import Period

router = APIRouter(
    prefix='transactions',
    tags=['transactions']
)


@router.get('/{user_id}')
@inject
async def get_user_current_period(
    user_id: str,
    command_bus: CommandBus = Provide[Container.command_bus]
):
    action = GetUserCurrentPeriod(user_id=user_id)
    result: Period = command_bus.handle(action)
    return {'message': 'Empty'}
