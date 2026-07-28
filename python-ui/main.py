# imports
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
