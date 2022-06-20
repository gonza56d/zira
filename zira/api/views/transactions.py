from fastapi import APIRouter


router = APIRouter(
    prefix='transactions',
    tags=['transactions']
)


@router.get('/{user_id}')
async def get_user_current_period(user_id: str):
    return {'message': 'Empty'}
