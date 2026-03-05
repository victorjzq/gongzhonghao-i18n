---
title: "Broad TR - Buy Low Sell High Scalp"
slug: "/visual-patterns/broad-tr-blshs-guide"
meta_description: "深度解析 Al Brooks PA 中的 Broad TR - Buy Low Sell High Scalp。完整规则、胜率数据与实战技巧。"
cluster: "视觉模式"
module_id: "M3_TRADING_RANGE"
pattern_id: "BROAD_TR_BLSHS"
direction: "both"
generated: "2026-03-05"
---

# Broad TR - Buy Low Sell High Scalp

> Broad TR 核心策略：BLSHS（Buy Low, Sell High, Scalp）。在先前低点买入、先前高点卖出，分批入场 + scalp。

---

## 什么是 Broad TR - Buy Low Sell High Scalp？

Broad TR 核心策略：BLSHS（Buy Low, Sell High, Scalp）。在先前低点买入、先前高点卖出，分批入场 + scalp。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **BTR_S1**: 确认 Broad TR 环境：价格在明确的区间内震荡，有清晰的顶部和底部

### 触发条件（Entry Rules）

1. **BTR_E1**: 在先前低点下方买入 + bear close 买入（逆向入场）
2. **BTR_E2**: 在先前高点上方卖出 + bull close 卖出
3. **BTR_E3**: TR 内出现强方向性推进时，可 buy high / sell low，用 stop order（动量入场）
4. **BTR_E4**: 上半区：卖每根大阳 bar 的收盘 + 卖先前高点上方 + 卖反转下跌
5. **BTR_E5**: 下半区：买每根大阴 bar 的收盘 + 买先前低点下方 + 买反转上涨

---

## 入场与出场逻辑

### 入场规则

- **BTR_E1**: 在先前低点下方买入 + bear close 买入（逆向入场）
- **BTR_E2**: 在先前高点上方卖出 + bull close 卖出
- **BTR_E3**: TR 内出现强方向性推进时，可 buy high / sell low，用 stop order（动量入场）
- **BTR_E4**: 上半区：卖每根大阳 bar 的收盘 + 卖先前高点上方 + 卖反转下跌
- **BTR_E5**: 下半区：买每根大阴 bar 的收盘 + 买先前低点下方 + 买反转上涨

### 止损止盈（Exit Rules）

- **BTR_X1**: 分批入场 + scalp 出场，可部分持仓做 swing trade
- **BTR_X2**: 大阳趋势 bar 收盘在 TR 上方 = 50% 概率是 Bull Trap → 卖收盘 + 卖反转

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | N/A |
| 备注 | BLSHS 策略本身无单一成功率；核心是利用 TR 的 mean-reversion 特性 |


---

## 补充规则

- **BTR_R1**: TR Day 中 expect breakouts to fail → 用限价单 betting on failed breakouts + scalp

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| [M1_MTR](./hh-mtr-top-guide.md) |related_to|60% 的 MTR 最终变成 TR|
| [M2_SPIKE_CHANNEL](./bear-channel-breakout-guide.md) |related_to|S&C 趋势 >60% 最终演变为 TR|
| [M4_MEASURED_MOVE](./mm-2nd-leg-trap-guide.md) |confirms|Valid BO + pullback → 60% 概率 Measured Move|
| [M5_SIGNAL_BAR](./bear-signal-bar-guide.md) |depends_on|BO 和 Failed BO 入场需要好的 Signal Bar|

---

## FAQ

**Q1: Broad TR - Buy Low Sell High Scalp 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Broad TR - Buy Low Sell High Scalp 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Broad TR - Buy Low Sell High Scalp 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Broad TR - Buy Low Sell High Scalp 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Brooks Encyclopedia of Chart Patterns, 625页 PDF OCR 提取*
