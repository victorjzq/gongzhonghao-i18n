---
title: "Bear Signal Bar（做空信号棒）"
slug: "/brooks-methodology/bear-signal-bar-guide"
meta_description: "深度解析 Al Brooks PA 中的 Bear Signal Bar（做空信号棒）。完整规则、胜率数据与实战技巧。"
cluster: "Brooks方法论"
module_id: "M5_SIGNAL_BAR"
pattern_id: "BEAR_SIGNAL_BAR"
direction: "short"
generated: "2026-03-05"
---

# Bear Signal Bar（做空信号棒）

> 阴线，收盘在 K 线下方 20% 以下位置，实体饱满(≥50%)，尾部小(<20%)。完全镜像 Bull Signal Bar。

---

## 什么是 Bear Signal Bar（做空信号棒）？

阴线，收盘在 K 线下方 20% 以下位置，实体饱满(≥50%)，尾部小(<20%)。完全镜像 Bull Signal Bar。

### 子类型一览

| 子类型 | 说明 | 特征 |
|--------|------|------|
| SB S Good | 典型好信号棒：强卖盘，做空信号 | 大实体, 收盘接近低点, 小尾部 |
| SB S Big | 大且强的卖出信号棒 | body 特大, 动能强但止损远 |
| SB S Small | 较小卖出信号棒 | body 小, 止损近但力量弱 |
| SB S HTF | 高时间框架卖出信号棒 | 在 HTF 上确认 |

---

## 识别规则图解

### 前置条件（Setup Rules）

1. **SSB_S1**: Always In 方向确认为空头
2. **SSB_S2**: 过去 15 根 K 线中 ≤1 根收盘在 EMA 上方
   - 参数: lookback_bars=15, max_ema_crosses=1, ema_period=20
3. **SSB_S3**: 不在 Tight Channel 中
4. **SSB_S4**: 不在 TR 中间 1/3

### 触发条件（Entry Rules）

1. **SSB_E1**: 阴线（Close < Open）
2. **SSB_E2**: 收盘在 K 线下方 20% 以下位置（close near its low）
3. **SSB_E3**: 实体饱满：body ≥ 50% 总高度
4. **SSB_E4**: 尾部小：上下影线 < 20% 总高度
5. **SSB_E5**: S below bear bar：信号棒低点 < 前一根阴线低点
6. **SSB_E6**: Sell Stop 入场：信号棒低点 - 1 tick

---

## 入场与出场逻辑

### 入场规则

- **SSB_E1**: 阴线（Close < Open）
- **SSB_E2**: 收盘在 K 线下方 20% 以下位置（close near its low）
- **SSB_E3**: 实体饱满：body ≥ 50% 总高度
- **SSB_E4**: 尾部小：上下影线 < 20% 总高度
- **SSB_E5**: S below bear bar：信号棒低点 < 前一根阴线低点
- **SSB_E6**: Sell Stop 入场：信号棒低点 - 1 tick

### 止损止盈（Exit Rules）

- **SSB_X1**: 止损 = signal_bar_high + 1 tick
- **SSB_X2**: R/R 必须 ≥ 2:1

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 70%+ (good SB) / <30% (weak SB) |
| 备注 | 镜像 Bull Signal Bar |


---

## 补充规则

- **SSB_R1**: 评分公式同 Bull Signal Bar 镜像：AI确认+0.25, EMA≤1穿越+0.20, 收盘20%-+0.15, Gap Bar+0.10, TR底部+0.10, Context AI+0.10, 分形确认+0.10

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| M1_MTR | confirms | MTR 入场需要好的 Signal Bar 确认 |
| M2_SPIKE_CHANNEL | related_to | Spike 后的 Channel 中 Signal Bar 质量影响入场决策 |
| M3_TRADING_RANGE | related_to | TR 边界的 Signal Bar 用于判断突破方向 |
| M4_MEASURED_MOVE | related_to | Signal Bar 入场后用 MM 计算止盈目标 |
| M6_H2_L2 | depends_on | H2/L2 本质上是特定 context 下的 Signal Bar |

---

## FAQ

**Q1: Bear Signal Bar（做空信号棒） 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Bear Signal Bar（做空信号棒） 失败后怎么办？**

L2 失败后应等待 L3（楔形顶），L3 出现时概率更高。

**Q3: Bear Signal Bar（做空信号棒） 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Bear Signal Bar（做空信号棒） 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 3 (D-F) Slides 350-385, Part 12 (Q-SL) pattern-index*
