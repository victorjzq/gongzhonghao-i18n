---
title: "Sell Climax → Measured Move Up"
slug: "/trade-management/mm-sell-climax-up-guide"
meta_description: "深度解析 Al Brooks PA 中的 Sell Climax → Measured Move Up。完整规则、胜率数据与实战技巧。"
cluster: "交易管理"
module_id: "M4_MEASURED_MOVE"
pattern_id: "MM_SELL_CLIMAX_UP"
direction: "long"
generated: "2026-03-05"
---

# Sell Climax → Measured Move Up

> Sell Climax 后预期出现 Measured Move Up，度量基础 = Sell Climax 那段下跌的高度。

---

## 什么是 Sell Climax → Measured Move Up？

Sell Climax 后预期出现 Measured Move Up，度量基础 = Sell Climax 那段下跌的高度。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **SX_S1**: 出现 Sell Climax：一根或多根大阴线，收盘远离 EMA，通常在下跌末期


---

## 入场与出场逻辑


### 止损止盈（Exit Rules）

- **SX_X1**: 保守目标：SX_low + SX_bar_body
- **SX_X2**: 激进目标：SX_low + SX_range

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60-70% |
| 备注 | 镜像 BX→MMD |


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

**Q1: Sell Climax → Measured Move Up 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Sell Climax → Measured Move Up 失败后怎么办？**

H2 失败（被止损）后应等待 H3（楔形底），H3 的概率通常更高。

**Q3: Sell Climax → Measured Move Up 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Sell Climax → Measured Move Up 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 10 (M), Part 1 BX MMD, Part 13 SX MMU*
