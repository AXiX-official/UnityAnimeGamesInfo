# 异界事务所(CounterSide)

## Info

| | |
| - | - |
| Unity Version | 2020.3.40f1 |
| Assets Encrypted | See below |
| Hotfix | lua5.4 |
| So Protection | |

## Assets Encryption

以下是一个解密逻辑的示例

``` python
import sys
import hashlib

def parse_uint64(value, format_flag):
    value = value.strip()
    if format_flag == 515:
        return int(value, 16)
    else:
        raise ValueError("Unsupported format flag")

if __name__ == '__main__':
    path = "ab_unit_face_card.asset"
    with open(path, "rb") as f:
        data = bytearray(f.read())
    decryptSize = min(len(data), 212)
    # calculate md5
    md5 = hashlib.md5(path.split('.')[0].lower().encode()).hexdigest()
    v25 = md5[:16]
    v26 = md5[16:32]
    v27 = md5[:8]
    v28 = md5[16:24]
    v29 = v27 + v28
    v30 = md5[8:16]
    v31 = md5[24:32]
    v32 = v30 + v31
    item = parse_uint64(v25, 515)
    v63 = parse_uint64(v26, 515)
    v62 = parse_uint64(v29, 515)
    v61 = parse_uint64(v32, 515)
    masklist = [item, v63, v62, v61]
    p = 0
    mask_pos = 0
    while p < decryptSize:
        if decryptSize - p > 7:
            value = int.from_bytes(data[p:p+8], byteorder='little')
            value ^= masklist[mask_pos]
            data[p:p+8] = value.to_bytes(8, byteorder='little')
            p += 8
        else:
            if p < decryptSize:
                pp = 0
                while p + pp < decryptSize:
                    data[p + pp] ^= ((0xFFFFFFFFFFFFFFFF >> pp) & 0xFF) & (masklist[mask_pos] & 0xFF)
                    pp += 1
                p = decryptSize
        mask_pos = (mask_pos + 1) % 4
    with open(path + ".dec", "wb") as f:
        f.write(data)
```