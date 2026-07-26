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

# bioreactor class
class Bioreactor:

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
