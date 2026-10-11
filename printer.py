from device import Device, DeviceStatus, INetworkable, Optional
class Printer(Device):
    def __init__(
        self,
        device_id: str,
        name: str,
        year_of_use: int,
        purchase_price: float,
        print_type: str,
        page_count: int,
        is_color: bool,
        status: DeviceStatus = DeviceStatus.Active
    ):
        super().__init__(device_id, name, year_of_use, purchase_price, status)
        self.print_type = print_type
        self.page_count = page_count
        self.is_color = is_color
    def calculate_maintenance_cost(self) -> float:
        cost = 0.04 * self.purchase_price
        if self.page_count > 100_000:
            cost += 500_000
        if self.is_color:
            cost += 300_000
        return cost

class NetworkPrinter(Printer, INetworkable):
    def __init__(
        self,
        device_id: str,
        name: str,
        year_of_use: int,
        purchase_price: float,
        print_type: str,
        page_count: int,
        is_color: bool,
        status: DeviceStatus = DeviceStatus.Active
    ):
        super().__init__(device_id, name, year_of_use, purchase_price, print_type, page_count, is_color, status)
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
                raise RuntimeError(f"Máy in {self.device_id} đang được kết nối.")
            self._ip_address = ip_address

    def disconnect(self) -> None:
            self._ip_address = None

        


        