#include <cstdio>
#include <iostream>

#include "utils.hpp"

void test_int_to_bytes() {
	int foo = 1221;
	uint8_t bar[4];
	int_to_bytes(foo, bar);
	for (int i=0; i < 4; i++) {
		printf("0x%x\n", bar[i]);
		std::cout << "byte: " << unsigned(bar[i]) << "\n";
	}
}

void test_int_to_bytes2() {
	int foo = 1221;
	uint8_t bar[4];
	int_to_bytes2(foo, bar);
	for (int i=0; i < 4; i++) {
		printf("0x%x\n", bar[i]);
		std::cout << "byte: " << unsigned(bar[i]) << "\n";
	}
}

void test_int_of_bytes() {
	int zee;
	uint8_t bar[4];
	int_of_bytes(zee, bar);
	std::cout << "int zee: " << zee << "\n";
}

// int main() {
// 	test_int_to_bytes();
// 	test_int_to_bytes2();
// 	test_int_of_bytes();
// }