import uos
from uhash import generate_hash


def copy_file(src_path, dest_path):
    with open(src_path, 'rb') as f_src:
        with open(dest_path, 'wb') as f_dest:
            while True:
                chunk = f_src.read(1024)
                if not chunk:
                    break
                f_dest.write(chunk)

def save_object(file_path):
    file_hash = generate_hash(file_path)
    
    # String Slicing (Same as laptop!)
    folder_name = file_hash[:2]
    file_name = file_hash[2:]
    
    
    base_dir = ".picogit"
    obj_dir = ".picogit/objects"
    db_path = f"{obj_dir}/{folder_name}"
    
    
    for directory in [base_dir, obj_dir, db_path]:
        try:
            uos.mkdir(directory)
        except OSError:
            
            pass 
            
    final_file_path = f"{db_path}/{file_name}"
    
    
    copy_file(file_path, final_file_path)
    
    print(f"Hardware copy saved to: {final_file_path}")
    return file_hash

if __name__ == "__main__":
    
    save_object("test.txt")