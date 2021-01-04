#!/usr/bin/env python

import webbrowser
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
exam = input("Enter exam : ")

browser = webdriver.Chrome()
url = 'https://bb.hh.se/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_98_1'
browser.get(url)

agree_button = wait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='agree_button']")))
agree_button.click()

username_button = browser.find_element_by_xpath("//*[@id='user_id']")
username_button.click()
username_button.send_keys("Username")

password_button = browser.find_element_by_xpath("//*[@id='password']")
password_button.click()
password_button.send_keys("Password")

login_button = browser.find_element_by_xpath("//*[@id='entry-login']")
login_button.click()


course_button = wait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='_25_1termCourses_noterm']/ul/li[2]/a")))
course_button.click()



content_button = browser.find_element_by_xpath("//*[@id='paletteItem:_123811_1']/a")

content_button.click()

browser.switch_to.window(browser.window_handles[-1])

a = browser.current_url

exams_button = browser.find_element_by_xpath("//*[@id='menu']/div[11]/a")
exams_button.click()



a = "//*[@id='content']/ul/li["
b="]/a"

exam_button = browser.find_element_by_xpath(a+exam+b)
exam_button.click()

tenta_url = browser.current_url

browser.switch_to.window(browser.window_handles[0])


course_button = browser.find_element_by_xpath("//*[@id='paletteItem:_123811_1']/a")
course_button.click()

browser.switch_to.window(browser.window_handles[-1])

formula = browser.find_element_by_xpath("//*[@id='menu']/div[9]/a")

formula.click()


browser.switch_to.window(browser.window_handles[0])
browser.close()

time.sleep(1)
browser.switch_to.window(browser.window_handles[0])

