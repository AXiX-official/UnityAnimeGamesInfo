# 交错战线(CrossCore)

## Info

| | |
| - | - |
| Unity Version | 2019.4.40f1 |
| Assets Encrypted | FakeHeader |
| Hotfix | XLua |
| So Protection | |

## luascripts

关于交错战线的lua脚本文件的解密和再封包在这篇Blog[解密与修改交错战线的LuaScripts](https://blog.axix.top/index.php/2024/03/21/103/)中已经讲的比较详细了。

## FakeHeader

FakeHeader本身就是在文件前加上一段任意的无效数据，往往是原文件头部一点长度的拷贝。

对于交错战线，这个长度不是固定的，其具体计算方法如下：

```Python
def get_ab_offset(filename: str)->int:
    if filename is None or len(filename) == 0:
        return 23
    filename = os.path.basename(filename)
    offset = 23
    len_filename = len(filename)
    for i in range(3):
        index = len_filename - i - 1
        if index < 0: 
            break
        char = ord(filename[index])
        hash_code = char | (char << 16)
        offset += hash_code
    offset = max(1, abs(offset) % 256)
    return offset
```