import serial
import datetime
import time
import geocoder
from pymongo import MongoClient

# Config
serial_port = '/dev/ttyACM0'
mongo_host = ""
mongodb = ""
location = geocoder.ip('me')

# Serial Connection
serial_conn = serial.Serial(serial_port, 9600, timeout=0)

# MongoDB Connection
client = MongoClient(mongodb, 27017)
db = client[mongodb]
collection = db['data']

upload_interval = 10
while 1:
    try:
        moisture_reading = serial_conn.readline().rstrip()
        temp_reading = serial_conn.readline().rstrip()

        if moisture_reading:
            doc_id = collection.insert_one({
                'moisture': moisture_reading,
                'temperature': temp_reading,
                'timestamp': datetime.datetime.now(),
                'location': location

            }).inserted_id
    except serial.SerialTimeoutException:
        print('Could not read data from unit')
    finally:
        time.sleep(upload_interval)




def fetch_sensor_data() -> dict:
    pass

def save_data():
    pass

