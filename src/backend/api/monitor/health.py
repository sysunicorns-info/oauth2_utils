from fastapi import APIRouter, Depends, Response, Request
from dependency_injector import providers
from pydantic import BaseModel
from typing import cast, Any

from backend.service import MonitorService, service_container_proxy

from .model.health import HealthModel, DatabaseHealthModel

api_router = APIRouter()

HEALTH_API_ROUTER_PREFIX = ""


@api_router.get(path="/health", tags=["monitor"], response_model=HealthModel)
async def get_health(
        request: Request,
        response: Response,
        monitor_service: MonitorService=Depends(service_container_proxy.monitor_service, use_cache=False)
    ) -> HealthModel:
    _healt_result = await monitor_service.get_health()
    return HealthModel(health=_healt_result.get('health', False), database=DatabaseHealthModel(
        pool_minsize=_healt_result["database"]["pool_minsize"],
        pool_maxsize=_healt_result["database"]["pool_maxsize"],
        pool_size=_healt_result["database"]["pool_size"],
        pool_freesize=_healt_result["database"]["pool_freesize"],
        closed=_healt_result["database"]["closed"]
    ))
