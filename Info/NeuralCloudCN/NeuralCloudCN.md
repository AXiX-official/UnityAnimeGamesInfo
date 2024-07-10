# 云图计划(Neural Cloud CN)

## Info

| | |
| - | - |
| Unity Version | 2018.4.36f1 |
| Assets Encrypted | [UnityCN](../../Info/UnityCN/UnityCN.md) |
| Hotfix | XLua(luac 5.3) |
| So Protection | tprt |

## XLua

如果你要用[unluac](https://sourceforge.net/projects/unluac/)来反编译xlua的luac文件，可以考虑使用这个[脚本](fixlua.py)修复文件头。
```shell
python fixlua.py PATH/TO/LUAC/FLOAD PATH/TO/OUTPUT/FLOAD PATH/TO/unluac.jar
```
当然你也可以直接尝试其他针对xlua的反编译工具。