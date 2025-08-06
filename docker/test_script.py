#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的MySQL集成测试脚本

使用这个文件来快速测试 Inline SQL 扩展的 MySQL 数据库集成功能。
在 VSCode 中打开此文件，观察 SQL 语句的语法高亮和 lint 检查结果。
"""

# 测试1: 正确的查询 - 应该通过检查
test_query_1 = """--sql
SELECT name, email FROM users WHERE age > 25
"""

# 测试2: 表不存在 - 应该报错
test_query_2 = """--sql
SELECT * FROM nonexistent_table
"""

# 测试3: 语法错误 - 应该报错
test_query_3 = """--sql
SELECT * FORM users
"""

# 测试4: 列不存在 - 应该报错
test_query_4 = """--sql
SELECT nonexistent_column FROM users
"""

# 测试5: 复杂但正确的查询
test_query_5 = """--sql
SELECT u.name, b.title 
FROM users u 
JOIN user_books ub ON u.id = ub.user_id 
JOIN books b ON ub.book_id = b.id
"""

print("MySQL 集成测试文件已准备就绪")
print("请在 VSCode 中查看各个 SQL 语句的检查结果")