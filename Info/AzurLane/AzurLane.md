# 碧蓝航线(Azur Lane)

## 从游戏外下载游戏资产

目前只适用于国内服务器

[AzurLaneAssetBundlesDownloader](https://github.com/AXiX-official/AzurLaneAssetBundlesDownloader)

更多细节可以参考这篇Blog[碧蓝航线资源的直链下载](https://blog.axix.top/index.php/2023/12/15/14/)和项目源码。

## 关于旧版本MOD迁移到新版本

图片可以直接用UABEA重新导入，或者UnityPY写个脚本批量

mesh主要是UABEA不支持导入obj格式而UnityPY当前还不支持修改mesh。新旧版本的Unity中的mesh格式不太一样，不过也可以参考新旧版本在UABEA导出的dump文件差异稍作修改就行。可以用UABEA作者的[AssetsTools.NET](https://github.com/nesrak1/AssetsTools.NET)写一个批量处理程序来着，但是我懒。