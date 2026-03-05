---
title: "Tight Trading Range 交易"
slug: "/visual-patterns/ttr-trading-guide"
meta_description: "深度解析 Al Brooks PA 中的 Tight Trading Range 交易。完整规则、胜率数据与实战技巧。"
cluster: "视觉模式"
module_id: "M3_TRADING_RANGE"
pattern_id: "TTR_TRADING"
direction: "both"
generated: "2026-03-05"
---

# Tight Trading Range 交易

> 极窄区间的连续重叠 K 线。最优策略是观望。如果交易，必须用限价单、fade 突破、分批建仓 + scalp。

---

## 什么是 Tight Trading Range 交易？

极窄区间的连续重叠 K 线。最优策略是观望。如果交易，必须用限价单、fade 突破、分批建仓 + scalp。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **TTR_S1**: Tight Trading Range 识别：连续多根 bar 在极小区间内重叠
2. **TTR_S2**: 趋势中的 TTR 约持续 20 根 bar（小回调牛市趋势中常见的暂停形态）
   - 参数: typical_duration=20
3. **TTR_S3**: TTR = 高时间框架的旗形，60% 概率趋势恢复
4. **TTR_S4**: 连环失败突破 = TTR：failed bull BO → failed bear BO → failed bull BO → Tight TR

### 触发条件（Entry Rules）

1. **TTR_E1**: 最好不交易 TTR
2. **TTR_E2**: 必须用限价单，绝对不用 stop order
3. **TTR_E3**: Fade 每一次突破：即使 strong trend bar 的突破也 fade，等下一根 bar 反转
4. **TTR_E4**: 大阳线卖、大阴线买：在先前高点附近卖大阳收盘；在先前低点附近买大阴收盘

---

## 入场与出场逻辑

### 入场规则

- **TTR_E1**: 最好不交易 TTR
- **TTR_E2**: 必须用限价单，绝对不用 stop order
- **TTR_E3**: Fade 每一次突破：即使 strong trend bar 的突破也 fade，等下一根 bar 反转
- **TTR_E4**: 大阳线卖、大阴线买：在先前高点附近卖大阳收盘；在先前低点附近买大阴收盘

### 止损止盈（Exit Rules）

- **TTR_X1**: Scale in + Scalp：分批建仓 + 只做 scalp

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60% 趋势恢复 |
| 备注 | TTR 作为高TF旗形，60% 概率趋势恢复；但 TTR 内部交易胜率低 |


---


## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| M1_MTR | related_to | 60% 的 MTR 最终变成 TR |
| M2_SPIKE_CHANNEL | related_to | S&C 趋势 >60% 最终演变为 TR |
| M4_MEASURED_MOVE | confirms | Valid BO + pullback → 60% 概率 Measured Move |
| M5_SIGNAL_BAR | depends_on | BO 和 Failed BO 入场需要好的 Signal Bar |

---

## FAQ

**Q1: Tight Trading Range 交易 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Tight Trading Range 交易 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Tight Trading Range 交易 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Tight Trading Range 交易 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Brooks Encyclopedia of Chart Patterns, 625页 PDF OCR 提取*
