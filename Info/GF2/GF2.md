# 少女前线2:追放

## Info

| | |
| - | - |
| Unity Version | 2019.4.40f1 |
| Assets Encrypted | |
| Hotfix | HybridCLR&Xlua |
| So Protection |  |

## AB文件加密/解密

### 类型1：Strip Version

抹去Unity版本信息，只需要在AssetStudio中设置Unity Version为2019.4.40f1或者2019.4.29f1即可。

### 类型2：XOR

前0x8000 bytes异或，每个文件的key不同。

``` python
import sys

std_header = [0x55, 0x6E, 0x69, 0x74, 0x79, 0x46, 0x53, 0x00, 0x00, 0x00, 0x00, 0x07, 0x35, 0x2E, 0x78, 0x2E]

key = []

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    with open(in_file, 'rb') as f:
        data = bytearray(f.read())
    for i in range(16):
        key.append(data[i] ^ std_header[i])
    i = 0
    while i < 0x8000:
        if i >= len(data):
            break
        data[i] ^= key[i % 16]
        i += 1
    with open(out_file, 'wb') as f:
        f.write(data)
```

## Lua

对于PC端，lua文件和热更新的dll一样在`GF2Exilium\GF2 Game\GF2_Exilium_Data\LocalCache\Data\ClientRes_Windows\2.0.2500\A5CFF04BAF8EAC27EF4D4716C075F344`这样的路径下。

每个字节对0xFF异或，然后使用[fixLuaS.py](../../Scripts/fixLuaS.py)来反编译