/*
 * Created by ArduinoGetStarted.com
 *
 * This example code is in the public domain
 *
 * Tutorial page: https://arduinogetstarted.com/tutorials/arduino-cooling-system-using-dht-sensor
 */

#include "DHT.h"

#define RELAY_FAN_PIN A5 // Arduino pin connected to relay which connected to fan
#define DHTPIN 12           // Arduino pin connected to relay which connected to DHT sensor
#define DHTTYPE DHT11

const int TEMP_THRESHOLD_UPPER = 25; // upper threshold of temperature, change to your desire value
const int TEMP_THRESHOLD_LOWER = 20; // lower threshold of temperature, change to your desire value

DHT dht(DHTPIN, DHTTYPE);

float temperature;    // temperature in Celsius

void setup()
{
  Serial.begin(9600); // initialize serial
  dht.begin();        // initialize the sensor
  pinMode(RELAY_FAN_PIN, OUTPUT); // initialize digital pin as an output
}

void loop()
{
  // wait a few seconds between measurements.
  delay(2000);

  temperature = dht.readTemperature();;  // read temperature in Celsius
  
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
