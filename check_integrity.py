import hashlib
import json
import os

def calculate_file_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    
    if not os.path.exists(file_path):
        return None  # File doesn't exist

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)
    
    return hasher.hexdigest()

def check_integrity(hash_file="hashes.json"):
    """Check if files have been modified or deleted."""
    try:
        with open(hash_file, "r") as f:
            stored_hashes = json.load(f)
    except FileNotFoundError:
        print("\n❌ 'hashes.json' not found! Please run 'store_hashes.py' first.")
        return

    for file, stored_hash in stored_hashes.items():
        current_hash = calculate_file_hash(file)

        if current_hash is None:
            print(f"❌ File '{file}' not found.")
        elif current_hash == stored_hash:
            print(f"✅ File '{file}' is intact.")
        else:
            print(f"⚠️ File '{file}' has been modified!")

if __name__ == "__main__":
    check_integrity()
