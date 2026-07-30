# imports
from time import time
import serial
from pathlib import Path
import csv
import json

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
                line = ser.readline().decode("utf-8").strip() # one json msg
                data = json.loads(line) # json to python

                reactor.temp = data.get("Temperature", reactor.temp)
                reactor.od = data.get("OD", reactor.od)
                reactor.ph = data.get("pH", reactor.ph)
                reactor.volume = data.get("Volume of Liquid", reactor.volume)

                reactor.time = time.time()

                reactor.history.append({
                    "time": reactor.time,
                    "temp": reactor.temp,
                    "od": reactor.od,
                    "ph": reactor.ph,
                    "volume": reactor.volume
                })

                save_csv(reactor)

            except json.JSONDecodeError:
                print(f"Invalid JSON received: {line}")

            except Exception as e:
                print(f"Error reading reactor {reactor.id}: {e}")

        time.sleep(0.05)
        
# parse data from serial port
def parse_data(reactor_number, line):
    reactor = reactors[reactor_number]

    try:
        data = json.loads(line)

        reactor.temp = data.get("Temperature", reactor.temp)
        reactor.od = data.get("OD", reactor.od)
        reactor.ph = data.get("pH", reactor.ph)
        reactor.volume = data.get("Volume of Liquid", reactor.volume)
        reactor.time = time()

        reactor.history.append({
            "time": reactor.time,
            "temp": reactor.temp,
            "od": reactor.od,
            "ph": reactor.ph,
            "volume": reactor.volume
        })

        save_csv(reactor)

    except json.JSONDecodeError:
        print(f"Invalid JSON from Reactor {reactor.id}: {line}")

# send command to bioreactor via serial port
def send_command():

# FORMAT:
# {
# “Temperature”: 50 (target Celsius),
# “Input Pump 1”: 1, 10 (volume (mL), time),
# “Input Pump 2”: 5, 20 (volume (mL), time),
# “Output Pump 1”: 2, 5 (volume (mL), time),
# “Stirring Fan”: 23 (target speed from 1 to 100)
# }

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
