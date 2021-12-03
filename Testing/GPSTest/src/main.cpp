#include <Arduino.h>
#include <Wire.h>
#include <SPI.h>
#include <FlexCAN_T4.h>
#include <Adafruit_GPS.h>

static CAN_message_t msg;
FlexCAN_T4<CAN0, RX_SIZE_256, TX_SIZE_16> Can0;

// what's the name of the hardware serial port?
#define GPSSerial Serial1

// Connect to the GPS on the hardware port
Adafruit_GPS GPS(&GPSSerial);

void canSniff(const CAN_message_t &msg)
{
  Serial.print("MB ");
  Serial.print(msg.mb);
  Serial.print("  OVERRUN: ");
  Serial.print(msg.flags.overrun);
  Serial.print("  LEN: ");
  Serial.print(msg.len);
  Serial.print(" EXT: ");
  Serial.print(msg.flags.extended);
  Serial.print(" TS: ");
  Serial.print(msg.timestamp);
  Serial.print(" ID: ");
  Serial.print(msg.id, HEX);
  Serial.print(" Buffer: ");
  for (uint8_t i = 0; i < msg.len; i++)
  {
    Serial.print(msg.buf[i], HEX);
    Serial.print(" ");
  }
}

void setup()
{
  // put your setup code here, to run once:
  GPS.begin(9600);
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);
  GPS.sendCommand(PGCMD_ANTENNA);
  GPSSerial.println(PMTK_Q_RELEASE);

  Wire.begin();

  pinMode(14, OUTPUT);
  digitalWrite(14, HIGH);
  for (size_t i = 0; i < 10; i++)
  {
    digitalWrite(14, HIGH);
    delay(100);
    digitalWrite(14, LOW);
  }

  digitalWrite(14, LOW);

  Serial.begin(9600);
  Serial.println("Serial Connected \n");

  Can0.begin();
  Can0.setBaudRate(500000);
  Can0.setMaxMB(16);
  Can0.enableFIFO();
  Can0.onReceive(FIFO, canSniff);
  Can0.mailboxStatus();

  //  delay(1000);
}

void loop()
{
  char c = GPS.read();

  Serial.print("Location: ");
  Serial.print(GPS.latitude, 4);
  Serial.print(GPS.lat);
  Serial.print(", ");
  Serial.print(GPS.longitude, 4);
  Serial.println(GPS.lon);
  Serial.print("Speed (knots): ");
  Serial.println(GPS.speed);
  Serial.print("Angle: ");
  Serial.println(GPS.angle);
  Serial.print("Altitude: ");
  Serial.println(GPS.altitude);
  Serial.print("Satellites: ");
  Serial.println((int)GPS.satellites);

  Can0.events();
  
  msg.len = 0x3;
  msg.id = 0x1;

  Can0.read(msg);
  delay(100);
  Serial.print("MB ");
  Serial.print(msg.mb);
  Serial.print(" OVERRUN: ");
  Serial.print(msg.flags.overrun);
  Serial.print(" LEN: ");
  Serial.print(msg.len);
  Serial.print(" EXT: ");
  Serial.print(msg.flags.extended);
  Serial.print(" TS: ");
  Serial.print(msg.timestamp);
  Serial.print(" ID: ");
  Serial.print(msg.id, HEX);
  Serial.print(" Buffer: ");
  for ( uint8_t i = 0; i < msg.len; i++ ) {
      Serial.print(msg.buf[i], HEX);
      Serial.print(" ");
  }
  Serial.println("\n");

  if ((msg.buf[0] + msg.buf[1] + msg.buf[2])/100 > 0)
  {
    digitalWrite(14, HIGH);
    delay(250);
  }
  digitalWrite(14, LOW);
}