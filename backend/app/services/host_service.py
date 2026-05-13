from app.services.firmware_bridge import bridge
class HostService:

    # ============ HOST CONTROLS ============
    async def control_host(self, device: str, action: str):
        return bridge.host_control(device, action)

    async def host_status(self, device: str):
        return bridge.host_status(device)

    async def all_hosts_status(self):
        return bridge.all_hosts_status()


host_service = HostService()