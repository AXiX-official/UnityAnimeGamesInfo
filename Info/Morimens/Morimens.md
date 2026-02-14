# 忘却前夜(Morimens)

## Info

| | |
| - | - |
| Unity Version | 2019.4.30f1 |
| Assets Encrypted | False |
| Hotfix | XLua |
| So Protection | |

## About

在`2019.4.x`的版本中，header中的`version`字段从6升级到了7。在`version` 7中，会在header之后做align。具体的版本是在`2019.4.14`以及之前是`version` 6而`2019.4.15`以及之后是`version` 7。

因为一些暂时无法考证的原因，某些游戏（比如本游戏），虽然版本号大于`2019.4.15`但是header中的`version`仍然是6，但是在header之后做了align。