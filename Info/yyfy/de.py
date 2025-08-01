import hashlib
original_head = [0x55, 0x6E, 0x69, 0x74, 0x79, 0x46, 0x53, 0x00, 0x00, 0x00, 0x00, 0x07, 0x35, 0x2E, 0x78, 0x2E]

if __name__ == "__main__" :
    file_path = r"C:\Users\AXiX\Desktop\jsBenCGM_11001.dat"
    with open(file_path, "rb") as f:
        data = bytearray(f.read())
        key = bytearray(16)
        for i in range(16):
            key[i] = data[i] ^ original_head[i]

        md5_hash = hashlib.md5(data).hexdigest()
        print("前16字节MD5:", md5_hash)
        print("key:", key.hex())

        for i in range(0x0D0):
            data[i] ^= key[i % 16]

        print("MD5:", hashlib.md5(data).hexdigest())

        with open(file_path + ".de", "wb") as ff:
            ff.write(data)