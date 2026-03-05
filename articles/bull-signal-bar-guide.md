---
title: "Bull Signal Bar（做多信号棒）"
slug: "/brooks-methodology/bull-signal-bar-guide"
meta_description: "深度解析 Al Brooks PA 中的 Bull Signal Bar（做多信号棒）。完整规则、胜率数据与实战技巧。"
cluster: "Brooks方法论"
module_id: "M5_SIGNAL_BAR"
pattern_id: "BULL_SIGNAL_BAR"
direction: "long"
generated: "2026-03-05"
---

# Bull Signal Bar（做多信号棒）

> 阳线，收盘在 K 线上半部 80%+ 位置，实体饱满(≥50%)，尾部小(<20%)。核心公式：有效交易 = Context × Signal 质量 × Entry 触发 × Follow-Through 确认。

---

## 什么是 Bull Signal Bar（做多信号棒）？

阳线，收盘在 K 线上半部 80%+ 位置，实体饱满(≥50%)，尾部小(<20%)。核心公式：有效交易 = Context × Signal 质量 × Entry 触发 × Follow-Through 确认。

### 子类型一览

| 子类型 | 说明 | 特征 |
|--------|------|------|
| SB B Good | 典型好信号棒：强买盘，做多信号 | 大实体, 收盘接近高点, 小尾部 |
| SB B Big | 大且强的买入信号棒，强劲上涨动能 | body 特大, 动能强但止损远 |
| SB B Small | 较小信号棒，买盘力量弱 | body 小, 止损近但力量弱 |
| SB B HTF | 高时间框架买入信号棒，预示更长周期上涨 | 在 HTF 上确认 |

---

## 识别规则图解

### 前置条件（Setup Rules）

1. **BSB_S1**: Always In 方向确认为多头
2. **BSB_S2**: 过去 15 根 K 线中 ≤1 根收盘在 EMA 下方
   - 参数: lookback_bars=15, max_ema_crosses=1, ema_period=20
3. **BSB_S3**: 不在 Tight Channel 中（Tight Channel 中再好的信号棒也是坏背景）
4. **BSB_S4**: 不在 TR 中间 1/3（50/50 概率，无优势）

### 触发条件（Entry Rules）

1. **BSB_E1**: 阳线（Close > Open）
2. **BSB_E2**: 收盘在 K 线上方 80%+ 位置（close near its high）
3. **BSB_E3**: 实体饱满：body ≥ 50% 总高度
4. **BSB_E4**: 尾部小：上下影线 < 20% 总高度
5. **BSB_E5**: B above bull bar：信号棒高点 > 前一根阳线高点
6. **BSB_E6**: Buy Stop 入场：信号棒高点 + 1 tick

---

## 入场与出场逻辑

### 入场规则

- **BSB_E1**: 阳线（Close > Open）
- **BSB_E2**: 收盘在 K 线上方 80%+ 位置（close near its high）
- **BSB_E3**: 实体饱满：body ≥ 50% 总高度
- **BSB_E4**: 尾部小：上下影线 < 20% 总高度
- **BSB_E5**: B above bull bar：信号棒高点 > 前一根阳线高点
- **BSB_E6**: Buy Stop 入场：信号棒高点 + 1 tick

### 止损止盈（Exit Rules）

- **BSB_X1**: 止损 = signal_bar_low - 1 tick
- **BSB_X2**: R/R 必须 ≥ 2:1，否则不入场

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 70%+ (good SB) / <30% (weak SB) |
| 备注 | 好信号棒 70%+ 胜率；差信号棒 <30% 胜率 |


---

## 补充规则

- **BSB_R1**: 信号棒质量评分公式：AI确认+0.25, EMA≤1穿越+0.20, 收盘80%++0.15, Gap Bar+0.10, TR顶部+0.10, Context AI+0.10, 分形确认+0.10。≥0.50可发信号，≥0.70高置信度。

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

**Q1: Bull Signal Bar（做多信号棒） 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Bull Signal Bar（做多信号棒） 失败后怎么办？**

H2 失败（被止损）后应等待 H3（楔形底），H3 的概率通常更高。

**Q3: Bull Signal Bar（做多信号棒） 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Bull Signal Bar（做多信号棒） 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 3 (D-F) Slides 350-385, Part 12 (Q-SL) pattern-index*
