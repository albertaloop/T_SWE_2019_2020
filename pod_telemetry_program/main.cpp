#include <Ethernet2.h>
#include <EthernetUdp2.h>

#define PACKET_LENGTH 34
#define DELAY 10

#define ACCELERATION_IDX 2
#define POSITION_IDX 6
#define VELOCITY_IDX 10
#define BATTERY_VOLTAGE_IDX 14

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress local_ip(192, 168, 2, 177);
IPAddress remote_ip(192, 168, 2, 30);

unsigned int local_port = 3000;
unsigned int remote_port = 3000;

EthernetUDP Udp;

uint8_t TEAM_ID = 0;

// TODO: implement this function
uint8_t get_status() {
  return 0;
}

// TODO: implement this function
uint32_t get_position() {
  return 2334566;
}

// TODO: implement this function
uint32_t get_velocity() {
  return 13454634;
}

// TODO: implement this function
uint32_t get_acceleration() {
  return 435468763;
}

uint8_t *build_packet() {
  static uint8_t packet[PACKET_LENGTH];
  packet[0] = TEAM_ID;
  packet[1] = get_status();

  uint32_t acceleration = get_acceleration();
  for (int i = ACCELERATION_IDX + 3; i >= ACCELERATION_IDX; i--) {
    packet[i] = acceleration & 0xFF;
    acceleration = acceleration >> 8;
  }

  uint32_t position = get_position();
  for (int i = POSITION_IDX + 3; i >= POSITION_IDX; i--) {
    packet[i] = position & 0xFF;
    position = position >> 8;
  }

  uint32_t velocity = get_velocity();
  for (int i = VELOCITY_IDX + 3; i >= VELOCITY_IDX; i--) {
    packet[i] = velocity & 0xFF;
    velocity = velocity >> 8;
  }

  for (int i = BATTERY_VOLTAGE_IDX; i < PACKET_LENGTH; i++) {
    packet[i] = 0;
  }

  return packet;
}

void setup() {
  Ethernet.begin(mac, local_ip);
  Udp.begin(local_port);
  Serial.begin(9600);
}

void loop() {
  Udp.beginPacket(remote_ip, remote_port);
  Udp.write(build_packet(), (size_t) PACKET_LENGTH);
  Udp.endPacket();
  delay(DELAY);
}