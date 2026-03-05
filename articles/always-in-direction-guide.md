---
title: "Always In方向判断（第二层）"
slug: "/cross-asset/always-in-direction-guide"
meta_description: "深度解析 Al Brooks PA 中的 Always In方向判断（第二层）。完整规则、胜率数据与实战技巧。"
cluster: "跨资产应用"
module_id: "M8_UNIFIED"
pattern_id: "ALWAYS_IN_DIRECTION"
direction: "both"
generated: "2026-03-05"
---

# Always In方向判断（第二层）

> 双层AI框架：AI by Price Action（即时K线）+ AI by Context（EMA/结构），冲突时Context优先

---

## 什么是 Always In方向判断（第二层）？

双层AI框架：AI by Price Action（即时K线）+ AI by Context（EMA/结构），冲突时Context优先


---

## 识别规则图解

### 前置条件（Setup Rules）

1. **AI_S1**: AI by PA Long：连续3-5根阳线收盘在90%位置，或单根惊奇阳线超过20-30根最高点，或突破Major Lower High
   - 参数: consecutive_bars=3, close_position_threshold=0.9, lookback=20
2. **AI_S2**: AI by PA Short：连续3-5根阴线收盘在10%位置，或单根惊奇阴线低于20-30根最低点，或跌破Major Higher Low
   - 参数: consecutive_bars=3, close_position_threshold=0.1, lookback=20
3. **AI_S3**: AI by Context Long：连续两根收盘在EMA20上方，至少一根完全在EMA之上（low > EMA）
   - 参数: ema_period=20
4. **AI_S4**: AI by Context Short：连续两根收盘在EMA20下方，至少一根完全在EMA之下（high < EMA）
   - 参数: ema_period=20
5. **AI_S5**: 冲突处理：PA与Context冲突时，Context AI优先


---

## 入场与出场逻辑



---

## 概率与期望值



---

## 补充规则

- **AI_R1**: AI翻转条件：反方向3-5根连续趋势棒，或反方向惊奇棒，或突破/跌破主要结构位，或EMA反向确认
- **AI_R2**: 4-6根粘性规则：AI翻转后新方向至少控制4-6根K线，翻转后第一个回调通常失败
- **AI_R3**: 向左看规则：方向不明时找最后一次明确AI状态，假设延续
- **AI_R4**: TR中的AI：底部1/3做多，顶部1/3做空，中间不做

---

## 关联形态

| 关联模块 | 关系 | 说明 |
|----------|------|------|
| M1_MTR | related_to | 第五层DT/DB判断中MTR是反转条件的核心组成 |
| M2_SPIKE_CHANNEL | related_to | 第一层市场状态的Spike→Channel转换 |
| M3_TRADING_RANGE | related_to | 第一层TR识别 + 80%突破失败规则 |
| M4_MEASURED_MOVE | confirms | 第三层Leg等长规则 + Phase 4目标计算 |
| M5_SIGNAL_BAR | depends_on | 第六层证据链中信号棒质量是关键环节 |
| M6_ENTRY_EXIT | depends_on | 入场/离场的具体执行规则 |
| M7_HIGH2 | depends_on | 第四层H2/L2定义的详细实现 |

---

## FAQ

**Q1: Always In方向判断（第二层） 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: Always In方向判断（第二层） 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: Always In方向判断（第二层） 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 Always In方向判断（第二层） 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: 公众号交易系列4篇 + Always In完整学习手册 + 概念解剖笔记*
