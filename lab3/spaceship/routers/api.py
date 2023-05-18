from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World! It is Alex Tkachenko from IM-11'}