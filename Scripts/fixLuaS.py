import os
import subprocess
import sys

HEAD_LEN = 33
FIXED_HEAD = (b'\x1B\x4C\x75\x61\x53\x00\x19\x93\x0D\x0A\x1A\x0A\x04\x04\x04\x08'
              b'\x08\x78\x56\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x28\x77\x40\x01')
unluac_path = "unluac.jar"


def fixFile(src: str, dst: str) -> str:
    '''
    修复luac文件的文件头
    '''
    with open(src, 'rb') as f:
        data = f.read()
    data = FIXED_HEAD + data[HEAD_LEN:]
    with open(dst, 'wb') as f:
        f.write(data)
    return dst

def fixDir(src: str, dst: str) -> list:
    files = os.walk(src)
    tmp_files = []
    for root, _, filenames in files:
        for filename in filenames:
            src_file = os.path.join(root, filename)
            dst_file = src_file.replace(src, dst)
            dst_dir = os.path.dirname(dst_file)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            tmp_files.append(fixFile(src_file, dst_file))
    return tmp_files


def decompile(src: str, dst: str) -> bool:
    '''
    使用unluac.jar解密luac文件
    '''
    command = f'java -jar {unluac_path} {src} -o {dst}'
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2]
    if len(sys.argv) == 4:
        unluac_path = str(sys.argv[3])
    if os.path.isfile(src):
        tmp = fixFile(src, dst)
        decompile(tmp, dst)
        os.remove(tmp)
    else:
        os.makedirs(".tmp")
        tmp_files = fixDir(src, ".tmp")
        decompile(".tmp", dst)
        os.system(f'rm -rf .tmp')
