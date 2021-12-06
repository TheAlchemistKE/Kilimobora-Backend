import serial
import datetime
import time
import geocoder
from pymongo import MongoClient

# Config
serial_port = '/dev/ttyACM0'
mongodb = "mongodb+srv://kelyn:Kelyn@cluster0.rvyrf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
location = geocoder.ip('me')

# Serial Connection
serial_conn = serial.Serial(serial_port, 9600, timeout=0)

# MongoDB Connection
client = MongoClient(mongodb)
db = client['kilimobora']
collection = db['sensor_data']




def fetch_sensor_data() -> dict:
    """
    :return: Dictionary of values gathered from the sensors
    """
    moisture_reading = serial_conn.readline().rstrip()
    temp_reading = serial_conn.readline().rstrip()
    if moisture_reading and temp_reading:
        return {
                'moisture': moisture_reading,
                'temperature': temp_reading,
                'timestamp': datetime.datetime.now(),
                'location': location

        }
    else:
        return {
            'message': 'Sensors offline'
        }
def save_data() -> None:
    """
    Loops infinitely and gathers data from the sensors after every 10 seconds
    :return: Nothing
    """
    delay = 10
    while 1:
        try:
            doc_id = collection.insert_one().inserted_id
        except serial.SerialTimeoutException:
            print('Could not read data from unit')
        finally:
            time.sleep(delay)

