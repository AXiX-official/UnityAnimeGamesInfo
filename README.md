# UnityAnimeGamesInfo

A repo collecting information about anime games made with Unity.

## Games

| Name | Unity Version | Assets Encryption Method | Hotfix | so protect |
|------|---------------|--------------------------|---------|------------|
| [碧蓝航线(Azur Lane)](Info/AzurLane/AzurLane.md) | 2020.3.48f1 | | toLua | |
| [PotK -Alternative Imitation-](Info/AlternativeImitation/AlternativeImitation.md) | 2019.4.35f1 | | | | |
| [百分之一](Info/OnePercent/OnePercent.md) | 2019.4.40f1c1 | no encryption but use DB store assets | | |
| [交错战线(CrossCore)](Info/CrossCore/CrossCore.md) | 2019.4.40f1 | [FakeHeader](Info/CrossCore/CrossCore.md#fakeheader) | [XLua](Info/CrossCore/CrossCore.md#luascripts) | |
| [苍雾残响](Info/cwcx/cwcx.md) | 2020.3.7f1 | | XLua | |
| [绯染天空(Heaven Burns Red)](Info/HeavenBurnsRed/HeavenBurnsRed.md) | 2020.3.15f2 | CRC校验 | XLua | tprt(国服) |
| [雷索纳斯(Resournance)](Info/Resournance/Resournance.md) | 2019.4.40f1c1 | [UnityCN](Info/UnityCN/UnityCN.md) | [XLua(luac 5.3)](Info/Xlua/LuaS.md) | |
| [MementoMori: AFKRPG](Info/MementoMori/MementoMori.md) | 2021.3.10f1 | | | | |
| [闻姬起舞(How To Raise A Harem)](Info/HTRAH/HTRAH.md) | 2021.3.31f1 | | XLua | |
| [云图计划(Neural Cloud CN)](Info/NeuralCloudCN/NeuralCloudCN.md) | 2021.3.30f1c1 | FakeHeader | [XLua(luac 5.3)](Info/Xlua/LuaS.md)	 | tprt | |
| [忘却前夜(Morimens)](Info/Morimens/Morimens.md) | 2019.4.30f1 | | XLua | |
| [环行旅舍(Kleins)](Info/Kleins/Kleins.md) | 2020.3.47f1 | FakeHeader | toLua | |
| [战双帕弥什(Punishing Gray Raven CN)](Info/PGRCN/PGRCN.md) | 2018.4.30f1 | [UnityCN](Info/UnityCN/UnityCN.md) | XLua | tprt(安卓) | |
| [萬源聖魔錄(Orisries)](Info/Orisries/Orisries.md) | 2022.3.32f1 | AES&抹去版本 | | |
| [吟游战记](Info/yyzj/yyzj.md) | 2022.3.6f1 | FakeHeader | toLua | | |
| [超次元女神](Info/ccyns/ccyns.md) | 2021.3.5f1 | 抹去版本 | XLua(luac 5.4) | | |
| [锚点降临(Anchor Panic)](Info/AnchorPanic/AnchorPanic.md) | 2021.3.31f1 | FakeHeader | [XLua(lua 5.1)](Info/AnchorPanic/AnchorPanic.md#luascripts) | |
| [神隐之子](Info/syzz/syzz.md) | 2021.3.35f1 | FakeHeader | toLua(LuaJIT 2.1.0-beta3) | |
| [行界](Info/xj/xj.md) | 2019.4.30f1 | | [toLua(luac 5.3)](Info/Xlua/LuaS.md) | |
| [艾塔纪元(E.T.E CHRONICLE)](Info/ete/ete.md) | 2019.4.36f1 | FakeHeader | Xlua | |
| [异尘：达米拉](Info/ycdml/ycdml.md) | 2019.4.38f1c1 | | Xlua | |
| [星落(Elpis)](Info/Elpis/Elpis.md) | 2021.3.32f1c1 | FakeHeader & [UnityCN](Info/UnityCN/UnityCN.md) | [Xlua(luac 5.4)](Info/Elpis/Elpis.md#luascripts) | to be determined |
| [拂晓](Info/fx/fx.md) | 2021.3.5f1 | FakeHeader | to be determined | |
| [BanG Dream!](Info/bangdream/bangdream.md) | 2021.3.36f1c1 | 抹去版本 | to be determined | |
| [异色边缘](Info/ysby/ysby.md) | 2021.3.32f1c1 | | HybridCLR | |
| [少女前线2:追放](Info/GF2/GF2.md) | 2019.4.40f1 | [more](Info/GF2/GF2.md#ab文件加密解密) | HybridCLR&Xlua | |
| [终焉誓约](Info/zysy/zysy.md) | 2020.3.47f1 | FakeHeader | toLua | |
| [命运圣契(Acmeis)](Info/Acmeis/Acmeis.md) | 2022.3.2t13 | FakeHeader | HybridCLR&Xlua(LuaJIT 2.1.0-beta3) | |
| [异界事务所(CounterSide)](Info/CounterSide/CounterSide.md) | 2020.3.40f1 | [more](Info/CounterSide/CounterSide.md#assets-encryption) | lua5.4 | |
| [物华弥新](Info/wuhua/wuhua.md) | 2018.4.36f1 | [more](Info/wuhua/wuhua.md#ab包解密加密) | HybridCLR&Xlua | |

备注：
- Assets Encrypted只表示脚本以外的资产加密情况，并不是上表中的每一个游戏我都研究过lua脚本的情况。

<table>
  <tr>
    <td><a href="Info/AzurLane/AzurLane.md"><img src="Icons/azurlane.webp" alt="Azur Lane" width="100%"/></td>
    <td><a href="Info/AlternativeImitation/AlternativeImitation.md"><img src="Icons/AlternativeImitation.webp" alt="Alternative Imitation" width="100%"/></td>
    <td><a href="Info/OnePercent/OnePercent.md"><img src="Icons/OnePercent.webp" alt="One Percent" width="100%"/></td>
    <td><a href="Info/CrossCore/CrossCore.m"><img src="Icons/crosscore.webp" alt="CrossCore" width="100%"/></td>
    <td><a href="Info/cwcx/cwcx.md"><img src="Icons/cwcx.webp" alt="cwcx" width="100%"/></td>
    <td><a href="Info/HeavenBurnsRed/HeavenBurnsRed.md"><img src="Icons/hbr.webp" alt="Heaven Burns Red" width="100%"/></td>
  </tr>
  <tr>
    <td><a href="Info/Resournance/Resournance.md"><img src="Icons/resonance.webp" alt="Resonance" width="100%"/></td>
    <td><a href="Info/MementoMori/MementoMori.md"><img src="Icons/MementoMori.webp" alt="MementoMori" width="100%"/></td>
    <td><a href="Info/HTRAH/HTRAH.md"><img src="Icons/HTRAH.webp" alt="How To Raise A Harem" width="100%"/></td>
    <td><a href="Info/NeuralCloudCN/NeuralCloudCN.md"><img src="Icons/NeuralCloud.webp" alt="Neural Cloud" width="100%"/></td>
    <td><a href="Info/Morimens/Morimens.md"><img src="Icons/Morimens.webp" alt="Morimens" width="100%"/></td>
    <td><a href="Info/Kleins/Kleins.md"><img src="Icons/kleins.webp" alt="Kleins" width="100%"/></td>
  </tr>
  <tr>
    <td><a href="Info/PGRCN/PGRCN.md"><img src="Icons/pgr.webp" alt="Punishing Gray Raven" width="100%"/></td>
    <td><a href="Info/Orisries/Orisries.md"><img src="Icons/Orisries.webp" alt="Orisries" width="100%"/></td>
    <td><a href="Info/yyzj/yyzj.md"><img src="Icons/yyzj.webp" alt="yyzj" width="100%"/></td>
    <td><a href="Info/ccyns/ccyns.md"><img src="Icons/ccyns.webp" alt="ccyns" width="100%"/></td>
    <td><a href="Info/AnchorPanic/AnchorPanic.md"><img src="Icons/AnchorPanic.webp" alt="Anchor Panic" width="100%"/></td>
    <td><a href="Info/syzz/syzz.md"><img src="Icons/syzz.webp" alt="syzz" width="100%"/></td>
  </tr>
  <tr>
    <td><a href="Info/xj/xj.md"><img src="Icons/xj.webp" alt="xj" width="100%"/></td>
    <td><a href="Info/ete/ete.md"><img src="Icons/ete.webp" alt="ete" width="100%"/></td>
    <td><a href="Info/ycdml/ycdml.md"><img src="Icons/ycdml.webp" alt="ycdml" width="100%"/></td>
    <td><a href="Info/Elpis/Elpisd.md"><img src="Icons/Elpis.webp" alt="Elpis" width="100%"/></td>
    <td><a href="Info/fx/fx.md"><img src="Icons/fx.webp" alt="fx" width="100%"/></td>
    <td><a href="Info/bangdream/bangdream.md"><img src="Icons/bangdream.webp" alt="BanG Dream!" width="100%"/></td>
  </tr>
  <tr>
    <td><a href="Info/ysby/ysby.md"><img src="Icons/ysby.webp" alt="异色边缘" width="100%"/></td>
    <td><a href="Info/GF2/GF2.md"><img src="Icons/GF2.webp" alt="少女前线2:追放" width="100%"/></td>
    <td><a href="Info/zysy/zysy.md"><img src="Icons/zysy.webp" alt="终焉誓约" width="100%"/></td>
    <td><a href="Info/Acmeis/Acmeis.md"><img src="Icons/Acmeis.webp" alt="命运圣契" width="100%"/></td>
    <td><a href="Info/CounterSide/CounterSide.md"><img src="Icons/CounterSide.webp" alt="异界事务所" width="100%"/></td>
    <td><a href="Info/wuhua/wuhua.md"><img src="Icons/wuhua.webp" alt="物华弥新" width="100%"/></td>
  </tr>
</table>