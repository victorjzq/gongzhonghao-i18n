---
title: "信号棒悬空入场"
slug: "/brooks-methodology/detached-signal-entry-guide"
meta_description: "深度解析 Al Brooks PA 中的 信号棒悬空入场。完整规则、胜率数据与实战技巧。"
cluster: "Brooks方法论"
module_id: "M6_ENTRY_EXIT"
pattern_id: "DETACHED_SIGNAL_ENTRY"
direction: "both"
generated: "2026-03-05"
---

# 信号棒悬空入场

> 连续强趋势棒突破后，PB第一次回调的信号棒悬空入场规则

---

## 什么是 信号棒悬空入场？

连续强趋势棒突破后，PB第一次回调的信号棒悬空入场规则


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **DS_S1**: 前提：连续强趋势棒突破（Spike），价格快速脱离EMA
2. **DS_S2**: PB第一次回调中无反向趋势棒（或趋势棒后立刻出现反向趋势棒抵消）

### 触发条件（Entry Rules）

1. **DS_E1**: 回调无趋势棒或趋势棒立刻反向 → H1入场
2. **DS_E2**: 回调有趋势棒但无跟随 → 等H2/DB确认

---

## 入场与出场逻辑

### 入场规则

- **DS_E1**: 回调无趋势棒或趋势棒立刻反向 → H1入场
- **DS_E2**: 回调有趋势棒但无跟随 → 等H2/DB确认


---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 65% |
| 备注 | H1入场概率稍低但止损近，H2入场概率更高 |


---


## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| [M1_MTR](./hh-mtr-top-guide.md) |depends_on|AI反向且无20 Gap Bar时需等MTR完成|
| [M5_SIGNAL_BAR](./bear-signal-bar-guide.md) |depends_on|所有入场都需要合格的信号棒|
| [M7_HIGH2](./h2-bull-flag-guide.md) |related_to|H2是核心入场设置之一|
| [M8_UNIFIED](./always-in-direction-guide.md) |related_to|AI方向判断的完整规则在统一手册中|

---

## FAQ

**Q1: 信号棒悬空入场 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: 信号棒悬空入场 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: 信号棒悬空入场 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 信号棒悬空入场 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Ali PTM 实战版入场离场规则, Always In 学习手册*
