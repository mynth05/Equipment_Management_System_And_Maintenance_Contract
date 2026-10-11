from device import Device, DeviceStatus
from typing import Optional, List
class LabRoom:
    def __init__(self, room_id: str, room_name: str, capacity: int):
        self.room_id = room_id
        self.room_name = room_name
        self.capacity = capacity
        self._devices: List[Device] = []

    @property
    def devices(self) -> List[Device]:
        return self._devices.copy()
    def add_device(self, device: Device):
        if device is None:
            raise ValueError("Không thể thêm đối tượng None vào phòng.")

        # Kiểm tra trùng mã thiết bị trùng trong phòng
        if any(d.device_id == device.device_id for d in self._devices):
            raise ValueError(f"Thiết bị {device.device_id} đã tồn tại trong phòng {self.room_id}.")

        self._devices.append(device)

    def remove_device(self, device_id: str) -> bool:
        device = self.find_device(device_id)
        if device:
            self._devices.remove(device)
            return True
        return False

    def find_device(self, device_id: str) -> Optional[Device]:
        for d in self._devices:
            if d.device_id == device_id:
                return d
        return None

    def calculate_annual_maintenance_cost(self) -> float:
        # Tính đa hình: Duck typing/ Dynamic dispatch
        return sum(d.calculate_maintenance_cost() for d in self._devices)


    def get_device_requiring_maintenance(self) -> List[Device]:
        return [d for d in self._devices if d.status == DeviceStatus.UnderMaintenance or d.get_years_in_use() > 5]