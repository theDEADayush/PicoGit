import network
import utime
from microdot import Microdot, Response
from ucommit import create_commit


SSID = "BH 1 WIFI"
PASSWORD = "AYUSHWIFI"

def connect_wifi():
    
    network.country('IN') 
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
   
    wlan.config(pm=0xa11140)
    
    wlan.connect(SSID, PASSWORD)
    print(f"Connecting to {SSID}...")
    
    max_wait = 20
    while max_wait > 0:
        status = wlan.status()
        if status < 0 or status >= 3:
            break
        max_wait -= 1
        print(f"Waiting... (Current Status: {status})")
        utime.sleep(1)
        
    status = wlan.status()
    if status != 3:
        print("\n--- CONNECTION FAILED ---")
        print(f"Final Error Code: {status}")
        if status == -1: print("Meaning: General connection failure (Router rejected us).")
        if status == -2: print("Meaning: Network not found (Antenna couldn't see it).")
        if status == -3: print("Meaning: Wrong Password or WPA3 Security blocked us.")
        raise RuntimeError('Wi-Fi connection failed!')
    else:
        ip_address = wlan.ifconfig()[0] 
        print(f"Connected successfully! Pico IP: {ip_address}")
        return ip_address


app = Microdot()
Response.default_content_type = 'application/json'

@app.route('/api/commit', methods=['POST', 'OPTIONS'])
def api_handle_commit(request):
    
    cors_headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Accept',
        'Access-Control-Max-Age': '86400'
    }

    
    if request.method == 'OPTIONS':
        return '', 200, cors_headers
        
    
    try:
        payload = request.json
        file_path = payload.get('file')
        message = payload.get('message')
        author = payload.get('author', 'Web App UI')
        
        record = create_commit(file_path, message, author)
        
        return record, 201, cors_headers
        
    except Exception as e:
        return {"error": str(e), "status": "failed"}, 500, cors_headers

if __name__ == '__main__':
    pico_ip = connect_wifi()
    print(f"\nStarting API Server. Tell the Web Dev to send POST requests to:")
    print(f"http://{pico_ip}/api/commit")
    app.run(port=80, debug=True)