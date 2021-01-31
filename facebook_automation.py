# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:03:04 2021

@author: anime
"""

# This Program will go on facebook and log with provided id pss and open the user Profile

# Importing required libraries
import time
from selenium import webdriver

# Lets Begin
# Dealing with Notifications pop in facebook
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

# Get start with Google
driver.get('https://www.google.com/')
time.sleep(5)

# Typing Facebook
driver.find_element_by_name('q').send_keys('Facebook')
time.sleep(3)
driver.find_element_by_class_name('gNO89b').click()
time.sleep(5)

# Open login page of Facebook
driver.find_element_by_class_name('l').click()
time.sleep(5)

# Typing Email Id Password (write email id and password in place of --)
driver.find_element_by_name('email').send_keys('----------@gmail.com')
time.sleep(2)
driver.find_element_by_name('pass').send_keys('------------')
time.sleep(2)
driver.find_element_by_name('login').click()
time.sleep(7)

# Posting Status
#button1 = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span').click()
#time.sleep(5)
#driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div').send_keys('Hello Guys..')
#time.sleep(8)
#post = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div').click()
#time.sleep(5)

# Liking Post

like1 = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]').click()
time.sleep(5)
like2 = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]').click()
time.sleep(5)
like3 = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[5]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]').click()
time.sleep(5)
like4 = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[7]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]').click()
time.sleep(5)


# Opening Profile
video = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[2]/span/div/a').click()
time.sleep(5)
group = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[4]/span/div/a').click()
time.sleep(5)
gaming = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[5]/span/div/a').click()
time.sleep(5)
profile = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[4]/div[1]/div[4]/a').click()
time.sleep(20)
driver.quit()


