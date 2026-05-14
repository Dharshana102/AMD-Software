from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.host_service import host_service
 
router = APIRouter()
 
 
# ============ NEW: RPI FEATURE CARD ENDPOINTS ============
 
@router.get("/rpi/ip")
async def get_rpi_ip():
    """
    Get Raspberry Pi IP address
    Returns the IP address of the connected Raspberry Pi
    """
    result = await host_service.get_rpi_ip()
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result
 
 
@router.get("/rpi/mac")
async def get_rpi_mac():
    """
    Get Raspberry Pi MAC address
    Returns the MAC address of the connected Raspberry Pi
    """
    result = await host_service.get_rpi_mac()
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result
 
 
@router.get("/rpi/info")
async def get_rpi_info():
    """
    Get Raspberry Pi IP and MAC address
    Returns both IP and MAC address of the connected Raspberry Pi
    """
    result = await host_service.get_rpi_info()
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result
 
 
@router.get("/rpi/status")
async def rpi_status():
    """
    Get Raspberry Pi connection status
    Returns whether the Raspberry Pi is online/offline
    """
    result = await host_service.rpi_status()
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result
 
 
# ============ EXISTING HOST SERVER ENDPOINTS ============
 
@router.post("/control")
async def control_host(
    device: str = Query(..., description="System Server, Database Server, Application Server, Backup Server"),
    action: str = Query(..., regex="^(on|off|restart)$", description="Action: on, off, restart")
):
    """Control host device"""
    result = await host_service.control_host(device, action)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result
 
 
@router.get("/status/{device}")
async def host_status(device: str):
    """Get host device status"""
    result = await host_service.host_status(device)
    return result
 
 
@router.get("/status/all")
async def all_hosts_status():
    """Get status of all host devices"""
    result = await host_service.all_hosts_status()
    return result