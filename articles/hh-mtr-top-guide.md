---
title: "Higher High MTR Top"
slug: "/price-action-basics/hh-mtr-top-guide"
meta_description: "深度解析 Al Brooks PA 中的 Higher High MTR Top。完整规则、胜率数据与实战技巧。"
cluster: "PA基础"
module_id: "M1_MTR"
pattern_id: "HH_MTR_TOP"
direction: "short"
generated: "2026-03-05"
---

# Higher High MTR Top

> 新高后反转，最常见的MTR Top。HH MTR通常也是Head & Shoulders Top。

---

## 什么是 Higher High MTR Top？

新高后反转，最常见的MTR Top。HH MTR通常也是Head & Shoulders Top。

### 子类型一览

| 子类型 | 说明 | 特征 |
|--------|------|------|
| DT MTR Top | 两次测试相同高点后反转 | 两个高点接近相同价位 |
| LH MTR Top | 更低的高点，通常是HH MTR的后续确认 | 第二个高点低于第一个, 通常跟在HH MTR后面 |
| Wedge MTR Top | 楔形顶（3 push up），可同时是HH MTR | 三次推高, 每次推高力度递减 |

---

## 识别规则图解

### 前置条件（Setup Rules）

1. **HH_TOP_S1**: Minor reversal breaks below bull trend line（第一次回调跌破牛趋势线）
2. **HH_TOP_S2**: PB reaches EMA and has about 10 or more bars（回调到达EMA，持续10+根K线）
   - 参数: min_bars=10, ema_period=20
3. **HH_TOP_S3**: Good if EMA Gap bar（K线完全在EMA下方，强空信号）
4. **HH_TOP_S4**: Resumption of rally tests the prior high（反弹测试前高，形成DT/HH/LH）
5. **HH_TOP_S5**: Resumption up has about 10 bars and is not strong（反弹约10根K线且不强势，overlap多、doji多）
   - 参数: min_rally_bars=10, max_strength=weak

### 触发条件（Entry Rules）

1. **HH_TOP_E1**: Good sell signal bar（收盘接近最低点的空头棒）
2. **HH_TOP_E2**: S below signal bar low, stop above signal bar high
3. **HH_TOP_E3**: 2nd S signal 更可靠（第二次做空信号）

---

## 入场与出场逻辑

### 入场规则

- **HH_TOP_E1**: Good sell signal bar（收盘接近最低点的空头棒）
- **HH_TOP_E2**: S below signal bar low, stop above signal bar high
- **HH_TOP_E3**: 2nd S signal 更可靠（第二次做空信号）

### 止损止盈（Exit Rules）

- **HH_TOP_X1**: 目标：至少2 legs down，first target = bottom of Final Flag
- **HH_TOP_X2**: Usually followed by LH MTR and 2nd leg down（2nd leg通常更大）

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 40% |
| 备注 | 40% chance of swing down（60%变成minor reversal进入TR） |


---


## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| M2_SPIKE_CHANNEL | related_to | Spike后进入Channel可能演变为MTR |
| M3_TRADING_RANGE | related_to | 60%的MTR最终变成TR |
| M4_MEASURED_MOVE | confirms | MTR完成后目标用Measured Move计算 |
| M5_SIGNAL_BAR | depends_on | MTR入场需要好的Signal Bar |

---

## FAQ

**Q1: Higher High MTR Top 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Higher High MTR Top 失败后怎么办？**

L2 失败后应等待 L3（楔形顶），L3 出现时概率更高。

**Q3: Higher High MTR Top 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Higher High MTR Top 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia, Part 10 (M), Slides 148-380*
