---
title: "2nd Leg Bear Trap (Failed Bear Breakout)"
slug: "/visual-patterns/failed-bo-bear-trap-guide"
meta_description: "深度解析 Al Brooks PA 中的 2nd Leg Bear Trap (Failed Bear Breakout)。完整规则、胜率数据与实战技巧。"
cluster: "视觉模式"
module_id: "M3_TRADING_RANGE"
pattern_id: "FAILED_BO_BEAR_TRAP"
direction: "long"
generated: "2026-03-05"
---

# 2nd Leg Bear Trap (Failed Bear Breakout)

> Surprisingly big BO below Wedge bottom → 2nd leg down 只有 1 bar → 反转上涨。50% pullback 处反转 = 2nd Leg Bear Trap。

---

## 什么是 2nd Leg Bear Trap (Failed Bear Breakout)？

Surprisingly big BO below Wedge bottom → 2nd leg down 只有 1 bar → 反转上涨。50% pullback 处反转 = 2nd Leg Bear Trap。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **FBRT_S1**: Surprisingly big Bear BO below Wedge bottom 或 TR 下方
2. **FBRT_S2**: 2nd leg down 只有 1 bar 或极小（力度耗尽）
3. **FBRT_S3**: 50% pullback 处出现反转 = 2nd Leg Bear Trap

### 触发条件（Entry Rules）

1. **FBRT_E1**: B above High 2 (Micro LL DB) 或 HL DB
2. **FBRT_E2**: Failed BO below HL 和 bull trend line → Bear Trap → Buy above bull bars reversing up from EMA

---

## 入场与出场逻辑

### 入场规则

- **FBRT_E1**: B above High 2 (Micro LL DB) 或 HL DB
- **FBRT_E2**: Failed BO below HL 和 bull trend line → Bear Trap → Buy above bull bars reversing up from EMA

### 止损止盈（Exit Rules）

- **FBRT_X1**: 目标回到 TR 中部或上方
- **FBRT_X2**: Stop 放在 BO 极值（2nd leg low）之外

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | ≥50% |
| 备注 | TR 中 BO 失败概率 ≥50%；Bear Trap 反转上涨概率高 |


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

**Q1: 2nd Leg Bear Trap (Failed Bear Breakout) 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: 2nd Leg Bear Trap (Failed Bear Breakout) 失败后怎么办？**

H2 失败（被止损）后应等待 H3（楔形底），H3 的概率通常更高。

**Q3: 2nd Leg Bear Trap (Failed Bear Breakout) 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 2nd Leg Bear Trap (Failed Bear Breakout) 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Brooks Encyclopedia of Chart Patterns, 625页 PDF OCR 提取*
