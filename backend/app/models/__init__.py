from app.models.schemas import (
    # Power module schemas
    LaptopPowerRequest,
    DesktopPowerRequest,
    CRBPowerRequest,
    RestartRequest,
    LaptopRestartRequest,
    PowerStatusResponse,
    # Display module schemas
    LidControlRequest,
    DisplayPropertiesResponse,
    # Camera/ISP module schemas
    RGBSetRequest,
    StepperMoveRequest,
    LightSensorResponse,
    # Audio/BT module schemas
    BTNameRequest,
    BTStatusResponse,
    # Host module schemas
    HostControlRequest
)
 
# Group schemas by module for organized access
POWER_SCHEMAS = [
    'LaptopPowerRequest',
    'DesktopPowerRequest',
    'CRBPowerRequest',
    'RestartRequest',
    'LaptopRestartRequest',
    'PowerStatusResponse'
]
 
DISPLAY_SCHEMAS = [
    'LidControlRequest',
    'DisplayPropertiesResponse'
]
 
CAMERA_SCHEMAS = [
    'RGBSetRequest',
    'StepperMoveRequest',
    'LightSensorResponse'
]
 
AUDIO_SCHEMAS = [
    'BTNameRequest',
    'BTStatusResponse'
]
 
HOST_SCHEMAS = [
    'HostControlRequest'
]
 
__all__ = (
    POWER_SCHEMAS +
    DISPLAY_SCHEMAS +
    CAMERA_SCHEMAS +
    AUDIO_SCHEMAS +
    HOST_SCHEMAS
)
 
__version__ = "1.0.0"
__description__ = "Pydantic data models for request/response validation"