from app.services.firmware_bridge import bridge


class PowerService:

    # ============ LAPTOP OEM ============
    async def laptop_power_on(self, angle: float, time: float):
        return bridge.laptop_power_on(angle, time)

    async def laptop_power_off(self, angle: float, time: float):
        return bridge.laptop_power_off(angle, time)

    async def laptop_restart(self, angle: float, time_on: float, wait_time: float, time_off: float):
        return bridge.laptop_restart(angle, time_on, wait_time, time_off)

    async def laptop_status(self):
        return bridge.laptop_status()

    # ============ DESKTOP ============
    async def desktop_power_on(self, time: float):
        return bridge.desktop_power_on(time)

    async def desktop_power_off(self, time: float):
        return bridge.desktop_power_off(time)

    async def desktop_restart(self, pulse_time: float):
        return bridge.desktop_restart(pulse_time)

    async def desktop_status(self):
        return bridge.desktop_status()

    # ============ CRB ============
    async def crb_power_on(self, time: float):
        return bridge.crb_power_on(time)

    async def crb_power_off(self, time: float):
        return bridge.crb_power_off(time)

    async def crb_restart(self, pulse_time: float):
        return bridge.crb_restart(pulse_time)

    async def crb_status(self):
        return bridge.crb_status()

    # ============ AC POWER ============
    async def ac_power_on(self):
        return bridge.ac_power_on()

    async def ac_power_off(self):
        return bridge.ac_power_off()

    async def ac_power_status(self):
        return bridge.ac_power_status()

    # ============ MODULE STATUS ============
    async def module_status(self, module_number: int):
        return bridge.module_status(module_number)

    # ============ COMBINATIONAL ============
    async def power_on_with_delay(self, time: float):
        return bridge.power_on_with_delay(time)

    async def close_lid_power_on_sut(self):
        return bridge.close_lid_power_on_sut()

    async def close_n_open_lid_power_on_sut(self):
        return bridge.close_n_open_lid_power_on_sut()

    async def close_lid_wait_open_lid(self, time: float):
        return bridge.close_lid_wait_open_lid(time)

    async def close_lid_hotplug_all_dps_n_open_lid_power_on_sut(self):
        return bridge.close_lid_hotplug_all_dps_n_open_lid_power_on_sut()

    async def hotplug_all_ports(self):
        return bridge.hotplug_all_ports()

    async def unplug_all_ports(self):
        return bridge.unplug_all_ports()


power_service = PowerService()