# imports
import serial

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
def save_csv():


if __name__ == "__main__":
