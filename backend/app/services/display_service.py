from app.services.firmware_bridge import bridge
class DisplayService:

    # ============ HOTPLUG COMMANDS ============
    async def hotplug_dp1(self):
        return bridge.hotplug_dp1()

    async def hotplug_dp2(self):
        return bridge.hotplug_dp2()

    async def hotplug_hdmi1(self):
        return bridge.hotplug_hdmi1()

    async def hotplug_hdmi2(self):
        return bridge.hotplug_hdmi2()

    async def hotplug_usb4_1(self):
        return bridge.hotplug_usb4_1()

    async def hotplug_usb4_2(self):
        return bridge.hotplug_usb4_2()

    # ============ UNPLUG COMMANDS ============
    async def unplug_dp1(self):
        return bridge.unplug_dp1()

    async def unplug_dp2(self):
        return bridge.unplug_dp2()

    async def unplug_hdmi1(self):
        return bridge.unplug_hdmi1()

    async def unplug_hdmi2(self):
        return bridge.unplug_hdmi2()

    async def unplug_usb4_1(self):
        return bridge.unplug_usb4_1()

    async def unplug_usb4_2(self):
        return bridge.unplug_usb4_2()

    # ============ PLUG STATUS COMMANDS ============
    async def plug_status_dp1(self):
        return bridge.plug_status_dp1()

    async def plug_status_dp2(self):
        return bridge.plug_status_dp2()

    async def plug_status_hdmi1(self):
        return bridge.plug_status_hdmi1()

    async def plug_status_hdmi2(self):
        return bridge.plug_status_hdmi2()

    async def plug_status_usb1(self):
        return bridge.plug_status_usb1()

    async def plug_status_usb2(self):
        return bridge.plug_status_usb2()

    # ============ LID COMMANDS ============
    async def lid_open_laptop(self, angle: float):
        return bridge.lid_open_laptop(angle)

    async def lid_close_laptop(self, angle: float, press_time: float):
        return bridge.lid_close_laptop(angle, press_time)

    async def lid_open_crb(self):
        return bridge.lid_open_crb()

    async def lid_close_crb(self):
        return bridge.lid_close_crb()

    # ============ DISPLAY PROPERTIES ============
    async def read_display_properties(self):
        return bridge.read_display_properties()

    # ============ COMBINATIONAL ============
    async def hotplug_all_ports(self):
        return bridge.hotplug_all_ports()

    async def unplug_all_ports(self):
        return bridge.unplug_all_ports()


display_service = DisplayService()