---
title: "差信号棒（Weak Signal Bar）"
slug: "/brooks-methodology/weak-signal-bar-guide"
meta_description: "深度解析 Al Brooks PA 中的 差信号棒（Weak Signal Bar）。完整规则、胜率数据与实战技巧。"
cluster: "Brooks方法论"
module_id: "M5_SIGNAL_BAR"
pattern_id: "WEAK_SIGNAL_BAR"
direction: "both"
generated: "2026-03-05"
---

# 差信号棒（Weak Signal Bar）

> 小实体(≤25%)、大尾部(>40%)、收盘在中间或反方向、未穿越前棒。胜率 <30%，通常不应入场。

---

## 什么是 差信号棒（Weak Signal Bar）？

小实体(≤25%)、大尾部(>40%)、收盘在中间或反方向、未穿越前棒。胜率 <30%，通常不应入场。


---

## 识别规则图解



---

## 入场与出场逻辑



---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | <30% |
| 备注 | 差信号棒胜率不到 30%，通常不应入场 |


---

## 补充规则

- **WEAK_R1**: 小实体：body ≤ 25% 总高度（近 doji），方向意愿不坚决
- **WEAK_R2**: 大尾部：上/下影线 > 40% 总高度，犹豫信号
- **WEAK_R3**: 收盘位置差：收盘在 K 线中间或反方向半部，力量不足
- **WEAK_R4**: 方向错误：牛市中出现阴线信号棒 / 熊市中出现阳线信号棒
- **WEAK_R5**: 未穿越前棒：没有超过前一根 K 线极值，缺乏突破力

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| M1_MTR | confirms | MTR 入场需要好的 Signal Bar 确认 |
| M2_SPIKE_CHANNEL | related_to | Spike 后的 Channel 中 Signal Bar 质量影响入场决策 |
| M3_TRADING_RANGE | related_to | TR 边界的 Signal Bar 用于判断突破方向 |
| M4_MEASURED_MOVE | related_to | Signal Bar 入场后用 MM 计算止盈目标 |
| M6_H2_L2 | depends_on | H2/L2 本质上是特定 context 下的 Signal Bar |

---

## FAQ

**Q1: 差信号棒（Weak Signal Bar） 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: 差信号棒（Weak Signal Bar） 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: 差信号棒（Weak Signal Bar） 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 差信号棒（Weak Signal Bar） 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 3 (D-F) Slides 350-385, Part 12 (Q-SL) pattern-index*
