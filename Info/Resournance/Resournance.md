# 雷索纳斯(Resournance)

## Info

| | |
| - | - |
| Unity Version | 2019.4.40f1c1 |
| Assets Encrypted | [UnityCN](../../Info/UnityCN/UnityCN.md) |
| Hotfix | XLua(luac 5.3) |
| So Protection | |

## UnityCN

首先，什么是UnityCN加密？请参看本仓库的[UnityCN](../UnityCN/UnityCN.md)页面。

## XLua

如果你要用[unluac](https://sourceforge.net/projects/unluac/)来反编译xlua的luac文件，可以考虑使用这个[脚本](../../Scripts/fixLuaS.py)修复文件头。
```shell
python fixLuaS.py PATH/TO/LUAC/FLOAD PATH/TO/OUTPUT/FLOAD PATH/TO/unluac.jar
```
当然你也可以直接尝试其他针对xlua的反编译工具。