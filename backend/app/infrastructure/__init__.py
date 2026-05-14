from app.infrastructure.uart_comm import (
    UARTCommunication,
    UARTSimulation,
    get_uart_interface,
    uart
)
 
__all__ = [
    'UARTCommunication',
    'UARTSimulation', 
    'get_uart_interface',
    'uart'
]
 
# Package initialization
import os
import logging
 
logger = logging.getLogger(__name__)
 
# Log communication mode on import
comm_mode = os.getenv("COMM_MODE", "simulation")
logger.info(f"Infrastructure initialized with COMM_MODE: {comm_mode}")
 
if comm_mode == "simulation":
    logger.warning("Running in SIMULATION mode - no hardware communication")
else:
    logger.info(f"Running in {comm_mode.upper()} mode for hardware communication")
 
__version__ = "1.0.0"
__description__ = "Hardware communication infrastructure"