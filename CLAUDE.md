# 公众号国际化项目

## 项目概述
将 351 篇中文 Price Action / Al Brooks 交易公众号文章翻译为 10 种语言，并发布到 Medium 和 Substack。

## 目标语言
en, vi, id, es, pt, ja, ko, de, ar, ru

## 文件夹结构
```
公众号文章/          # 中文原文（14个分类）
translated/{lang}/   # 翻译后文件，保持原分类结构
terminology/         # 术语表 JSON
logs/                # 翻译进度、发布日志
published/           # 已发布归档
```

## 翻译规范
1. 内容不增不减不改，只忠实翻译
2. 保留所有 Markdown 格式
3. 移除微信特有元素：封面图链接、"在小说阅读器中沉浸阅读"、作者署名行、知识星球广告
4. 保留文章内图片链接
5. 强制使用 terminology/terminology.json 中的术语对照
6. Al Brooks 特有概念保留英文原文 + 本地化注释

## 14 个文章分类
AI与学习、K线与信号、交易书籍、交易区间、交易原则、交易手册、交易策略、入场与出场、入门与成长、其他概念、心理与错误、突破与反转、认知杂文、趋势

## 质量检查
- 段落数量必须与原文对齐
- 术语翻译必须一致（用 terminology.json 校验）
- 不允许遗漏任何段落

## 发布平台
- Medium: 通过 API 发布
- Substack: 通过可用方式发布（API/邮件/自动化）

## 进度追踪
- logs/translation_progress.json: 翻译进度
- logs/publish_log.json: 发布日志
- logs/file_index.txt: 所有源文件索引
