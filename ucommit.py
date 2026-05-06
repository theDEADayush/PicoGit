import uos
import ujson
import utime

from ustore import save_object 

DB_FILE = ".picogit/commits.json"

def check_file_exists(filename):
    try:
        uos.stat(filename)
        return True
    except OSError:
        return False

def create_commit(file_path, message, author="Embedded Lead"):
    
    file_hash = save_object(file_path)
    
    
    if check_file_exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            ledger = ujson.load(f)
    else:
        ledger = [] 
        
    
    commit_record = {
        "commit_id": len(ledger) + 1,
        
        "timestamp": utime.time(), 
        "author": author,
        "message": message,
        "file": file_path,
        "hash": file_hash
    }
    
    
    ledger.append(commit_record)
    
    with open(DB_FILE, "w") as f:
         
        
        ujson.dump(ledger, f)
        
    print(f"Commit #{commit_record['commit_id']} successful: {message}")
    return commit_record

if __name__ == "__main__":
    
    create_commit("test.txt", "First bare-metal commit!")