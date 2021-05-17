#include <Arduino.h>
#include <Ethernet2.h>
#include <SPI.h>
#include "ChRt.h"
#include "CANBus.h"
#include "circular_buffer.h"

#define PACKET_LENGTH 34
#define ACCELERATION_IDX 2
#define POSITION_IDX 6
#define VELOCITY_IDX 10
#define BATTERY_VOLTAGE_IDX 14

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress local_ip(192, 168, 2, 177);
IPAddress remote_ip(192, 168, 2, 30);

unsigned int local_port = 3000;
unsigned int remote_port = 3000;

EthernetServer server(80);
EthernetUDP Udp;

uint8_t team_id = 0;

unsigned long wait_time = 400; // 400 ms

enum Status {
              Fault = 0,
              SafeToApproach = 1,
              ReadyToLaunch = 2,
              Launching = 3,
              Coasting = 4,
              Braking = 5,
              Crawling = 6
            };

uint8_t status = Status::SafeToApproach;

double position = 0;
double velocity = 0;
double acceleration = 0;

FlexCAN CANBus0(100000, 0);
FlexCAN CANBus1(100000, 1);

static CAN_message_t msg, rxmsg;


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

uint8_t *build_packet(uint8_t team_id, uint8_t status, int32_t acceleration, int32_t position, int32_t velocity) {
  static uint8_t packet[PACKET_LENGTH];
  packet[0] = team_id;
  packet[1] = status;

  for (int i = ACCELERATION_IDX + 3; i >= ACCELERATION_IDX; i--) {
    packet[i] = acceleration & 0xFF;
    acceleration = acceleration >> 8;
  }

  for (int i = POSITION_IDX + 3; i >= POSITION_IDX; i--) {
    packet[i] = position & 0xFF;
    position = position >> 8;
  }

  for (int i = VELOCITY_IDX + 3; i >= VELOCITY_IDX; i--) {
    packet[i] = velocity & 0xFF;
    velocity = velocity >> 8;
  }

  for (int i = BATTERY_VOLTAGE_IDX; i < PACKET_LENGTH; i++) {
    packet[i] = 0;
  }

  return packet;
}

void print_packet(uint8_t *packet) {
  for (int i = 0; i < PACKET_LENGTH; i++) {
    Serial.print(packet[i], HEX);
    Serial.print(" ");
  }
  Serial.println();
}

void runTelemetry() {
  status = get_status();
  position = get_position();
  velocity = get_velocity();
  acceleration = get_acceleration();

  Udp.beginPacket(remote_ip, remote_port);
  uint8_t *packet = build_packet(team_id, status, (int32_t) acceleration, (int32_t) position, (int32_t) velocity);
  print_packet(packet);
  Udp.write(packet, (size_t) PACKET_LENGTH);
  Udp.endPacket();

  chThdSleepMilliseconds(wait_time);
}

void runCommandServer() {
  EthernetClient client = server.available();
  if (client) {
    Serial.println("new client");
    while (client.connected()) {
      if (client.available()) {
        int c = client.read();
        Serial.write(c);
        if (c == 1) {
          Serial.println("TEST");
        }
      }
    }
    chThdSleepMilliseconds(1000);
    client.stop();
    Serial.println("client disconnected");
  }
}

void runCanbusReceive() {
  Serial.println("No data available");
  if (CANBus1.available()) {
    Serial.println("Data available");
    CANBus1.read(rxmsg);
    for (int i = 0; i < 5; i++) {
      Serial.print(rxmsg.buf[i]);
    }
    Serial.println();
  }
  chThdSleepMilliseconds(100);
}

void runCanbusSend() {
  for (int i = 0; i < 9; i++) {
    msg.id = 0x222;
    msg.len = 6;
    strcpy((char*) msg.buf, "Msg ");
    msg.buf[5] = '0' + i;
    CANBus0.write(msg);
    Serial.println("Message sent!");
    chThdSleepMilliseconds(100);
  }
}

void setupEthernet() {
  Ethernet.begin(mac, local_ip);
  Udp.begin(local_port);
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());
}

void setupCANBus() {
  CANBus0.begin();
  CANBus1.begin();
}

//------------------------------------------------------------------------------
// thread 1 blink LED
// 64 byte stack beyond task switch and interrupt needs.
static THD_WORKING_AREA(waThread1, 128);

static THD_FUNCTION(Thread1, arg) {
  (void)arg;
  while (true) {
    runTelemetry();
    chThdSleepMilliseconds(150);
  }
}
//------------------------------------------------------------------------------
// thread 2
// 64 byte stack beyond task switch and interrupt needs.
static THD_WORKING_AREA(waThread2, 128);

static THD_FUNCTION(Thread2, arg) {
  (void)arg;
  while (true) {
    runCommandServer();
    chThdSleepMilliseconds(150);
  }
}
//------------------------------------------------------------------------------
// thread 3
// 64 byte stack beyond task switch and interrupt needs.
static THD_WORKING_AREA(waThread3, 128);

static THD_FUNCTION(Thread3, arg) {
  (void)arg;
  while (true) {
    runCanbusReceive();
    chThdSleepMilliseconds(150);
  }
}

//------------------------------------------------------------------------------
// thread 4
// 64 byte stack beyond task switch and interrupt needs.
static THD_WORKING_AREA(waThread4, 128);

static THD_FUNCTION(Thread4, arg) {
  (void)arg;
  runCanbusSend();
  chThdSleepMilliseconds(150);
}

//------------------------------------------------------------------------------
// Continue setup() after chBegin().
void chSetup() {
  chThdCreateStatic(waThread1, sizeof(waThread1),
    NORMALPRIO, Thread1, NULL);

  chThdCreateStatic(waThread2, sizeof(waThread2),
    NORMALPRIO, Thread2, NULL);

  chThdCreateStatic(waThread3, sizeof(waThread3),
    NORMALPRIO, Thread3, NULL);

  chThdCreateStatic(waThread4, sizeof(waThread4),
    NORMALPRIO, Thread4, NULL);
}
//------------------------------------------------------------------------------
void setup() {
  Serial.begin(9600);
  
  // Wait for USB Serial.
  while (!Serial) {}
  
  setupEthernet();
  setupCANBus();
  chBegin(chSetup);
  // chBegin() resets stacks and should never return.
  while (true) {}
}
//------------------------------------------------------------------------------
void loop() {
  while (true) {
    chThdSleepMilliseconds(1000);
  }
}