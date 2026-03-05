---
title: "Breakout Below Bear Channel"
slug: "/visual-patterns/bear-channel-breakout-guide"
meta_description: "深度解析 Al Brooks PA 中的 Breakout Below Bear Channel。完整规则、胜率数据与实战技巧。"
cluster: "视觉模式"
module_id: "M2_SPIKE_CHANNEL"
pattern_id: "BEAR_CHANNEL_BREAKOUT"
direction: "long"
generated: "2026-03-05"
---

# Breakout Below Bear Channel

> 向下突破 Bear Channel 仅 25% 能持续下跌，60% 概率反转上涨。跌破通道常是卖出高潮。

---

## 什么是 Breakout Below Bear Channel？

向下突破 Bear Channel 仅 25% 能持续下跌，60% 概率反转上涨。跌破通道常是卖出高潮。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **BRBO_S1**: 价格跌破 Bear Channel 下轨线

### 触发条件（Entry Rules）

1. **BRBO_E1**: 不追空 → 60% 概率反转上涨，等反转信号做多
2. **BRBO_E2**: Exhaustive Sell Climax = 跌破通道 → 准备反转做多

---

## 入场与出场逻辑

### 入场规则

- **BRBO_E1**: 不追空 → 60% 概率反转上涨，等反转信号做多
- **BRBO_E2**: Exhaustive Sell Climax = 跌破通道 → 准备反转做多

### 止损止盈（Exit Rules）

- **BRBO_X1**: 仅 25% swing down 能持续 → 如持有空仓，做好获利准备

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 25% 继续下跌 |
| 备注 | 向下突破 Bear Channel 仅 25% 持续下跌；Failed BO below 60% 反转上涨 |


---

## 补充规则

- **BRBO_R1**: 3 Day Bear Channel → 预期 Strong Bull BO

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

**Q1: Breakout Below Bear Channel 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Breakout Below Bear Channel 失败后怎么办？**

H2 失败（被止损）后应等待 H3（楔形底），H3 的概率通常更高。

**Q3: Breakout Below Bear Channel 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Breakout Below Bear Channel 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia, Spike/Channel 相关页面 (P556-P6730)*
