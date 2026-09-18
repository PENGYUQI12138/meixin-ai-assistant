# Skills 研究记录

研究日期：2026-09-18
范围：软件架构、Python/FastAPI、数据库、前端、测试、Git 管理。

Codex Skills 是把项目工作流和约束封装为可复用说明的机制。是否安装应以能否减少重复工作、是否来自可信来源、是否与本项目技术栈吻合为准；通用工程能力不需要用大量 Skills 替代项目自身的 `AGENTS.md`、测试和代码审查。

| 名称 | 地址 | 作用 | 是否推荐 |
|---|---|---|---|
| OpenAI Codex Skills 官方文档 | https://learn.chatgpt.com/docs/build-skills | 说明 Skill 的结构、触发和维护方式 | 推荐作为规范参考；无需项目内安装 |
| OpenAI Skills Catalog | https://github.com/openai/skills | 官方示例与可安装技能目录 | 推荐作为可信检索入口；不整库安装 |
| playwright | https://github.com/openai/skills/tree/main/skills/.curated/playwright | 用真实浏览器验证行政端关键流程和回归 | 推荐在阶段 2 页面成形时安装；当前骨架阶段暂不安装 |
| security-best-practices | https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices | 对认证、权限、敏感数据和依赖做安全检查 | 推荐在登录/权限开发前安装 |
| gh-fix-ci | https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci | 定位并修复 GitHub Actions 失败 | 条件推荐；建立 CI 后再安装 |
| gh-address-comments | https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments | 系统处理 PR 审查意见 | 条件推荐；多人 PR 流程稳定后再安装 |
| render-deploy | https://github.com/openai/skills/tree/main/skills/.curated/render-deploy | 辅助在 Render 部署应用 | 暂不推荐；需先确定实际部署平台 |
| jupyter-notebook | https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook | 数据探索、迁移验证和可复现分析 | 暂不安装；Excel 导入排查复杂时再用 |

## 结论

- 当前不安装额外 Skill。第一阶段最重要的是建立仓库内的长期规范和可测试骨架。
- 官方可用清单中没有一个专门、可信且必要的 FastAPI/SQLAlchemy 架构 Skill；框架规范应由 `AGENTS.md`、官方框架文档、类型检查和测试共同保证。
- 首选后续安装顺序：`playwright`（阶段 2）→ `security-best-practices`（认证与权限前）→ GitHub 工作流相关 Skills（CI/PR 实际启用后）。
- 任何第三方 Skill 安装前必须阅读其 `SKILL.md` 和脚本，确认不会上传业务数据、执行不透明命令或引入与本项目冲突的工作流。
