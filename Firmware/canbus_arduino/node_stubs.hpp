const float BMS_MIN_VOLTAGE = 10.0; // Volts
const float BMS_MAX_VOLTAGE = 12.0;
const float BMS_MIN_CURRENT = 0.1; // Amps
const float BMS_MAX_CURRENT = 3.0;
const float BMS_MIN_TEMP = 15.0; // Celcius
const float BMS_MAX_TEMP = 40.0;

enum nodes {
	BMS,
	NAV,
	BRAKES,
	MOTOR,
	OBC
};

struct bms {
	nodes node = BMS;
	float voltage;
	float current;
	float temp;
};

float get_bounded_random_number(float lower, float upper);
void update_bms(struct bms & _bms);
int stringify_bms(char * buffer, struct bms &_bms);
void seed_random(int seed);