#-------------------------------------------------------------------------------
# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import requests
from selenium import webdriver
import time

#-------------------------------------------------------------------------------
# Setup

firstname = 0

with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.get('https://forms.gle/qY3oxu4s7ZWjjzKF8')

        time.sleep(5)
        firstname = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input') 
        firstname.send_keys(line[0])
        submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit.click()

      

#-------------------------------------------------------------------------------