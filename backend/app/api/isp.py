from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.isp_service import isp_service

router = APIRouter()


# ============ RGB LED COMMANDS ============
@router.post("/rgb/set")
async def rgb_set(
    led_id: int = Query(..., ge=1, le=2, description="LED ID: 1 or 2"),
    r: int = Query(..., ge=0, le=255, description="Red intensity 0-255"),
    g: int = Query(..., ge=0, le=255, description="Green intensity 0-255"),
    b: int = Query(..., ge=0, le=255, description="Blue intensity 0-255")
):
    result = await isp_service.rgb_set(led_id, r, g, b)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.post("/rgb/off")
async def rgb_off(led_id: int = Query(..., ge=1, le=2, description="LED ID: 1 or 2")):
    result = await isp_service.rgb_off(led_id)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


# ============ STEPPER MOTOR COMMANDS ============
@router.post("/stepper/move")
async def stepper_move(
    direction: str = Query(..., regex="^(CW|CCW)$", description="Direction: CW or CCW"),
    steps: int = Query(..., ge=1, le=2048, description="Number of steps (full rotation ~2048)"),
    speed_ms: int = Query(..., ge=1, le=500, description="Delay between steps in milliseconds")
):
    result = await isp_service.stepper_move(direction, steps, speed_ms)
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


@router.post("/stepper/stop")
async def stepper_stop():
    result = await isp_service.stepper_stop()
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result


# ============ LIGHT SENSOR ============
@router.get("/light/read")
async def light_read():
    result = await isp_service.light_read()
    return result