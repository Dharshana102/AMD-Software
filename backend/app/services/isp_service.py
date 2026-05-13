from app.services.firmware_bridge import bridge
class ISPService:

    # ============ RGB LED COMMANDS ============
    async def rgb_set(self, led_id: int, r: int, g: int, b: int):
        return bridge.rgb_set(led_id, r, g, b)

    async def rgb_off(self, led_id: int):
        return bridge.rgb_off(led_id)

    # ============ STEPPER MOTOR COMMANDS ============
    async def stepper_move(self, direction: str, steps: int, speed_ms: int):
        return bridge.stepper_move(direction, steps, speed_ms)

    async def stepper_stop(self):
        return bridge.stepper_stop()

    # ============ LIGHT SENSOR ============
    async def light_read(self):
        return bridge.light_read()


isp_service = ISPService()