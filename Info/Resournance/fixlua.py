import os
import subprocess
import sys

HEAD_LEN = 33
FIXED_HEAD = (b'\x1B\x4C\x75\x61\x53\x00\x19\x93\x0D\x0A\x1A\x0A\x04\x04\x04\x08'
              b'\x08\x78\x56\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x28\x77\x40\x01')
unluac_path = "unluac.jar"


def fixlua(src: str, dst: str):
    '''
    修复luac文件的文件头
    '''
    with open(src, 'rb') as f:
        data = f.read()
    data = FIXED_HEAD + data[HEAD_LEN:]
    with open(dst, 'wb') as f:
        f.write(data)


def decompile(src: str, dst: str) -> bool:
    '''
    使用unluac.jar解密luac文件
    '''
    command = f'java -jar {unluac_path} {src} > {dst}'
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        return True
    else:
        return False


def fix_and_decompile(src: str, dst: str) -> bool:
    tmp = dst + '.tmp'
    fixlua(src, tmp)
    flag = decompile(tmp, dst)
    if flag:
        os.remove(tmp)
    return flag


def main(src: str, dst: str):
    files = os.walk(src)
    count = 0
    failed_files = []
    for root, _, filenames in files:
        for filename in filenames:
            if filename.endswith('.lua'):
                src_file = os.path.join(root, filename)
                dst_file = src_file.replace(src, dst)
                dst_dir = os.path.dirname(dst_file)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                flag = fix_and_decompile(src_file, dst_file)
                count += 1
                print(count)
                if not flag:
                    failed_files.append((src_file, dst_file))
    for src_file, dst_file in failed_files:
        print(f'Failed to fix {src_file} to {dst_file}')


if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2]
    if len(sys.argv) == 4:
        unluac_path = str(sys.argv[3])
    main(src, dst)