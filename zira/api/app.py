from fastapi import FastAPI
from zira.api.views.transactions import router as transactions_router
from zira.api.views.users import router as users_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(transactions_router)
    app.include_router(users_router)
    return FastAPI()
