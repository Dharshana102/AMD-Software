from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

# ============ POWER MODULE SCHEMAS ============

class LaptopPowerRequest(BaseModel):
    angle: float = Field(..., ge=0, le=180, description="Angle in degrees (0-180)")
    time: float = Field(..., ge=1, le=60, description="Time in seconds (1-60)")


class DesktopPowerRequest(BaseModel):
    time: float = Field(..., ge=1, le=5, description="Time in seconds (1-5)")


class CRBPowerRequest(BaseModel):
    time: float = Field(..., ge=1, le=5, description="Time in seconds (1-5)")


class RestartRequest(BaseModel):
    pulse_time: float = Field(..., ge=1, le=60, description="Pulse time in seconds")


class LaptopRestartRequest(BaseModel):
    angle: float = Field(..., ge=0, le=180)
    time_on: float = Field(..., ge=1, le=60)
    wait_time: float = Field(..., ge=1, le=60)
    time_off: float = Field(..., ge=1, le=60)


# ============ DISPLAY MODULE SCHEMAS ============

class LidControlRequest(BaseModel):
    angle: float = Field(..., ge=0, le=180)
    press_time: Optional[float] = Field(None, ge=1, le=300)


# ============ CAMERA MODULE SCHEMAS ============

class RGBSetRequest(BaseModel):
    led_id: int = Field(..., ge=1, le=2)
    r: int = Field(..., ge=0, le=255)
    g: int = Field(..., ge=0, le=255)
    b: int = Field(..., ge=0, le=255)


class StepperMoveRequest(BaseModel):
    direction: Literal["CW", "CCW"]
    steps: int = Field(..., ge=1, le=2048)
    speed_ms: int = Field(..., ge=1, le=500)


# ============ AUDIO/BT MODULE SCHEMAS ============

class BTNameRequest(BaseModel):
    new_name: str = Field(..., min_length=1, max_length=50)


# ============ HOST MODULE SCHEMAS ============

class HostControlRequest(BaseModel):
    device: Literal["System Server", "Database Server", "Application Server", "Backup Server"]
    action: Literal["on", "off", "restart"]


# ============ RESPONSE SCHEMAS ============

class PowerStatusResponse(BaseModel):
    device: str
    status: Literal["online", "offline"]
    voltage: Optional[float] = None
    timestamp: datetime


class DisplayPropertiesResponse(BaseModel):
    R: int
    G: int
    B: int
    C: int
    LUX: float
    CT: int
    K_INT: int
    timestamp: datetime


class LightSensorResponse(BaseModel):
    adc: int
    lux: float
    timestamp: datetime


class BTStatusResponse(BaseModel):
    status: Literal["ON", "OFF", "CONNECTED", "PAIRING_MODE"]
    device_name: Optional[str] = None
    timestamp: datetime