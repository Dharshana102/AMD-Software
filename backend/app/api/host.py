from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.host_service import host_service

router = APIRouter()

# ============ HOST CONTROLS ============
@router.post("/control")
async def control_host(
    device: str = Query(..., description="System Server, Database Server, Application Server, Backup Server"),
    action: str = Query(..., regex="^(on|off|restart)$", description="Action: on, off, restart")
):
    result = await host_service.control_host(device, action)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.get("/status/{device}")
async def host_status(device: str):
    result = await host_service.host_status(device)
    return result


@router.get("/status/all")
async def all_hosts_status():
    result = await host_service.all_hosts_status()
    return result