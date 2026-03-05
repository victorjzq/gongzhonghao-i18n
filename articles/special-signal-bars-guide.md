---
title: "特殊类型信号棒"
slug: "/brooks-methodology/special-signal-bars-guide"
meta_description: "深度解析 Al Brooks PA 中的 特殊类型信号棒。完整规则、胜率数据与实战技巧。"
cluster: "Brooks方法论"
module_id: "M5_SIGNAL_BAR"
pattern_id: "SPECIAL_SIGNAL_BARS"
direction: "both"
generated: "2026-03-05"
---

# 特殊类型信号棒

> Outside Up/Down、Strong、Weak 等特殊信号棒类型（来自 Part 12 pattern-index）。

---

## 什么是 特殊类型信号棒？

Outside Up/Down、Strong、Weak 等特殊信号棒类型（来自 Part 12 pattern-index）。


---

## 识别规则图解



---

## 入场与出场逻辑



---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | varies |
| 备注 | Outside bars 概率取决于 context；2nd signal 最可靠 |


---

## 补充规则

- **SPEC_R1**: Outside Up (SB OU)：外围上涨买入信号棒，K 线 high > 前棒 high 且 low < 前棒 low，收盘在上半部
- **SPEC_R2**: Outside Down (SB OD)：外围下跌卖出信号棒，K 线 high > 前棒 high 且 low < 前棒 low，收盘在下半部
- **SPEC_R3**: 第 2 次信号（SB B2/S2）比第 1 次更可靠；第 3 次信号（SB B3/S3 Avoid）是危险信号
- **SPEC_R4**: Bad Context：信号棒本身好但背景差 = 不应交易

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

**Q1: 特殊类型信号棒 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: 特殊类型信号棒 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: 特殊类型信号棒 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 特殊类型信号棒 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 3 (D-F) Slides 350-385, Part 12 (Q-SL) pattern-index*
