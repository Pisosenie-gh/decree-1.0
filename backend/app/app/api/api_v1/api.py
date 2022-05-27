from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, eds_provider_type, signature_resolution, decree_change_action,\
    signature_type, decree_kind, counter, decree_type, decree, signature

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(eds_provider_type.router, prefix="/core/eds-provider-type", tags=["eds_provider_type"])
api_router.include_router(signature_resolution.router, prefix="/core/signature-resolution", tags=["signature_resolution"])
api_router.include_router(decree_change_action.router, prefix="/core/decree-change-action", tags=["decree_change_action"])
api_router.include_router(signature_type.router, prefix="/core/signature-type", tags=["signature_type"])
api_router.include_router(decree_kind.router, prefix="/core/decree-kind", tags=["decree-kind"])
api_router.include_router(counter.router, prefix="/core/counter", tags=["counter"])
api_router.include_router(decree_type.router, prefix="/core/decree-type", tags=["decree_type"])
api_router.include_router(decree.router, prefix="/decree", tags=["decree"])
api_router.include_router(signature.router, prefix="/signature", tags=["signature"])


