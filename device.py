from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from typing import Optional, List

class DeviceStatus (Enum):
    Active = "Active" #thiết bị đang hoạt động bình thường
    UnderMaintenance = "Under Maintenance" #thiết bị đang được bảo trì
    Retired = "Retired" #thiết bị đã thanh lý/ ngừng sử dụng

class INetworkable(ABC):
    @property
    @abstractmethod
    def id_address(self) -> Optional[str]:
        pass
    @property
    @abstractmethod
    def is_connected(self) -> bool:
        pass
    @abstractmethod
    def connect(self) -> None:
        pass
    @abstractmethod
    def disconnect(self) -> None:
        pass

class Device(ABC):
    def __init__(
        self,
        device_id: str,
        name: str,
        year_of_use: int,
        purchase_price: float,
        status: DeviceStatus = DeviceStatus.Active,
    ):
        if not device_id or not device_id.strip():
            raise ValueError("Mã thiêt bị không được để trống.")
        if purchase_price < 0:
            raise ValueError("Giá mua phải lớn hơn 0.")
        if year_of_use > datetime.now().year:
            raise ValueError("Năm đưa vào sử dụng không được lớn hơn năm hiện tại.")

        self.device_id = device_id
        self.name = name
        self.year_of_use = year_of_use
        self.purchase_price = purchase_price
        self.status = status

        @property
        def device_id(self) -> str:
            return self._device_id

        def get_years_in_use(self) -> int:
            return datetime.now().year - self._year_of_use

        @abstractmethod
        def calculate_maintenance_cost(self) -> float:
            """Phương thức trừu tượng tính chi phí bảo trì dự kiến trong một năm"""
            pass

        def __str__(self) -> str:
            return (
                f"[{self.device_id}]{self.name} |"
                f"Năm: {self.year_of_use} |"
                f"Giá: {self.purchase_price:,.0f}đ |"
                f"Trạng thái: {self.status.value} |"
                f"Bảo trì: {self.calculate_maintenance_cost():,.0f}đ" 
            )