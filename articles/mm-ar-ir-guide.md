---
title: "Measured Move Based on Actual Risk / Implied Risk"
slug: "/trade-management/mm-ar-ir-guide"
meta_description: "深度解析 Al Brooks PA 中的 Measured Move Based on Actual Risk / Implied Risk。完整规则、胜率数据与实战技巧。"
cluster: "交易管理"
module_id: "M4_MEASURED_MOVE"
pattern_id: "MM_AR_IR"
direction: "both"
generated: "2026-03-05"
---

# Measured Move Based on Actual Risk / Implied Risk

> 基于实际风险 (AR) 和隐含风险 (IR) 计算 MM 目标。AR = 入场到止损距离，IR = Spike/BO Bar/Flag 高度。

---

## 什么是 Measured Move Based on Actual Risk / Implied Risk？

基于实际风险 (AR) 和隐含风险 (IR) 计算 MM 目标。AR = 入场到止损距离，IR = Spike/BO Bar/Flag 高度。


---

## 识别规则图解



---

## 入场与出场逻辑


### 止损止盈（Exit Rules）

- **AR_X1**: 1R Target = Entry ± AR（最小目标：1倍实际风险）
- **AR_X2**: 2R Target = Entry ± 2×AR（标准目标：2倍实际风险）
- **AR_X3**: MM Target = Entry ± IR（等距目标：基于隐含风险）

---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | varies |
| 备注 | 取决于 AR 与 IR 的比值：AR < IR → 好交易；AR > IR → 谨慎 |


---

## 补充规则

- **AR_R1**: AR = |Entry Price - Stop Price|
- **AR_R2**: Spike and Channel 中：IR = Spike 的高度
- **AR_R3**: Breakout 中：IR = BO Bar 的高度
- **AR_R4**: Flag 中：IR = Flag 的高度
- **AR_R5**: 当 AR < IR 时，入场时机好，R/R 更佳；当 AR > IR 时，入场晚，可能只能 scalp
- **AR_R6**: Scalp 用 AR 的 1-2 倍；Swing 用 MM (IR) 作为目标

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

**Q1: Measured Move Based on Actual Risk / Implied Risk 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Measured Move Based on Actual Risk / Implied Risk 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Measured Move Based on Actual Risk / Implied Risk 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Measured Move Based on Actual Risk / Implied Risk 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Al Brooks Encyclopedia Part 10 (M), Part 1 BX MMD, Part 13 SX MMU*
