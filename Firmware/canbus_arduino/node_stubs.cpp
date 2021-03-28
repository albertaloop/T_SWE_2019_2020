#include <cstdio>
#include <cstdlib>
#include <stdexcept>

#include "node_stubs.hpp"

bool seeded = false;

float get_bounded_random_number(float lower, float upper) {
	if (lower >= upper) {
		return -1.0;
	}
	if (not seeded) {
		return -1.0;
	}
	return lower + (rand() / ( RAND_MAX / (upper-lower) ) ) ;
}

void update_bms(struct bms &_bms) {
	_bms.voltage = get_bounded_random_number(BMS_MIN_VOLTAGE,BMS_MAX_VOLTAGE);
	_bms.current = get_bounded_random_number(BMS_MIN_CURRENT,BMS_MAX_CURRENT);
	_bms.temp = get_bounded_random_number(BMS_MIN_TEMP,BMS_MAX_TEMP);
}

int stringify_bms(char* buffer, struct bms &_bms) {
	return sprintf(buffer, "BMS Voltage: %lf. Current: %lf. Temperature: %lf", _bms.voltage, _bms.current, _bms.temp);
}

void seed_random(int seed) {
	srand((unsigned) seed);
	seeded = true;
}