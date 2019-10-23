from __future__ import unicode_literals, print_function
import time
from netmiko import ConnectHandler, redispatch

cisco_SW5 = {
    'device_type': 'cisco_ios',
	# 'protocol':   'telnet',
    'host':   '10.31.3.1',
    'username': 'POD1_10',
    'password': 'nvmdd',
    'port' : 10001,          # optional, defaults to 22
    # 'secret': 'nvmdd',     # optional, defaults to ''
}
# net_connect = ConnectHandler(
    # device_type = 'terminal_server',        # changed
	# protocol:   'telnet',
	# device_type="cisco_ios_telnet",
    # ip = '10.31.3.1',
    # username = 'POD1_10',
    # password = 'nvmdd',
	# global_delay_factor = 4,
	# default_enter = '\r\n',
    # port=17018
# )
net_connect = ConnectHandler(**cisco_SW5)
print(net_connect)