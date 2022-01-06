# pylint: disable=invalid-name

import os
import time
import sys
import logging
import threading
import argparse
import pychromecast



############################################
#Under Dev - DO NO USE


## Clear Screen
clear = lambda: os.system('cls')
clear()

## You Tube Id
VIDEO_ID = "dQw4w9WgXcQ"

## cli interface
parser = argparse.ArgumentParser()
parser.add_argument("--debug", help="Enable debug log", action="store_true")
args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)
    #logging.getLogger("pychromecast").setLevel(logging.DEBUG)
    logging.getLogger("zeroconf").setLevel(logging.DEBUG)



# List chromecasts on the network, but don't connect
services, browser = pychromecast.discovery.discover_chromecasts()

pychromecast.discovery.stop_discovery(browser)

print("_services_", services)

# chromecasts, browser = pychromecast.get_listed_chromecasts()
# [cc.device.friendly_name for cc in chromecasts]





if services != None:
    for index, device in enumerate(services):
        print("_dev_ ", device)

        uuid = [device[1]]

        chromecasts, browser = pychromecast.discovery.discover_listed_chromecasts(uuids=uuid)


        cast = chromecasts[0]

        print("dir", dir(cast))

        print("list,", list(cast))

       # cast.wait()

        #print(cast.device)

       #print("_cast_", cast)

        # for dev in cast:
        #     print(device)
        #     dev.wait()       
        # print(cast)
        # cast.start()

        # yt = YouTubeController()
        # cast.register_handler(yt)
        # yt.play_video(VIDEO_ID)





        print("=== Device Found " , index +1 ,"=================================================")     
        print("  Full Info: ", device)
        print("    Serivce:  ", device[0])        
        print("    UUID:  ", device[1])        
        print("    Model: ", device[2])
        print("    Name:  ", device[3])
        print("    Host:  ", device[4])
        print("    Port:  ", device[5])







# chromecasts = pychromecast.get_chromecasts()

# chromecasts = chromecasts[0]

# for dev in chromecasts:
#     print(dev)
#     dev.wait()
#     yt = YouTubeController()
#     dev.register_handler(yt)
#     yt.play_video(VIDEO_ID)



