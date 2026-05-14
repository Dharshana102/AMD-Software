from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.display_service import display_service

router = APIRouter()

# ============ HOTPLUG ENDPOINTS ============
@router.post("/hotplug/dp1")
async def hotplug_dp1():
    result = await display_service.hotplug_dp1()
    return result


@router.post("/hotplug/dp2")
async def hotplug_dp2():
    result = await display_service.hotplug_dp2()
    return result


@router.post("/hotplug/hdmi1")
async def hotplug_hdmi1():
    result = await display_service.hotplug_hdmi1()
    return result


@router.post("/hotplug/hdmi2")
async def hotplug_hdmi2():
    result = await display_service.hotplug_hdmi2()
    return result


@router.post("/hotplug/usb4_1")
async def hotplug_usb4_1():
    result = await display_service.hotplug_usb4_1()
    return result


@router.post("/hotplug/usb4_2")
async def hotplug_usb4_2():
    result = await display_service.hotplug_usb4_2()
    return result


# ============ UNPLUG ENDPOINTS ============
@router.post("/unplug/dp1")
async def unplug_dp1():
    result = await display_service.unplug_dp1()
    return result


@router.post("/unplug/dp2")
async def unplug_dp2():
    result = await display_service.unplug_dp2()
    return result


@router.post("/unplug/hdmi1")
async def unplug_hdmi1():
    result = await display_service.unplug_hdmi1()
    return result


@router.post("/unplug/hdmi2")
async def unplug_hdmi2():
    result = await display_service.unplug_hdmi2()
    return result


@router.post("/unplug/usb4_1")
async def unplug_usb4_1():
    result = await display_service.unplug_usb4_1()
    return result


@router.post("/unplug/usb4_2")
async def unplug_usb4_2():
    result = await display_service.unplug_usb4_2()
    return result


# ============ PLUG STATUS ENDPOINTS ============
@router.get("/status/dp1")
async def plug_status_dp1():
    result = await display_service.plug_status_dp1()
    return result


@router.get("/status/dp2")
async def plug_status_dp2():
    result = await display_service.plug_status_dp2()
    return result


@router.get("/status/hdmi1")
async def plug_status_hdmi1():
    result = await display_service.plug_status_hdmi1()
    return result


@router.get("/status/hdmi2")
async def plug_status_hdmi2():
    result = await display_service.plug_status_hdmi2()
    return result


@router.get("/status/usb1")
async def plug_status_usb1():
    result = await display_service.plug_status_usb1()
    return result


@router.get("/status/usb2")
async def plug_status_usb2():
    result = await display_service.plug_status_usb2()
    return result


# ============ LID ENDPOINTS ============
@router.post("/lid/laptop/open")
async def lid_open_laptop(angle: float = Query(..., ge=0, le=180)):
    result = await display_service.lid_open_laptop(angle)
    return result


@router.post("/lid/laptop/close")
async def lid_close_laptop(angle: float = Query(..., ge=0, le=180), press_time: float = Query(..., ge=1, le=300)):
    result = await display_service.lid_close_laptop(angle, press_time)
    return result


@router.post("/lid/crb/open")
async def lid_open_crb():
    result = await display_service.lid_open_crb()
    return result


@router.post("/lid/crb/close")
async def lid_close_crb():
    result = await display_service.lid_close_crb()
    return result


# ============ DISPLAY PROPERTIES ============
@router.get("/properties")
async def read_display_properties():
    result = await display_service.read_display_properties()
    return result


# ============ COMBINATIONAL ============
@router.post("/hotplug/all")
async def hotplug_all_ports():
    result = await display_service.hotplug_all_ports()
    return result


@router.post("/unplug/all")
async def unplug_all_ports():
    result = await display_service.unplug_all_ports()
    return result