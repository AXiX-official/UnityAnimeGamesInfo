from Crypto.Cipher import AES
import struct
import binascii

key = b'wiki is transfer'

def decrypt_aes(encrypted_file, output_file):
    with open(encrypted_file, 'rb') as f:
        file_content = f.read()

    if file_content[:7] == b'UnityFS':
        with open(output_file, 'wb') as f:
            f.write(file_content)
        return

    iv_length = struct.unpack('<I', file_content[-4:])[0]
    assert iv_length == 16
    l = len(file_content)
    data_end = l - 4 - iv_length
    iv = file_content[data_end:l - 4]
    encrypted_data = file_content[:data_end]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    pad = decrypted_data[-1]
    decrypted_data = decrypted_data[:-pad]
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

if __name__ == '__main__':
    import sys
    # Usage: python decrypt.py encrypted_dir output_dir
    encrypted_dir = sys.argv[1]
    output_dir = sys.argv[2]
    import os
    for root, dirs, files in os.walk(encrypted_dir):
        for file in files:
            encrypted_file = os.path.join(root, file)
            output_file = os.path.join(output_dir, file)
            decrypt_aes(encrypted_file, output_file)