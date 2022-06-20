from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory, Singleton
from pymessagebus import CommandBus

from zira.core.actions.transactions import GetUserCurrentPeriod
from zira.core.handlers.transactions import GetUserCurrentPeriodHandler
from zira.repositories.relational import PostgresPeriodRepository


def make_command_bus(commands: dict) -> CommandBus:
    command_bus = CommandBus()
    for command in commands.items():
        command_bus.add_handler(*command)
    return command_bus


class Container(DeclarativeContainer):

    config = Configuration()

    period_repo = Singleton(PostgresPeriodRepository)

    get_user_current_period_handler = Factory(
        GetUserCurrentPeriodHandler,
        period_repo=period_repo
    )

    command_bus = make_command_bus({
        GetUserCurrentPeriod: get_user_current_period_handler,
    })
