---
title: "Broad Channel"
slug: "/visual-patterns/broad-channel-guide"
meta_description: "深度解析 Al Brooks PA 中的 Broad Channel。完整规则、胜率数据与实战技巧。"
cluster: "视觉模式"
module_id: "M2_SPIKE_CHANNEL"
pattern_id: "BROAD_CHANNEL"
direction: "both"
generated: "2026-03-05"
---

# Broad Channel

> 回调深、腿与腿之间大量重叠的宽幅通道，接近 Trading Range。可双向交易。

---

## 什么是 Broad Channel？

回调深、腿与腿之间大量重叠的宽幅通道，接近 Trading Range。可双向交易。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **BC_S1**: Broad Channel 识别：回调深（>50% of prior leg），腿间大量重叠
   - 参数: min_pullback_pct=0.5

### 触发条件（Entry Rules）

1. **BC_E1**: 可双向交易：牛腿中可以 Always In Long
2. **BC_E2**: 弱 Bear Channel 可能是 Bull Reversal Day → 准备做多

---

## 入场与出场逻辑

### 入场规则

- **BC_E1**: 可双向交易：牛腿中可以 Always In Long
- **BC_E2**: 弱 Bear Channel 可能是 Bull Reversal Day → 准备做多

### 止损止盈（Exit Rules）

- **BC_X1**: 大部分 Broad Bear Channel 底部做多会失败
- **BC_X2**: 强反弹后通常回调到新低 → 不要在反弹中持多仓太久

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | N/A |
| 备注 | Broad Channel 本质接近 TR，双向交易，无单一方向成功率 |


---

## 补充规则

- **BC_R1**: 弱 Broad Bear Channel 收盘接近开盘 = TR Day

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

**Q1: Broad Channel 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Broad Channel 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Broad Channel 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Broad Channel 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia, Spike/Channel 相关页面 (P556-P6730)*
