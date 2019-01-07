# em4-tcpip-tester
Read/Writes to all TCPIP registers on a Crouzet EM4 using Python

This script will run against any EM4 with TCP Modbus enabled, the
included pm4 program can be used with the simulator boards to get
a visual feedback of correct value writing.


1. Install the python requirements
2. If needed, write the program to the PLC, updating the stored controller
ip if required.
3. Run `python run_test.py`