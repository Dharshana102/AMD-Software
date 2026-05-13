__version__ = "1.0.0"
__author__ = "Device Control Team"
__description__ = "Industrial Device Control System"
 
# Package initialization
import logging
 
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
 
logger.info(f"Initializing {__name__} package v{__version__}")
 
# Expose main components for easier imports
from app.infrastructure.uart_comm import uart
from app.services.firmware_bridge import bridge
 
__all__ = [
    'uart',
    'bridge',
    '__version__',
    '__author__',
    '__description__'
]