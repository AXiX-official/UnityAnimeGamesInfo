## XLua

似乎XLua对lua5.3做了一些修改，导致XLua生成的luac文件的文件头与lua5.3的不同，所以需要修复文件头才能使用[unluac](https://sourceforge.net/projects/unluac/)来反编译。

但是原版的unluac只能一次处理一个文件，如果批量调用会很慢，可以试试我修改后支持对文件夹处理的版本：[unluac](https://github.com/AXiX-official/unluac)

配合修复文件头的[脚本](../../Scripts/fixLuaS.py)，可以批量处理文件夹下的所有luac文件

```shell
python fixLuaS.py input_folder output_folder <unluac_path>
```

反编译出来的文件中的中文字符往往是形如`\228\189\160\229\165\189`，可以使用这个脚本来转换为正常的中文字符：[fixLuazh.py](../../Scripts/fixLuazh.py)

```shell
python fixLuazh.py input_file <output_file>
```

## 参考

- [某游戏 xLua 逆向笔记](https://blog.berd.moe/archives/xlua-reverse-note/)
- [XLua源码](https://github.com/Tencent/xLua)
