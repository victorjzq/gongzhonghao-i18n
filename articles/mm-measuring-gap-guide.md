---
title: "Measuring Gap → Measured Move"
slug: "/trade-management/mm-measuring-gap-guide"
meta_description: "深度解析 Al Brooks PA 中的 Measuring Gap → Measured Move。完整规则、胜率数据与实战技巧。"
cluster: "交易管理"
module_id: "M4_MEASURED_MOVE"
pattern_id: "MM_MEASURING_GAP"
direction: "both"
generated: "2026-03-05"
---

# Measuring Gap → Measured Move

> 趋势 Spike 中两根 K 线实体之间的缺口，该缺口是整段运动的大约中点。从缺口可以计算 MM 目标。

---

## 什么是 Measuring Gap → Measured Move？

趋势 Spike 中两根 K 线实体之间的缺口，该缺口是整段运动的大约中点。从缺口可以计算 MM 目标。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **MG_S1**: 必须在强趋势（Spike / Breakout）中出现
2. **MG_S2**: 缺口 = 前一根K线的 close 与后一根K线的 open 之间没有重叠（也可是 body gap）
3. **MG_S3**: Measuring Gap 通常不会被回补（如果被回补，说明趋势可能结束）
4. **MG_S4**: 多个 Measuring Gap 可以出现在同一段趋势中，每个都给出一个 MM 目标


---

## 入场与出场逻辑


### 止损止盈（Exit Rules）

- **MG_X1**: 多头 MM Up：Target = 2 × Gap_midpoint - Swing_Low
- **MG_X2**: 空头 MM Down：Target = 2 × Gap_midpoint - Swing_High

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60-70% |
| 备注 | Measuring Gap 是整段运动的中点，止盈目标是 gap_midpoint 到起点距离的翻倍 |


---

## 补充规则

- **MG_R1**: BO Test 成功（没有跌破/突破）确认了 Measuring Gap
- **MG_R2**: End of Day bear trap 在牛趋势中 → BO Test → 确认 MG → 达到 MMU

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| [M1_MTR](./hh-mtr-top-guide.md) |related_to|MTR 完成后目标用 Measured Move 计算|
| [M2_SPIKE_CHANNEL](./bear-channel-breakout-guide.md) |related_to|Spike 中的 Measuring Gap 用于计算 MM 目标；BO Point to Extreme 度量适用于 Spike and Channel|
| [M3_TRADING_RANGE](./bear-bo-from-tr-guide.md) |related_to|到达 MM 目标后常出现 Trading Range|
| [M5_SIGNAL_BAR](./bear-signal-bar-guide.md) |depends_on|MM 入场需要 H2/L2 Signal Bar 在 C 点附近确认|
| M6_H2_L2 | confirms | H2 的止盈目标就是 MM；H2 出现在 C 点附近 |

---

## FAQ

**Q1: Measuring Gap → Measured Move 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Measuring Gap → Measured Move 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Measuring Gap → Measured Move 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Measuring Gap → Measured Move 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 10 (M), Part 1 BX MMD, Part 13 SX MMU*
