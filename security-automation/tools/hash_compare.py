import hashlib
import sys


def calculate_sha256(filename):
    """
    Calculate and return the SHA-256 hash of a file.
    """

    # Open the file in binary mode so the hash is based on the exact file bytes.
    with open(filename, "rb") as file:
        file_bytes = file.read()

    return hashlib.sha256(file_bytes).hexdigest()


def compare_hash(filename, known_hash):
    """
    Compare a file's SHA-256 hash against a known hash value.
    """

    calculated_hash = calculate_sha256(filename)

    print("Hash Comparison")
    print("-" * 40)
    print(f"File: {filename}")
    print(f"Calculated SHA-256: {calculated_hash}")
    print(f"Known SHA-256:      {known_hash}")
    print()

    # Normalize both hashes to lowercase before comparing.
    if calculated_hash.lower() == known_hash.lower():
        print("[MATCH] The file hash matches the known hash.")
    else:
        print("[NO MATCH] The file hash does not match the known hash.")


if __name__ == "__main__":
    # Expected usage:
    # python3 tools/hash_compare.py <filename> <known_sha256_hash>
    if len(sys.argv) < 3:
        print("Usage: python3 tools/hash_compare.py <filename> <known_sha256_hash>")
        sys.exit(1)

    filename = sys.argv[1]
    known_hash = sys.argv[2]

    compare_hash(filename, known_hash)
