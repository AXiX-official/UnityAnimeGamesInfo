import sys
import os
import hashlib
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

mCommonKey = "rfizzapj"
mCommonKey = hashlib.md5(mCommonKey.encode()).hexdigest()
mCommonKey = mCommonKey[-8:]
#mDesMKeys = [111, 151, 50, 205, 123, 222, 185, 45]
mDesMKeys = b'\x6f\x97\x32\xcd\x7b\xde\xb9\x2d'

def DecryptBytes(bytes, key) :
    key = key.encode()
    cipher = DES.new(key, DES.MODE_CBC, mDesMKeys)
    decrypted_data = unpad(cipher.decrypt(bytes), DES.block_size)
    return decrypted_data

def DecryptFile(source, target) :
    with open(source, "rb") as f :
        data = f.read()
    decrypted_data = DecryptBytes(data, mCommonKey)
    with open(target, "wb") as f :
        f.write(decrypted_data)

def Decrypt(source, target) :
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
            DecryptFile(source_file, target_file)


if __name__ == "__main__" :
    if sys.argv.__len__() < 3 :
        print("Usage: python decrypt.py source target")
        sys.exit()
    source = sys.argv[1]
    target = sys.argv[2]
    if os.path.isdir(source) :
        Decrypt(source, target)
    else :
        DecryptFile(source, target)