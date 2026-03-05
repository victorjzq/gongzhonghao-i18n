---
title: "EMA20上方1根趋势棒入场"
slug: "/brooks-methodology/ema20-1bar-entry-guide"
meta_description: "深度解析 Al Brooks PA 中的 EMA20上方1根趋势棒入场。完整规则、胜率数据与实战技巧。"
cluster: "Brooks方法论"
module_id: "M6_ENTRY_EXIT"
pattern_id: "EMA20_1BAR_ENTRY"
direction: "both"
generated: "2026-03-05"
---

# EMA20上方1根趋势棒入场

> EMA20上方出现1根趋势棒时，根据AI方向和20 Gap Bar状态决定是否入场

---

## 什么是 EMA20上方1根趋势棒入场？

EMA20上方出现1根趋势棒时，根据AI方向和20 Gap Bar状态决定是否入场


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **E1_S1**: 确认当前AI方向（AI by Price Action + AI by Context）
2. **E1_S2**: 检测是否为20 Gap Bar（K线完全在EMA20一侧，表示Context层已翻转）
   - 参数: ema_period=20
3. **E1_S3**: 信号棒必须悬空（detached from EMA），不与EMA接触

### 触发条件（Entry Rules）

1. **E1_E1**: AI同向 + weak PB → 直接入场
2. **E1_E2**: AI反向 + 20 Gap Bar → 直接入场（Context翻转信号）
3. **E1_E3**: AI反向 + 非20 Gap Bar → 不入场，等MTR完成

---

## 入场与出场逻辑

### 入场规则

- **E1_E1**: AI同向 + weak PB → 直接入场
- **E1_E2**: AI反向 + 20 Gap Bar → 直接入场（Context翻转信号）
- **E1_E3**: AI反向 + 非20 Gap Bar → 不入场，等MTR完成


---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60-70% |
| 备注 | AI同向时胜率最高；20 Gap Bar入场胜率次之 |


---


## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| M1_MTR | depends_on | AI反向且无20 Gap Bar时需等MTR完成 |
| M5_SIGNAL_BAR | depends_on | 所有入场都需要合格的信号棒 |
| M7_HIGH2 | related_to | H2是核心入场设置之一 |
| M8_UNIFIED | related_to | AI方向判断的完整规则在统一手册中 |

---

## FAQ

**Q1: EMA20上方1根趋势棒入场 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: EMA20上方1根趋势棒入场 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: EMA20上方1根趋势棒入场 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 EMA20上方1根趋势棒入场 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Ali PTM 实战版入场离场规则, Always In 学习手册*
