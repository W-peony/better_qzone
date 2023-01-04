from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from time import sleep

base_path = __file__[:__file__.rfind('\\') + 1]


def add_cookie(driver, file_path):

    with open(base_path + file_path, 'r') as file:
        data = file.read().strip('\'')
    for item in data.split(';'):
        item = item.strip(' ')
        driver.add_cookie({
            'domain': '.qq.com',
            'name': item.split('=')[0],
            'value': item.split('=')[1],
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        })
    sleep(3)
    driver.refresh()


url = 'https://i.qq.com/'
driver = webdriver.Chrome(
    service=chromeService(base_path + 'chromedriver.exe')
)
driver.maximize_window()
driver.get(url)
add_cookie(driver, 'cookie.dat')

while True:
    pass
