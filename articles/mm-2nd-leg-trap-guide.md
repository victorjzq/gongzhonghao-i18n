---
title: "Failed 2nd Leg Trap → Measuring Gap"
slug: "/trade-management/mm-2nd-leg-trap-guide"
meta_description: "深度解析 Al Brooks PA 中的 Failed 2nd Leg Trap → Measuring Gap。完整规则、胜率数据与实战技巧。"
cluster: "交易管理"
module_id: "M4_MEASURED_MOVE"
pattern_id: "MM_2ND_LEG_TRAP"
direction: "both"
generated: "2026-03-05"
---

# Failed 2nd Leg Trap → Measuring Gap

> 失败的 2nd Leg 变成 Measuring Gap，从这个 MG 可以计算 MM 目标。这是 trap → MM 的经典转换。

---

## 什么是 Failed 2nd Leg Trap → Measuring Gap？

失败的 2nd Leg 变成 Measuring Gap，从这个 MG 可以计算 MM 目标。这是 trap → MM 的经典转换。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **TRAP_S1**: 价格尝试第二次突破（2nd Leg Bear/Bull Trap）
2. **TRAP_S2**: 突破失败，失败点变成 Measuring Gap


---

## 入场与出场逻辑


### 止损止盈（Exit Rules）

- **TRAP_X1**: 从 Measuring Gap 计算 MM 目标（同 MG 公式）

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | 60%+ |
| 备注 | Trap 转 MG 后方向更明确 |


---

## 补充规则

- **TRAP_R1**: Failed H2/L2 可以变成 Measuring Gap，确认更大级别的 MM 方向

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| M1_MTR | related_to | MTR 完成后目标用 Measured Move 计算 |
| M2_SPIKE_CHANNEL | related_to | Spike 中的 Measuring Gap 用于计算 MM 目标；BO Point to Extreme 度量适用于 Spike and Channel |
| M3_TRADING_RANGE | related_to | 到达 MM 目标后常出现 Trading Range |
| M5_SIGNAL_BAR | depends_on | MM 入场需要 H2/L2 Signal Bar 在 C 点附近确认 |
| M6_H2_L2 | confirms | H2 的止盈目标就是 MM；H2 出现在 C 点附近 |

---

## FAQ

**Q1: Failed 2nd Leg Trap → Measuring Gap 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Failed 2nd Leg Trap → Measuring Gap 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Failed 2nd Leg Trap → Measuring Gap 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Failed 2nd Leg Trap → Measuring Gap 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 10 (M), Part 1 BX MMD, Part 13 SX MMU*
