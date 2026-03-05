---
title: "Follow-Through Bar（跟随棒验证）"
slug: "/brooks-methodology/follow-through-guide"
meta_description: "深度解析 Al Brooks PA 中的 Follow-Through Bar（跟随棒验证）。完整规则、胜率数据与实战技巧。"
cluster: "Brooks方法论"
module_id: "M5_SIGNAL_BAR"
pattern_id: "FOLLOW_THROUGH"
direction: "both"
generated: "2026-03-05"
---

# Follow-Through Bar（跟随棒验证）

> 入场棒之后的判决 K 线。跟随棒是仓位扩张与否的唯一硬确认。哪怕 1 tick 的反向 body 就降低概率。

---

## 什么是 Follow-Through Bar（跟随棒验证）？

入场棒之后的判决 K 线。跟随棒是仓位扩张与否的唯一硬确认。哪怕 1 tick 的反向 body 就降低概率。


---

## 识别规则图解



---

## 入场与出场逻辑


### 止损止盈（Exit Rules）

- **FT_X1**: 反向趋势棒 + Follow-Through → 信号棒下方 1 tick 离场
- **FT_X2**: 反向 DB/DT 形成 → 下方 1 tick 离场
- **FT_X3**: 反向光头信号棒 → 下方 1 tick 离场
- **FT_X4**: 连续 3 根反向信号棒（无趋势棒）→ 前高离场

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | varies |
| 备注 | 强同向 FT 大幅提升成功率；1 tick 反向 body 即降级为 minor |


---

## 补充规则

- **FT_R1**: 好跟随棒：与信号棒同向、大实体非 doji、收盘在上半部(多)/下半部(空)、无反向 body、不形成反向吞没
- **FT_R2**: 1 tick 反向 body 就足以让运动被判定为 minor（Slide 350 原文）
- **FT_R3**: 跟随棒决策表：强同向FT→持有/加仓全仓；中等FT→持有不加仓；弱FT→减仓50%收紧止损；无FT/反向→减仓/退出看下一根；反向吞没→止损清仓

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| [M1_MTR](./hh-mtr-top-guide.md) |confirms|MTR 入场需要好的 Signal Bar 确认|
| [M2_SPIKE_CHANNEL](./bear-channel-breakout-guide.md) |related_to|Spike 后的 Channel 中 Signal Bar 质量影响入场决策|
| [M3_TRADING_RANGE](./bear-bo-from-tr-guide.md) |related_to|TR 边界的 Signal Bar 用于判断突破方向|
| [M4_MEASURED_MOVE](./mm-2nd-leg-trap-guide.md) |related_to|Signal Bar 入场后用 MM 计算止盈目标|
| M6_H2_L2 | depends_on | H2/L2 本质上是特定 context 下的 Signal Bar |

---

## FAQ

**Q1: Follow-Through Bar（跟随棒验证） 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Follow-Through Bar（跟随棒验证） 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Follow-Through Bar（跟随棒验证） 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Follow-Through Bar（跟随棒验证） 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 3 (D-F) Slides 350-385, Part 12 (Q-SL) pattern-index*
