from app.infrastructure.uart_comm import uart
from app.utils.protocol import UARTProtocol
from app.utils.command_builder import CommandBuilder


class FirmwareBridge:

    @staticmethod
    def ensure_connection():
        if not uart.is_connected():
            if not uart.connect():
                raise Exception("Failed to connect to firmware via UART")

    @staticmethod
    def send_command(command: str, timeout: int = None) -> dict:
        """Send command and receive response"""
        FirmwareBridge.ensure_connection()
        result = uart.send_command(command, wait_response=True, timeout=timeout)

        if not result.get("success"):
            return result

        response = result.get("response", "")
        return UARTProtocol.parse_response(response)

    # ================================================================
    # MODULE 1: POWER COMMANDS
    # ================================================================

    # Laptop OEM Commands
    def laptop_power_on(self, angle: float, time: float) -> dict:
        command = CommandBuilder.laptop_power_on(angle, time)
        return self.send_command(command)

    def laptop_power_off(self, angle: float, time: float) -> dict:
        command = CommandBuilder.laptop_power_off(angle, time)
        return self.send_command(command)

    def laptop_restart(self, angle: float, time_on: float, wait_time: float, time_off: float) -> dict:
        command = CommandBuilder.laptop_restart(angle, time_on, wait_time, time_off)
        return self.send_command(command)

    def laptop_status(self) -> dict:
        command = CommandBuilder.laptop_status()
        return self.send_command(command)

    # Desktop Commands
    def desktop_power_on(self, time: float) -> dict:
        command = CommandBuilder.desktop_power_on(time)
        return self.send_command(command)

    def desktop_power_off(self, time: float) -> dict:
        command = CommandBuilder.desktop_power_off(time)
        return self.send_command(command)

    def desktop_restart(self, pulse_time: float) -> dict:
        command = CommandBuilder.desktop_restart(pulse_time)
        return self.send_command(command)

    def desktop_status(self) -> dict:
        command = CommandBuilder.desktop_status()
        return self.send_command(command)

    # CRB Commands
    def crb_power_on(self, time: float) -> dict:
        command = CommandBuilder.crb_power_on(time)
        return self.send_command(command)

    def crb_power_off(self, time: float) -> dict:
        command = CommandBuilder.crb_power_off(time)
        return self.send_command(command)

    def crb_restart(self, pulse_time: float) -> dict:
        command = CommandBuilder.crb_restart(pulse_time)
        return self.send_command(command)

    def crb_status(self) -> dict:
        command = CommandBuilder.crb_status()
        return self.send_command(command)

    # AC Power Commands
    def ac_power_on(self) -> dict:
        command = CommandBuilder.ac_power_on()
        return self.send_command(command)

    def ac_power_off(self) -> dict:
        command = CommandBuilder.ac_power_off()
        return self.send_command(command)

    def ac_power_status(self) -> dict:
        command = CommandBuilder.ac_power_status()
        return self.send_command(command)

    # Module Status
    def module_status(self, module_number: int) -> dict:
        command = CommandBuilder.module_status(module_number)
        return self.send_command(command)

    # ================================================================
    # MODULE 2: DISPLAY COMMANDS
    # ================================================================

    # Hotplug Commands
    def hotplug_dp1(self) -> dict:
        return self.send_command(CommandBuilder.hotplug_dp1())

    def hotplug_dp2(self) -> dict:
        return self.send_command(CommandBuilder.hotplug_dp2())

    def hotplug_hdmi1(self) -> dict:
        return self.send_command(CommandBuilder.hotplug_hdmi1())

    def hotplug_hdmi2(self) -> dict:
        return self.send_command(CommandBuilder.hotplug_hdmi2())

    def hotplug_usb4_1(self) -> dict:
        return self.send_command(CommandBuilder.hotplug_usb4_1())

    def hotplug_usb4_2(self) -> dict:
        return self.send_command(CommandBuilder.hotplug_usb4_2())

    # Unplug Commands
    def unplug_dp1(self) -> dict:
        return self.send_command(CommandBuilder.unplug_dp1())

    def unplug_dp2(self) -> dict:
        return self.send_command(CommandBuilder.unplug_dp2())

    def unplug_hdmi1(self) -> dict:
        return self.send_command(CommandBuilder.unplug_hdmi1())

    def unplug_hdmi2(self) -> dict:
        return self.send_command(CommandBuilder.unplug_hdmi2())

    def unplug_usb4_1(self) -> dict:
        return self.send_command(CommandBuilder.unplug_usb4_1())

    def unplug_usb4_2(self) -> dict:
        return self.send_command(CommandBuilder.unplug_usb4_2())

    # Plug Status Commands
    def plug_status_dp1(self) -> dict:
        return self.send_command(CommandBuilder.plug_status_dp1())

    def plug_status_dp2(self) -> dict:
        return self.send_command(CommandBuilder.plug_status_dp2())

    def plug_status_hdmi1(self) -> dict:
        return self.send_command(CommandBuilder.plug_status_hdmi1())

    def plug_status_hdmi2(self) -> dict:
        return self.send_command(CommandBuilder.plug_status_hdmi2())

    def plug_status_usb1(self) -> dict:
        return self.send_command(CommandBuilder.plug_status_usb1())

    def plug_status_usb2(self) -> dict:
        return self.send_command(CommandBuilder.plug_status_usb2())

    # LID Commands
    def lid_open_laptop(self, angle: float) -> dict:
        command = CommandBuilder.lid_open_laptop(angle)
        return self.send_command(command)

    def lid_close_laptop(self, angle: float, press_time: float) -> dict:
        command = CommandBuilder.lid_close_laptop(angle, press_time)
        return self.send_command(command)

    def lid_open_crb(self) -> dict:
        return self.send_command(CommandBuilder.lid_open_crb())

    def lid_close_crb(self) -> dict:
        return self.send_command(CommandBuilder.lid_close_crb())

    # Display Properties
    def read_display_properties(self) -> dict:
        return self.send_command(CommandBuilder.read_display_properties())

    # ================================================================
    # MODULE 3: CAMERA / ISP COMMANDS
    # ================================================================

    # RGB LED Commands
    def rgb_set(self, led_id: int, r: int, g: int, b: int) -> dict:
        command = CommandBuilder.rgb_set(led_id, r, g, b)
        return self.send_command(command)

    def rgb_off(self, led_id: int) -> dict:
        command = CommandBuilder.rgb_off(led_id)
        return self.send_command(command)

    # Stepper Motor Commands
    def stepper_move(self, direction: str, steps: int, speed_ms: int) -> dict:
        command = CommandBuilder.stepper_move(direction, steps, speed_ms)
        return self.send_command(command)

    def stepper_stop(self) -> dict:
        return self.send_command(CommandBuilder.stepper_stop())

    # Light Sensor
    def light_read(self) -> dict:
        return self.send_command(CommandBuilder.light_read())

    # ================================================================
    # MODULE 4: AUDIO / BLUETOOTH COMMANDS
    # ================================================================

    # Audio Hotplug/Unplug Commands
    def hotplug_35mm(self) -> dict:
        return self.send_command(CommandBuilder.hotplug_35mm())

    def unplug_35mm(self) -> dict:
        return self.send_command(CommandBuilder.unplug_35mm())

    def hotplug_usb_a(self) -> dict:
        return self.send_command(CommandBuilder.hotplug_usb_a())

    def unplug_usb_a(self) -> dict:
        return self.send_command(CommandBuilder.unplug_usb_a())

    def hotplug_usb_c(self) -> dict:
        return self.send_command(CommandBuilder.hotplug_usb_c())

    def unplug_usb_c(self) -> dict:
        return self.send_command(CommandBuilder.unplug_usb_c())

    def hotplug_hdmi_audio(self) -> dict:
        return self.send_command(CommandBuilder.hotplug_hdmi_audio())

    def unplug_hdmi_audio(self) -> dict:
        return self.send_command(CommandBuilder.unplug_hdmi_audio())

    # Bluetooth Basic Commands
    def bt_turn_on(self) -> dict:
        return self.send_command(CommandBuilder.bt_turn_on())

    def bt_turn_off(self) -> dict:
        return self.send_command(CommandBuilder.bt_turn_off())

    def bt_change_name(self, new_name: str) -> dict:
        command = CommandBuilder.bt_change_name(new_name)
        return self.send_command(command)

    def bt_enable_pairing(self) -> dict:
        return self.send_command(CommandBuilder.bt_enable_pairing())

    def bt_connection_status(self) -> dict:
        return self.send_command(CommandBuilder.bt_connection_status())

    def bt_connect(self) -> dict:
        return self.send_command(CommandBuilder.bt_connect())

    def bt_disconnect(self) -> dict:
        return self.send_command(CommandBuilder.bt_disconnect())

    # Bluetooth Audio Controls
    def bt_audio_up(self) -> dict:
        return self.send_command(CommandBuilder.bt_audio_up())

    def bt_audio_down(self) -> dict:
        return self.send_command(CommandBuilder.bt_audio_down())

    def bt_audio_mute(self) -> dict:
        return self.send_command(CommandBuilder.bt_audio_mute())

    def bt_audio_unmute(self) -> dict:
        return self.send_command(CommandBuilder.bt_audio_unmute())

    # Bluetooth Media Controls
    def bt_play(self) -> dict:
        return self.send_command(CommandBuilder.bt_play())

    def bt_pause(self) -> dict:
        return self.send_command(CommandBuilder.bt_pause())

    def bt_next(self) -> dict:
        return self.send_command(CommandBuilder.bt_next())

    def bt_previous(self) -> dict:
        return self.send_command(CommandBuilder.bt_previous())

    # Bluetooth Logs
    def bt_get_logs(self) -> dict:
        return self.send_command(CommandBuilder.bt_get_logs())

    # ================================================================
    # MODULE 5: HOST COMMANDS
    # ================================================================

    def host_control(self, device: str, action: str) -> dict:
        """Control host device (on/off/restart)"""
        device_map = {
            "System Server": "01",
            "Database Server": "02",
            "Application Server": "03",
            "Backup Server": "04"
        }
        action_map = {
            "on": "01",
            "off": "02",
            "restart": "03"
        }
        device_id = device_map.get(device, "00")
        action_id = action_map.get(action, "00")
        command = f"HST:{device_id}:{action_id};"
        return self.send_command(command)

    def host_status(self, device: str) -> dict:
        """Get host device status"""
        device_map = {
            "System Server": "01",
            "Database Server": "02",
            "Application Server": "03",
            "Backup Server": "04"
        }
        device_id = device_map.get(device, "00")
        command = f"HST_STATUS:{device_id};"
        return self.send_command(command)

    def all_hosts_status(self) -> dict:
        """Get status of all host devices"""
        command = "HST_STATUS_ALL;"
        return self.send_command(command)

    # ================================================================
    # COMBINATIONAL COMMANDS (Module 0 & 1)
    # ================================================================

    def power_on_with_delay(self, time: float) -> dict:
        command = CommandBuilder.power_on_with_delay(time)
        return self.send_command(command)

    def close_lid_power_on_sut(self) -> dict:
        return self.send_command(CommandBuilder.close_lid_power_on_sut())

    def close_n_open_lid_power_on_sut(self) -> dict:
        return self.send_command(CommandBuilder.close_n_open_lid_power_on_sut())

    def close_lid_wait_open_lid(self, time: float) -> dict:
        command = CommandBuilder.close_lid_wait_open_lid(time)
        return self.send_command(command)

    def close_lid_hotplug_all_dps_n_open_lid_power_on_sut(self) -> dict:
        return self.send_command(CommandBuilder.close_lid_hotplug_all_dps_n_open_lid_power_on_sut())

    def hotplug_all_ports(self) -> dict:
        return self.send_command(CommandBuilder.hotplug_all_ports())

    def unplug_all_ports(self) -> dict:
        return self.send_command(CommandBuilder.unplug_all_ports())


# Create global instance
bridge = FirmwareBridge()
