# imports
from time import time

import serial
from pathlib import Path
import csv

# constants

PORTS = [
    "COM3",
    "COM4",
    "COM5",
    "COM6",
    "COM7",
    "COM8",
    "COM9",
    "COM10"
]

BAUDRATE = 115200

# variables
connections = []
reactors = []

# bioreactor class
class Bioreactor:

    def __init__(self, reactor_id):

        self.id = reactor_id

        self.time = 0
        self.temp = 0
        self.od = 0
        self.stir = 0
        self.heat = 0
        self.pump = 0
        self.ph = 7

        self.history = []

# connect to serial ports
def connect_serial():
    for i, port in enumerate(PORTS):
        try:
            ser = serial.Serial(port, BAUDRATE, timeout=1)
            connections.append(ser)
            reactors.append(Bioreactor(i + 1))
            print(f"Connected to {port}")
        except serial.SerialException:
            print(f"Could not connect to {port}")

# read data from serial ports
def serial_thread():
    while True:

        for ser, reactor in zip(connections, reactors):

            if ser.in_waiting == 0:
                continue

            try:
                line = ser.readline().decode("utf-8").strip()
            
                temp, od, ph, volume, timestamp = line.split(",")

                reactor.temp = float(temp)
                reactor.od = float(od)
                reactor.ph = float(ph)
                reactor.pump = float(volume) 
                reactor.time = float(timestamp)

                reactor.history.append({
                    "temp": reactor.temp,
                    "od": reactor.od,
                    "ph": reactor.ph,
                    "volume": reactor.pump,
                    "time": reactor.time
                })

                save_csv(reactor)

            except Exception as e:
                print(f"Error reading reactor {reactor.id}: {e}")

        time.sleep(0.05)
        
# parse data from serial port
def parse_data(reactor_number, line):

# send command to bioreactor via serial port
def send_command():
    

# update graphs with new data w every refresh
def update_graphs():

# update tkinter / other gui w every refresh
def update_gui():

# save data to CSV file
def save_csv(temp, od, ph, volume, time):
    csv_path = "python-ui/data.csv"
    file_exists = csv_path.exists()

    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "temp",
                "OD",
                "pH",
                "volume of liquid",
                "time"
            ])

        writer.writerow([
            temp,
            od,
            ph,
            volume,
            time
        ])


if __name__ == "__main__":
