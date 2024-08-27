# 系统设计文档
## 系统架构
该系统使用Python和selenium爬虫技术爬取scrape book这个图书网站的图书信息，并通过MySQL数据库进行存储，系统包含以下几个模块：  
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
test.py: 确保数据库连接配置正确，并确保目标网站可以访问。  
main.py: 主程序模块，负责爬取网页数据，并调用插入数据模块将信息存入数据库。  
## 环境配置
开发工具：PyCharm
数据库管理工具：Navicat Premium   
编译器：Python 3.7  
pip install selenium  
pip install pymysql  

# 使用文档
## 具体流程
1.配置数据库：在运行脚本前，请确保MySQL服务已启动，并根据需要修改数据库连接参数。  
2.运行python dataset.py  
3.运行python connect.py，这个模块定义了一个函数connect_mysql()，用于连接MySQL数据库，并返回连接对象。我们需要提供数据库的主机地址、用户名、密码、数据库名以及字符集等信息。  
4.运行python create_table.py，在这个模块中，我们使用了connect.py中定义的连接函数，连接到MySQL数据库。然后，我们使用SQL语句创建了一个名为book_info的数据表，用于存储图书信息。  
5.运行python insert_info.py，这个模块定义了一个函数insert_info(info)，用于向数据库中插入图书信息。我们需要提供待插入的图书信息作为参数，并通过SQL语句执行插入操作。  
6.运行python test.py，这个模块对数据库连接测试，数据表创建测试及数据插入进行简单的测试，确保在爬取数据时能够正常运行。 
7.运行python main.py，这是项目的核心模块，主要负责爬取网页数据。我们使用了Selenium库来模拟浏览器行为，从指定的网站获取图书信息。然后，我们调用插入数据模块将信息存入数据库。  
## 实现过程
1.运行main.py，它会打开一个Chrome浏览器窗口，并访问指定的网站（https://spa5.scrape.center）。  
2.通过Selenium模拟点击页面中的链接，进入到具体的图书信息页面。  
3.在每个图书信息页面中，我们使用Selenium获取图书的标题、评分、标签、价格、作者、出版日期、出版社、页数和ISBN等信息。  
4.我们调用插入数据模块，将获取到的信息存入MySQL数据库中的book_info表中。  
5.我们在循环中重复以上步骤，直到获取了足够的图书信息为止。  

# 测试文档
## 测试目标
验证各模块功能，确保数据库连接、数据表创建和数据插入正常工作。
## 测试用例
1.数据库连接测试，定义了test_connect_mysql()函数，测试数据库连接是否正常。    
2. 数据表创建测试，定义了def test_create_tables()函数，测试数据表是否能成功创建。    
3. 数据插入测试，定义了def test_insert_info()，测试能否成功插入数据。  
# 爬取数据展示
总共爬取了1617条数据，若想获取更多的数据，重复运行主函数即可。
![image](https://github.com/user-attachments/assets/732e5be3-502a-439f-9588-0ec78250e369)






