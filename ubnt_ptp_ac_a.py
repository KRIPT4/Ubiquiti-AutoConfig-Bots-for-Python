#!/usr/bin/env python
"""
ubnt_ptp_ac_a.py - AutoConfig UBNT PTP AC BASE (ACCESS POINT)
Copyright 2017, KRIPT4

Testing: UBIQUITI POWERBEAM 5AC ISO - FW: XC.v7.2.1 (11/5/2017) = OK

More info:
 * KRIPT4: https://github.com/KRIPT4/Ubiquiti-AutoConfig-Bots-for-Python
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

varIPAD = '192.168.1.20'		# DEFAULT IP ADDRESS
varUSER = 'ubnt'				# DEFAULT USERNAME
varPASS = 'ubnt'				# DEFAULT PASSWORD
varSSID = 'BASE-PtP-SSID'		# SSID
varDBM  = '24'					# TX POWER
varWPA2 = '0123456789'			# WPA2-AES
varDNS1 = '8.8.8.8'				# DNS1
varDNS2 = '8.8.4.4'				# DNS2
varNTPS = '2.ar.pool.ntp.org'	# NTP SERVER
varNUSR = 'KRIPT4'				# NEW USERNAME
varNPSS = 'KRIPT4'				# NEW PASSWORD
varNAMD = 'BASE PTP AC'			# NEW DIVICE NAME	

start_time = time.time()		# TIME EXECUTION TEST

#https://github.com/SeleniumHQ/selenium/blob/master/py/selenium/webdriver/chrome/options.py

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--no-referrers')
chrome_options.add_argument('--window-size=900,900')
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://'+ varIPAD +'/')
time.sleep(4)

## LOGIN
driver.find_element_by_name('username').send_keys(varUSER)
driver.find_element_by_name('password').send_keys(varPASS)
time.sleep(1)
driver.find_element_by_id('country').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="country"]/option[2]').click()
time.sleep(1)
driver.find_element_by_id('agreed').click()
time.sleep(1)
driver.find_element_by_name('login').click()
#time.sleep(2)
## END LOGIN

## CHANGE PASSWORD DIALOG:
time.sleep(5)
driver.find_element_by_xpath('//*[@id="button-0"]').click()
time.sleep(2)
driver.find_element_by_id('pwd_old').send_keys(varPASS)
driver.find_element_by_id('pwd_1').send_keys(varNPSS)
driver.find_element_by_id('pwd_2').send_keys(varNPSS)
time.sleep(1)
driver.find_element_by_id('change_pwd').click()
time.sleep(2)
## END CHANGE PASSWORD DIALOG:

## WIRELESS CONFIG
driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[2]/a').click()
time.sleep(2)
driver.find_element_by_id('wmode').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="wmode"]/option[1]').click() #Access Point PtP
#driver.find_element_by_xpath('//*[@id="wmode"]/option[2]').click() #Access Point PtMP
driver.find_element_by_id('essid').clear()
driver.find_element_by_id('essid').send_keys(varSSID)
time.sleep(1)
driver.find_element_by_id('centerFrequency').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="centerFrequency"]/option[3]').click()
time.sleep(1)
driver.find_element_by_id('antenna').click()
driver.find_element_by_xpath('//*[@id="antenna"]/option[1]').click()
time.sleep(1)
driver.find_element_by_id('obey_regulatory_status').click()
time.sleep(1)
driver.find_element_by_id('output_power_val').clear()
driver.find_element_by_id('output_power_val').send_keys(varDBM)
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element_by_name('protocol').click()
driver.find_element_by_xpath('//*[@id="protocol"]/option[2]').click() #WPA2
time.sleep(1)
driver.find_element_by_name('wpaPsk').send_keys(varWPA2)
driver.find_element_by_id('signal_led0').clear()
driver.find_element_by_id('signal_led0').send_keys('80')
driver.find_element_by_id('signal_led1').clear()
driver.find_element_by_id('signal_led1').send_keys('70')
driver.find_element_by_id('signal_led2').clear()
driver.find_element_by_id('signal_led2').send_keys('60')
driver.find_element_by_id('signal_led3').clear()
driver.find_element_by_id('signal_led3').send_keys('55')
## END WIRELESS CONFIG

## NETWORK CONFIG
driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[3]/a').click()
time.sleep(2)
driver.find_element_by_name('dns1').send_keys(varDNS1)
driver.find_element_by_name('dns2').send_keys(varDNS2)
driver.find_element_by_id('mlanStp').click()
time.sleep(3)
## END NETWORK CONFIG

## SERVICES CONFIG
driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[4]/a').click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.find_element_by_id('f_cdp_status').click() # CDP
time.sleep(3)
## END SERVICES CONFIG

## SYSTEM CONFIG
driver.find_element_by_xpath('//*[@id="main_menu"]/ul/li[5]/a').click()
time.sleep(2)
driver.find_element_by_id('f_hostname').clear()
driver.find_element_by_id('f_hostname').send_keys(varNAMD)
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element_by_id('f_adminName').clear()
driver.find_element_by_id('f_adminName').send_keys(varNUSR)
## END SYSTEM CONFIG

## SAVE CHANGE
driver.find_element_by_id('changes_apply_button').click()
time.sleep(5)
## END SAVE CHANGE

driver.quit()

elapsed_time = time.time() - start_time
print("Elapsed time: %.10f seconds." % elapsed_time)