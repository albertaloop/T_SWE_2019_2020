### Setup

Insert main.cpp into a PlatformIO or Arduino project.

Add the Ethernet2 library with the description "Enables network connection (local and Internet) using W5500 based Ethernet shields...."

Using PlatformIO, search for the Ethernet2 library and import it to your project so that it's under ./pio/libdeps/.../Ethernet2

Connect to the WIZ850IO module with an Ethernet cable.

Set local_ip to any ip address with the same subnet that the remote machine is on.

Set remote_ip to the ip address of your machine.

Build and upload the program to the board.

To verify that it's working, run the telemetry_module/telemetry_module_test.py script in another shell to receive the packets being sent from the board.
