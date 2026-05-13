from app.services.power_service import power_service
from app.services.display_service import display_service
from app.services.audio_service import audio_service
from app.services.isp_service import isp_service
from app.services.host_service import host_service
from app.services.firmware_bridge import bridge
 
# Export all services for easy access
__all__ = [
    'power_service',
    'display_service',
    'audio_service',
    'isp_service',
    'host_service',
    'bridge'
]
 
# Package metadata
__version__ = "1.0.0"
__description__ = "Business logic services for device control"
 
# Service factory function
def get_service(service_name: str):
    """Get service instance by name"""
    services = {
        'power': power_service,
        'display': display_service,
        'audio': audio_service,
        'isp': isp_service,
        'host': host_service
    }
    return services.get(service_name)
 
# Service names for reference
SERVICE_NAMES = ['power', 'display', 'audio', 'isp', 'host']