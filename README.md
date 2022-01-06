# pyNevayaCastUtilities (Use at own rist.)

## Unifi Auth
Simple CLI to auth the Nevaya Server MAC's on a Unifi Network using Unifi Guest Portal. This will auth the Nevaya MAC's for 10 Years..

Example Result
=== ==============================================================
NEVAYA Casting Unifi Config Starting...

  Connecting to Controller on 192.168.1.1
Nevaya 0 Done: [{'_id': '61d656f3b60cef058dec6d51', 'mac': '00:11:22:33:33:33', 'start': 1641436915, 'site_id': '61bd46e4806f2c067914a0ec', 'authorized_by': 'api', 'end': 1957009124}]
Nevaya 1 Done: [{'_id': '61d656f4b60cef058dec6d53', 'mac': '00:11:22:33:45:01', 'start': 1641436916, 'site_id': '61bd46e4806f2c067914a0ec', 'authorized_by': 'api', 'end': 1957009124}]


## Sniff Chromecast
Simple test to sniff out chromecast once auth on Guest Network and Nevaya Service.

Example Result.
=== Device Found  1 =================================================
  Full Info:  CastInfo(services={ServiceInfo(type='mdns', data='Chromecast-9a720aad27ed05abf4aac254a0f1382e._googlecast._tcp.local.')}, uuid=UUID('9a720aad-27ed-05ab-f4aa-c254a0f1382e'), model_name='Chromecast', friendly_name='The Carlin TV 23', host='172.20.0.8', port=8009, cast_type=None, manufacturer=None)
    Serivce:   {ServiceInfo(type='mdns', data='Chromecast-9a720aad27ed05abf4aac254a0f1382e._googlecast._tcp.local.')}
    UUID:   9a720aad-27ed-05ab-f4aa-c254a0f1382e
    Model:  Chromecast
    Name:   The Carlin TV 23
    Host:   172.20.0.8
    Port:   8009