#include <Arduino.h>
#include <ChibiOS_ARM.h>
#include "CANBus.h"
#include "circular_buffer.h"

//flexcan config script made with help of
//http://eet.etec.wwu.edu/KurtTaylor/project/docs/Bibleography/MCU/ConnSoftDocs/Kinetis%20SDK%20v2.0.0%20API%20Reference%20Manual/group__flexcan__driver.html
flexcan_config_t flexcanConfig;

FLEXCAN_GetDefaultConfig(&flexcanConfig);
FLEXCAN_Init(CAN_SETUP, &flexcanConfig);
FLEXCAN_Enable(CAN_SETUP, true);

FlexCAN Cbus(500000);
CircularBuffer<CAN_message_t, 10> in_buff, out_buff;
uint16_t wait_time = 40; // 40 ms
uint8_t CAN_id = 0;


static struct States
{
    uint32_t pod_state = Status::SafeToApproach;
    bool ready_to_send = false;
    bool fault_detected = false;
    uint32_t fault_type = FaultType::No_Fault;
    double position = 0;
    double velocity = 0;
    double acceleration = 0;
    bool should_launch = true;
} pod_context;

enum Status
{
    Fault = 0,
    SafeToApproach = 1,
    ReadyToLaunch = 2,
    Launching = 3,
    Coasting = 4,
    Braking = 5,
    Crawling = 6
};

enum Msg_Type
{
    Telemetry = 0,
    Command = 1,
    Fault = 2
};

enum CANID_List
{
    General = 0,
    BMS = 1,
    Nav = 2,
    Brk = 3,
    Mtr = 4
};

enum FaultType
{
    No_Fault = 0,
    Gen_Fault = 1,
    Mtr_Fault = 2,
    Nav_Fault = 3,
    Brk_Fault = 4
};

uint8_t *fault_msg(uint8_t CAN_id, uint8_t fault_type)
{
    if (fault_detected)
    {
        switch (fault_type)
        {
        case FaultType::Gen_Fault:
            /* insert response */
            break;

        case FaultType::Mtr_Fault:
            /* insert response */
            break;

        case FaultType::Nav_Fault:
            /* insert response */
            break;

        case FaultType::Brk_Fault:
            /* insert response */
            break;

        default:
            /* insert response */
            break;
        }
    }
    else
    {
        return -1; //error, fault hasn't been identified
    }

    return 0;
}

CAN_message_t *build_msg(uint8_t recipient_id, uint8_t msg_type)
{
    CAN_message_t out_msg;
    out_msg.ext = 0;
    out_msg.id = recipient_id;
    out_msg.len = PACKET_LENGTH;
    for (size_t i = 0; i < PACKET_LENGTH; i++)
    {
        out_msg.buf[i] = 0x0F; //just a placeholder. fill according to situation.
    }

    // out_msg.timeout = wait_time;

    //cbus.write(out_msg);
    return out_msg;
}



void setup()
{
    Cbus.begin();
    halInit();
    chSysInit();
}

void loop()
{
    //add getter for ready to send flag here
    if (pod_context.ready_to_send)
    {
        //read context file to know request type here
        msg_type = Msg_Type::Telemetry;     //placeholder
        recipient_id = CANID_List::General; //placeholder
        CAN_message_t *out_msg = build_msg(recipient_id, msg_type);
        out_buff.Write(out_msg);
        //Cbus.write(out_msg);
    }

    //begin reading messages
    while (Cbus.available())
    {
        CAN_message_t in_msg;
        Cbus.read(in_msg);
        in_buff.Write(in_msg);
    }

    //unpacking messages
    for (size_t i = 0; i < in_buff.numElements(); i++)
    {
        CAN_message_t in_msg = in_buff.Read();

        //here, check the contents of the message
        msg_type == Msg_Type::Telemetry //placeholder. change.
            if (msg_type == Msg_Type::Telemetry)
        {
            //handle each CANbus member differently
            //add to context, and pass info to UDP module via context
        }
        elif (msg_type == Msg_Type::Fault)
        {
            //handle each CANbus member differently
            recipient_id = CANID_List::General;
            CAN_message_t *out_msg = build_msg(0, msg_type);
            out_buff.Write(out_msg);
        }
    }
    delay(wait_time);
}