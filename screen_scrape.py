import datetime
import math

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# Open the National Rail site and scrape the status for the specified journey
def screen_scrape(train_from, train_to, train_time):
  current_time = datetime.datetime.now()
  print('Running scrape: ' + current_time.strftime('%d-%m-%Y %H:%M'))

  browser = webdriver.Firefox()
  browser.get('http://www.nationalrail.co.uk/')

  delay = 30
  try:
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#txtFrom')))
  except TimeoutException:
    print "Loading took too much time!"
    return

  # Fill in the journey information
  minute_closest_15 = '{num:2.0f}'.format(num=math.floor(train_time.minute / 15) * 15)

  element_input_from = browser.find_element_by_css_selector('#txtFrom')
  element_input_to = browser.find_element_by_css_selector('#txtTo')
  element_select_hours = browser.find_element_by_css_selector('#sltHours')
  element_select_minutes = browser.find_element_by_css_selector('#sltMins')
  element_button_go = browser.find_element_by_css_selector('#jp > div.b1-m.clear > div.jp-left > button')

  browser.execute_script("arguments[0].value = arguments[1];", element_input_from, train_from)
  browser.execute_script("arguments[0].value = arguments[1];", element_input_to, train_to)

  element_select_hours.find_element_by_css_selector('option[value="' + train_time.strftime('%H') + '"]').click()
  element_select_minutes.find_element_by_css_selector('option[value="' + minute_closest_15.strip() + '"]').click()

  element_button_go.send_keys(Keys.ENTER)

  try:
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#oft > tbody > tr.first.mtx.sel')))
  except TimeoutException:
    print "Loading took too much time!"
    return

  departure_row = browser.find_element_by_css_selector('#oft > tbody > tr.first.mtx.sel')
  print(departure_row.find_element_by_css_selector('.dep').text)
  print(departure_row.find_element_by_css_selector('.status').text)
