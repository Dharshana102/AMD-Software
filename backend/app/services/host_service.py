from app.services.firmware_bridge import bridge
 
 
class HostService:

    # ============ RPI FEATURE CARD ============

    async def get_rpi_ip(self) -> dict:

        """Get Raspberry Pi IP address"""

        return bridge.get_rpi_ip()

    async def get_rpi_mac(self) -> dict:

        """Get Raspberry Pi MAC address"""

        return bridge.get_rpi_mac()

    async def get_rpi_info(self) -> dict:

        """Get Raspberry Pi IP and MAC address"""

        return bridge.get_rpi_info()

    async def rpi_status(self) -> dict:

        """Get Raspberry Pi connection status"""

        return bridge.rpi_status()

    # ============ HOST SERVER CONTROLS ============

    async def control_host(self, device: str, action: str) -> dict:

        """Control host device (System Server, Database Server, etc.)"""

        return bridge.host_control(device, action)

    async def host_status(self, device: str) -> dict:

        """Get host device status"""

        return bridge.host_status(device)

    async def all_hosts_status(self) -> dict:

        """Get status of all host devices"""

        return bridge.all_hosts_status()
 
 
host_service = HostService()
 