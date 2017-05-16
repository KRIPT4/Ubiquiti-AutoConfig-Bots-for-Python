#!/usr/bin/env python
"""
ubnt_ptp_a.py - AutoConfig UBNT PTP BASE (ACCESS POINT)
Copyright 2017, KRIPT4

Testing:
- UBIQUITI NANOLOCO M5 - FW: XW.v6.0.4 (10/5/2017) = OK
- UBIQUITI ROCKET M5 - FW: XW.v5.6.9 (16/5/2017) = OK

More info:
 * KRIPT4: https://github.com/KRIPT4/Ubiquiti-AutoConfig-Bots-for-Python
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
global driver

def mainExe():

	# CONFIGURE:
	varIPAD = '192.168.1.20'		# DEFAULT IP ADDRESS
	varUSER = 'ubnt'				# DEFAULT USERNAME
	varPASS = 'ubnt'				# DEFAULT PASSWORD
	varSSID = 'BASE-PtP-SSID'		# SSID
	varWPA2 = '0123456789'			# WPA2-AES
	varDNS1 = '8.8.8.8'				# DNS1
	varDNS2 = '8.8.4.4'				# DNS2
	varNTPS = '2.ar.pool.ntp.org'	# NTP SERVER
	varNUSR = 'KRIPT4'				# NEW USERNAME
	varNPSS = 'KRIPT4'				# NEW PASSWORD
	varNAMD = 'BASE PTP'			# NEW DIVICE NAME	

	start_time = time.time()		# TIME EXECUTION TEST

	global driver #executable_path = '?:\PATH\TO\chromedriver.exe', 
	driver = webdriver.Chrome(chrome_options = chrome_options)
	driver.get('http://'+ varIPAD +'/')
	time.sleep(1)

	## LOGIN
	retryElementNAME('username').send_keys(varUSER)
	retryElementNAME('password').send_keys(varPASS)
	retryElementID('country').click()
	retryElement('//*[@id="country"]/option[2]').click()
	retryElementID('agreed').click()
	retryElement('/html/body/table/tbody/tr[5]/td/input').click()
	## END LOGIN

	## WIRELESS CONFIG
	retryElement('/html/body/table/tbody/tr[2]/td[1]/a[3]').click()
	retryElementID('wmode').click()
	retryElement('//*[@id="wmode"]/option[2]').click()
	retryElementID('essid').clear()
	retryElementID('essid').send_keys(varSSID)
	retryElementID('dfs').click() # DISABLE DFS
	retryElementID('chan_freq').click()
	retryElement('//*[@id="chan_freq"]/option[7]').click()
	retryElementID('security').click()
	retryElement('//*[@id="security"]/option[3]').click() #WPA2-AES
	retryElementID('wpa_key').send_keys(varWPA2)
	retryElementID('hide-warning').click()
	retryElement('//*[@id="this_form"]/table/tbody[3]/tr/td/input').click()
	## END WIRELESS CONFIG.

	## CHANGE PASSWORD DIALOG:
	retryElement('//*[@id="dlgOldPassword"]').send_keys(varPASS)
	retryElement('//*[@id="dlgNewPassword"]').send_keys(varNPSS)
	retryElement('//*[@id="dlgNewPassword2"]').send_keys(varNPSS)
	retryElement('/html/body/div[2]/div[3]/div/button[2]').click()
	time.sleep(2)
	## END CHANGE PASSWORD DIALOG

	## NETWORK CONFIG
	retryElement('/html/body/table/tbody/tr[2]/td[1]/a[4]').click()
	retryElement('//*[@id="mgmtStp"]').click()
	retryElementID('mgmtDns1').clear()
	retryElementID('mgmtDns1').send_keys(varDNS1)
	retryElementID('mgmtDns2').clear()
	retryElementID('mgmtDns2').send_keys(varDNS2)
	retryElement('//*[@id="change"]').click()
	## END NETWORK CONFIG

	## ADVANCED CONFIG
	retryElement('/html/body/table/tbody/tr[2]/td[1]/a[5]').click()
	retryElementID('led1').clear()
	retryElementID('led1').send_keys('80')
	retryElementID('led2').clear()
	retryElementID('led2').send_keys('70')
	retryElementID('led3').clear()
	retryElementID('led3').send_keys('60')
	retryElementID('led4').clear()
	retryElementID('led4').send_keys('55')
	retryElement('//*[@id="adv_form"]/table/tbody/tr[24]/td/input').click()
	## END ADVANCED CONFIG

	## SERVICES CONFIG
	retryElement('/html/body/table/tbody/tr[2]/td[1]/a[6]').click()
	retryElementID('https_status').click()
	retryElementID('telnetd_status').click()
	retryElementID('ntpStatus').click()
	retryElementID('ntpServer').clear()
	retryElementID('ntpServer').send_keys(varNTPS)
	retryElement('//*[@id="svc_form"]/table/tbody/tr[36]/td/input').click()
	## EN SERVICES CONFIG

	## SYSTEM CONFIG
	retryElement('/html/body/table/tbody/tr[2]/td[1]/a[7]').click()
	retryElementID('hostname').clear()
	retryElementID('hostname').send_keys(varNAMD)
	retryElementID('adminname').clear()
	retryElementID('adminname').send_keys(varNUSR)
	retryElementID('system_change').click()
	retryElementID('apply_button').click()
	## END SYSTEM CONFIG

	driver.quit()

	elapsed_time = time.time() - start_time
	print("Elapsed time: %.10f seconds." % elapsed_time)

def retryElement(xpath):
	for i in range(0,50):
		try:
			element = driver.find_element_by_xpath(xpath)
			return element
		except Exception as e:
			time.sleep(0.1)
			continue
	brikear(("Error xpath: %s" % xpath))

def retryElementID(idpath):
	for i in range(0,50):
		try:
			element = driver.find_element_by_id(idpath)
			return element
		except Exception as e:
			time.sleep(0.1)
			continue
	brikear(("Error ID: %s" % idpath))

def retryElementNAME(namepath):
	for i in range(0,50):
		try:
			element = driver.find_element_by_name(namepath)
			return element
		except Exception as e:
			time.sleep(0.1)
			continue
	brikear(("Error NAME: %s" % namepath))

def brikear(msg):
	print(msg)
	closeDriver()
	sys.exit(1)

def closeDriver():
	global driver
	driver.quit()

try:
	mainExe()
except Exception as e:
	print(e)
	closeDriver()