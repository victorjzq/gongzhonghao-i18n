---
title: "可逆向交易的例外场景（第十层）"
slug: "/cross-asset/counter-trend-exceptions-guide"
meta_description: "深度解析 Al Brooks PA 中的 可逆向交易的例外场景（第十层）。完整规则、胜率数据与实战技巧。"
cluster: "跨资产应用"
module_id: "M8_UNIFIED"
pattern_id: "COUNTER_TREND_EXCEPTIONS"
direction: "both"
generated: "2026-03-05"
---

# 可逆向交易的例外场景（第十层）

> 明确列出何时可以逆向交易、何时绝对不可以

---

## 什么是 可逆向交易的例外场景（第十层）？

明确列出何时可以逆向交易、何时绝对不可以


---

## 识别规则图解



---

## 入场与出场逻辑



---

## 概率与期望值



---

## 补充规则

- **CT_R1**: 可逆向：TR中（80%突破失败）、宽幅通道（回调够深）、趋势末期耗竭、三推楔形、MTR形态
- **CT_R2**: 绝对不逆向：紧密通道、强突破阶段

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| [M1_MTR](./hh-mtr-top-guide.md) |related_to|第五层DT/DB判断中MTR是反转条件的核心组成|
| [M2_SPIKE_CHANNEL](./bear-channel-breakout-guide.md) |related_to|第一层市场状态的Spike→Channel转换|
| [M3_TRADING_RANGE](./bear-bo-from-tr-guide.md) |related_to|第一层TR识别 + 80%突破失败规则|
| [M4_MEASURED_MOVE](./mm-2nd-leg-trap-guide.md) |confirms|第三层Leg等长规则 + Phase 4目标计算|
| [M5_SIGNAL_BAR](./bear-signal-bar-guide.md) |depends_on|第六层证据链中信号棒质量是关键环节|
| [M6_ENTRY_EXIT](./always-in-supreme-guide.md) |depends_on|入场/离场的具体执行规则|
| [M7_HIGH2](./h2-bull-flag-guide.md) |depends_on|第四层H2/L2定义的详细实现|

---

## FAQ

**Q1: 可逆向交易的例外场景（第十层） 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: 可逆向交易的例外场景（第十层） 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: 可逆向交易的例外场景（第十层） 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 可逆向交易的例外场景（第十层） 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: 公众号交易系列4篇 + Always In完整学习手册 + 概念解剖笔记*
