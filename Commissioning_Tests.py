from netmiko import Netmiko


mgmt_IP = '10.31.3.1'
port = 17002
ONEA = '57334740'
router = {
    "host": mgmt_IP,
	"port": port,
    # "username": "POD1_10",
    # "password": getpass(),
	"global_delay_factor":4,
	"blocking_timeout": 8,
    # "default_enter":'\r\n',
	# "default_enter":'\r',
    "device_type": "cisco_ios_telnet"
}


net_connect = Netmiko(**router)
print(net_connect.enable())

print('Reading the commissioning template...')
config_commands = []
f = open("XIAN_Commissioning_Template.txt", "r")
for line in f:
	if line[0] != '!':
		if len(line) > 1:
			print('Command Received: ',line)
			config_commands.append(line)
#print(config_commands)
#for cmd in config_commands:
#	print(net_connect.send_command(cmd))
#print(net_connect.send_config_set(config_commands))
output = net_connect.send_config_set(config_commands)
print(output)

net_connect.disconnect()


