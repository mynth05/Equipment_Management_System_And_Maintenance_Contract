from device import Device, DeviceStatus, INetworkable
from typing import Optional
class Computer(Device, INetworkable):
    def __init__(
        self,
        device_id: str,
        name: str,
        year_of_use: int,
        purchase_price: float,
        ram: int,
        cpu_type: str,
        has_discrete_gpu: bool,
        status: DeviceStatus = DeviceStatus.Active
    ):
        super().__init__(device_id, name, year_of_use, purchase_price, status)
        self.ram = ram
        self.cpu_type = cpu_type
        self.has_discrete_gpu = has_discrete_gpu
        self._ip_address: Optional[str] = None

    @property
    def ip_address(self) -> Optional[str]:
            return self._ip_address

    @property
    def is_connected(self) -> bool:
            return self._ip_address is not None

    def connect(self, ip_address: str) -> None:
            if not ip_address or not ip_address.strip():
                raise ValueError("Địa chỉ IP không được để trống.")
            if self.is_connected:
                raise RuntimeError(f"Thiết bị {self.device_id} đang được kết nối.")
            self._ip_address = ip_address

    def disconnect(self) -> None:
            self._ip_address = None

    def calculate_maintenance_cost(self) -> float:
        cost = 0.05 * self.purchase_price
        if self.has_discrete_gpu:
            cost += 0.02 * self.purchase_price
        if self.get_years_in_use() > 5:
            cost += 0.01 * self.purchase_price
        return cost