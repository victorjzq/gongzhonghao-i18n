---
title: "Bear Breakout from Trading Range"
slug: "/visual-patterns/bear-bo-from-tr-guide"
meta_description: "深度解析 Al Brooks PA 中的 Bear Breakout from Trading Range。完整规则、胜率数据与实战技巧。"
cluster: "视觉模式"
module_id: "M3_TRADING_RANGE"
pattern_id: "BEAR_BO_FROM_TR"
direction: "short"
generated: "2026-03-05"
---

# Bear Breakout from Trading Range

> 向下突破 TR，60% 概率 Measured Move down。需要连续大阴 bar + follow-through 确认。

---

## 什么是 Bear Breakout from Trading Range？

向下突破 TR，60% 概率 Measured Move down。需要连续大阴 bar + follow-through 确认。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **BRBO_S1**: Valid Bear BO：连续大同向阴线，至少一根收盘靠近低点 = Strong BO
2. **BRBO_S2**: Follow-through bar 确认：跟随 bar 不能有 bull body

### 触发条件（Entry Rules）

1. **BRBO_E1**: Strong BO 确认后做空，至少预期小的 2nd leg down

---

## 入场与出场逻辑

### 入场规则

- **BRBO_E1**: Strong BO 确认后做空，至少预期小的 2nd leg down

### 止损止盈（Exit Rules）

- **BRBO_X1**: 目标：Measured Move = TR 高度向下投影

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60% |
| 备注 | Bear BO below TR → 60% 概率 Measured Move down |


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

**Q1: Bear Breakout from Trading Range 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Bear Breakout from Trading Range 失败后怎么办？**

L2 失败后应等待 L3（楔形顶），L3 出现时概率更高。

**Q3: Bear Breakout from Trading Range 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Bear Breakout from Trading Range 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Brooks Encyclopedia of Chart Patterns, 625页 PDF OCR 提取*
