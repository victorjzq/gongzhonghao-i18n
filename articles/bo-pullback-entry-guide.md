---
title: "Breakout Pullback / Breakout Test 入场"
slug: "/visual-patterns/bo-pullback-entry-guide"
meta_description: "深度解析 Al Brooks PA 中的 Breakout Pullback / Breakout Test 入场。完整规则、胜率数据与实战技巧。"
cluster: "视觉模式"
module_id: "M3_TRADING_RANGE"
pattern_id: "BO_PULLBACK_ENTRY"
direction: "both"
generated: "2026-03-05"
---

# Breakout Pullback / Breakout Test 入场

> Valid BO 确认后，在回撤位（EMA、50% pullback、前一 TR 边界）出现反转信号时入场。目标 = Measured Move。

---

## 什么是 Breakout Pullback / Breakout Test 入场？

Valid BO 确认后，在回撤位（EMA、50% pullback、前一 TR 边界）出现反转信号时入场。目标 = Measured Move。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **BPE_S1**: 前提：Valid BO 已确认（连续 2+ 根大同向 bar + follow-through bar 无反向 body）
2. **BPE_S2**: 回撤到 EMA 附近
   - 参数: ema_period=20
3. **BPE_S3**: 回撤到前一推进的 50% 位置
4. **BPE_S4**: DB Breakout Test：回到前一双底突破点测试后买入

### 触发条件（Entry Rules）

1. **BPE_E1**: 出现反转信号 bar（收盘靠近有利方向极值）后入场
2. **BPE_E2**: 20-Gap Bar Buy Signal = bear trap → at DB Breakout Test 买入
3. **BPE_E3**: Strong bull bar closing near its H 上方买入（BO 失败后 scale in 加仓点）

---

## 入场与出场逻辑

### 入场规则

- **BPE_E1**: 出现反转信号 bar（收盘靠近有利方向极值）后入场
- **BPE_E2**: 20-Gap Bar Buy Signal = bear trap → at DB Breakout Test 买入
- **BPE_E3**: Strong bull bar closing near its H 上方买入（BO 失败后 scale in 加仓点）

### 止损止盈（Exit Rules）

- **BPE_X1**: 目标 = Measured Move（TR 高度向 BO 方向投影）
- **BPE_X2**: Stop 放在回撤低点/高点之外

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60% |
| 备注 | Valid BO + pullback + 确认 → 60% 概率 Measured Move |


---

## 补充规则

- **BPE_R1**: TTR 后的 BO 如果确认为趋势恢复 → 60% 概率至少小幅趋势延续
- **BPE_R2**: Late BO Test：日内 H/L 确立后，对该极值的再测试

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| [M1_MTR](./hh-mtr-top-guide.md) |related_to|60% 的 MTR 最终变成 TR|
| [M2_SPIKE_CHANNEL](./bear-channel-breakout-guide.md) |related_to|S&C 趋势 >60% 最终演变为 TR|
| [M4_MEASURED_MOVE](./mm-2nd-leg-trap-guide.md) |confirms|Valid BO + pullback → 60% 概率 Measured Move|
| [M5_SIGNAL_BAR](./bear-signal-bar-guide.md) |depends_on|BO 和 Failed BO 入场需要好的 Signal Bar|

---

## FAQ

**Q1: Breakout Pullback / Breakout Test 入场 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Breakout Pullback / Breakout Test 入场 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Breakout Pullback / Breakout Test 入场 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Breakout Pullback / Breakout Test 入场 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Brooks Encyclopedia of Chart Patterns, 625页 PDF OCR 提取*
