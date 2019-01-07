from pyModbusTCP.client import ModbusClient

em4_ip = "192.168.69.192"

c = ModbusClient(host=em4_ip, auto_open=True, auto_close=True)
f = True

while True:

    if f:
        v = 0
    else:
        v = 65535
    f = not f

    # INPUT 1-25
    for i in range(1, 26):
        is_ok = c.write_single_register(i, v)
        if is_ok:
            print("bit #" + str(i) + ": write to " + str(v))
        else:
            print("bit #" + str(i) + ": unable to write " + str(v))


    # OUTPUT 26-50
    for i in range(1, 51):
        regs = c.read_holding_registers(i, 1)
        if regs:
            print("reg ad # " + str(i) + ": " + str(regs))
        else:
            print("Error")
