---
title: "Bull Breakout from Trading Range"
slug: "/visual-patterns/bull-bo-from-tr-guide"
meta_description: "深度解析 Al Brooks PA 中的 Bull Breakout from Trading Range。完整规则、胜率数据与实战技巧。"
cluster: "视觉模式"
module_id: "M3_TRADING_RANGE"
pattern_id: "BULL_BO_FROM_TR"
direction: "long"
generated: "2026-03-05"
---

# Bull Breakout from Trading Range

> 向上突破 TR，60% 概率 Measured Move up。需要连续大同向 bar + follow-through 确认。

---

## 什么是 Bull Breakout from Trading Range？

向上突破 TR，60% 概率 Measured Move up。需要连续大同向 bar + follow-through 确认。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **BUBO_S1**: Valid Bull BO：连续大同向 bar，至少一根收盘靠近极值 = Strong BO
2. **BUBO_S2**: Follow-through bar 确认：跟随 bar 不能有 bear body

### 触发条件（Entry Rules）

1. **BUBO_E1**: Strong BO 确认后买入，至少预期小的 2nd leg
2. **BUBO_E2**: Bull BO above TR + pullback + 确认 → 60% 概率 Measured Move up

---

## 入场与出场逻辑

### 入场规则

- **BUBO_E1**: Strong BO 确认后买入，至少预期小的 2nd leg
- **BUBO_E2**: Bull BO above TR + pullback + 确认 → 60% 概率 Measured Move up

### 止损止盈（Exit Rules）

- **BUBO_X1**: 目标：Measured Move = TR 高度向上投影

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60% |
| 备注 | Bull BO above TR → 60% 概率 Measured Move up |


---


## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| M1_MTR | related_to | 60% 的 MTR 最终变成 TR |
| M2_SPIKE_CHANNEL | related_to | S&C 趋势 >60% 最终演变为 TR |
| M4_MEASURED_MOVE | confirms | Valid BO + pullback → 60% 概率 Measured Move |
| M5_SIGNAL_BAR | depends_on | BO 和 Failed BO 入场需要好的 Signal Bar |

---

## FAQ

**Q1: Bull Breakout from Trading Range 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Bull Breakout from Trading Range 失败后怎么办？**

H2 失败（被止损）后应等待 H3（楔形底），H3 的概率通常更高。

**Q3: Bull Breakout from Trading Range 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Bull Breakout from Trading Range 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Brooks Encyclopedia of Chart Patterns, 625页 PDF OCR 提取*
