import re
import os

def tran(input_path, output_path):
    pattern = re.compile(r'(\\(\d{3}))+')

    with open(input_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    def replace_long_match(match):
        codes = match.group().split('\\')[1:] 
        byte_values = [int(code) for code in codes]
        byte_sequence = bytes(byte_values)
        result = ""
        try:
            result = byte_sequence.decode('utf-8')
        except UnicodeDecodeError:
            result = match.group()
        return result

    content = pattern.sub(replace_long_match, content)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(content)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py input_file <output_file>")
        sys.exit(1)
    input_path = sys.argv[1]
    if os.path.isfile(input_path):
        tran(input_path, input_path)
    else:
        files = os.walk(input_path)
        for path, _, file_list in files:
            for file_name in file_list:
                file_path = os.path.join(path, file_name)
                tran(file_path, file_path)