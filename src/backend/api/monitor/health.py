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
    #
    _health_report = await monitor_service.get_health_report()
    _health_report_database = _health_report.get('database', None)
    #
    if isinstance(_health_report_database, dict):
        _health_report_database = DatabaseHealthModel(
                health=_health_report_database["health"],
                pool_minsize=_health_report_database["pool_minsize"],
                pool_maxsize=_health_report_database["pool_maxsize"],
                pool_size=_health_report_database["pool_size"],
                pool_freesize=_health_report_database["pool_freesize"],
                closed=_health_report_database["closed"]
            )
    else:
        _health_report_database = None
    #
    return HealthModel(
        health=_health_report.get('health', False),
        database=_health_report_database
    )

