# pylint: disable=invalid-name
import os
import logging
import argparse
import pychromecast

## Clear Screen
clear = lambda: os.system('cls')
clear()

## cli interface
parser = argparse.ArgumentParser()
parser.add_argument("--debug", help="Enable debug log", action="store_true")
args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("zeroconf").setLevel(logging.DEBUG)



# List chromecasts on the network, but don't connect
services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)


if services != None:
    for index, device in enumerate(services):
        print("_dev_ ", device)

        uuid = [device[1]]
        print("=== Device Found " , index +1 ,"=================================================")     
        print("  Full Info: ", device)
        print("    Serivce:  ", device[0])        
        print("    UUID:  ", device[1])        
        print("    Model: ", device[2])
        print("    Name:  ", device[3])
        print("    Host:  ", device[4])
        print("    Port:  ", device[5])

else:
    print("=== No Devices Found =================================================")     