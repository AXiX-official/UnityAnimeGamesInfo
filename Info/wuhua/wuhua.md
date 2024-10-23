# 物华弥新

## Info

| | |
| - | - |
| Unity Version | 2018.4.36f1 |
| Assets Encrypted | See below |
| Hotfix | HybridCLR&Xlua |
| So Protection | |

## AB包解密&加密

简单的xor加密，但是xor的字节范围经常改变，而且没花时间去研究key的计算规则

一个简单的解密逻辑如下

```python
import sys

if __name__ == '__main__':
    inPath = sys.argv[1]
    outPath = sys.argv[2]
    with open(inPath, 'rb') as f:
        data = bytearray(f.read())
    key = data[51]
    for i in range(50, 120):
        data[i] ^= key
    with open(outPath, 'wb') as f:
        f.write(data)
```