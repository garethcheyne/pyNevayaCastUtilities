# pylint: disable=invalid-name
import os
import sys
import logging
import argparse
import zeroconf
import pychromecast
from pychromecast.controllers.youtube import YouTubeController
from subprocess import check_output

## Clear Screen
clear = lambda: os.system('cls')
clear()

# Change to the name of your Chromecast
CAST_NAME = "The Carlin TV 23"

VIDEO_ID = "VafTMsrnSTU"

## cli interface
parser = argparse.ArgumentParser()
parser.add_argument("--debug", help="Enable debug log", action="store_true")
parser.add_argument("--tofile", help="Enable debug log to file", action="store_true")
args = parser.parse_args()

if args.debug:
    if args.tofile:
        Log_Format = "%(levelname)s %(asctime)s - %(message)s"

        logging.basicConfig(filename = "logfile.log",
                            filemode = "w",
                            format = Log_Format, 
                            level = logging.ERROR)

        logger = logging.getLogger("zeroconf").setLevel(logging.DEBUG)

    else:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("zeroconf").setLevel(logging.DEBUG)


print("\n=== ARP (MAC's) =================================================")     

os.system('arp -a')

print("=== END ARP (MAC's) =================================================\n")  


# List chromecasts on the network, but don't connect
services, browser = pychromecast.discovery.discover_chromecasts()

# pychromecast.discovery.stop_discovery(browser)


if services != None:
    for index, device in enumerate(services):     

        chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[device[3]])
        cast = chromecasts[0]
        cast.wait()

        yt = YouTubeController()
        cast.register_handler(yt)
        yt.play_video(VIDEO_ID)

        print("=== Device Found " , index +1 ,"=================================================")     
        print("  Full Info: ", device)
        print("    Serivce:  ", device[0])        
        print("    UUID:  ", device[1])        
        print("    Model: ", device[2])
        print("    Name:  ", device[3])
        print("    Host:  ", device[4])
        print("    Port:  ", device[5])

else:
    print("=== No Devices Found =================================================\n")     



