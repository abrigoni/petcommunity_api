from fastapi import APIRouter

from app.api.v1 import kind, breeds, alert_type, user

api_router = APIRouter()
api_router.include_router(kind.router, prefix='/kinds', tags=['Kind'])
api_router.include_router(breeds.router, prefix='/breeds', tags=['Breed'])
api_router.include_router(alert_type.router, prefix='/alert_types', tags=['Alert Type'])
api_router.include_router(user.router, prefix='/users', tags=['User'])
