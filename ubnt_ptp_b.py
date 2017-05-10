#!/usr/bin/env python
"""
ubnt_ptp_b.py - AutoConfig UBNT PTP REMOTE (STATION)
Copyright 2017, KRIPT4

Testing: UBIQUITI NANOLOCO M5 - FW: XW.v6.0.4 (10/5/2017) = OK

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
varWPA2 = '0123456789'			# WPA2-AES
varIPAN = '192.168.1.21'		# NEW IP ADDRESS
varDNS1 = '8.8.8.8'				# DNS1
varDNS2 = '8.8.4.4'				# DNS2
varNTPS = '2.ar.pool.ntp.org'	# NTP SERVER
varNUSR = 'KRIPT4'				# NEW USERNAME
varNPSS = 'KRIPT4'				# NEW PASSWORD
varNAMD = 'REMOTE PTP'			# NEW DIVICE NAME	

start_time = time.time()		# TIME EXECUTION TEST

#https://github.com/SeleniumHQ/selenium/blob/master/py/selenium/webdriver/chrome/options.py

chrome_options = Options()
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
driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/input').click()
## END LOGIN

## WIRELESS CONFIG
time.sleep(5)
driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/a[3]').click()
time.sleep(1)
driver.find_element_by_id('essid').clear()
driver.find_element_by_id('essid').send_keys(varSSID)
driver.find_element_by_id('dfs').click() # DISABLE DFS
driver.find_element_by_id('security').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="security"]/option[3]').click() #WPA2-AES
driver.find_element_by_id('wpa_key').send_keys(varWPA2)
time.sleep(1)
driver.find_element_by_id('hide-warning').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="this_form"]/table/tbody[3]/tr/td/input').click()
time.sleep(4)
## END WIRELESS CONFIG

## CHANGE PASSWORD DIALOG:
driver.find_element_by_xpath('//*[@id="dlgOldPassword"]').send_keys(varPASS)
driver.find_element_by_xpath('//*[@id="dlgNewPassword"]').send_keys(varNPSS)
driver.find_element_by_xpath('//*[@id="dlgNewPassword2"]').send_keys(varNPSS)
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/button[2]').click()
time.sleep(4)
## END CHANGE PASSWORD DIALOG

## NETWORK CONFIG
driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/a[4]').click()
time.sleep(2)
driver.find_element_by_id('mgmtIpAddr').clear()
driver.find_element_by_id('mgmtIpAddr').send_keys(varIPAN)
driver.find_element_by_id('mgmtDns1').clear()
driver.find_element_by_id('mgmtDns1').send_keys(varDNS1)
driver.find_element_by_id('mgmtDns2').clear()
driver.find_element_by_id('mgmtDns2').send_keys(varDNS2)
driver.find_element_by_id('mgmtStp').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="change"]').click()
time.sleep(2)
## END NETWORK CONFIG

## ADVANCED CONFIG
driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/a[5]').click()
time.sleep(1)
driver.find_element_by_id('led1').clear()
driver.find_element_by_id('led1').send_keys('80')
driver.find_element_by_id('led2').clear()
driver.find_element_by_id('led2').send_keys('70')
driver.find_element_by_id('led3').clear()
driver.find_element_by_id('led3').send_keys('60')
driver.find_element_by_id('led4').clear()
driver.find_element_by_id('led4').send_keys('55')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="adv_form"]/table/tbody/tr[22]/td/input').click()
## END ADVANCED CONFIG

## SERVICES CONFIG
time.sleep(2)
driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/a[6]').click()
time.sleep(1)
driver.find_element_by_id('https_status').click()
driver.find_element_by_id('telnetd_status').click()
driver.find_element_by_id('ntpStatus').click()
driver.find_element_by_id('ntpServer').clear()
driver.find_element_by_id('ntpServer').send_keys(varNTPS)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="svc_form"]/table/tbody/tr[36]/td/input').click()
time.sleep(2)
## EN SERVICES CONFIG

## SYSTEM CONFIG
driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/a[7]').click()
time.sleep(1)
driver.find_element_by_id('hostname').clear()
driver.find_element_by_id('hostname').send_keys(varNAMD)
driver.find_element_by_id('adminname').clear()
driver.find_element_by_id('adminname').send_keys(varNUSR)
driver.find_element_by_id('system_change').click()
time.sleep(5)
driver.find_element_by_id('apply_button').click()
time.sleep(3)
## END SYSTEM CONFIG

driver.quit()

elapsed_time = time.time() - start_time
print("Elapsed time: %.10f seconds." % elapsed_time)