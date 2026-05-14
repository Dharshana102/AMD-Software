from app.utils.protocol import UARTProtocol
from app.utils.command_builder import CommandBuilder
 
__all__ = [
    'UARTProtocol',
    'CommandBuilder'
]
 
# Package metadata
__version__ = "1.0.0"
__description__ = "Utility functions and protocol definitions"
 
# Import logging for initialization
import logging
 
logger = logging.getLogger(__name__)
logger.info(f"Utils package initialized with protocol v{__version__}")
 
# Protocol version (should match firmware protocol version)
PROTOCOL_VERSION = "1.0.0"
 
# Command/response format documentation
PROTOCOL_DOC = """
UART Communication Protocol (Excel Sheet Format):
- Baudrate: 115200
- Data bits: 8
- Parity: None
- Stop bits: 1
- Command format: [COMMAND]:[ARG1],[ARG2];\\n
- Response format: [RESPONSE]:[VALUE];\\n
 
Example Commands:
- PWR_ON_LT:45,10;
- PWR_STATUS_LT;
- HOTPLUG_DP_1;
- READ_DISP_PROP;
- RGB_SET:1,255,128,0;
- STEPPER_MOVE:CW,1024,100;
- TURN_ON_BT;
"""
 
# Export protocol documentation
__doc__ = PROTOCOL_DOC