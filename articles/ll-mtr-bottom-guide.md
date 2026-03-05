---
title: "Lower Low MTR Bottom"
slug: "/price-action-basics/ll-mtr-bottom-guide"
meta_description: "深度解析 Al Brooks PA 中的 Lower Low MTR Bottom。完整规则、胜率数据与实战技巧。"
cluster: "PA基础"
module_id: "M1_MTR"
pattern_id: "LL_MTR_BOTTOM"
direction: "long"
generated: "2026-03-05"
---

# Lower Low MTR Bottom

> 新低后反转，MTR Bottom的基础形态。镜像HH MTR Top。

---

## 什么是 Lower Low MTR Bottom？

新低后反转，MTR Bottom的基础形态。镜像HH MTR Top。

### 子类型一览

| 子类型 | 说明 | 特征 |
|--------|------|------|
| DB MTR Bottom | 两次测试相同低点后反转 | 两个低点接近相同价位 |
| HL MTR Bottom | 更高的低点，通常是LL MTR的后续确认 | 第二个低点高于第一个, often only 2-3 bars in 1st hour |
| Wedge MTR Bottom | 楔形底（3 push down） | 三次下探, 每次下探力度递减 |

---

## 识别规则图解

### 前置条件（Setup Rules）

1. **LL_BOT_S1**: Minor reversal breaks above bear trend line（第一次反弹突破熊趋势线）
2. **LL_BOT_S2**: Rally reaches EMA and has about 10 or more bars
   - 参数: min_bars=10, ema_period=20
3. **LL_BOT_S3**: Good if EMA Gap bar above（K线完全在EMA上方）
4. **LL_BOT_S4**: Selloff resumes and tests the prior low（回调测试前低）
5. **LL_BOT_S5**: Selloff has about 10 bars and is not strong（回调不强势）
   - 参数: min_selloff_bars=10

### 触发条件（Entry Rules）

1. **LL_BOT_E1**: Good buy signal bar（bull bar closing near its H）
2. **LL_BOT_E2**: B above signal bar high, stop below signal bar low
3. **LL_BOT_E3**: Big 2 bar reversal 是强信号

---

## 入场与出场逻辑

### 入场规则

- **LL_BOT_E1**: Good buy signal bar（bull bar closing near its H）
- **LL_BOT_E2**: B above signal bar high, stop below signal bar low
- **LL_BOT_E3**: Big 2 bar reversal 是强信号

### 止损止盈（Exit Rules）

- **LL_BOT_X1**: 目标：至少2 legs up，first target = top of Final Bear Flag

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 40% |
| 备注 | 40% chance of swing up |


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

**Q1: Lower Low MTR Bottom 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Lower Low MTR Bottom 失败后怎么办？**

H2 失败（被止损）后应等待 H3（楔形底），H3 的概率通常更高。

**Q3: Lower Low MTR Bottom 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Lower Low MTR Bottom 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia, Part 10 (M), Slides 148-380*
