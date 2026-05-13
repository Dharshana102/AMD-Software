"""
UART Protocol Definition - Matches Excel Sheet Commands Exactly
 
Command Format: [COMMAND]:[ARG1],[ARG2],[ARG3];
Response Format: [STATUS]:[VALUE];
 
Examples from Excel:
- Send: PWR_ON_LT:45,5;
- Receive: LAPTOP POWERED ON;
 
- Send: READ_DISP_PROP;
- Receive: R:100, G:150, B:200, C:50, LUX:450, CT:6500, K INT:500;
"""
 
class UARTProtocol:
    """Protocol constants matching Excel sheet commands"""
    # ============ MODULE 0: Raspberry Pi ============
    CMD_DISPLAY_WELCOME = "DISPLAY_WELCOME"
    CMD_GET_IP_ADDRESS = "GET_IP_ADDRESS"
    # ============ MODULE 1: POWER COMMANDS ============
    # Laptop OEM Commands
    CMD_PWR_ON_LT = "PWR_ON_LT"           # PWR_ON_LT:<ANGLE>,<TIME>;
    CMD_PWR_OFF_LT = "PWR_OFF_LT"         # PWR_OFF_LT:<ANGLE>,<TIME>;
    CMD_PWR_RST_LT = "PWR_RST_LT"         # PWR_RST_LT:<ANGLE>,<TIME_ON>,<WAIT>,<TIME_OFF>;
    CMD_PWR_STATUS_LT = "PWR_STATUS_LT"   # PWR_STATUS_LT;
    # Desktop Commands
    CMD_PWR_ON_DT = "PWR_ON_DT"           # PWR_ON_DT:<TIME>;
    CMD_PWR_OFF_DT = "PWR_OFF_DT"         # PWR_OFF_DT:<TIME>;
    CMD_PWR_RST_DT = "PWR_RST_DT"         # PWR_RST_DT:<PULSE_TIME>;
    CMD_PWR_STATUS_DT = "PWR_STATUS_DT"   # PWR_STATUS_DT;
    # CRB Commands
    CMD_PWR_ON_CRB = "PWR_ON_CRB"         # PWR_ON_CRB:<TIME>;
    CMD_PWR_OFF_CRB = "PWR_OFF_CRB"       # PWR_OFF_CRB:<TIME>;
    CMD_PWR_RST_CRB = "PWR_RST_CRB"       # PWR_RST_CRB:<PULSE_TIME>;
    CMD_PWR_STATUS_CRB = "PWR_STATUS_CRB" # PWR_STATUS_CRB;
    # AC Power Commands
    CMD_PWR_ON_AC = "PWR_ON_AC"           # PWR_ON_AC;
    CMD_PWR_OFF_AC = "PWR_OFF_AC"         # PWR_OFF_AC;
    CMD_PWR_STATUS_AC = "PWR_STATUS_AC"   # PWR_STATUS_AC;
    # Module Status
    CMD_MODULE_STATUS = "MODULE_STATUS"   # MODULE_STATUS:<ModuleNumber>;
    # ============ MODULE 2: DISPLAY COMMANDS ============
    # Hotplug Commands
    CMD_HOTPLUG_DP_1 = "HOTPLUG_DP_1"
    CMD_HOTPLUG_DP_2 = "HOTPLUG_DP_2"
    CMD_HOTPLUG_HDMI_1 = "HOTPLUG_HDMI_1"
    CMD_HOTPLUG_HDMI_2 = "HOTPLUG_HDMI_2"
    CMD_HOTPLUG_USB4_1 = "HOTPLUG_USB4_1"
    CMD_HOTPLUG_USB4_2 = "HOTPLUG_USB4_2"
    # Unplug Commands
    CMD_UNPLUG_DP_1 = "UNPLUG_DP_1"
    CMD_UNPLUG_DP_2 = "UNPLUG_DP_2"
    CMD_UNPLUG_HDMI_1 = "UNPLUG_HDMI_1"
    CMD_UNPLUG_HDMI_2 = "UNPLUG_HDMI_2"
    CMD_UNPLUG_USB4_1 = "UNPLUG_USB4_1"
    CMD_UNPLUG_USB4_2 = "UNPLUG_USB4_2"
    # Plug Status Commands
    CMD_PLUG_STATUS_DP_1 = "PLUG_STATUS_DP_1"
    CMD_PLUG_STATUS_DP_2 = "PLUG_STATUS_DP_2"
    CMD_PLUG_STATUS_HDMI_1 = "PLUG_STATUS_HDMI_1"
    CMD_PLUG_STATUS_HDMI_2 = "PLUG_STATUS_HDMI_2"
    CMD_PLUG_STATUS_USB_1 = "PLUG_STATUS_USB_1"
    CMD_PLUG_STATUS_USB_2 = "PLUG_STATUS_USB_2"
    # LID Commands
    CMD_LID_OPEN_LT = "LID_OPEN_LT"           # LID_OPEN_LT:<ANGLE>;
    CMD_LID_CLOSE_LT = "LID_CLOSE_LT"         # LID_CLOSE_LT:<ANGLE>,<PRESSTIME>;
    CMD_LID_OPEN_CRB = "LID_OPEN_CRB"
    CMD_LID_CLOSE_CRB = "LID_CLOSE_CRB"
    # Display Properties
    CMD_READ_DISP_PROP = "READ_DISP_PROP"     # READ_DISP_PROP;
    # ============ MODULE 3: CAMERA COMMANDS ============
    CMD_RGB_SET = "RGB_SET"                   # RGB_SET:<LED_ID>,<R>,<G>,<B>;
    CMD_RGB_OFF = "RGB_OFF"                   # RGB_OFF:<LED_ID>;
    CMD_STEPPER_MOVE = "STEPPER_MOVE"         # STEPPER_MOVE:<DIR>,<STEPS>,<SPEED_MS>;
    CMD_STEPPER_STOP = "STEPPER_STOP"
    CMD_LIGHT_READ = "LIGHT_READ"
    # ============ MODULE 4: AUDIO/BT COMMANDS ============
    CMD_HOTPLUG_3_5_MM = "HOTPLUG_3_5_MM"
    CMD_UNPLUG_3_5_MM = "UNPLUG_3_5_MM"
    CMD_HOTPLUG_USB_A = "HOTPLUG_USB_A"
    CMD_UNPLUG_USB_A = "UNPLUG_USB_A"
    CMD_HOTPLUG_USB_C = "HOTPLUG_USB_C"
    CMD_UNPLUG_USB_C = "UNPLUG_USB_C"
    CMD_HOTPLUG_HDMI = "HOTPLUG_HDMI"
    CMD_UNPLUG_HDMI = "UNPLUG_HDMI"
    CMD_TURN_ON_BT = "TURN_ON_BT"
    CMD_TURN_OFF_BT = "TURN_OFF_BT"
    CMD_CHANGE_BT_NAME = "CHANGE_BT_NAME"     # CHANGE_BT_NAME:<NEW_NAME>;
    CMD_EN_BT_PARING_MODE = "EN_BT_PARING_MODE"
    CMD_BT_CONNECTION_STATUS = "BT_CONNECTION_STATUS"
    CMD_BT_CONNECT = "BT_CONNECT"
    CMD_BT_DISCONNECT = "BT_DISCONNECT"
    CMD_BT_AUDIO_UP = "BT_AUDIO_UP"
    CMD_BT_AUDIO_DOWN = "BT_AUDIO_DOWN"
    CMD_BT_AUDIO_MUTE = "BT_AUDIO_MUTE"
    CMD_BT_AUDIO_UNMUTE = "BT_AUDIO_UNMUTE"
    CMD_BT_PLAY = "BT_PLAY"
    CMD_BT_PAUSE = "BT_PAUSE"
    CMD_BT_NEXT = "BT_NEXT"
    CMD_BT_PREVIOUS = "BT_PREVIOUS"
    CMD_BT_AUDIO_GET_LOGS = "BT_AUDIO_GET_LOGS"
    # ============ COMBINATIONAL COMMANDS ============
    CMD_PWRON_WITH_DELAY = "PWRON_WITH_DELAY"                 # PWRON_WITH_DELAY:<TIME>;
    CMD_CLOSE_LID_PWRON_SUT = "CLOSE_LID_PWRON_SUT"
    CMD_CLOSE_N_OPEN_LID_PWRON_SUT = "CLOSE_N_OPEN_LID_PWRON_SUT"
    CMD_CLOSE_LID_WAIT_OPEN_LID = "CLOSE_LID_WAIT_OPEN_LID"   # CLOSE_LID_WAIT_OPEN_LID:<TIME>;
    CMD_CLOSE_LID_HOTPLUG_ALL_DPS_N_OPEN_LID_PWRDON_SUT = "CLOSE_LID_HOTPLUG_ALL_DPS_N_OPEN_LID_PWRDON_SUT"
    CMD_HOTPLUG_ALL_PORTS = "HOTPLUG_ALL_PORTS"
    CMD_UNPLUG_ALL_PORTS = "UNPLUG_ALL_PORTS"
    # ============ RESPONSE PARSING ============
    @staticmethod
    def build_command(command: str, *args) -> str:
        """
        Build command string in exact Excel format: COMMAND:ARG1,ARG2,ARG3;
        Examples:
        - build_command("PWR_ON_LT", 45, 10) → "PWR_ON_LT:45,10;"
        - build_command("PWR_STATUS_LT") → "PWR_STATUS_LT;"
        """
        # Filter out None or empty args
        valid_args = [str(arg).strip() for arg in args if arg is not None and str(arg).strip()]
        if not valid_args:
            return f"{command};"
        return f"{command}:{','.join(valid_args)};"
    @staticmethod
    def parse_response(response: str) -> dict:
        """
        Parse firmware response from Excel format
        Examples:
        - "LAPTOP POWERED ON;" → {"success": True, "message": "LAPTOP POWERED ON"}
        - "OK:1;" → {"success": True, "status": "OK", "value": "1"}
        - "ERR:TIMEOUT;" → {"success": False, "error": "TIMEOUT"}
        - "R:100, G:150, B:200, C:50, LUX:450, CT:6500, K INT:500;" → parsed sensor data
        """
        if not response:
            return {"success": False, "error": "Empty response"}
        response = response.strip().rstrip(';')
        # Check for error response
        if response.startswith("ERR:"):
            error_msg = response.split(":", 1)[1] if ":" in response else response
            return {"success": False, "error": error_msg}
        # Check for OK response
        if response.startswith("OK:"):
            value = response.split(":", 1)[1] if ":" in response else "1"
            return {"success": True, "status": "OK", "value": value}
        # Parse power status: "LAPTOP POWERED: ON, 230V;"
        if "POWERED:" in response:
            device = response.split("POWERED:")[0].strip()
            parts = response.split("POWERED:")[1].split(",")
            status = parts[0].strip().lower()
            voltage = parts[1].strip() if len(parts) > 1 else None
            return {
                "success": True,
                "type": "power_status",
                "device": device,
                "status": status,
                "voltage": voltage
            }
        # Parse AC status: "AC:ON, 230V;"
        if response.startswith("AC:"):
            parts = response.split(":")[1].split(",")
            status = parts[0].strip().lower()
            voltage = parts[1].strip() if len(parts) > 1 else None
            return {
                "success": True,
                "type": "ac_status",
                "status": status,
                "voltage": voltage
            }
        # Parse display properties: "R:100, G:150, B:200, C:50, LUX:450, CT:6500, K INT:500;"
        if "R:" in response and "G:" in response and "B:" in response:
            result = {"success": True, "type": "display_properties"}
            pairs = response.split(",")
            for pair in pairs:
                if ":" in pair:
                    key, val = pair.split(":", 1)
                    result[key.strip()] = val.strip()
            return result
        # Parse plug status: "DP_1:PLUGED;"
        if ":" in response and ("PLUGED" in response or "UNPLUGED" in response):
            parts = response.split(":", 1)
            return {
                "success": True,
                "type": "plug_status",
                "port": parts[0],
                "status": parts[1].rstrip(';').lower()
            }
        # Parse RGB response: "RGB LED 1 SET : R:230, G:153, B:176;"
        if "RGB LED" in response:
            return {
                "success": True,
                "type": "rgb_status",
                "message": response
            }
        # Parse stepper response: "STEPPER MOVED CW STEPS:1024"
        if "STEPPER" in response:
            return {
                "success": True,
                "type": "stepper_status",
                "message": response
            }
        # Parse light sensor: "ADC: 512, LUX: 450;"
        if "ADC:" in response and "LUX:" in response:
            adc_val = response.split("ADC:")[1].split(",")[0].strip()
            lux_val = response.split("LUX:")[1].split(";")[0].strip()
            return {
                "success": True,
                "type": "light_sensor",
                "adc": int(adc_val) if adc_val.isdigit() else adc_val,
                "lux": float(lux_val) if lux_val.replace('.', '').isdigit() else lux_val
            }
        # Parse BT status
        if "BT_" in response or "BLUETOOTH" in response.upper():
            return {
                "success": True,
                "type": "bt_status",
                "message": response
            }
        # Generic success - return raw response
        return {
            "success": True,
            "response": response,
            "message": response
        }