from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.audio_service import audio_service

router = APIRouter()


# ============ AUDIO HOTPLUG/UNPLUG ============
@router.post("/hotplug/35mm")
async def hotplug_35mm():
    result = await audio_service.hotplug_35mm()
    return result


@router.post("/unplug/35mm")
async def unplug_35mm():
    result = await audio_service.unplug_35mm()
    return result


@router.post("/hotplug/usb-a")
async def hotplug_usb_a():
    result = await audio_service.hotplug_usb_a()
    return result


@router.post("/unplug/usb-a")
async def unplug_usb_a():
    result = await audio_service.unplug_usb_a()
    return result


@router.post("/hotplug/usb-c")
async def hotplug_usb_c():
    result = await audio_service.hotplug_usb_c()
    return result


@router.post("/unplug/usb-c")
async def unplug_usb_c():
    result = await audio_service.unplug_usb_c()
    return result


@router.post("/hotplug/hdmi")
async def hotplug_hdmi_audio():
    result = await audio_service.hotplug_hdmi_audio()
    return result


@router.post("/unplug/hdmi")
async def unplug_hdmi_audio():
    result = await audio_service.unplug_hdmi_audio()
    return result


# ============ BLUETOOTH BASIC ============
@router.post("/bt/on")
async def bt_turn_on():
    result = await audio_service.bt_turn_on()
    return result


@router.post("/bt/off")
async def bt_turn_off():
    result = await audio_service.bt_turn_off()
    return result


@router.post("/bt/name")
async def bt_change_name(new_name: str):
    result = await audio_service.bt_change_name(new_name)
    return result


@router.post("/bt/pairing")
async def bt_enable_pairing():
    result = await audio_service.bt_enable_pairing()
    return result


@router.get("/bt/status")
async def bt_connection_status():
    result = await audio_service.bt_connection_status()
    return result


@router.post("/bt/connect")
async def bt_connect():
    result = await audio_service.bt_connect()
    return result


@router.post("/bt/disconnect")
async def bt_disconnect():
    result = await audio_service.bt_disconnect()
    return result


# ============ BLUETOOTH AUDIO CONTROLS ============
@router.post("/bt/volume/up")
async def bt_audio_up():
    result = await audio_service.bt_audio_up()
    return result


@router.post("/bt/volume/down")
async def bt_audio_down():
    result = await audio_service.bt_audio_down()
    return result


@router.post("/bt/volume/mute")
async def bt_audio_mute():
    result = await audio_service.bt_audio_mute()
    return result


@router.post("/bt/volume/unmute")
async def bt_audio_unmute():
    result = await audio_service.bt_audio_unmute()
    return result


# ============ BLUETOOTH MEDIA CONTROLS ============
@router.post("/bt/media/play")
async def bt_play():
    result = await audio_service.bt_play()
    return result


@router.post("/bt/media/pause")
async def bt_pause():
    result = await audio_service.bt_pause()
    return result


@router.post("/bt/media/next")
async def bt_next():
    result = await audio_service.bt_next()
    return result


@router.post("/bt/media/previous")
async def bt_previous():
    result = await audio_service.bt_previous()
    return result


# ============ BLUETOOTH LOGS ============
@router.get("/bt/logs")
async def bt_get_logs():
    result = await audio_service.bt_get_logs()
    return result