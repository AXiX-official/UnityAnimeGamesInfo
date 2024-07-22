import os
import sys

key_bytes = [51,54,49,53,49,52,50,99,98,57,49,52,57,99,100,97,48,52,53,98,48,102,98,50,101,100,102,49,55,55,55,50]

def decrypt_file(in_path, out_path):
    with open(in_path, 'rb') as f:
        data = f.read()
    data = bytearray(data)
    v6 = 0
    while v6 < len(data):
        v9 = v6 % len(key_bytes)
        data[v6] ^= key_bytes[v9]
        v6 += 1
    with open(out_path, 'wb') as f:
        f.write(data)

def decrypt(source, target) :
    if not os.path.exists(target) :
        os.makedirs(target)
    for root, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root, source)
        target_dir = os.path.join(target, rel_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_dir, file)
            decrypt_file(source_file, target_file)

if __name__ == "__main__" :
    if sys.argv.__len__() < 3 :
        print("Usage: python decrypt.py source target")
        sys.exit()
    source = sys.argv[1]
    target = sys.argv[2]
    if os.path.isdir(source) :
        decrypt(source, target)
    else :
        decrypt_file(source, target)
