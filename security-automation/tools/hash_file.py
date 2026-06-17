import hashlib
import sys

def calculate_sha256(filename):
    with open(filename, "rb") as file:
        file_bytes = file.read()
        return hashlib.sha256(file_bytes).hexdigest()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 hash_file.py <filename>")
        sys.exit(1)
        
    filename = sys.argv[1]
        
    hash_value = calculate_sha256(filename)
    print("Hash:", hash_value)
