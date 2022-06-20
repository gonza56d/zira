from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from pymessagebus import CommandBus

from zira.containers import Container

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
@inject
async def users(
    command_bus: CommandBus = Provide[Container.command_bus]
) -> dict:
    return {'message': 'Empty'}
