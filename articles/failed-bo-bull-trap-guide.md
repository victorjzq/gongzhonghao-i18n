---
title: "2nd Leg Bull Trap (Failed Bull Breakout)"
slug: "/visual-patterns/failed-bo-bull-trap-guide"
meta_description: "深度解析 Al Brooks PA 中的 2nd Leg Bull Trap (Failed Bull Breakout)。完整规则、胜率数据与实战技巧。"
cluster: "视觉模式"
module_id: "M3_TRADING_RANGE"
pattern_id: "FAILED_BO_BULL_TRAP"
direction: "short"
generated: "2026-03-05"
---

# 2nd Leg Bull Trap (Failed Bull Breakout)

> Strong BO（2 根大阳 bar）→ 小 2nd leg up → 反转下跌。通常导致大卖出但不太可能形成强 bear trend，更可能回到 TR。

---

## 什么是 2nd Leg Bull Trap (Failed Bull Breakout)？

Strong BO（2 根大阳 bar）→ 小 2nd leg up → 反转下跌。通常导致大卖出但不太可能形成强 bear trend，更可能回到 TR。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **FBT_S1**: Strong Bull BO：至少 2 根大阳 bar 突破 TR 上方
2. **FBT_S2**: 小 2nd leg up 形成（第二段上推力度弱）
3. **FBT_S3**: Follow-through bar disappointed：大影线、反向 bar、无法收盘靠近极值

### 触发条件（Entry Rules）

1. **FBT_E1**: S below bear bar 或 S below bear bar closing near its low
2. **FBT_E2**: Micro DT 形成在 TR 上方 → 确认 Failed BO → 做空

---

## 入场与出场逻辑

### 入场规则

- **FBT_E1**: S below bear bar 或 S below bear bar closing near its low
- **FBT_E2**: Micro DT 形成在 TR 上方 → 确认 Failed BO → 做空

### 止损止盈（Exit Rules）

- **FBT_X1**: 不太可能形成强 bear trend，更可能回到 TR 中部 → 目标设在 TR 中部
- **FBT_X2**: Stop 放在 BO 极值（2nd leg high）之外

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | ≥50% |
| 备注 | TR 中任何 BO 失败概率 ≥50%；但 failed BO 做空后更可能回到 TR 而非大跌 |


---

## 补充规则

- **FBT_R1**: Late Bull Trap：BO above TR → follow-through bar 是 bear bar closing near its L → Micro DT → 反转回 TR
- **FBT_R2**: TR Day 中大阳趋势 bar 收盘在 TR 上方 = 50% 概率是 Bull Trap

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

**Q1: 2nd Leg Bull Trap (Failed Bull Breakout) 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: 2nd Leg Bull Trap (Failed Bull Breakout) 失败后怎么办？**

L2 失败后应等待 L3（楔形顶），L3 出现时概率更高。

**Q3: 2nd Leg Bull Trap (Failed Bull Breakout) 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 2nd Leg Bull Trap (Failed Bull Breakout) 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Brooks Encyclopedia of Chart Patterns, 625页 PDF OCR 提取*
