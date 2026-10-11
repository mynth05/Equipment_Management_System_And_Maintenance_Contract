"""
Họ và tên: Phạm Thị Minh Thuý
MSSV: 202418992
"""
from labroom import LabRoom
from device import Device, DeviceStatus, INetworkable
from computer import Computer
from printer import Printer, NetworkPrinter
from projector import Projector
from typing import List
if __name__ == "__main__":
    # Khởi tạo theo yêu cầu của đề bài
    computer1 = Computer("PC01", "Dell Optiplex", 2022 , 15_000_000, ram = 16, cpu_type = "core i5", has_discrete_gpu = False)
    computer2 = Computer("PC02", "Dell Precision", 2019, 25_000_000, ram = 32, cpu_type = "core i7", has_discrete_gpu = True)

    printer1 = Printer ("PR1", "HP LaserJet", 2023, 5_000_000, print_type = "Laser", page_count = 120_000, is_color = False)
    printer2 = NetworkPrinter ( "PR2", "Canon Color Net", 2024, 8_000_000, print_type = "Laser", page_count = 20_000, is_color = True)

    projector1 = Projector("PJ1", "Sony VPL", 2021, 10_000_000, lumens = 3500, lamp_hours = 3200)

    lab1 = LabRoom ("Lab01", "Phòng máy tính 1", 40)
    lab2 = LabRoom ("Lab02", "Phòng máy tính 2", 30)

    #1. Thêm thiết bị vào phòng
    lab1.add_device(computer1)
    lab1.add_device(printer2)
    lab1.add_device(projector1)

    lab2.add_device(computer2)
    lab2.add_device(printer1)

    #2. Thử thêm một thiết bị bị trùng mã

    try:
        lab1.add_device(computer1)  # Thử thêm thiết bị trùng mã
    except ValueError as e:
        print(f"[Bắt ngoại lệ trùng mã]: {e}\n")

    # 4. In thông tin và tổng chi phí bảo trì từng phòng
    for room in [lab1, lab2]:
        print(f"=== {room.room_name} ({room.room_id}) ===")
        for d in room.devices:
            print(d)
        print(f"=> Tổng chi phí bảo trì: {room.calculate_annual_maintenance_cost():,.0f} VNĐ\n")

    # 5. Liệt kê thiết bị cần bảo trì
    print("--- THIẾT BỊ CẦN BẢO TRÌ TẠI LAB 1 ---")
    for d in lab1.get_device_requiring_maintenance():
        print(f"* {d.name} (Mã: {d.device_id}, Năm SD: {d.year_of_use})")
    print()

    # 6. Kết nối mạng và duyệt danh sách qua interface INetworkable
    network_devices: List[INetworkable] = [computer1, computer2, printer2]

    computer1.connect("192.168.1.10")
    computer2.connect("192.168.1.11")
    printer2.connect("192.168.1.50")

    print("--- DUYỆT THIẾT BỊ QUA INTERFACE INETWORKABLE ---")
    for net_dev in network_devices:
        print(f"IP: {net_dev.ip_address:<15} | Đang kết nối: {str(net_dev.is_connected):<5} | Loại: {type(net_dev).__name__}")