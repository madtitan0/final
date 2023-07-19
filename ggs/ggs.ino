#include <Arduino.h>

void setup() {
  Serial.begin(9600); // Set the baud rate to match the Django application
}

void loop() {
  // Read EMG sensor value
  int sensorValue = analogRead(A0); // Assuming the EMG sensor is connected to analog pin A0

  // Map the sensor value to the range of 0-255
  int mappedValue = map(sensorValue, 0, 1023, 0, 255);

  // Constrain the mapped value to the range of 0-255
  mappedValue = constrain(mappedValue, 0, 255);

  // Send the mapped value via serial communication
  Serial.println(mappedValue);

  delay(10); // Adjust the delay based on your requirements
}
