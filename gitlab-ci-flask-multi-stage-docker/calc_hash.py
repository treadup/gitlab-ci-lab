import sys
import hashlib
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: python3 calc_hash.py [filename]")

filename = sys.argv[1]

if not Path(filename).is_file():
    print(f"File does not exist: {filename}")
    exit(1)

with open(filename, "rb") as f:
    data = f.read()

hash_object = hashlib.sha1(data)
print(hash_object.hexdigest())
