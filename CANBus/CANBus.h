#ifndef __CANBus__
#define __CANBus__

#include <FlexCAN.h>
#include "circular_buffer.h"

struct CANBus
{
    FlexCAN* fc;

    void receive_input();
    void process_input();

    void send_output();
}

extern CANBus can_bus;


#endif