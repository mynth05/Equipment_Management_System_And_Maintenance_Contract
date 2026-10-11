from device import Device, DeviceStatus, INetworkable, Optional
class Projector(Device):
    def __init__(
        self,
        device_id: str,
        name: str,
        year_of_use: int,
        purchase_price: float,
        lumens: int,
        lamp_hours: int,
        status: DeviceStatus = DeviceStatus.Active
    ):
        super().__init__(device_id, name, year_of_use, purchase_price, status)
        self.lumen_count = lumens
        self.lamp_hours = lamp_hours
    def calculate_maintenance_cost(self) -> float:
        cost = 0.03 * self.purchase_price
        if self.lamp_hours > 3000:
            cost += 1_500_000
        return cost