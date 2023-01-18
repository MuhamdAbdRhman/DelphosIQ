import time
from datetime import datetime

import bs4 as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from loans.models import Country, Sector


def prepare_date(data):
    return datetime.strptime(data, '%d %B %Y').date().strftime('%Y-%m-%d')


def prepare_amount(data):
    return float(data.replace('€', '').replace(',', ''))


def prepare_country(data):
    country, _ = Country.objects.get_or_create(name=data)
    return country


def prepare_sector(data):
    sector, _ = Sector.objects.get_or_create(name=data)
    return sector


def get_table_rows_from_url(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(
        command_executor='http://chrome:4444/wd/hub',
        options=options
    )
    driver.get(url)
    time.sleep(10)  # Sleep to w8 page to be fully loaded
    select = Select(driver.find_element(by=By.ID, value='show-entries'))
    select.select_by_value('100')
    time.sleep(30)  # Sleep to w8 page to be fully loaded
    webpage = driver.page_source
    soup = bs.BeautifulSoup(webpage, 'lxml')
    table = soup.find('div', id='mainlist')
    rows = table.find_all('div', class_='row-list')
    return rows
