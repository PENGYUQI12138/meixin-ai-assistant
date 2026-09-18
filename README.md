# 美心 AI 行政助手

面向美心教育机构行政人员的内部业务系统。项目目标是以可审计、可测试的方式管理学生、课程、排课、签到、课消、缴费、教师课时、工资基础计算和经营日报。

当前状态：第一阶段基础框架。已有项目规范、系统/数据库设计、路线规划、中文首页和健康检查；尚未实现业务 CRUD，不应作为已上线系统使用。

## 技术栈

- Python 3.12 + FastAPI
- SQLAlchemy 2 + Alembic
- 生产 PostgreSQL；本地开发/测试 SQLite
- Jinja2 + HTMX 思路的服务端页面（当前骨架不依赖 Node.js）
- pytest + Ruff

## 目录

```text
backend/                 FastAPI 应用
  app/api/               HTTP 路由
  app/core/              配置等基础设施
  app/models/            SQLAlchemy 模型（阶段 2 开始）
  app/schemas/           输入输出模型（阶段 2 开始）
  app/services/          业务服务（阶段 2 开始）
frontend/templates/      Jinja2 页面
frontend/static/         样式和前端静态资源
database/migrations/     Alembic 数据库迁移
docs/                    系统、数据库、路线和 Skills 文档
tests/                   自动化测试
```

## 本地启动（PowerShell）

需要 Python 3.12。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
Copy-Item .env.example .env
uvicorn backend.app.main:app --reload
```

浏览器打开 <http://127.0.0.1:8000>。健康检查：

- `GET /health/live`：应用进程存活。
- `GET /health/ready`：数据库连接可用。

默认 `.env.example` 使用 `database/meixin_dev.db`，只适合开发。不要提交本地数据库或真实学生资料。

## PostgreSQL 启动

已安装 Docker Desktop 时：

```powershell
Copy-Item .env.example .env
docker compose up --build
```

应用地址为 <http://127.0.0.1:8000>。Compose 使用 PostgreSQL，并等待数据库健康后启动应用。首次加入模型后执行：

```powershell
alembic upgrade head
```

## 测试和检查

```powershell
pytest
ruff check .
```

## 配置

所有配置从环境变量或 `.env` 读取。主要变量见 `.env.example`：

- `APP_ENV`：`development/test/production`
- `DATABASE_URL`：SQLAlchemy 数据库连接串
- `SECRET_KEY`：会话签名密钥；生产必须替换
- `APP_TIMEZONE`：默认 `Asia/Shanghai`
- `LOG_LEVEL`：日志等级
- `AI_PROVIDER`、`AI_API_KEY`：后续 AI 模块使用；未配置时核心业务照常运行

生产环境还必须具备 HTTPS、强随机密钥、数据库自动备份、恢复演练、受控账号和日志保留策略。

## 开发入口

参与开发前必须阅读 [AGENTS.md](AGENTS.md) 和 [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md)。长期设计见：

- [系统设计文档](docs/系统设计文档.md)
- [数据库设计](docs/数据库设计.md)
- [开发路线](docs/开发路线.md)
- [Skills 研究](docs/Skills研究.md)

## 下一步

先取得并脱敏现有学生、课程、教师 Excel 样例，确认课消和计薪规则；随后进入阶段 2：登录权限、学生/家长/教师/课程基础模型，以及带预览和错误报告的 Excel 导入。
