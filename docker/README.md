# MySQL 数据库集成测试环境

这个目录包含了用于测试 Inline SQL 扩展 MySQL 数据库集成功能的 Docker 环境。

## 快速开始

### 1. 启动 MySQL 容器

```bash
cd docker
docker-compose up -d
```

### 2. 等待数据库初始化完成

```bash
# 检查容器状态
docker-compose ps

# 查看初始化日志
docker-compose logs mysql
```

### 3. 验证数据库连接

```bash
# 连接到 MySQL 容器
docker-compose exec mysql mysql -u testuser -ptestpass testdb

# 或者使用 root 用户
docker-compose exec mysql mysql -u root -prootpassword testdb
```

### 4. 配置 VSCode 扩展

在 VSCode 设置中添加以下配置：

```json
{
    "inlineSQL.enableDBIntegration": true,
    "inlineSQL.dbDriver": "mysql",
    "inlineSQL.dbHost": "localhost",
    "inlineSQL.dbPort": 3306,
    "inlineSQL.dbUser": "testuser",
    "inlineSQL.dbPassword": "testpass"
}
```

## 数据库信息

- **数据库名**: `testdb`
- **用户名**: `testuser`
- **密码**: `testpass`
- **Root密码**: `rootpassword`
- **端口**: `3306`

## 测试表结构

### users 表
- `id` (INT, 主键, 自增)
- `name` (VARCHAR(100))
- `email` (VARCHAR(100), 唯一)
- `age` (INT)
- `created_at` (TIMESTAMP)

### books 表
- `id` (INT, 主键, 自增)
- `title` (VARCHAR(200))
- `author` (VARCHAR(100))
- `isbn` (VARCHAR(20), 唯一)
- `price` (DECIMAL(10, 2))
- `published_date` (DATE)
- `created_at` (TIMESTAMP)

### user_books 表
- `id` (INT, 主键, 自增)
- `user_id` (INT, 外键)
- `book_id` (INT, 外键)
- `borrowed_date` (DATE)
- `return_date` (DATE)

## 停止和清理

```bash
# 停止容器
docker-compose down

# 停止并删除数据卷
docker-compose down -v
```

## 测试 SQL 示例

可以在 Python 文件中使用以下 SQL 语句进行测试：

```python
# 正确的 SQL
query1 = """--sql
SELECT * FROM users WHERE age > 25
"""

# 错误的 SQL (用于测试 lint 功能)
query2 = """--sql
SELECT * FROM nonexistent_table
"""

# 语法错误的 SQL
query3 = """--sql
SELECT * FORM users
"""
```