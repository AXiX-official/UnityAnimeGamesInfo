## XLua

似乎XLua对lua5.3做了一些修改，导致XLua生成的luac文件的文件头与lua5.3的不同，所以需要修复文件头才能使用[unluac](https://sourceforge.net/projects/unluac/)来反编译。

但是原版的unluac只能一次处理一个文件，如果批量调用会很慢，可以试试我修改后支持对文件夹处理的版本：[unluac](https://github.com/AXiX-official/unluac)

配合修复文件头的[脚本](../../Scripts/fixLuaS.py)，可以批量处理文件夹下的所有luac文件

```shell
python fixLuaS.py input_folder output_folder <unluac_path>
```