---
title: "Breakout Above Bull Channel"
slug: "/visual-patterns/bull-channel-breakout-guide"
meta_description: "深度解析 Al Brooks PA 中的 Breakout Above Bull Channel。完整规则、胜率数据与实战技巧。"
cluster: "视觉模式"
module_id: "M2_SPIKE_CHANNEL"
pattern_id: "BULL_CHANNEL_BREAKOUT"
direction: "short"
generated: "2026-03-05"
---

# Breakout Above Bull Channel

> 向上突破 Bull Channel 的 75% 失败规则。突破通常是买入高潮，利润回吐导致失败。

---

## 什么是 Breakout Above Bull Channel？

向上突破 Bull Channel 的 75% 失败规则。突破通常是买入高潮，利润回吐导致失败。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **BCBO_S1**: 价格突破 Bull Channel 上轨线

### 触发条件（Entry Rules）

1. **BCBO_E1**: 75% 概率失败 → 不追涨，等失败后做空或获利了结
2. **BCBO_E2**: 成功的 25%：用 Measured Move 计算目标

---

## 入场与出场逻辑

### 入场规则

- **BCBO_E1**: 75% 概率失败 → 不追涨，等失败后做空或获利了结
- **BCBO_E2**: 成功的 25%：用 Measured Move 计算目标

### 止损止盈（Exit Rules）

- **BCBO_X1**: Failed BO above → 利润回吐，做空或获利

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 25% |
| 备注 | 向上突破 Bull Channel 75% 失败，仅 25% 成功延续 |


---

## 补充规则

- **BCBO_R1**: 强 BO above Wedge Channel 偶有巨大趋势，但罕见

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| [M1_MTR](./hh-mtr-top-guide.md) |related_to|Spike 后进入 Channel 可能演变为 MTR|
| [M3_TRADING_RANGE](./bear-bo-from-tr-guide.md) |related_to|S&C 趋势 >60% 最终演变为 TR|
| [M4_MEASURED_MOVE](./mm-2nd-leg-trap-guide.md) |confirms|成功的 Channel BO 用 Measured Move 计算目标|
| [M5_SIGNAL_BAR](./bear-signal-bar-guide.md) |depends_on|Channel 入场和 Wedge 反转需要好的 Signal Bar|

---

## FAQ

**Q1: Breakout Above Bull Channel 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Breakout Above Bull Channel 失败后怎么办？**

L2 失败后应等待 L3（楔形顶），L3 出现时概率更高。

**Q3: Breakout Above Bull Channel 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Breakout Above Bull Channel 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia, Spike/Channel 相关页面 (P556-P6730)*
