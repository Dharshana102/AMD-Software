import serial
import serial.tools.list_ports
import threading
import queue
import time
from typing import Optional
import os
from dotenv import load_dotenv
 
load_dotenv()
 
 
class UARTCommunication:
    """UART communication handler for C firmware"""
    def __init__(self):
        # Read UART configuration from environment variables
        self.port = os.getenv("UART_PORT", "/dev/ttyUSB0")
        self.baudrate = int(os.getenv("UART_BAUDRATE", 115200))
        self.timeout = int(os.getenv("UART_TIMEOUT", 2))
        self.bytesize = int(os.getenv("UART_BYTESIZE", 8))
        self.parity = os.getenv("UART_PARITY", "N")
        self.stopbits = float(os.getenv("UART_STOPBITS", 1))
        self.serial_conn: Optional[serial.Serial] = None
        self.response_queue = queue.Queue()
        self.running = False
        self.read_thread: Optional[threading.Thread] = None
        self.connected = False
        # Read RPi configuration from .env file
        self.rpi_ip = os.getenv("RPI_IP", "192.168.1.100")
        self.rpi_mac = os.getenv("RPI_MAC", "AA:BB:CC:DD:EE:FF")
        self.rpi_status = os.getenv("RPI_STATUS", "online")
        # Parity mapping for pyserial
        self.parity_map = {
            'N': serial.PARITY_NONE,
            'E': serial.PARITY_EVEN,
            'O': serial.PARITY_ODD
        }
    def list_available_ports(self) -> list:
        """List all available serial ports for debugging"""
        try:
            ports = serial.tools.list_ports.comports()
            return [{"port": port.device, "description": port.description} for port in ports]
        except Exception as e:
            return [{"error": str(e)}]
    def connect(self) -> bool:
        """Establish UART connection with firmware"""
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout,
                write_timeout=self.timeout,
                bytesize=self.bytesize,
                parity=self.parity_map.get(self.parity, serial.PARITY_NONE),
                stopbits=self.stopbits
            )
            if self.serial_conn.is_open:
                self.connected = True
                self.running = True
                # Start response reading thread
                self.read_thread = threading.Thread(target=self._read_loop, daemon=True)
                self.read_thread.start()
                print(f"[UART] Connected to {self.port} @ {self.baudrate} baud")
                return True
            return False
        except serial.SerialException as e:
            print(f"[UART] Connection failed: {e}")
            return False
        except Exception as e:
            print(f"[UART] Unexpected error: {e}")
            return False
    def _read_loop(self):
        """Continuous read thread for UART responses from firmware"""
        buffer = ""
        while self.running and self.serial_conn and self.serial_conn.is_open:
            try:
                if self.serial_conn.in_waiting > 0:
                    # Read raw bytes
                    raw_data = self.serial_conn.read(self.serial_conn.in_waiting)
                    # Decode to string (firmware sends ASCII/UTF-8)
                    try:
                        data = raw_data.decode('utf-8', errors='ignore')
                        buffer += data
                        # Process complete lines (firmware sends newline terminated responses)
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            if line:
                                self.response_queue.put(line)
                                print(f"[UART] Received: {line}")
                    except UnicodeDecodeError:
                        # Handle binary data if needed
                        print(f"[UART] Raw binary data: {raw_data.hex()}")
                time.sleep(0.01)  # Small delay to prevent CPU overuse
            except Exception as e:
                print(f"[UART] Read error: {e}")
                time.sleep(0.1)
    def send_command(self, command: str, wait_response: bool = True, timeout: int = None) -> dict:
        """
        Send command to firmware via UART and wait for response
        Args:
            command: Command string (firmware expects newline terminated)
            wait_response: Whether to wait for response
            timeout: Response timeout in seconds
        Returns:
            Dictionary with success status and response data
        """
        if not self.connected or not self.serial_conn or not self.serial_conn.is_open:
            return {"success": False, "error": "UART not connected"}
        try:
            # Clear any pending responses before sending
            while not self.response_queue.empty():
                try:
                    self.response_queue.get_nowait()
                except queue.Empty:
                    break
            # Send command with newline (C firmware expects this format)
            command_with_newline = f"{command}\n"
            bytes_sent = self.serial_conn.write(command_with_newline.encode('utf-8'))
            self.serial_conn.flush()
            print(f"[UART] Sent: {command}")
            if not wait_response:
                return {"success": True, "message": "Command sent", "bytes_sent": bytes_sent}
            # Wait for response
            timeout_value = timeout or self.timeout
            response = self.response_queue.get(timeout=timeout_value)
            return {"success": True, "response": response, "raw_command": command}
        except queue.Empty:
            return {"success": False, "error": f"No response from firmware (timeout: {timeout_value}s)"}
        except serial.SerialTimeoutException:
            return {"success": False, "error": "UART write timeout"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    def send_binary_command(self, command_bytes: bytes, wait_response: bool = True, timeout: int = None) -> dict:
        """Send binary command to firmware (alternative to string commands)"""
        if not self.connected or not self.serial_conn or not self.serial_conn.is_open:
            return {"success": False, "error": "UART not connected"}
        try:
            # Clear queue
            while not self.response_queue.empty():
                try:
                    self.response_queue.get_nowait()
                except queue.Empty:
                    break
            # Send binary data
            bytes_sent = self.serial_conn.write(command_bytes)
            self.serial_conn.flush()
            print(f"[UART] Sent (binary): {command_bytes.hex()}")
            if not wait_response:
                return {"success": True, "message": "Binary command sent", "bytes_sent": bytes_sent}
            # Wait for response
            timeout_value = timeout or self.timeout
            response = self.response_queue.get(timeout=timeout_value)
            return {"success": True, "response": response, "raw_bytes": command_bytes}
        except queue.Empty:
            return {"success": False, "error": f"No response from firmware (timeout: {timeout_value}s)"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    def read_response(self, timeout: int = None) -> Optional[str]:
        """Read single response from queue without sending command"""
        try:
            timeout_value = timeout or self.timeout
            response = self.response_queue.get(timeout=timeout_value)
            return response
        except queue.Empty:
            return None
    def flush_buffer(self):
        """Flush UART buffer"""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.reset_input_buffer()
            self.serial_conn.reset_output_buffer()
        # Clear queue
        while not self.response_queue.empty():
            try:
                self.response_queue.get_nowait()
            except queue.Empty:
                break
    def disconnect(self):
        """Close UART connection"""
        self.running = False
        if self.read_thread and self.read_thread.is_alive():
            self.read_thread.join(timeout=2)
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
        self.connected = False
        print("[UART] Disconnected")
    def is_connected(self) -> bool:
        """Check if UART is connected"""
        return self.connected and self.serial_conn and self.serial_conn.is_open
 
 
# ================================================================
# SIMULATION MODE - For testing without hardware
# ================================================================
 
class UARTSimulation:
    """Simulate UART communication for testing without hardware"""
    def __init__(self):
        self.connected = False
        # Read RPi configuration from .env file (not hardcoded)
        self.rpi_ip = os.getenv("RPI_IP", "192.168.1.100")
        self.rpi_mac = os.getenv("RPI_MAC", "AA:BB:CC:DD:EE:FF")
        self.rpi_status = os.getenv("RPI_STATUS", "online")
        self.device_states = {
            "Laptop OEM": "offline",
            "Desktop": "offline",
            "CRB": "offline",
            "DP_1": "unplugged",
            "DP_2": "unplugged",
            "HDMI_1": "unplugged",
            "HDMI_2": "unplugged",
            "USB4_1": "unplugged",
            "USB4_2": "unplugged",
        }
    def list_available_ports(self) -> list:
        return [{"port": "SIMULATION", "description": "Simulation mode - No hardware"}]
    def connect(self) -> bool:
        self.connected = True
        print("[SIM] UART Simulation Mode - Connected (No hardware)")
        print(f"[SIM] RPi IP configured: {self.rpi_ip}")
        print(f"[SIM] RPi MAC configured: {self.rpi_mac}")
        return True
    def send_command(self, command: str, wait_response: bool = True, timeout: int = None) -> dict:
        print(f"[SIM] Sending: {command}")
        if not wait_response:
            return {"success": True, "message": "Command sent (simulation)"}
        # Simulate response based on command
        command_upper = command.upper()
        # ============ RPI COMMANDS (from .env file) ============
        if "GET_RPI_IP" in command_upper:
            return {"success": True, "response": f"IP:{self.rpi_ip};"}
        elif "GET_RPI_MAC" in command_upper:
            return {"success": True, "response": f"MAC:{self.rpi_mac};"}
        elif "GET_RPI_INFO" in command_upper:
            return {"success": True, "response": f"IP:{self.rpi_ip}, MAC:{self.rpi_mac};"}
        elif "RPI_STATUS" in command_upper:
            return {"success": True, "response": f"RPI_STATUS:{self.rpi_status.upper()};"}
        # ============ POWER COMMANDS ============
        elif "PWR_ON_LT" in command_upper:
            return {"success": True, "response": "LAPTOP POWERED ON;"}
        elif "PWR_OFF_LT" in command_upper:
            return {"success": True, "response": "LAPTOP POWERED OFF;"}
        elif "PWR_STATUS_LT" in command_upper:
            return {"success": True, "response": "LAPTOP POWERED: ON, 230V;"}
        elif "PWR_ON_DT" in command_upper:
            return {"success": True, "response": "DESKTOP POWERED ON;"}
        elif "PWR_STATUS_DT" in command_upper:
            return {"success": True, "response": "DESKTOP POWERED: ON, 220V;"}
        elif "PWR_ON_CRB" in command_upper:
            return {"success": True, "response": "CRB POWERED ON;"}
        elif "PWR_ON_AC" in command_upper:
            return {"success": True, "response": "AC ON;"}
        elif "PWR_OFF_AC" in command_upper:
            return {"success": True, "response": "AC OFF;"}
        elif "PWR_STATUS_AC" in command_upper:
            return {"success": True, "response": "AC:ON, 230V;"}
        # ============ DISPLAY COMMANDS ============
        elif "HOTPLUG_DP_1" in command_upper:
            return {"success": True, "response": "DP_1 HOTPLUGED;"}
        elif "HOTPLUG_HDMI_1" in command_upper:
            return {"success": True, "response": "HDMI_1 HOTPLUGED;"}
        elif "UNPLUG_DP_1" in command_upper:
            return {"success": True, "response": "DP_1 UNPLUGED;"}
        elif "PLUG_STATUS_DP_1" in command_upper:
            return {"success": True, "response": "DP_1:PLUGED;"}
        elif "READ_DISP_PROP" in command_upper:
            return {"success": True, "response": "R:100, G:150, B:200, C:50, LUX:450, CT:6500, K INT:500;"}
        elif "LID_OPEN_LT" in command_upper:
            return {"success": True, "response": "LID_OPENED;"}
        elif "LID_CLOSE_LT" in command_upper:
            return {"success": True, "response": "LID_CLOSED;"}
        # ============ CAMERA COMMANDS ============
        elif "RGB_SET" in command_upper:
            return {"success": True, "response": "RGB LED 1 SET : R:230, G:153, B:176;"}
        elif "RGB_OFF" in command_upper:
            return {"success": True, "response": "RGB LED 1 OFF;"}
        elif "STEPPER_MOVE" in command_upper:
            return {"success": True, "response": "STEPPER MOVED CW STEPS:1024"}
        elif "STEPPER_STOP" in command_upper:
            return {"success": True, "response": "STEPPER_STOPPED;"}
        elif "LIGHT_READ" in command_upper:
            return {"success": True, "response": "ADC: 512, LUX: 450;"}
        # ============ AUDIO/BT COMMANDS ============
        elif "HOTPLUG_3_5_MM" in command_upper:
            return {"success": True, "response": "3.5_MM_HOTPLUGGED;"}
        elif "TURN_ON_BT" in command_upper:
            return {"success": True, "response": "BT_TURNED_ON;"}
        elif "TURN_OFF_BT" in command_upper:
            return {"success": True, "response": "BT_TURNED_OFF;"}
        elif "BT_CONNECTION_STATUS" in command_upper:
            return {"success": True, "response": "CONNECTED;"}
        elif "BT_AUDIO_UP" in command_upper:
            return {"success": True, "response": "BT_AUDIO_VOL-INCREASED;"}
        elif "BT_PLAY" in command_upper:
            return {"success": True, "response": "BT_PLAYED;"}
        # ============ HOST COMMANDS ============
        elif "HST_STATUS_ALL" in command_upper:
            return {"success": True, "response": "ALL_HOSTS:ONLINE,ONLINE,OFFLINE,ONLINE;"}
        elif "HST_STATUS:" in command_upper:
            return {"success": True, "response": "HOST_STATUS:ONLINE;"}
        # ============ MODULE STATUS ============
        elif "MODULE_STATUS" in command_upper:
            return {"success": True, "response": "ONLINE;"}
        # ============ COMBINATIONAL COMMANDS ============
        elif "HOTPLUG_ALL_PORTS" in command_upper:
            return {"success": True, "response": "HOTPLUGED_ALL_PORTS;"}
        elif "UNPLUG_ALL_PORTS" in command_upper:
            return {"success": True, "response": "UNPLUGED_ALL_PORTS;"}
        # ============ DEFAULT RESPONSE ============
        else:
            return {"success": True, "response": "OK:1;"}
    def disconnect(self):
        self.connected = False
        print("[SIM] UART Simulation Disconnected")
    def is_connected(self) -> bool:
        return self.connected
 
 
# ================================================================
# FACTORY FUNCTION - Get appropriate UART interface
# ================================================================
 
def get_uart_interface():
    """Get appropriate UART interface based on configuration"""
    comm_mode = os.getenv("COMM_MODE", "simulation").lower()
    if comm_mode == "simulation":
        print("[UART] Running in SIMULATION mode")
        return UARTSimulation()
    elif comm_mode == "uart":
        print("[UART] Running in UART mode")
        return UARTCommunication()
    else:
        print(f"[UART] Unknown mode '{comm_mode}', falling back to SIMULATION")
        return UARTSimulation()
 
 
# Create global UART instance
uart = get_uart_interface()