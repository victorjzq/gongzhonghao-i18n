---
title: "离场规则"
slug: "/brooks-methodology/exit-rules-guide"
meta_description: "深度解析 Al Brooks PA 中的 离场规则。完整规则、胜率数据与实战技巧。"
cluster: "Brooks方法论"
module_id: "M6_ENTRY_EXIT"
pattern_id: "EXIT_RULES"
direction: "both"
generated: "2026-03-05"
---

# 离场规则

> 基于反向K线信号的离场条件

---

## 什么是 离场规则？

基于反向K线信号的离场条件


---

## 识别规则图解



---

## 入场与出场逻辑


### 止损止盈（Exit Rules）

- **EX_X1**: 反向趋势棒 + Follow-Through → 下方1 tick离场 + 前高离场
- **EX_X2**: 反向DB/DT形成 → 下方1 tick离场
- **EX_X3**: 反向光头信号棒 → 下方1 tick离场
- **EX_X4**: 连续3根反向信号棒（无趋势棒） → 下方1 tick离场 + 前高离场

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | N/A |
| 备注 | 离场规则无独立胜率，与入场规则配合使用 |


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

**Q1: 离场规则 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: 离场规则 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: 离场规则 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 离场规则 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Ali PTM 实战版入场离场规则, Always In 学习手册*
