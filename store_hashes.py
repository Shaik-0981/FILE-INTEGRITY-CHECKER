import hashlib
import json
import os

def calculate_file_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return None  # File doesn't exist
    
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)
    
    return hasher.hexdigest()

def store_hashes(file_paths, hash_file="hashes.json"):
    """Store hash values of files in a JSON file."""
    file_hashes = {}

    for file in file_paths:
        file_hashes[file] = calculate_file_hash(file)

    with open(hash_file, "w") as f:
        json.dump(file_hashes, f, indent=4)

    print("\n✅ Hashes stored successfully in 'hashes.json'.")

if __name__ == "__main__":
    file_paths = input("Enter file paths separated by space: ").split()
    store_hashes(file_paths)
