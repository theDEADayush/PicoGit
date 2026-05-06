import uhashlib
import ubinascii

def generate_hash(file_path):
    
    sha256_hash = uhashlib.sha256()
    
    with open(file_path, "rb") as f:
        while True:
            
           
            chunk = f.read(1024)
            if not chunk:
                break
            sha256_hash.update(chunk)
            
    
    raw_bytes = sha256_hash.digest()
    
    hex_string = ubinascii.hexlify(raw_bytes).decode('utf-8')
    
    return hex_string

if __name__ == "__main__":
    with open("test.txt", "w") as f:
        f.write("Hello from the Pico W!")
    print("Hardware Hash:", generate_hash("test.txt"))