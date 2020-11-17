#include <Arduino.h>
#include <ChibiOS_ARM.h>

// This program demonstrates cooperative multitasking

bool led_on = false;


THD_WORKING_AREA(waThread1, 128);

static THD_FUNCTION(Thread1, arg) {
  (void)arg;
  chRegSetThreadName("slow_blink");
  int i = 0;
  while (1) {
    Serial.println("Thread 1");
    i = 0;
    // Blink LED every 500 ms.
    for(int j = 0; j < 10; j++) {
      if (i == 5) {
        digitalWrite(13, HIGH);
        led_on = true;
      } else {
        if(led_on) {
          digitalWrite(13, LOW);
          led_on = false;
        }
      }
      i += 1;
      delay(100);
    }
    chThdYield();
  }
}


THD_WORKING_AREA(waThread2, 128);

static THD_FUNCTION(Thread2, arg) {
  (void)arg;
  chRegSetThreadName("fast_blink");
  while (1) {
    Serial.println("Thread 2");
    // Blink LED every 100 ms
    for(int i = 0; i < 10; i++) {
      if(led_on) {
        digitalWrite(13, LOW);
      } else {
        digitalWrite(13, HIGH );
      }
      led_on = !led_on;
      delay(100);
    }
    chThdYield();
  }
}


void setup() {
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW );

  halInit();
  chSysInit();

  chThdCreateStatic(waThread1, sizeof(waThread1),
    NORMALPRIO, Thread1, NULL);
  chThdCreateStatic(waThread2, sizeof(waThread2),
    NORMALPRIO, Thread2, NULL);

}

void loop() {
  Serial.println("Main thread");
  chThdYield();
}