# auto get WF mortgage rates for a new purchase in CA and San Francisco county.
# 1/ do a search for home loans
# 2/ find the right url links from search results
# 3/ fill out the loan details, e.g. home value, download payment, state and county
# 4/ click to get the rates 
# 5/ save a copy 

from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser  = webdriver.Chrome(r"D:\github\walter-repo\Selenium\chromedriver.exe")
browser.get('https://www.wellsfargo.com')

searchElem = browser.find_element_by_id("inputTopSearchField")
searchElem.send_keys("home loans")
searchElem.submit()

homeloanElem = browser.find_element_by_link_text("Home Loans and Home Financing – Wells Fargo")
homeloanElem.click()

homeValueElem = browser.find_element_by_id("homeValue")
homeValueElem.send_keys("1000000")

homeValueElem = browser.find_element_by_id("downPayment")
homeValueElem.send_keys("500000")

#RPCElem = browser.find_element_by_id("RPC")
#RPCElem.click()

selectpropertyState = Select(browser.find_element_by_id('propertyState'))
selectpropertyState.select_by_visible_text('CA')

selectpropertyCounty = Select(browser.find_element_by_id('propertyCounty'))
selectpropertyCounty.select_by_visible_text('San Francisco')

# below is the final calculate button !
CalculateButton = browser.find_element_by_id("NID1_13_1_2_4_1_3_2_2")
CalculateButton.click()

browser.save_screenshot('D:/Akamai/api-kickstart/wf-mortgage-rate1.png')

'''
D:\Akamai\api-kickstart>python auto-wf-mortgage-rates1.py

DevTools listening on ws://127.0.0.1:52865/devtools/browser/afc95313-bc09-4376-b2e7-e4e74ce9deea
[51220:76684:0113/140419.946:ERROR:platform_sensor_reader_win.cc(242)] NOT IMPLEMENTED

D:\Akamai\api-kickstart>ls -l *wf*
-rwxrwx---+ 1 user1 None   1493 Jan 13 14:04 auto-wf-mortgage-rates1.py
-rwxrwx---+ 1 user1 None 992617 Jan 13 13:48 auto-wf-mortgage-rates2.mp4
-rwxrwx---+ 1 user1 None 116907 Jan 13 14:04 wf-mortgage-rate1.png
'''
