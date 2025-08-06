#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MySQL 数据库集成测试文件

这个文件包含了各种 SQL 语句，用于测试 Inline SQL 扩展的 MySQL 数据库集成功能。
确保在运行测试前已经启动了 Docker 容器并配置了正确的数据库连接参数。
"""

# 正确的查询语句 - 应该通过 lint 检查
valid_select_query = """--sql
SELECT id, name, email, age 
FROM users 
WHERE age > 25 
ORDER BY name
"""

valid_join_query = """--sql
SELECT u.name, b.title, ub.borrowed_date
FROM users u
JOIN user_books ub ON u.id = ub.user_id
JOIN books b ON ub.book_id = b.id
WHERE ub.return_date IS NULL
"""

valid_insert_query = """--sql
INSERT INTO users (name, email, age) 
VALUES ('测试用户', 'test@example.com', 30)
"""

valid_update_query = """--sql
UPDATE books 
SET price = 99.99 
WHERE id = 1
"""

valid_delete_query = """--sql
DELETE FROM user_books 
WHERE return_date < '2023-05-01'
"""

# 包含语法错误的查询 - 应该被 lint 检测到
syntax_error_query = """--sql
SELECT * FORM users
"""

missing_from_query = """--sql
SELECT name, email
"""

invalid_column_query = """--sql
SELECT nonexistent_column FROM users
"""

# 表不存在的查询 - 应该被数据库集成检测到
invalid_table_query = """--sql
SELECT * FROM nonexistent_table
"""

# 复杂查询测试
complex_query = """--sql
SELECT 
    u.name AS user_name,
    COUNT(ub.book_id) AS books_borrowed,
    AVG(b.price) AS avg_book_price
FROM users u
LEFT JOIN user_books ub ON u.id = ub.user_id
LEFT JOIN books b ON ub.book_id = b.id
GROUP BY u.id, u.name
HAVING COUNT(ub.book_id) > 0
ORDER BY books_borrowed DESC
"""

# 子查询测试
subquery_test = """--sql
SELECT name, email
FROM users
WHERE id IN (
    SELECT user_id 
    FROM user_books 
    WHERE return_date IS NULL
)
"""

# 聚合函数测试
aggregate_query = """--sql
SELECT 
    COUNT(*) as total_users,
    AVG(age) as average_age,
    MIN(age) as youngest,
    MAX(age) as oldest
FROM users
"""

# 日期函数测试
date_query = """--sql
SELECT 
    title,
    published_date,
    DATEDIFF(NOW(), published_date) as days_since_published
FROM books
WHERE published_date > '2023-01-01'
"""

# 字符串函数测试
string_query = """--sql
SELECT 
    UPPER(name) as name_upper,
    LOWER(email) as email_lower,
    CONCAT(name, ' - ', email) as name_email
FROM users
WHERE name LIKE '%三%'
"""

# 使用变量的查询（参数化查询示例）
user_id = 1
parameterized_query = """--sql
SELECT * FROM users WHERE id = ?
"""

# f-string 查询（不推荐，但用于测试）
table_name = "users"
f_string_query = f"""--sql
SELECT COUNT(*) FROM {table_name}
"""

# 创建表的 DDL 语句
create_table_query = """--sql
CREATE TABLE test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

# 索引创建
create_index_query = """--sql
CREATE INDEX idx_users_email ON users(email)
"""

# 视图创建
create_view_query = """--sql
CREATE VIEW active_borrowers AS
SELECT u.name, u.email, COUNT(ub.id) as active_books
FROM users u
JOIN user_books ub ON u.id = ub.user_id
WHERE ub.return_date IS NULL
GROUP BY u.id, u.name, u.email
"""

if __name__ == "__main__":
    print("这是一个用于测试 Inline SQL 扩展 MySQL 数据库集成功能的文件")
    print("请在 VSCode 中打开此文件，并确保已正确配置数据库连接参数")
    print("观察各个 SQL 语句的语法高亮和 lint 检查结果")