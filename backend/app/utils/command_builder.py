
from app.utils.protocol import UARTProtocol
 
class CommandBuilder:
    """Helper class to build exact Excel format commands"""
    # ============ POWER MODULE COMMANDS ============
    @staticmethod
    def laptop_power_on(angle: float, time: float) -> str:
        """PWR_ON_LT:<ANGLE>,<TIME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_ON_LT, angle, time)
    @staticmethod
    def laptop_power_off(angle: float, time: float) -> str:
        """PWR_OFF_LT:<ANGLE>,<TIME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_OFF_LT, angle, time)
    @staticmethod
    def laptop_restart(angle: float, time_on: float, wait_time: float, time_off: float) -> str:
        """PWR_RST_LT:<ANGLE>,<TIME_ON>,<WAIT>,<TIME_OFF>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_RST_LT, angle, time_on, wait_time, time_off)
    @staticmethod
    def laptop_status() -> str:
        """PWR_STATUS_LT;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_STATUS_LT)
    @staticmethod
    def desktop_power_on(time: float) -> str:
        """PWR_ON_DT:<TIME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_ON_DT, time)
    @staticmethod
    def desktop_power_off(time: float) -> str:
        """PWR_OFF_DT:<TIME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_OFF_DT, time)
    @staticmethod
    def desktop_restart(pulse_time: float) -> str:
        """PWR_RST_DT:<PULSE_TIME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_RST_DT, pulse_time)
    @staticmethod
    def desktop_status() -> str:
        """PWR_STATUS_DT;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_STATUS_DT)
    @staticmethod
    def crb_power_on(time: float) -> str:
        """PWR_ON_CRB:<TIME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_ON_CRB, time)
    @staticmethod
    def crb_power_off(time: float) -> str:
        """PWR_OFF_CRB:<TIME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_OFF_CRB, time)
    @staticmethod
    def crb_restart(pulse_time: float) -> str:
        """PWR_RST_CRB:<PULSE_TIME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_RST_CRB, pulse_time)
    @staticmethod
    def crb_status() -> str:
        """PWR_STATUS_CRB;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_STATUS_CRB)
    @staticmethod
    def ac_power_on() -> str:
        """PWR_ON_AC;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_ON_AC)
    @staticmethod
    def ac_power_off() -> str:
        """PWR_OFF_AC;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_OFF_AC)
    @staticmethod
    def ac_power_status() -> str:
        """PWR_STATUS_AC;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWR_STATUS_AC)
    @staticmethod
    def module_status(module_number: int) -> str:
        """MODULE_STATUS:<ModuleNumber>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_MODULE_STATUS, module_number)
    # ============ DISPLAY MODULE COMMANDS ============
    @staticmethod
    def hotplug_dp1() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_DP_1)
    @staticmethod
    def hotplug_dp2() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_DP_2)
    @staticmethod
    def hotplug_hdmi1() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_HDMI_1)
    @staticmethod
    def hotplug_hdmi2() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_HDMI_2)
    @staticmethod
    def hotplug_usb4_1() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_USB4_1)
    @staticmethod
    def hotplug_usb4_2() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_USB4_2)
    @staticmethod
    def unplug_dp1() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_DP_1)
    @staticmethod
    def unplug_dp2() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_DP_2)
    @staticmethod
    def unplug_hdmi1() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_HDMI_1)
    @staticmethod
    def unplug_hdmi2() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_HDMI_2)
    @staticmethod
    def unplug_usb4_1() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_USB4_1)
    @staticmethod
    def unplug_usb4_2() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_USB4_2)
    @staticmethod
    def plug_status_dp1() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_PLUG_STATUS_DP_1)
    @staticmethod
    def plug_status_dp2() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_PLUG_STATUS_DP_2)
    @staticmethod
    def plug_status_hdmi1() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_PLUG_STATUS_HDMI_1)
    @staticmethod
    def plug_status_hdmi2() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_PLUG_STATUS_HDMI_2)
    @staticmethod
    def plug_status_usb1() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_PLUG_STATUS_USB_1)
    @staticmethod
    def plug_status_usb2() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_PLUG_STATUS_USB_2)
    @staticmethod
    def lid_open_laptop(angle: float) -> str:
        """LID_OPEN_LT:<ANGLE>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_LID_OPEN_LT, angle)
    @staticmethod
    def lid_close_laptop(angle: float, press_time: float) -> str:
        """LID_CLOSE_LT:<ANGLE>,<PRESSTIME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_LID_CLOSE_LT, angle, press_time)
    @staticmethod
    def lid_open_crb() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_LID_OPEN_CRB)
    @staticmethod
    def lid_close_crb() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_LID_CLOSE_CRB)
    @staticmethod
    def read_display_properties() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_READ_DISP_PROP)
    # ============ CAMERA MODULE COMMANDS ============
    @staticmethod
    def rgb_set(led_id: int, r: int, g: int, b: int) -> str:
        """RGB_SET:<LED_ID>,<R>,<G>,<B>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_RGB_SET, led_id, r, g, b)
    @staticmethod
    def rgb_off(led_id: int) -> str:
        """RGB_OFF:<LED_ID>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_RGB_OFF, led_id)
    @staticmethod
    def stepper_move(direction: str, steps: int, speed_ms: int) -> str:
        """STEPPER_MOVE:<DIR>,<STEPS>,<SPEED_MS>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_STEPPER_MOVE, direction, steps, speed_ms)
    @staticmethod
    def stepper_stop() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_STEPPER_STOP)
    @staticmethod
    def light_read() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_LIGHT_READ)
    # ============ AUDIO/BT MODULE COMMANDS ============
    @staticmethod
    def hotplug_35mm() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_3_5_MM)
    @staticmethod
    def unplug_35mm() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_3_5_MM)
    @staticmethod
    def hotplug_usb_a() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_USB_A)
    @staticmethod
    def unplug_usb_a() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_USB_A)
    @staticmethod
    def hotplug_usb_c() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_USB_C)
    @staticmethod
    def unplug_usb_c() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_USB_C)
    @staticmethod
    def hotplug_hdmi_audio() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_HDMI)
    @staticmethod
    def unplug_hdmi_audio() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_HDMI)
    @staticmethod
    def bt_turn_on() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_TURN_ON_BT)
    @staticmethod
    def bt_turn_off() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_TURN_OFF_BT)
    @staticmethod
    def bt_change_name(new_name: str) -> str:
        """CHANGE_BT_NAME:<NEW_NAME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_CHANGE_BT_NAME, new_name)
    @staticmethod
    def bt_enable_pairing() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_EN_BT_PARING_MODE)
    @staticmethod
    def bt_connection_status() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_CONNECTION_STATUS)
    @staticmethod
    def bt_connect() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_CONNECT)
    @staticmethod
    def bt_disconnect() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_DISCONNECT)
    @staticmethod
    def bt_audio_up() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_AUDIO_UP)
    @staticmethod
    def bt_audio_down() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_AUDIO_DOWN)
    @staticmethod
    def bt_audio_mute() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_AUDIO_MUTE)
    @staticmethod
    def bt_audio_unmute() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_AUDIO_UNMUTE)
    @staticmethod
    def bt_play() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_PLAY)
    @staticmethod
    def bt_pause() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_PAUSE)
    @staticmethod
    def bt_next() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_NEXT)
    @staticmethod
    def bt_previous() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_PREVIOUS)
    @staticmethod
    def bt_get_logs() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_BT_AUDIO_GET_LOGS)
    
    # ============ NEW: RPI COMMANDS ============
    @staticmethod
    def get_rpi_ip() -> str:
        """GET_RPI_IP; - Get Raspberry Pi IP address"""
        return UARTProtocol.build_command(UARTProtocol.CMD_GET_RPI_IP)
    @staticmethod
    def get_rpi_mac() -> str:
        """GET_RPI_MAC; - Get Raspberry Pi MAC address"""
        return UARTProtocol.build_command(UARTProtocol.CMD_GET_RPI_MAC)
    @staticmethod
    def get_rpi_info() -> str:
        """GET_RPI_INFO; - Get both IP and MAC address"""
        return UARTProtocol.build_command(UARTProtocol.CMD_GET_RPI_INFO)
    @staticmethod
    def rpi_status() -> str:
        """RPI_STATUS; - Get Raspberry Pi connection status"""
        return UARTProtocol.build_command(UARTProtocol.CMD_RPI_STATUS)
    
        # ============ HOST MODULE COMMANDS ============
    @staticmethod
    def host_control(device: str, action: str) -> str:
        """HST:DEVICE:ACTION; - Control host device"""
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
        return UARTProtocol.build_command(UARTProtocol.CMD_HOST_CONTROL, device_id, action_id)
    @staticmethod
    def host_status(device: str) -> str:
        """HST_STATUS:DEVICE; - Get host device status"""
        device_map = {
            "System Server": "01",
            "Database Server": "02",
            "Application Server": "03",
            "Backup Server": "04"
        }
        device_id = device_map.get(device, "00")
        return UARTProtocol.build_command(UARTProtocol.CMD_HOST_STATUS, device_id)
    @staticmethod
    def all_hosts_status() -> str:
        """HST_STATUS_ALL; - Get status of all host devices"""
        return UARTProtocol.build_command(UARTProtocol.CMD_HOST_STATUS_ALL)
    

    # ============ COMBINATIONAL COMMANDS ============
    @staticmethod
    def power_on_with_delay(time: float) -> str:
        """PWRON_WITH_DELAY:<TIME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_PWRON_WITH_DELAY, time)
    @staticmethod
    def close_lid_power_on_sut() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_CLOSE_LID_PWRON_SUT)
    @staticmethod
    def close_n_open_lid_power_on_sut() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_CLOSE_N_OPEN_LID_PWRON_SUT)
    @staticmethod
    def close_lid_wait_open_lid(time: float) -> str:
        """CLOSE_LID_WAIT_OPEN_LID:<TIME>;"""
        return UARTProtocol.build_command(UARTProtocol.CMD_CLOSE_LID_WAIT_OPEN_LID, time)
    @staticmethod
    def close_lid_hotplug_all_dps_n_open_lid_power_on_sut() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_CLOSE_LID_HOTPLUG_ALL_DPS_N_OPEN_LID_PWRDON_SUT)
    @staticmethod
    def hotplug_all_ports() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_HOTPLUG_ALL_PORTS)
    @staticmethod
    def unplug_all_ports() -> str:
        return UARTProtocol.build_command(UARTProtocol.CMD_UNPLUG_ALL_PORTS)