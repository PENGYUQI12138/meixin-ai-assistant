# 数据库目录

- `migrations/` 保存 Alembic 迁移。
- 本地 SQLite 文件会生成在本目录但已被 Git 忽略。
- 生产使用 PostgreSQL，不把数据库备份提交到仓库。

创建模型后生成迁移：

```powershell
alembic revision --autogenerate -m "create initial business tables"
alembic upgrade head
```
