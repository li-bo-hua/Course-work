# 导入所需的库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import insert_info

# 初始化一个 Chrome WebDriver 实例
driver = webdriver.Chrome()
driver.maximize_window()  # 设置浏览器全屏
driver.get('https://spa5.scrape.center')  # 打开目标网站
time.sleep(2)  # 等待 2 秒，确保页面加载完成


# 定义函数，用于获取书籍信息
def get_info():
    # 初始化一个空列表，用于存放书籍的标签
    ty = []
    # 获取书籍标签
    try:
        # 使用 XPath 定位符找到包含标签信息的按钮元素
        t = driver.find_elements(by=By.XPATH,
                                 value="//button[@class='el-button el-button--primary el-button--mini']/span")
        for i in t:  # 遍历按钮元素，提取其中的文本信息，将标签存入列表中
            ty.extend(i.text)
            ty.extend('/')
            # 将列表中的标签信息拼接为一个字符串，并删除最后一个字符（因为最后一个字符是多余的斜杠）
        tag = ''.join(ty)[:-1]
    except:
        tag = 'N/A'
    # 获取评分信息
    try:
        score = driver.find_element(by=By.XPATH, value="//span[@class='score m-r']").text
    except:
        score = 'N/A'
    # 获取书籍标题信息
    try:
        title = driver.find_element(by=By.XPATH, value="//h2[@class='m-b-sm name' ]").text
    except:
        title = 'N/A'
    # 获取价格信息
    try:
        price = driver.find_element(by=By.XPATH, value="//div[@class='info']/p[@class='price']").text
    except:
        price = 'N/A'
    # 获取作者信息
    try:
        author = driver.find_element(by=By.XPATH, value="//div[@class='info']/p[@class='authors']").text
    except:
        author = 'N/A'
    # 获取出版日期信息
    try:
        published_at = driver.find_element(by=By.XPATH, value="//div[@class='info']/p[@class='published-at']").text
    except:
        published_at = 'N/A'
    # 获取出版社信息
    try:
        publisher = driver.find_element(by=By.XPATH, value="//div[@class='info']/p[@class='publisher']").text
    except:
        publisher = 'N/A'
    # 获取页数信息
    try:
        page_number = driver.find_element(by=By.XPATH, value="//div[@class='info']/p[@class='page-number']").text
    except:
        page_number = 'N/A'
    # 获取ISBN信息
    try:
        isbm = driver.find_element(by=By.XPATH, value="//div[@class='info']/p[@class='isbn']").text
    except:
        isbm = 'N/A'
    # 将所有信息组合成一个列表并返回
    full_info = [title, score, tag, price, author, published_at, publisher, page_number, isbm]

    return full_info


# 设置一个循环，用于爬取多页数据
o = 0
while o < 100:
    o += 1
    # 等待页面元素加载完成
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='top el-row']/div[@class='el-col el-col-24']/a")))
    time.sleep(3)
    book_page = driver.find_elements(By.XPATH, "//div[@class='top el-row']/div[@class='el-col el-col-24']/a")
    for i in range(len(book_page)):
        # 点击链接，进入书籍详情页面
        driver.execute_script("arguments[0].click();", book_page[i])
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='info']")))
        # 调用 get_info 函数获取书籍信息，并插入数据库
        insert_info.insert_info(get_info())
        # 返回上一页
        driver.back()
        # 再次等待书籍列表页面加载完成
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='top el-row']/div[@class='el-col el-col-24']/a")))
        book_page = driver.find_elements(By.XPATH, "//div[@class='top el-row']/div[@class='el-col el-col-24']/a")
    # 等待翻页按钮加载完成
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='top el-row']/div[@class='el-col el-col-24']/a")))
    # 找到并点击下一页按钮
    next_btn = driver.find_element(By.CLASS_NAME, "btn-next")  # 修改为 next_btn，避免拼写错误
    driver.execute_script("arguments[0].click();", next_btn)
# 关闭浏览器
driver.close()