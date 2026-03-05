---
title: "市场状态识别（第一层）"
slug: "/cross-asset/market-state-guide"
meta_description: "深度解析 Al Brooks PA 中的 市场状态识别（第一层）。完整规则、胜率数据与实战技巧。"
cluster: "跨资产应用"
module_id: "M8_UNIFIED"
pattern_id: "MARKET_STATE"
direction: "both"
generated: "2026-03-05"
---

# 市场状态识别（第一层）

> 市场永远处于 Spike→Channel→Trading Range 三阶段循环之一

---

## 什么是 市场状态识别（第一层）？

市场永远处于 Spike→Channel→Trading Range 三阶段循环之一


---

## 识别规则图解



---

## 入场与出场逻辑



---

## 概率与期望值



---

## 补充规则

- **MS_R1**: Spike特征：连续多根同方向强趋势棒，K线重叠极少，价格快速脱离之前结构
- **MS_R2**: Channel特征：趋势延续但斜率变缓，回调深度30-50%
- **MS_R3**: Trading Range特征：K线大量重叠，双向交易，80%突破尝试失败
- **MS_R4**: Spike→Channel转换：出现首次30-50%深度的有意义回调
- **MS_R5**: Channel→TR转换：K线大量重叠 + 突破后立即回撤 + 不再创显著新高/低
- **MS_R6**: TR→新Spike转换：连续3根以上大实体同向K线 + 突破后快速远离边界
- **MS_R7**: 趋势死亡：Major Higher Low被跌破→牛死；Major Lower High被突破→熊死
- **MS_R8**: 20根K线规则：回调<20根→仍是趋势回调；回调≥20根→已进入TR
- **MS_R9**: 75%趋势先进入TR，25%直接反转

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

**Q1: 市场状态识别（第一层） 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: 市场状态识别（第一层） 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: 市场状态识别（第一层） 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 市场状态识别（第一层） 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: 公众号交易系列4篇 + Always In完整学习手册 + 概念解剖笔记*
