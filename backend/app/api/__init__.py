from app.api import power, display, audio, isp, host
 
# List of modules to export when using "from app.api import *"
__all__ = [
    'power',
    'display',
    'audio',
    'isp',
    'host'
]
 
# Package metadata
__version__ = "1.0.0"
__description__ = "API routes for device control"
 
# Router factory function
def get_all_routers():
    """Return list of all API routers for registration in main.py"""
    return [
        power.router,
        display.router,
        audio.router,
        isp.router,
        host.router
    ]
 
# Router prefix mapping
ROUTER_PREFIXES = {
    "power": "/api/power",
    "display": "/api/display",
    "audio": "/api/audio",
    "isp": "/api/isp",
    "host": "/api/host"
}