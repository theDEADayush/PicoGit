import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Scanning the airwaves...")
networks = wlan.scan()

print(f"Found {len(networks)} networks:")
for net in networks:
    
    ssid = net[0].decode('utf-8')
    rssi = net[3]
    print(f" - {ssid} (Signal: {rssi})")