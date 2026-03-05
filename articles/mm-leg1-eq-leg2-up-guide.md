---
title: "Leg 1 = Leg 2 MM Up (AB=CD Up)"
slug: "/trade-management/mm-leg1-eq-leg2-up-guide"
meta_description: "深度解析 Al Brooks PA 中的 Leg 1 = Leg 2 MM Up (AB=CD Up)。完整规则、胜率数据与实战技巧。"
cluster: "交易管理"
module_id: "M4_MEASURED_MOVE"
pattern_id: "MM_LEG1_EQ_LEG2_UP"
direction: "long"
generated: "2026-03-05"
---

# Leg 1 = Leg 2 MM Up (AB=CD Up)

> 两段等距上涨：Leg1 (A→B) 完成后回调到 C，Leg2 (C→D) 长度等于 Leg1。最常用、最可靠的 MM 类型。

---

## 什么是 Leg 1 = Leg 2 MM Up (AB=CD Up)？

两段等距上涨：Leg1 (A→B) 完成后回调到 C，Leg2 (C→D) 长度等于 Leg1。最常用、最可靠的 MM 类型。

### 子类型一览

| 子类型 | 说明 | 特征 |
|--------|------|------|
| High to Low 度量 | 极值到极值度量，最常用最直观 | A=swing_low, B=swing_high |
| Close to Close 度量 | 收盘到收盘度量，更保守 | 用收盘价替代极值 |
| Body 中点度量 | 实体中点间距离，精确度量 | body_mid = (open + close) / 2 |
| BO Point to Extreme 度量 | 突破点到极值度量，适用于 Spike and Channel | 起点=突破位，终点=极值 |

---

## 识别规则图解

### 前置条件（Setup Rules）

1. **MM_UP_S1**: 识别 Leg 1：至少 3 根同方向阳线，或 1 根 Surprise Bull Bar
   - 参数: min_consecutive_bars=3
2. **MM_UP_S2**: Leg 1 起点 A = swing low，终点 B = swing high
3. **MM_UP_S3**: 回调形成 C 点：反向运动，深度 < Leg 1 的 75%（否则可能是反转）
   - 参数: max_pullback_ratio=0.75
4. **MM_UP_S4**: 回调通常形成 Bull Flag 形态
5. **MM_UP_S5**: Leg 2 开始：趋势恢复，突破回调区间，方向与 Leg 1 相同

### 触发条件（Entry Rules）

1. **MM_UP_E1**: H2 出现在 C 点附近，是最佳入场信号

---

## 入场与出场逻辑

### 入场规则

- **MM_UP_E1**: H2 出现在 C 点附近，是最佳入场信号

### 止损止盈（Exit Rules）

- **MM_UP_X1**: 止盈目标 D = C + Leg1 = C + (B - A)
- **MM_UP_X2**: 价格接近目标 (>80%) 时准备部分获利，vacuum effect 可能加速到达
- **MM_UP_X3**: 到达 MM 目标后获利或收紧止损，多头集中获利+空头进场→急速反转或 TR
- **MM_UP_X4**: 超越 MM 目标 → 下一个目标：2× Leg1 或更高级别 MM

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60-70% |
| 备注 | 机构算法大量使用 MM 作为止盈点，到达概率高 |


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

**Q1: Leg 1 = Leg 2 MM Up (AB=CD Up) 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Leg 1 = Leg 2 MM Up (AB=CD Up) 失败后怎么办？**

H2 失败（被止损）后应等待 H3（楔形底），H3 的概率通常更高。

**Q3: Leg 1 = Leg 2 MM Up (AB=CD Up) 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Leg 1 = Leg 2 MM Up (AB=CD Up) 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 10 (M), Part 1 BX MMD, Part 13 SX MMU*
