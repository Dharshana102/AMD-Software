from app.services.firmware_bridge import bridge
class AudioService:

    # ============ AUDIO HOTPLUG/UNPLUG ============
    async def hotplug_35mm(self):
        return bridge.hotplug_35mm()

    async def unplug_35mm(self):
        return bridge.unplug_35mm()

    async def hotplug_usb_a(self):
        return bridge.hotplug_usb_a()

    async def unplug_usb_a(self):
        return bridge.unplug_usb_a()

    async def hotplug_usb_c(self):
        return bridge.hotplug_usb_c()

    async def unplug_usb_c(self):
        return bridge.unplug_usb_c()

    async def hotplug_hdmi_audio(self):
        return bridge.hotplug_hdmi_audio()

    async def unplug_hdmi_audio(self):
        return bridge.unplug_hdmi_audio()

    # ============ BLUETOOTH BASIC ============
    async def bt_turn_on(self):
        return bridge.bt_turn_on()

    async def bt_turn_off(self):
        return bridge.bt_turn_off()

    async def bt_change_name(self, new_name: str):
        return bridge.bt_change_name(new_name)

    async def bt_enable_pairing(self):
        return bridge.bt_enable_pairing()

    async def bt_connection_status(self):
        return bridge.bt_connection_status()

    async def bt_connect(self):
        return bridge.bt_connect()

    async def bt_disconnect(self):
        return bridge.bt_disconnect()

    # ============ BLUETOOTH AUDIO CONTROLS ============
    async def bt_audio_up(self):
        return bridge.bt_audio_up()

    async def bt_audio_down(self):
        return bridge.bt_audio_down()

    async def bt_audio_mute(self):
        return bridge.bt_audio_mute()

    async def bt_audio_unmute(self):
        return bridge.bt_audio_unmute()

    # ============ BLUETOOTH MEDIA CONTROLS ============
    async def bt_play(self):
        return bridge.bt_play()

    async def bt_pause(self):
        return bridge.bt_pause()

    async def bt_next(self):
        return bridge.bt_next()

    async def bt_previous(self):
        return bridge.bt_previous()

    # ============ BLUETOOTH LOGS ============
    async def bt_get_logs(self):
        return bridge.bt_get_logs()


audio_service = AudioService()