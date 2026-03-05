---
title: "Surprise Bar → Measured Move"
slug: "/trade-management/mm-surprise-bar-guide"
meta_description: "深度解析 Al Brooks PA 中的 Surprise Bar → Measured Move。完整规则、胜率数据与实战技巧。"
cluster: "交易管理"
module_id: "M4_MEASURED_MOVE"
pattern_id: "MM_SURPRISE_BAR"
direction: "both"
generated: "2026-03-05"
---

# Surprise Bar → Measured Move

> 极大的惊奇 K 线（低概率事件），60-70% 概率基于 body 出现 MM，通常还有至少 2 条以上的腿，最终目标到 Wedge Top/Bottom。

---

## 什么是 Surprise Bar → Measured Move？

极大的惊奇 K 线（低概率事件），60-70% 概率基于 body 出现 MM，通常还有至少 2 条以上的腿，最终目标到 Wedge Top/Bottom。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **SURP_S1**: 出现 Surprise Bull/Bear Bar：极大的趋势 K 线，body 显著大于平均值
   - 参数: body_multiplier=2.5, lookback=20


---

## 入场与出场逻辑


### 止损止盈（Exit Rules）

- **SURP_X1**: MM 目标基于 body：Bull → close + body; Bear → close - body

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60-70% |
| 备注 | 60-70% 概率基于 body 出现 MM，至少 2 条以上的腿 |


---

## 补充规则

- **SURP_R1**: 通常有至少 2 条以上的腿继续运动
- **SURP_R2**: 最终目标通常到 Wedge Top（多）/ Wedge Bottom（空）

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| M1_MTR | related_to | MTR 完成后目标用 Measured Move 计算 |
| M2_SPIKE_CHANNEL | related_to | Spike 中的 Measuring Gap 用于计算 MM 目标；BO Point to Extreme 度量适用于 Spike and Channel |
| M3_TRADING_RANGE | related_to | 到达 MM 目标后常出现 Trading Range |
| M5_SIGNAL_BAR | depends_on | MM 入场需要 H2/L2 Signal Bar 在 C 点附近确认 |
| M6_H2_L2 | confirms | H2 的止盈目标就是 MM；H2 出现在 C 点附近 |

---

## FAQ

**Q1: Surprise Bar → Measured Move 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Surprise Bar → Measured Move 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Surprise Bar → Measured Move 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Surprise Bar → Measured Move 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 10 (M), Part 1 BX MMD, Part 13 SX MMU*
