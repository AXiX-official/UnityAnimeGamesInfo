import re
import os

def tran(input_path, output_path):
    # 定义匹配转义序列的正则表达式
    pattern = re.compile(r'\\(\d{3})\\(\d{3})\\(\d{3})')

    # 读取输入文件内容
    with open(input_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    # 替换匹配的转义序列为对应的中文字符
    def replace_match(match):
        code1 = int(match.group(1))
        code2 = int(match.group(2))
        code3 = int(match.group(3))
        if code1 >= 0xe0 and code1 < 0xef and code2 >= 0x80 and code2 <= 0xbf and code3 >= 0x80 and code3 <= 0xbf:
            # UTF-8编码中，一个中文字符由3个字节表示
            return bytes([code1, code2, code3]).decode('utf-8')
        else:
            # 如果不是中文字符的转义序列，则原样返回
            return match.group(0)

    # 使用正则表达式替换
    content = pattern.sub(replace_match, content)

    # 将处理后的内容写入输出文件
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