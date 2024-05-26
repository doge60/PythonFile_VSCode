'''
Author: doge60 3020118317@qq.com
Date: 2024-05-15 21:56:47
LastEditors: doge60 3020118317@qq.com
LastEditTime: 2024-05-26 13:21:12
FilePath: \PythonFile_VSCode\Logistics_Race\rpi_opencv_detect\serial_test.py
Description: 

Copyright (c) 2024 by doge60 3020118317@qq.com, All Rights Reserved. 
'''
import struct
import time
import serial
import serial.tools.list_ports

# 列出所有可用的串口设备
ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    # print(f"{port}: {desc} [{hwid}]")
    if desc[:16] == "USB-SERIAL CH340":
        ser = serial.Serial(port, 9600)
   
serial_port_state = ser.is_open # 打开ttyUSB0，将波特率配置为115200，其余参数使用默认值
while 1:
    weight_data = [2, 3, 4]
    pack_data = struct.pack('<BBfffBB', 0xFF,0xFE, weight_data[0], weight_data[1], weight_data[2], 0xFE,0xFF)
    ser.write(pack_data)  # 将数据打包发送到串口
    time.sleep(0.1)