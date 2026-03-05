---
title: "执行检查清单（程序化实现）"
slug: "/cross-asset/execution-checklist-guide"
meta_description: "深度解析 Al Brooks PA 中的 执行检查清单（程序化实现）。完整规则、胜率数据与实战技巧。"
cluster: "跨资产应用"
module_id: "M8_UNIFIED"
pattern_id: "EXECUTION_CHECKLIST"
direction: "both"
generated: "2026-03-05"
---

# 执行检查清单（程序化实现）

> 四阶段执行流程：市场状态→入场信号→过滤确认→管理

---

## 什么是 执行检查清单（程序化实现）？

四阶段执行流程：市场状态→入场信号→过滤确认→管理


---

## 识别规则图解



---

## 入场与出场逻辑



---

## 概率与期望值



---

## 补充规则

- **CL_R1**: Phase 1：判断Spike/Channel/TR → 判断AI by PA → 判断AI by Context → 两者一致=明确方向，冲突=Context优先
- **CL_R2**: Phase 2：计数Leg位置 → 识别H1/H2/L1/L2 → 在Leg 2位置寻找信号棒
- **CL_R3**: Phase 3：检查信号棒质量 → 检查S/R障碍 → R/R≥2:1 → 等入场棒触发 → 检查跟随棒
- **CL_R4**: Phase 4：止损设在结构位 → 仓位=可承受亏损÷止损距离 → 目标=磁吸位/MM/2R

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

**Q1: 执行检查清单（程序化实现） 的信号K线如何判断？**

根据规则，信号K线需要满足方向性（阳线/阴线）、收盘位置（上/下半部）和实体饱满度等条件。具体请参考上方触发条件。

**Q2: 执行检查清单（程序化实现） 失败后怎么办？**

失败后应等待下一个更高级别的确认信号，避免连续止损。

**Q3: 执行检查清单（程序化实现） 适用于哪些市场？**

Price Action 反映的是人类交易心理，因此 执行检查清单（程序化实现） 适用于股票、期货、外汇、加密货币等所有流动性充足的市场。

---

*本文基于 Al Brooks Price Action 体系自动生成，数据来源: 公众号交易系列4篇 + Always In完整学习手册 + 概念解剖笔记*
