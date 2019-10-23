from netmiko import Netmiko


XIAN_1= { 
    "host": "10.31.3.1",
	"port":17002,
    # "username": "POD1_10",
    # "password": getpass(),
	"global_delay_factor":4,
	#"blocking_timeout": 8,
    # "default_enter":'\r\n',
	# "default_enter":'\r',
    "device_type": "cisco_ios_telnet"  
}
print("Initalizing Router 1...")
hostname = "bxcs-r-btbbmr491045"
loopback10 = "172.108.23.5 255.255.255.255"
vlan1_ip = "10.10.160.4 255.255.255.0"

net_connect = Netmiko(**XIAN_1)
print(net_connect.enable())
print(net_connect.send_config_set("hostname "+hostname))
print(net_connect.send_config_set("int lo10 \r no sh \r ip addr "+loopback10))
print(net_connect.send_config_set("int vlan 1 \r no sh \r ip addr "+vlan1_ip))
print(net_connect.send_command("show ip int brief"))
net_connect.disconnect()

XIAN_2 = {
    "host": "10.31.3.1",
	"port":17004,
    # "username": "POD1_10",
    # "password": getpass(),
	"global_delay_factor":4,
	#"blocking_timeout": 8,
    # "default_enter":'\r\n',
	# "default_enter":'\r',
    "device_type": "cisco_ios_telnet"  
}
print("Initalizing Router 2...")
hostname = "bxcs-r-btbbmr491046"
loopback10 = "172.108.23.6 255.255.255.255"
vlan1_ip = "10.10.160.8 255.255.255.0"

net_connect = Netmiko(**XIAN_2)
print(net_connect.enable())
print(net_connect.send_config_set("hostname "+hostname))
print(net_connect.send_config_set("int lo10 \r no sh \r ip addr "+loopback10))
print(net_connect.send_config_set("int vlan 1 \r no sh \r ip addr "+vlan1_ip))
print(net_connect.send_command("show ip int brief"))
net_connect.disconnect()

XIAN_3 = {
    "host": "10.31.3.1",
	"port":17006,
    # "username": "POD1_10",
    # "password": getpass(),
	"global_delay_factor":4,
	#"blocking_timeout": 8,
    # "default_enter":'\r\n',
	# "default_enter":'\r',
    "device_type": "cisco_ios_telnet"  
}
print("Initalizing Router 3...")
hostname = "bxcs-r-btbbmr491047"
loopback10 = "172.108.23.7 255.255.255.255"
vlan1_ip = "10.10.160.12 255.255.255.0"

net_connect = Netmiko(**XIAN_3)
print(net_connect.enable())
print(net_connect.send_config_set("hostname "+hostname))
print(net_connect.send_config_set("int lo10 \r no sh \r ip addr "+loopback10))
print(net_connect.send_config_set("int vlan 1 \r no sh \r ip addr "+vlan1_ip))
print(net_connect.send_command("show ip int brief"))
net_connect.disconnect()

XIAN_4 = {
    "host": "10.31.3.1",
	"port":17008,
    # "username": "POD1_10",
    # "password": getpass(),
	"global_delay_factor":4,
	#"blocking_timeout": 8,
    # "default_enter":'\r\n',
	# "default_enter":'\r',
    "device_type": "cisco_ios_telnet"  
}
print("Initalizing Router 4...")
hostname = "bxcs-r-btbbmr491048"
loopback10 = "172.108.23.8 255.255.255.255"
vlan1_ip = "10.10.160.16 255.255.255.0"

net_connect = Netmiko(**XIAN_4)
print(net_connect.enable())
print(net_connect.send_config_set("hostname "+hostname))
print(net_connect.send_config_set("int lo10 \r no sh \r ip addr "+loopback10))
print(net_connect.send_config_set("int vlan 1 \r no sh \r ip addr "+vlan1_ip))
print(net_connect.send_command("show ip int brief"))
net_connect.disconnect()

print('All XIAN routers initial config done!')