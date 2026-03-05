---
title: "Entry Bar（入场棒触发）"
slug: "/brooks-methodology/entry-bar-guide"
meta_description: "深度解析 Al Brooks PA 中的 Entry Bar（入场棒触发）。完整规则、胜率数据与实战技巧。"
cluster: "Brooks方法论"
module_id: "M5_SIGNAL_BAR"
pattern_id: "ENTRY_BAR"
direction: "both"
generated: "2026-03-05"
---

# Entry Bar（入场棒触发）

> 信号棒之后 1-2 根出现的触发 K 线，价格突破信号棒极值激活入场。三种入场模式：EMA上方1根趋势棒、悬空信号棒(H1入场)、EMA上方2根趋势棒。

---

## 什么是 Entry Bar（入场棒触发）？

信号棒之后 1-2 根出现的触发 K 线，价格突破信号棒极值激活入场。三种入场模式：EMA上方1根趋势棒、悬空信号棒(H1入场)、EMA上方2根趋势棒。


---

## 识别规则图解


### 触发条件（Entry Rules）

1. **EB_E1**: Buy Entry：价格突破信号棒高点 + 1 tick → Buy Stop 激活
2. **EB_E2**: Sell Entry：价格跌破信号棒低点 - 1 tick → Sell Stop 激活
3. **EB_E3**: EMA20 上方 1 根趋势棒 + AI 同向 + weak PB → 直接入场
4. **EB_E4**: 悬空信号棒（Detached SB）：信号棒不与 EMA 接触，趋势极强回调极浅，可在 H1 入场

---

## 入场与出场逻辑

### 入场规则

- **EB_E1**: Buy Entry：价格突破信号棒高点 + 1 tick → Buy Stop 激活
- **EB_E2**: Sell Entry：价格跌破信号棒低点 - 1 tick → Sell Stop 激活
- **EB_E3**: EMA20 上方 1 根趋势棒 + AI 同向 + weak PB → 直接入场
- **EB_E4**: 悬空信号棒（Detached SB）：信号棒不与 EMA 接触，趋势极强回调极浅，可在 H1 入场

### 止损止盈（Exit Rules）

- **EB_X1**: H2 做多：stop = signal_bar_low - 1 tick; risk = entry - stop; position_size = acceptable_loss / risk
- **EB_X2**: L2 做空：stop = signal_bar_high + 1 tick

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | varies |
| 备注 | 取决于 Signal Bar 质量和 Context |


---

## 补充规则

- **EB_R1**: 不入场的 5 种情况：(1) Score < 0.50 (2) AI 反向/紧密通道 (3) TR 中间 (4) 阻力位阻挡目标空间不足 (5) R/R < 2:1

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| [M1_MTR](./hh-mtr-top-guide.md) |confirms|MTR 入场需要好的 Signal Bar 确认|
| [M2_SPIKE_CHANNEL](./bear-channel-breakout-guide.md) |related_to|Spike 后的 Channel 中 Signal Bar 质量影响入场决策|
| [M3_TRADING_RANGE](./bear-bo-from-tr-guide.md) |related_to|TR 边界的 Signal Bar 用于判断突破方向|
| [M4_MEASURED_MOVE](./mm-2nd-leg-trap-guide.md) |related_to|Signal Bar 入场后用 MM 计算止盈目标|
| M6_H2_L2 | depends_on | H2/L2 本质上是特定 context 下的 Signal Bar |

---

## FAQ

**Q1: Entry Bar（入场棒触发） 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Entry Bar（入场棒触发） 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Entry Bar（入场棒触发） 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Entry Bar（入场棒触发） 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 3 (D-F) Slides 350-385, Part 12 (Q-SL) pattern-index*
