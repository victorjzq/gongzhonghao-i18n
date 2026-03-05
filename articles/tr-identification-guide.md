---
title: "Trading Range 识别"
slug: "/visual-patterns/tr-identification-guide"
meta_description: "深度解析 Al Brooks PA 中的 Trading Range 识别。完整规则、胜率数据与实战技巧。"
cluster: "视觉模式"
module_id: "M3_TRADING_RANGE"
pattern_id: "TR_IDENTIFICATION"
direction: "both"
generated: "2026-03-05"
---

# Trading Range 识别

> 市场先大涨再大跌（或反之），双方都没控制权，价格在区间内反复震荡。TR 是磁铁，至少 50% 概率任何突破会失败。

---

## 什么是 Trading Range 识别？

市场先大涨再大跌（或反之），双方都没控制权，价格在区间内反复震荡。TR 是磁铁，至少 50% 概率任何突破会失败。


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **TRI_S1**: Big Up + Big Down = Big Confusion → TR 最可能
2. **TRI_S2**: 2nd Leg Bull/Bear Trap 出现 = 强烈 TR 信号
3. **TRI_S3**: K线大量重叠，突破频繁失败
4. **TRI_S4**: Lower Highs + Lower Lows 也可以是 TR：弱 Bear Channel 本质上是 TR
5. **TRI_S5**: Major Bear/Bull Surprise 后出现 Trap → TR Day
6. **TRI_S6**: 开盘前 9 根 bar 都有大影线、没有好的 stop entry 信号 bar → TR Day
   - 参数: check_bars=9


---

## 入场与出场逻辑



---

## 概率与期望值

| 指标 | 数值 |
|------|------|
| 预期胜率 | ≥50% BO fail |
| 备注 | TR 是磁铁，至少 50% 概率任何突破会失败并把价格拉回区间 |


---

## 补充规则

- **TRI_R1**: TR Open 通常不会变成大趋势日
- **TRI_R2**: 50+ bar 的横盘 = Strong TR，突破大概率失败

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| [M1_MTR](./hh-mtr-top-guide.md) |related_to|60% 的 MTR 最终变成 TR|
| [M2_SPIKE_CHANNEL](./bear-channel-breakout-guide.md) |related_to|S&C 趋势 >60% 最终演变为 TR|
| [M4_MEASURED_MOVE](./mm-2nd-leg-trap-guide.md) |confirms|Valid BO + pullback → 60% 概率 Measured Move|
| [M5_SIGNAL_BAR](./bear-signal-bar-guide.md) |depends_on|BO 和 Failed BO 入场需要好的 Signal Bar|

---

## FAQ

**Q1: Trading Range 识别 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Trading Range 识别 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Trading Range 识别 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Trading Range 识别 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: Brooks Encyclopedia of Chart Patterns, 625页 PDF OCR 提取*
