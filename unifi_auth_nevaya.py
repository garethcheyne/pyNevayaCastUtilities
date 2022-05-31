import os
import urllib3
import argparse
urllib3.disable_warnings()
from pyunifi.controller import APIError, Controller

####
## Exmaple for UDM
# python .\unifi_auth_nevaya.py --ip 192.168.1.1 --u johndoe --p secret
## Example for CloudKey Gen 1
# python .\unifi_auth_nevaya.py --ip 192.168.1.1 --s 8443 --v v4 --u johndoe --p secret
###

#Nevaya MAC address for Casting Service.
NEVAYA_MACS = ["00:11:22:33:33:33","00:11:22:33:45:01"]

UNIFI_IP = "192.168.0.1"
UNIFI_PORT = 443
USERNAME = "ubnt"
PASSWORD  = "ubnt"
VERSION = "UDMP-unifiOS"


## Clear Screen
clear = lambda: os.system('cls')
clear()
print("=================================================================")
print("NEVAYA Casting Unifi Config Starting...")

##  CLI Arguments
parser = argparse.ArgumentParser(description="Arguments for Nevaya Server setting auto add for Ubuquiti Unifi Controller API,")

parser.add_argument("--ip", help="Unifi Service IP (Default 192.168.0.1)", action="store")
parser.add_argument("--s", help="Unifi Service Port/Socket (Default 443)", action="store")
parser.add_argument("--v", help="Unifi Type (UDMP-unifiOS, unifiOS, or version#, Default UDMP)", action="store")
parser.add_argument("--u", help="Unifi Admin Login", action="store", required=True)
parser.add_argument("--p", help="Unifi Admin Padssword", action="store", required=True)
args = parser.parse_args()

if args.ip:
    UNIFI_IP = args.ip

if args.s:
    UNIFI_PORT = args.s

if args.v:
    VERSION = args.v

if args.u:
    USERNAME = args.u

if args.p:
    PASSWORD = args.p



## Run Update.
#Create Connection
print("  Connecting to Controller on {} port: {}, version: {}".format(UNIFI_IP, UNIFI_PORT, VERSION))
try:
    unifi = Controller(host=UNIFI_IP, username=USERNAME, password=PASSWORD, port=UNIFI_PORT, version=VERSION, ssl_verify=False)
    print("\n\n")

        # Auth Nevaya MAC's on Guest VLAN

    
    for i, mac in enumerate(NEVAYA_MACS):

        response = unifi.authorize_guest(mac, 15259487) # 30 Years
        print("Nevaya {} Done: {}".format(i, response))
        
    print("\n\n")

except APIError():

    print("\n\n Failed to conntect, please check the arguments settings. \n\n")
    print("Unifi Controller IP: {}".format(UNIFI_IP))
    print("Unifi Controller Port: {}".format(UNIFI_PORT))
    print("Unifi Controller Username : {}".format(USERNAME))
    print("Unifi Controller Password: {}".format(PASSWORD))
    print("\n\n")


