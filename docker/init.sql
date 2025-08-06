-- 初始化测试数据库
USE testdb;

-- 创建用户表
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建书籍表
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    price DECIMAL(10, 2),
    published_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入测试数据
INSERT INTO users (name, email, age) VALUES
('张三', 'zhangsan@example.com', 25),
('李四', 'lisi@example.com', 30),
('王五', 'wangwu@example.com', 28),
('赵六', 'zhaoliu@example.com', 35);

INSERT INTO books (title, author, isbn, price, published_date) VALUES
('Python编程入门', '作者A', '978-1234567890', 59.99, '2023-01-15'),
('数据库设计原理', '作者B', '978-1234567891', 79.99, '2023-02-20'),
('Web开发实战', '作者C', '978-1234567892', 69.99, '2023-03-10'),
('算法与数据结构', '作者D', '978-1234567893', 89.99, '2023-04-05');

-- 创建一个有外键关系的表
CREATE TABLE user_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrowed_date DATE,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO user_books (user_id, book_id, borrowed_date, return_date) VALUES
(1, 1, '2023-05-01', '2023-05-15'),
(2, 2, '2023-05-02', NULL),
(3, 3, '2023-05-03', '2023-05-17'),
(1, 4, '2023-05-04', NULL);