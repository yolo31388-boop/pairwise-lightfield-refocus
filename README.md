# pairwise-lightfield-refocus

## 领域

游戏、图形与多媒体

## 主题

光场相机重聚焦与微透镜标定

## 说明

微透镜网格标定、焦栈自适应细分、视角到达栅栏。

初始状态下 `graphics/lightfield.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
