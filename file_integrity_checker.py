import hashlib

def calculate_file_hash(file_path):
    """Calculate SHA-256 hash of a given file."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    hash_value = calculate_file_hash(file_path)
    if hash_value:
        print(f"SHA-256 Hash: {hash_value}")
    else:
        print("File not found!")
