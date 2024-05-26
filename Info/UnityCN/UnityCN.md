# UnityCN 加密

## 什么是UnityCN加密？

我没找到官方文档（懒）所以我会用我的理解来讲解一下。

UnityCN是一种Unity中国官方内置于中国特供版中的加密方式(虽然你会看到版本号不带c1的游戏也使用了这种加密方式)。

具体的加密方式这里略去不谈，感兴趣的可以去看看[Razmoth](https://github.com/Razmoth)佬的[CNStudio](https://github.com/Razmoth/CNStudio)了解一下具体过程。

## 怎么处理UnityCN加密的文件？

### 读取与查看

[Razmoth](https://github.com/Razmoth)佬维护的[Studio](https://github.com/RazTools/Studio)支持UnityCN加密的文件的读取与查看。

大致流程如下

- `Options` -> `Specify Game` -> `UnityCN`
- `Options` -> `Specify UnityCN Key`然后在弹出的对话框中根据游戏名字选择对应的key，如果没有找到可以尝试自己获取key填入。
- 然后就可以像正常的查看文件一样查看了。

### 修改

尝试一下就知道UABEA是无法直接读取UnityCN加密的文件的。在[UnityCN的加密与解密](https://blog.axix.top/index.php/2024/03/12/72/)中我大概讲解了一下UnityCN加密是怎么工作的，文末的repo [UnityCN-Helper](https://github.com/AXiX-official/UnityCN-Helper)支持从UnityCN加密的文件导出不加密的文件和使用原始文件对修改后的文件进行加密。

实际上，使用[UnityCN-Helper](https://github.com/AXiX-official/UnityCN-Helper)导出的不加密文件在UABEA修改后就可以直接丢回游戏了，似乎对于UnityCN加密来讲，不加密的文件也是能正常读取的。当然如果没能正常读取可以重新加密试试。

### UABEA

在这个编辑的时间点(2024/5/25)，[UABEA](https://github.com/nesrak1/UABEA)的最新Release是[seventh release](https://github.com/nesrak1/UABEA/releases/tag/v7)，作者在重写UABEA，也就是[UABEANext](https://github.com/nesrak1/UABEANext)。按作者原话是不会考虑对UnityCN Encryption的支持，因为他从来没遇到过(哈哈)，所以我fork了一个支持UnityCN Encryption的[UABEA](https://github.com/AXiX-official/UABEA)版本。

## 一些补充

根据我在网上看到的信息，UnityCN要求数据是LZ4压缩的，但是实际上会出现某些block的压缩类型为None。我询问了一些人，他们告诉我这是Unity Vanilad的处理，如果lz4压缩后的数据比原始数据大，Unity会选择不压缩。

## 本仓库涉及的UnityCN加密游戏的Key

| Game Name | Key |
|-----------|-----|
| 雷索纳斯(Resournance) | 5265736F6E616E63655265626F726E52 |
| 云图计划(国服) | 62363238363766353164326561376266 |
| 云图计划(国际服) | 31636162383436663532393031633965 |
| 战双帕弥什(Punishing Gray Raven)(CN/JP/TW) | 7935585076714C4F72436F6B57524961 |
| 战双帕弥什(Punishing Gray Raven)(GLB/KR) | 6B75726F6B75726F6B75726F6B75726F |