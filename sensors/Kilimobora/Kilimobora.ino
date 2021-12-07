
#include "DHT.h"
int relayPin = 8;
int sensor_pin = 4; // Soil Sensor input at Digital Pin
int output_value ;



float temperature;

#define RELAY_FAN_PIN A5 // Arduino pin connected to relay which connected to fan
#define DHTPIN 12 
#define DHTTYPE DHT11   
DHT dht(DHTPIN, DHTTYPE);// Arduino pin connected to relay which connected to DHT sensor


const int TEMP_THRESHOLD_UPPER = 25; // upper threshold of temperature, change to your desire value
const int TEMP_THRESHOLD_LOWER = 20; // lower threshold of temperature, change to your desire value
int pump= 5;//pumpimng water
void setup() {
  Serial.begin(9600);                 
  pinMode(relayPin, OUTPUT);
  pinMode(sensor_pin, INPUT);
  dht.begin();        // initialize the sensor
  pinMode(RELAY_FAN_PIN, OUTPUT); // initialize digital pin as an output
  Serial.println("Reading From the Sensor ...");
  delay(2000);

}

void loop() {
  coolingSystem();
  //irrigationSystem();
  irrigationSystems();
  

}

void coolingSystem() {
   // wait a few seconds between measurements.
  delay(2000);

  temperature = dht.readTemperature();  // read temperature in Celsius
  
  if (isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
  } else {
    if(temperature > TEMP_THRESHOLD_UPPER){
      Serial.println("The fan is turned on");
      digitalWrite(RELAY_FAN_PIN, HIGH); // turn on
    } else if(temperature < TEMP_THRESHOLD_LOWER){
      Serial.println("The fan is turned off");
      digitalWrite(RELAY_FAN_PIN, LOW); // turn on
    }
  }
   
}

void irrigationSystem() {
   output_value= digitalRead(sensor_pin);
   output_value = map(output_value,550,10,0,100);
   Serial.print("Mositure : ");
   Serial.print(output_value);
   Serial.println("%");
   if(output_value<20){
    digitalWrite(relayPin, LOW);
   }
   else
   {
    digitalWrite(relayPin, HIGH);       
   }
   delay(1000);
  
  
}


void irrigationSystems() {
  digitalWrite(pump, HIGH);
  delay(100);
  
    digitalWrite(pump,LOW);
   delay(300000);
  
}
