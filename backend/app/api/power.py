from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.power_service import power_service

router = APIRouter()


# ============ LAPTOP OEM ENDPOINTS ============
@router.post("/laptop/on")
async def laptop_power_on(angle: float = Query(..., ge=0, le=180), time: float = Query(..., ge=1, le=60)):
    result = await power_service.laptop_power_on(angle, time)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.post("/laptop/off")
async def laptop_power_off(angle: float = Query(..., ge=0, le=180), time: float = Query(..., ge=1, le=60)):
    result = await power_service.laptop_power_off(angle, time)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.post("/laptop/restart")
async def laptop_restart(
    angle: float = Query(..., ge=0, le=180),
    time_on: float = Query(..., ge=1, le=60),
    wait_time: float = Query(..., ge=1, le=60),
    time_off: float = Query(..., ge=1, le=60)
):
    result = await power_service.laptop_restart(angle, time_on, wait_time, time_off)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.get("/laptop/status")
async def laptop_status():
    result = await power_service.laptop_status()
    return result


# ============ DESKTOP ENDPOINTS ============
@router.post("/desktop/on")
async def desktop_power_on(time: float = Query(..., ge=1, le=5)):
    result = await power_service.desktop_power_on(time)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.post("/desktop/off")
async def desktop_power_off(time: float = Query(..., ge=1, le=5)):
    result = await power_service.desktop_power_off(time)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.post("/desktop/restart")
async def desktop_restart(pulse_time: float = Query(..., ge=1, le=60)):
    result = await power_service.desktop_restart(pulse_time)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.get("/desktop/status")
async def desktop_status():
    result = await power_service.desktop_status()
    return result


# ============ CRB ENDPOINTS ============
@router.post("/crb/on")
async def crb_power_on(time: float = Query(..., ge=1, le=5)):
    result = await power_service.crb_power_on(time)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.post("/crb/off")
async def crb_power_off(time: float = Query(..., ge=1, le=5)):
    result = await power_service.crb_power_off(time)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.post("/crb/restart")
async def crb_restart(pulse_time: float = Query(..., ge=1, le=60)):
    result = await power_service.crb_restart(pulse_time)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.get("/crb/status")
async def crb_status():
    result = await power_service.crb_status()
    return result


# ============ AC POWER ENDPOINTS ============
@router.post("/ac/on")
async def ac_power_on():
    result = await power_service.ac_power_on()
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.post("/ac/off")
async def ac_power_off():
    result = await power_service.ac_power_off()
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.get("/ac/status")
async def ac_power_status():
    result = await power_service.ac_power_status()
    return result


# ============ MODULE STATUS ============
@router.get("/module/{module_number}")
async def module_status(module_number: int):
    result = await power_service.module_status(module_number)
    return result


# ============ COMBINATIONAL ENDPOINTS ============
@router.post("/combo/power-delay")
async def power_on_with_delay(time: float = Query(..., ge=1, le=1000)):
    result = await power_service.power_on_with_delay(time)
    return result


@router.post("/combo/close-lid-power-on")
async def close_lid_power_on_sut():
    result = await power_service.close_lid_power_on_sut()
    return result


@router.post("/combo/close-n-open-lid-power-on")
async def close_n_open_lid_power_on_sut():
    result = await power_service.close_n_open_lid_power_on_sut()
    return result


@router.post("/combo/close-lid-wait-open-lid")
async def close_lid_wait_open_lid(time: float = Query(..., ge=1, le=1000)):
    result = await power_service.close_lid_wait_open_lid(time)
    return result


@router.post("/combo/close-lid-hotplug-all-dps")
async def close_lid_hotplug_all_dps_n_open_lid_power_on_sut():
    result = await power_service.close_lid_hotplug_all_dps_n_open_lid_power_on_sut()
    return result


@router.post("/combo/hotplug-all-ports")
async def hotplug_all_ports():
    result = await power_service.hotplug_all_ports()
    return result


@router.post("/combo/unplug-all-ports")
async def unplug_all_ports():
    result = await power_service.unplug_all_ports()
    return result