---
title: "Trap Detector前置过滤"
slug: "/brooks-methodology/trap-filter-guide"
meta_description: "深度解析 Al Brooks PA 中的 Trap Detector前置过滤。完整规则、胜率数据与实战技巧。"
cluster: "Brooks方法论"
module_id: "M6_ENTRY_EXIT"
pattern_id: "TRAP_FILTER"
direction: "both"
generated: "2026-03-05"
---

# Trap Detector前置过滤

> Trap Detector是入场的前置过滤层，PA和Context冲突时提高入场门槛

---

## 什么是 Trap Detector前置过滤？

Trap Detector是入场的前置过滤层，PA和Context冲突时提高入场门槛


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **TF_S1**: 检测Trap信号：PA和Context冲突
2. **TF_S2**: 检测20 Gap Bar：Context层已翻转，PA层即将跟上
   - 参数: ema_period=20

### 触发条件（Entry Rules）

1. **TF_E1**: Trap触发时不自动阻止入场，但提高入场条件门槛（如要求H2确认而非H1）
2. **TF_E2**: 检测到20 Gap Bar时，取消同方向的Trap警告

---

## 入场与出场逻辑

### 入场规则

- **TF_E1**: Trap触发时不自动阻止入场，但提高入场条件门槛（如要求H2确认而非H1）
- **TF_E2**: 检测到20 Gap Bar时，取消同方向的Trap警告


---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | N/A |
| 备注 | 过滤层，用于调整其他Pattern的入场条件 |


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

**Q1: Trap Detector前置过滤 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Trap Detector前置过滤 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Trap Detector前置过滤 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Trap Detector前置过滤 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Ali PTM 实战版入场离场规则, Always In 学习手册*
