from app.infrastructure.uart_comm import uart
from app.utils.protocol import UARTProtocol
 
class FirmwareBridge:
    """Bridge between API and C firmware - ALL modules"""
 
    @staticmethod
    def ensure_connection():
        if not uart.is_connected():
            uart.connect()
 
    @staticmethod
    def send_raw_command(command: str) -> dict:
        """Send any raw command string to hardware"""
        FirmwareBridge.ensure_connection()
        if not uart.is_connected():
            # Simulation mode
            return {"success": True, "response": f"OK:{command}", "message": "Simulated"}
        result = uart.send_command(command, wait_response=True)
        if result.get("success"):
            response = result.get("response", "")
            return UARTProtocol.parse_response(response)
        return result
 
    # ============ POWER COMMANDS ============
    def laptop_power_on(self, angle: float, time: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_ON_LT, angle, time)
        return self.send_raw_command(cmd)
 
    def laptop_power_off(self, angle: float, time: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_OFF_LT, angle, time)
        return self.send_raw_command(cmd)
 
    def laptop_restart(self, angle: float, time_on: float, wait: float, time_off: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_RST_LT, angle, time_on, wait, time_off)
        return self.send_raw_command(cmd)
 
    def laptop_status(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_STATUS_LT)
        return self.send_raw_command(cmd)
 
    def desktop_power_on(self, time: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_ON_DT, time)
        return self.send_raw_command(cmd)
 
    def desktop_power_off(self, time: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_OFF_DT, time)
        return self.send_raw_command(cmd)
 
    def desktop_restart(self, pulse_time: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_RST_DT, pulse_time)
        return self.send_raw_command(cmd)
 
    def desktop_status(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_STATUS_DT)
        return self.send_raw_command(cmd)
 
    def crb_power_on(self, time: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_ON_CRB, time)
        return self.send_raw_command(cmd)
 
    def crb_power_off(self, time: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_OFF_CRB, time)
        return self.send_raw_command(cmd)
 
    def crb_restart(self, pulse_time: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_RST_CRB, pulse_time)
        return self.send_raw_command(cmd)
 
    def crb_status(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_STATUS_CRB)
        return self.send_raw_command(cmd)
 
    def ac_on(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_ON_AC)
        return self.send_raw_command(cmd)
 
    def ac_off(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_OFF_AC)
        return self.send_raw_command(cmd)
 
    def ac_status(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWR_STATUS_AC)
        return self.send_raw_command(cmd)
 
    # ============ DISPLAY COMMANDS ============
    def hotplug(self, port: str, number: int):
        port_upper = port.upper()
        cmd_map = {
            'DP': {1: UARTProtocol.CMD_HOTPLUG_DP_1, 2: UARTProtocol.CMD_HOTPLUG_DP_2},
            'HDMI': {1: UARTProtocol.CMD_HOTPLUG_HDMI_1, 2: UARTProtocol.CMD_HOTPLUG_HDMI_2},
            'USB4': {1: UARTProtocol.CMD_HOTPLUG_USB4_1, 2: UARTProtocol.CMD_HOTPLUG_USB4_2}
        }
        cmd = UARTProtocol.build_command(cmd_map[port_upper][number])
        return self.send_raw_command(cmd)
 
    def unplug(self, port: str, number: int):
        port_upper = port.upper()
        cmd_map = {
            'DP': {1: UARTProtocol.CMD_UNPLUG_DP_1, 2: UARTProtocol.CMD_UNPLUG_DP_2},
            'HDMI': {1: UARTProtocol.CMD_UNPLUG_HDMI_1, 2: UARTProtocol.CMD_UNPLUG_HDMI_2},
            'USB4': {1: UARTProtocol.CMD_UNPLUG_USB4_1, 2: UARTProtocol.CMD_UNPLUG_USB4_2}
        }
        cmd = UARTProtocol.build_command(cmd_map[port_upper][number])
        return self.send_raw_command(cmd)
 
    def plug_status(self, port: str, number: int):
        port_upper = port.upper()
        cmd_map = {
            'DP': {1: UARTProtocol.CMD_PLUG_STATUS_DP_1, 2: UARTProtocol.CMD_PLUG_STATUS_DP_2},
            'HDMI': {1: UARTProtocol.CMD_PLUG_STATUS_HDMI_1, 2: UARTProtocol.CMD_PLUG_STATUS_HDMI_2},
            'USB': {1: UARTProtocol.CMD_PLUG_STATUS_USB_1, 2: UARTProtocol.CMD_PLUG_STATUS_USB_2}
        }
        cmd = UARTProtocol.build_command(cmd_map[port_upper][number])
        return self.send_raw_command(cmd)
 
    def lid_open_laptop(self, angle: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_LID_OPEN_LT, angle)
        return self.send_raw_command(cmd)
 
    def lid_close_laptop(self, angle: float, press_time: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_LID_CLOSE_LT, angle, press_time)
        return self.send_raw_command(cmd)
 
    def lid_open_crb(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_LID_OPEN_CRB)
        return self.send_raw_command(cmd)
 
    def lid_close_crb(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_LID_CLOSE_CRB)
        return self.send_raw_command(cmd)
 
    def read_display_properties(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_READ_DISP_PROP)
        return self.send_raw_command(cmd)
 
    # ============ ISP/CAMERA COMMANDS ============
    def rgb_set(self, led_id: int, r: int, g: int, b: int):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_RGB_SET, led_id, r, g, b)
        return self.send_raw_command(cmd)
 
    def rgb_off(self, led_id: int):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_RGB_OFF, led_id)
        return self.send_raw_command(cmd)
 
    def stepper_move(self, direction: str, steps: int, speed_ms: int):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_STEPPER_MOVE, direction, steps, speed_ms)
        return self.send_raw_command(cmd)
 
    def stepper_stop(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_STEPPER_STOP)
        return self.send_raw_command(cmd)
 
    def light_read(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_LIGHT_READ)
        return self.send_raw_command(cmd)
 
    # ============ AUDIO/BT COMMANDS ============
    def audio_hotplug(self, port: str):
        port_map = {
            '3.5_MM': UARTProtocol.CMD_HOTPLUG_3_5_MM,
            'USB_A': UARTProtocol.CMD_HOTPLUG_USB_A,
            'USB_C': UARTProtocol.CMD_HOTPLUG_USB_C,
            'HDMI': UARTProtocol.CMD_HOTPLUG_HDMI
        }
        cmd = UARTProtocol.build_command(port_map.get(port, UARTProtocol.CMD_HOTPLUG_3_5_MM))
        return self.send_raw_command(cmd)
 
    def audio_unplug(self, port: str):
        port_map = {
            '3.5_MM': UARTProtocol.CMD_UNPLUG_3_5_MM,
            'USB_A': UARTProtocol.CMD_UNPLUG_USB_A,
            'USB_C': UARTProtocol.CMD_UNPLUG_USB_C,
            'HDMI': UARTProtocol.CMD_UNPLUG_HDMI
        }
        cmd = UARTProtocol.build_command(port_map.get(port, UARTProtocol.CMD_UNPLUG_3_5_MM))
        return self.send_raw_command(cmd)
 
    def bt_turn_on(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_TURN_ON_BT)
        return self.send_raw_command(cmd)
 
    def bt_turn_off(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_TURN_OFF_BT)
        return self.send_raw_command(cmd)
 
    def bt_change_name(self, name: str):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_CHANGE_BT_NAME, name)
        return self.send_raw_command(cmd)
 
    def bt_pairing_mode(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_EN_BT_PARING_MODE)
        return self.send_raw_command(cmd)
 
    def bt_connect(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_BT_CONNECT)
        return self.send_raw_command(cmd)
 
    def bt_disconnect(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_BT_DISCONNECT)
        return self.send_raw_command(cmd)
 
    def bt_status(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_BT_CONNECTION_STATUS)
        return self.send_raw_command(cmd)
 
    def bt_volume_up(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_BT_AUDIO_UP)
        return self.send_raw_command(cmd)
 
    def bt_volume_down(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_BT_AUDIO_DOWN)
        return self.send_raw_command(cmd)
 
    def bt_mute(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_BT_AUDIO_MUTE)
        return self.send_raw_command(cmd)
 
    def bt_unmute(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_BT_AUDIO_UNMUTE)
        return self.send_raw_command(cmd)
 
    def bt_play(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_BT_PLAY)
        return self.send_raw_command(cmd)
 
    def bt_pause(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_BT_PAUSE)
        return self.send_raw_command(cmd)
 
    def bt_next(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_BT_NEXT)
        return self.send_raw_command(cmd)
 
    def bt_previous(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_BT_PREVIOUS)
        return self.send_raw_command(cmd)
 
    # ============ HOST COMMANDS ============
    def module_status(self, module_num: int):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_MODULE_STATUS, module_num)
        return self.send_raw_command(cmd)
 
    def get_rpi_info(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_GET_RPI_INFO)
        return self.send_raw_command(cmd)
 
    def get_rpi_ip(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_GET_RPI_IP)
        return self.send_raw_command(cmd)
 
    def get_rpi_mac(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_GET_RPI_MAC)
        return self.send_raw_command(cmd)
 
    def rpi_status(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_RPI_STATUS)
        return self.send_raw_command(cmd)
 
    # ============ COMBINATIONAL COMMANDS ============
    def pwron_with_delay(self, time: float):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_PWRON_WITH_DELAY, time)
        return self.send_raw_command(cmd)
 
    def close_lid_pwron_sut(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_CLOSE_LID_PWRON_SUT)
        return self.send_raw_command(cmd)
 
    def hotplug_all_ports(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_ALL_PORTS)
        return self.send_raw_command(cmd)
 
    def unplug_all_ports(self):
        cmd = UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_ALL_PORTS)
        return self.send_raw_command(cmd)
 
 
# Singleton instance
bridge = FirmwareBridge()