---
title: "1个高胜率L2看跌形态：精准捕捉空头趋势的做空指南"
slug: "/brooks-methodology/l2-bear-flag-guide"
meta_description: "深度解析 Al Brooks PA 中的 L2 Bear 形态。掌握做空入场、止损逻辑与胜率数据。"
cluster: "Brooks方法论"
module_id: "M7_HIGH2"
pattern_id: "L2_BEAR_FLAG"
direction: "short"
generated: "2026-03-05"
---

# Low 2 Bear Flag Sell Setup

> H2的完全镜像。熊趋势或交易区间底部中的第二次反弹卖出设置。

---

## 什么是 Low 2 Bear Flag Sell Setup？

H2的完全镜像。熊趋势或交易区间底部中的第二次反弹卖出设置。

### 子类型一览

| 子类型 | 说明 | 特征 |
|--------|------|------|
| Simple L2 | 标准两次反弹做空 | 两次反弹清晰可辨 |
| Gap Bar L2 | 信号K线开盘 < 前一根低点 | signal_bar_open < prior_bar_low |
| TR Bottom L2 | L2出现在TR底部，前面有熊趋势 | price_in_lower_third_of_TR |
| AIS L2 | Always In Short状态下的L2 | ai_short_confirmed, price_below_ema20 |
| Big L2 | 大反弹到EMA附近后大反转 | rally_to_ema_area, best_risk_reward |
| Nested L2 | 小L2嵌套在大L2内 | fractal_confirmation |
| Wedge L2 | L2在楔形反弹中 | wedge_shaped_rally |

---

## 识别规则图解

### 前置条件（Setup Rules）

1. **L2_S1**: AI方向必须为Short（Always In Short确认）
2. **L2_S2**: 趋势上下文：熊趋势中的反弹 或 TR底部
3. **L2_S3**: EMA过滤（镜像）：过去15根中收盘高于EMA的不超过1根
   - 参数: lookback=15, max_above_ema=1, ema_period=20

### 触发条件（Entry Rules）

1. **L2_E1**: 计数：数跌破前一根K线低点的次数，第二次即为L2
2. **L2_E2**: 信号K线：阴线 + 收盘接近最低点 + 低于前一根阴线
3. **L2_E3**: 入场：信号K线低点下方1 tick挂卖出止损单

---

## 入场与出场逻辑

### 入场规则

- **L2_E1**: 计数：数跌破前一根K线低点的次数，第二次即为L2
- **L2_E2**: 信号K线：阴线 + 收盘接近最低点 + 低于前一根阴线
- **L2_E3**: 入场：信号K线低点下方1 tick挂卖出止损单

### 止损止盈（Exit Rules）

- **L2_X1**: 止损：信号K线高点上方1 tick
- **L2_X2**: 目标与H2镜像：1:1, 2:1, Measured Move

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60-70% |
| 备注 | 与H2镜像，AI Short确认时概率最高 |

### 交易方式对比

| 交易方式 | 市场环境 | 预期胜率 | 建议盈亏比 |
|----------|----------|----------|-----------|
| 顺势短线 | 强空头趋势小幅反弹 | 60%-70% | 1:1 |
| 波段交易 | EMA附近深度反弹 | 40%-50% | 2:1+ |
| 逆势交易 | 牛势回调 | <30% | 不建议 |

---


## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| [M1_MTR](./hh-mtr-top-guide.md) |related_to|MTR完成后AI翻转，H2/L2方向跟随新AI|
| [M3_TRADING_RANGE](./bear-bo-from-tr-guide.md) |related_to|TR中DT=L2, DB=H2等价关系|
| [M4_MEASURED_MOVE](./mm-2nd-leg-trap-guide.md) |confirms|H2/L2目标可用Measured Move计算|
| [M5_SIGNAL_BAR](./bear-signal-bar-guide.md) |depends_on|H2/L2入场需要合格信号棒|
| [M6_ENTRY_EXIT](./always-in-supreme-guide.md) |related_to|H2是入场规则的核心设置之一|
| [M8_UNIFIED](./always-in-direction-guide.md) |related_to|H2/L2在统一手册第四层详细定义|

---

## FAQ

**Q1: Low 2 Bear Flag Sell Setup 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Low 2 Bear Flag Sell Setup 失败后怎么办？**

L2 失败后应等待 L3（楔形顶），L3 出现时概率更高。

**Q3: Low 2 Bear Flag Sell Setup 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Low 2 Bear Flag Sell Setup 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 9 + victorjia Always In 笔记*
