from fastapi import APIRouter


router = APIRouter(
    prefix='users',
    tags=['users']
)


@router.get('/')
async def users():
    return {'message': 'Empty'}
