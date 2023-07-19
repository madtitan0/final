#include <Arduino.h>

const int emgPin = A0;  // Analog pin connected to the EMG sensor

void setup() {
  Serial.begin(9600);  // Set the baud rate to match the Python program
}

void loop() {
  int sensorValue = analogRead(emgPin);  // Read the sensor value
  Serial.println(sensorValue);  // Send the sensor value over the serial port
  delay(10);  // Adjust the delay as per your requirements
}
