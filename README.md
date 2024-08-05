# 系统设计文档
## 系统架构
该系统使用Python和selenium爬虫技术爬取的是一个图书网站：scrape book的图书信息，并通过MySQL数据库进行存储，系统包含以下几个模块：  
1.数据库创建模块  
2.数据库连接模块  
3.数据表创建模块  
4.数据插入模块  
5.测试模块  
6.数据爬取模块  
## 数据库设计
数据库名称：Scrape_book  
表名称：book_info  
表结构：  
key INT AUTO_INCREMENT PRIMARY KEY：主键，唯一标识表中每一行，自动递增。  
title VARCHAR(50)：存储书籍标题，据类型是可变长度字符串，最大长度为50个字符。  
score VARCHAR(20)：存储书籍的评分。  
typeN VARCHAR(50)：存储书籍的类型或类别。  
price VARCHAR(20)：存储书籍价格。  
author VARCHAR(50)：存储书籍作者。  
published_at  VARCHAR(50)：存储书籍出版日期。  
page_number VARCHAR(50)：存储书籍的页数。  
publisher VARCHAR(50)：存储书籍的出版社。  
isbm VARCHAR(50)：存储书籍的ISBN号码。  

# 说明文档
## 文件结构
dataset.py: 创建MySQL数据库。  
connect.py: 连接数据库模块，负责与MySQL数据库建立连接。  
create_table.py: 创建数据表模块，创建一个名为book_info的数据表，用于存储图书信息。  
insert_info.py: 插入数据模块，向数据表中插入图书信息。  
test.py: 进行数据库连接测试，数据表创建测试及数据插入测试，保数据库连接配置正确，并确保目标网站可以访问。  
main.py: 主程序模块，负责爬取网页数据，并调用插入数据模块将信息存入数据库。  
## 环境配置
数据库管理工具：Navicat Premium   
Python 3.7  
pip install selenium  
pip install pymysql  

# 使用文档
# 测试文档
# 爬取数据展示
![image](https://github.com/user-attachments/assets/732e5be3-502a-439f-9588-0ec78250e369)






