import os
import sys
import json

def extract(file_obj, offset, output_path, name):
    file_obj.seek(offset + 32)
    size = int.from_bytes(file_obj.read(8), byteorder="big")
    file_obj.seek(offset)
    data = file_obj.read(size)
    with open(os.path.join(output_path, name), "wb") as f:
        f.write(data)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python extract.py <asset_path> <json_path> <output_path>")
        sys.exit(1)
    asset_path = sys.argv[1]
    json_path = sys.argv[2]
    output_path = sys.argv[3]
    with open(asset_path, "rb") as asset_file:
        with open(json_path, "r") as f:
            jsonData = f.read()
        data = json.loads(jsonData)["data"]
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        for item in data:
            key, offset = item["key"], item["offset"]
            if offset != 0:
                extract(asset_file, offset, output_path, key)