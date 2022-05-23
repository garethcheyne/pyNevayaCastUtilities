#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Rogue DHCP server discovery
# Simon Schürg

import scapy 
import re
import requests

def _get_oui_from_mac(mac: str) -> str:
    """ 
    Returnes the OUI – Organizationally Unique Identifier of a given mac address.
    """
    assert isinstance(mac, str)
    assert mac is not ''
    mac = re.sub('[.:-]', '', mac).upper()  # remove delimiters and convert to lower case
    mac = ''.join(mac.split())  # remove whitespaces
    oui = mac[:6]
    return oui 


def find_dhcp_servers():
    # The answers to the DHCP Discovers come from different IP addresses, thats why the check has to be false
    scapy.conf.checkIPaddr = False
    # don't display scapy output
    scapy.conf.verb = 0 
    

    hw = bytes(scapy.get_if_raw_hwaddr(scapy.conf.iface))

    dhcp_discover = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") /\
                    scapy.IP(src="0.0.0.0", dst="255.255.255.255") /\
                    scapy.UDP(sport=68, dport=67) /\
                    scapy.BOOTP(chaddr=hw) /\
                    scapy.DHCP(options=[("message-type", "discover"), "end"])

    # We wait 5 seconds for the DHCP Servers to answer
    ans, unans = scapy.srp(dhcp_discover, timeout=5, multi=True)

    dhcp_servers = []
    for p in ans:
        oui = _get_oui_from_mac(p[1][scapy.Ether].src)
        dhcp_servers.append({
            'ip': p[1][scapy.IP].src,
            'mac': p[1][scapy.Ether].src,
            'vendor': requests.get('https://api.macvendors.com/{}'.format(oui)).text
            })  

    return dhcp_servers

if __name__ == "__main__":
    servers = find_dhcp_servers()
    for server in servers:
        print('Found DHCP server with IP {}, MAC {} and Vendor "{}"'.format(server['ip'], server['mac'], server['vendor']))