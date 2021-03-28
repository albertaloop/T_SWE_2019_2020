#include <FlexCAN_T4.h>
#include <StensTimer.h>

#include "node_stubs.hpp"

const int TICK_ACTION = 1;

FlexCAN_T4<CAN1, RX_SIZE_256, TX_SIZE_16> can1;
FlexCAN_T4<CAN2, RX_SIZE_256, TX_SIZE_16> can2;
CAN_message_t msg;
struct bms _bms;

enum CAN_ID {
  CAN_BMS_ID = 0x100,
  CAN_NAV_ID = 0x200,
  CAN_BRK_ID = 0x300,
  CAN_MTR_ID = 0x400,
  CAN_OBC_ID = 0x500,
};

char bms_print_buffer[100];
StensTimer* bmsTimer = NULL;
static uint8_t hex[17] = "0123456789abcdef";

static void hexDump(uint8_t dumpLen, uint8_t *bytePtr)
{
  uint8_t working;
  while( dumpLen-- ) {
    working = *bytePtr++;
    Serial.write( hex[ working>>4 ] );
    Serial.write( hex[ working&15 ] );
  }
  Serial.write('\r');
  Serial.write('\n');
}

void float_to_byte(float f, uint8_t &b) {
  // float to big-endian
  // no negative numbers/overflow support
  // https://stackoverflow.com/questions/27007322/c-how-to-correctly-round-a-const-float-to-unsigned-int
  ((float *) b)[0] = f;
  // unsigned int i= static_cast<unsigned int>(f);
  // b[0] = ((i >> 24) && 0xFF);
  // b[1] = ((i >> 16) && 0xFF);
  // b[2] = ((i >> 8 ) && 0xFF);
  // b[3] = ((i      ) && 0xFF);
}

void float_of_byte(uint8_t &b, float &f) {
  f = ((float *) b)[0];
}

CAN_message_t prepare_bms_message(struct bms &_bms) {
  CAN_message_t msg;
  msg.id = CAN_BMS_ID;
  msg.len = 8;
  float_to_byte(_bms.current, msg.buf[0]);
  float_to_byte(_bms.voltage, msg.buf[4]);
  Serial.print("bms curr: ");
  Serial.println(((float *) msg.buf)[0]);
  Serial.print("bms volt: ");
  Serial.println(((float *) msg.buf)[1]);
}

void timerCallback(Timer* timer){
  if(TICK_ACTION == timer->getAction()){
    update_bms(_bms);
    stringify_bms(bms_print_buffer, _bms);
    Serial.println(bms_print_buffer);
    prepare_bms_message(_bms);
  }
}

void setup(void) {
  delay(1000);
  Serial.println(F("Hello Teensy 3.6 dual CAN Test."));

  can1.begin();
  can2.begin();

  seed_random(analogRead(0));

  bmsTimer = StensTimer::getInstance();
  bmsTimer->setStaticCallback(timerCallback);
  Timer* myFirstTimer = bmsTimer->setInterval(TICK_ACTION, 100);
}

void loop() {
  bmsTimer->run();
  // CAN_message_t inMsg;
  // int count = 0;
  //
  // while (count++ < 100)
  // {
  //   can1.read(inMsg);
  //   if (count % 10 == 0)
  //     Serial.print("CAN bus 0: "); hexDump(8, inMsg.buf);
  // }
  // for (int i=0; i < 5; ++i) {
  //   msg.buf[0]++;
  //   can2.write(msg);
  // }
  // delay(2000);
}
