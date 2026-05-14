from fastapi import APIRouter
from pydantic import BaseModel
from app.services.firmware_bridge import bridge

router = APIRouter()
class CommandRequest(BaseModel):
    command: str
 
@router.post("/send-command")
async def send_command(request: CommandRequest):
    """Receive command from frontend and send to hardware"""
    command = request.command.strip()
    print(f"[API] TX → {command}")
    try:
        result = bridge.send_raw_command(command)
        if result.get("success"):
            response = result.get("response", result.get("message", "OK"))
            print(f"[API] RX ← {response}")
            return {
                "success": True,
                "response": response,
                "message": response
            }
        else:
            error = result.get("error", "Unknown error")
            print(f"[API] ERROR: {error}")
            return {
                "success": False,
                "error": error
            }
    except Exception as e:
        print(f"[API] Exception: {e}")
        return {
            "success": False,
            "error": str(e)
        }