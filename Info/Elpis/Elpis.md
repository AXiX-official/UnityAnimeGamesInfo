# 星落(Elpis)

## Info

| | |
| - | - |
| Unity Version | 2021.3.32f1c1 |
| Assets Encrypted | FakeHeader & [UnityCN](../UnityCN/UnityCN.md) |
| Hotfix | Xlua |
| So Protection | to be determined |

## APK内的文件

APK内主要的ab文件被首尾相连的存储在`assets\PlayerAssets\playerassets.assets`中，同目录下的`playerassets.json`记录了每个ab包的hash key和offset，可以使用这个[脚本](extract.py)来提取ab包。