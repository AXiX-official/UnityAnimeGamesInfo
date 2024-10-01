from pathlib import Path
from UnityPy.enums import TextureFormat
from UnityPy.export import Texture2DConverter
from lz4.frame import decompress as dlz4frame

DBrFile = r'_DBreezeResources'
ExtPath = Path(r'extract')
ExtPath.mkdir(parents=True, exist_ok=True)

class texture2d:
    _slots = ['image_data', 'm_TextureFormat', 'm_Width', 'm_Height']
    platform = 13
    version = '2018.4.34f1'
    def __init__(self, image_data, m_TextureFormat, width, height):
        self.image_data = image_data
        self.m_TextureFormat = m_TextureFormat
        self.m_Width = width
        self.m_Height = height

def sbin(name: str, data: bytes):
    ext = ''
    if data.startswith(b'UnityFS\x00'):
        ext = '.ab'
    elif data.startswith(b'OggS'):
        ext = '.ogg'
    path = ExtPath.joinpath(f'{name}{ext}')
    if path.exists(): return
    with open(path, 'wb') as f:
        f.write(data)

def bint(data:bytes, pos:int):
    return int.from_bytes(data[pos:pos+4], byteorder='little')

def extpng(name: str, data: bytes):
    width = bint(data, 0x11D)
    height = bint(data, 0x133)
    format = bint(data, 0x160)
    img = data[0x1C1:]
    texFormat = TextureFormat(format)
    tex = texture2d(img, texFormat, width, height)
    patha, pathb = ExtPath.joinpath(name), ExtPath.joinpath(f'{name}.png')
    if patha.exists() or pathb.exists():
        return
    try:
        new_tex = Texture2DConverter.get_image_from_texture2d(tex)
        new_tex.save(pathb.as_posix())
    except:
        print('Error - ', name)
        sbin(name, data)

def extfile(name: str, data: bytes):
    if data[:4] != b'\x04\x22\x4D\x18':
        if name.startswith('utex2.'):
            extpng(name, data)
        else:
            sbin(name, data)
        return
    try: 
        decd = dlz4frame(data)
    except:
        print('Error - ', name)
        sbin(name, data)
    if not name.startswith('utex2.'):
        sbin(name, decd)
        return
    extpng(name, decd)

def DBreeze(fp: str = r'_DBreezeResources'):
    gint = lambda reader, num, endian='big': int.from_bytes(reader.read(num), byteorder=endian)
    with open(fp, 'rb') as f:
        f.seek(12)
        count = gint(f, 3)
        f.seek(64)
        for _ in range(count):
            while True:
                elen = gint(f, 2)
                if elen == 0: break
                else: f.seek(elen, 1)
            nlen = gint(f, 1) # name length
            dlen = gint(f, 4) # data length
            name = f.read(nlen).decode('utf-8')
            extfile(name, f.read(dlen))

DBreeze(DBrFile)