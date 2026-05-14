"""
Device Control Backend Application
FastAPI server for controlling hardware devices via UART
"""
 
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api import command 
import logging
import os
from dotenv import load_dotenv
 
# Load environment variables
load_dotenv()
 
# Import API routers
from app.api import power, display, audio, isp, host
from app.infrastructure.uart_comm import uart


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
 
# Create FastAPI app
app = FastAPI(
    title="Device Control API",
    description="API for controlling hardware devices via UART communication",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
 
# Configure CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",      # Vite dev server
        "http://localhost:3000",
        "http://localhost:3004",   
              # React dev server
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3004",
        "http://192.168.1.*",         # Network access
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(command.router, prefix="/api", tags=["Command"]) # Configure logging
 
# ================================================================
# EVENT HANDLERS
# ================================================================
 
@app.on_event("startup")
async def startup_event():
    """Initialize UART connection on startup"""
    logger.info("Starting Device Control API...")
    # Try to connect to UART
    if not uart.is_connected():
        if uart.connect():
            logger.info("UART connection established successfully")
        else:
            logger.warning("UART connection failed - running in simulation mode")
 
 
@app.on_event("shutdown")
async def shutdown_event():
    """Close UART connection on shutdown"""
    logger.info("Shutting down Device Control API...")
    uart.disconnect()
    logger.info("UART connection closed")
 
 
# ================================================================
# ROOT ENDPOINTS
# ================================================================
 
@app.get("/")
async def root():
    """Root endpoint - API status"""
    return {
        "name": "Device Control API",
        "version": "1.0.0",
        "status": "running",
        "uart_connected": uart.is_connected(),
        "comm_mode": os.getenv("COMM_MODE", "simulation"),
        "endpoints": {
            "power": "/api/power",
            "display": "/api/display",
            "audio": "/api/audio",
            "isp": "/api/isp",
            "host": "/api/host"
        }
    }
 
 
@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "uart_connected": uart.is_connected(),
        "timestamp": import_time()
    }
 
 
@app.get("/api/uart/status")
async def uart_status():
    """Get UART connection status"""
    return {
        "connected": uart.is_connected(),
        "mode": os.getenv("COMM_MODE", "simulation"),
        "port": os.getenv("UART_PORT", "/dev/ttyUSB0") if uart.is_connected() else None
    }
 
 
@app.get("/api/uart/ports")
async def list_uart_ports():
    """List available UART ports for debugging"""
    return {"ports": uart.list_available_ports()}
 
 
@app.get("/api/uart/test")
async def test_uart():
    """Test UART communication by sending a test command"""
    if not uart.is_connected():
        raise HTTPException(status_code=400, detail="UART not connected")
    result = uart.send_command("MODULE_STATUS:1;", wait_response=True, timeout=3)
    return result
 
 
def import_time():
    """Helper function to get current timestamp"""
    from datetime import datetime
    return datetime.now().isoformat()
 
 
# ================================================================
# INCLUDE API ROUTERS
# ================================================================
 
# Power Module Routes (prefix: /api/power)
app.include_router(power.router, prefix="/api/power", tags=["Power Module"])
 
# Display Module Routes (prefix: /api/display)
app.include_router(display.router, prefix="/api/display", tags=["Display Module"])
 
# Audio Module Routes (prefix: /api/audio)
app.include_router(audio.router, prefix="/api/audio", tags=["Audio/BT Module"])
 
# ISP/Camera Module Routes (prefix: /api/isp)
app.include_router(isp.router, prefix="/api/isp", tags=["ISP/Camera Module"])
 
# Host Module Routes (prefix: /api/host)
app.include_router(host.router, prefix="/api/host", tags=["Host Module"])
 
 
# ================================================================
# ERROR HANDLERS
# ================================================================
 
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.detail,
            "status_code": exc.status_code
        }
    )
 
 
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal server error",
            "detail": str(exc) if os.getenv("DEBUG", "false").lower() == "true" else None
        }
    )
 
 
# ================================================================
# MAIN ENTRY POINT (when run directly)
# ================================================================
 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=os.getenv("DEBUG", "false").lower() == "true"
    )