# 星落(Elpis)

## Info

| | |
| - | - |
| Unity Version | 2021.3.32f1c1 |
| Assets Encrypted | FakeHeader & [UnityCN](../UnityCN/UnityCN.md) |
| Hotfix | [Xlua(luac 5.4)](Info/Elpis/Elpis.md#luascripts) |
| So Protection | to be determined |

## APK内的文件

APK内主要的ab文件被首尾相连的存储在`assets\PlayerAssets\playerassets.assets`中，同目录下的`playerassets.json`记录了每个ab包的hash key和offset，可以使用这个[脚本](extract.py)来提取ab包。

## Luascripts

lua脚本在`65b7b25ae5b0db3233364259a98109bd.bundle`,`d12a1efcaf91222406270a545c6ea088.bundle`这两个ab包中，我不确定这两个hash key后续是否会变化。

luac反编译脚本在[DeLua.py](DeLua.py)中，记得同时下载同目录下的[opmap](opmap)文件。

具体细节参见[星落(Elpis）的Lua脚本解密](https://blog.axix.top/index.php/2024/07/23/189/)