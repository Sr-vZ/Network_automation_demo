#!/usr/bin/env python
from netmiko import Netmiko

cisco1 = {
    "host": "10.31.3.1",
	"port":17022,
    # "username": "POD1_10",
    # "password": getpass(),
	"global_delay_factor":4,
	"blocking_timeout": 8,
    # "default_enter":'\r\n',
	# "default_enter":'\r',
    "device_type": "cisco_ios_telnet"
}
print('Script Started!')

cfg_commands = ["logging buffered 10000", "no logging console"]
net_connect = Netmiko(**cisco1)

# print(net_connect.send_config_set("en"))
print(net_connect.enable())
print(net_connect.send_command("show ip int brief"))

print(net_connect.send_command("show int | i rate"))
# print(net_connect.send_command("show int summary"))
#output = net_connect.send_config_set("en")
# print(output)
#output = net_connect.send_config_set(cfg_commands)
# print(output)
# print(net_connect.send_config_set("int gi0/1"))
print(net_connect.send_config_set("int gi0/1 \r ip address 172.10.10.2 255.255.255.0 \r no sh"))
# print(net_connect.send_config_set("ip address 172.10.10.1 255.255.255.255"))

print(net_connect.send_command("show ip int brief"))
net_connect.disconnect()
