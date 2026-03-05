---
title: "Leg 1 = Leg 2 MM Down (AB=CD Down)"
slug: "/trade-management/mm-leg1-eq-leg2-down-guide"
meta_description: "深度解析 Al Brooks PA 中的 Leg 1 = Leg 2 MM Down (AB=CD Down)。完整规则、胜率数据与实战技巧。"
cluster: "交易管理"
module_id: "M4_MEASURED_MOVE"
pattern_id: "MM_LEG1_EQ_LEG2_DOWN"
direction: "short"
generated: "2026-03-05"
---

# Leg 1 = Leg 2 MM Down (AB=CD Down)

> 两段等距下跌：Leg1 (A→B) 完成后反弹到 C，Leg2 (C→D) 长度等于 Leg1。镜像 MM Up。

---

## 什么是 Leg 1 = Leg 2 MM Down (AB=CD Down)？

两段等距下跌：Leg1 (A→B) 完成后反弹到 C，Leg2 (C→D) 长度等于 Leg1。镜像 MM Up。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **MM_DN_S1**: 识别 Leg 1：至少 3 根同方向阴线，或 1 根 Surprise Bear Bar
   - 参数: min_consecutive_bars=3
2. **MM_DN_S2**: Leg 1 起点 A = swing high，终点 B = swing low
3. **MM_DN_S3**: 反弹形成 C 点：反向运动，深度 < Leg 1 的 75%
   - 参数: max_pullback_ratio=0.75
4. **MM_DN_S4**: 反弹通常形成 Bear Flag 形态
5. **MM_DN_S5**: Leg 2 开始：下跌恢复，跌破反弹区间

### 触发条件（Entry Rules）

1. **MM_DN_E1**: L2 出现在 C 点附近，是最佳做空入场信号

---

## 入场与出场逻辑

### 入场规则

- **MM_DN_E1**: L2 出现在 C 点附近，是最佳做空入场信号

### 止损止盈（Exit Rules）

- **MM_DN_X1**: 止盈目标 D = C - Leg1 = C - (A - B)
- **MM_DN_X2**: 价格接近目标 (>80%) 时准备部分获利

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60-70% |
| 备注 | 镜像 MM Up，机构算法同样使用 |


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

**Q1: Leg 1 = Leg 2 MM Down (AB=CD Down) 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Leg 1 = Leg 2 MM Down (AB=CD Down) 失败后怎么办？**

L2 失败后应等待 L3（楔形顶），L3 出现时概率更高。

**Q3: Leg 1 = Leg 2 MM Down (AB=CD Down) 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Leg 1 = Leg 2 MM Down (AB=CD Down) 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 10 (M), Part 1 BX MMD, Part 13 SX MMU*
