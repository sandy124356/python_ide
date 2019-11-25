from selenium import webdriver
import re
import ctypes
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
#driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)


browser = webdriver.Chrome()
browser.get('https://www.naukri.com/nlogin/logout')

#shoe= browser.find_element_by_xpath('//*[@id="mountRoot"]/div/div/main/div[2]/div[2]/div[1]/p[1]/span[1]/strong/').text




login_id=browser.find_element_by_xpath('//*[@id="usernameField"]')

password_id=browser.find_element_by_xpath('//*[@id="passwordField"]')


login_id.send_keys("nemmalurisanthosh@yahoo.com")
password_id.send_keys("Ammu@123")


submitButton = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
submitButton.click()

#browser.find_element_by_link_text("My Naukri").click()

browser.get('https://www.naukri.com/mnjuser/profile?id=&altresid')

"""

shoe_xpath=browser.find_element_by_xpath('//*[@id="mountRoot"]/div/div/main/div[2]/div[2]/div[1]/p[1]/span[1]/strong').text

print('hello', shoe_class_id)

print('kello', shoe_xpath)

print ('finally its here',re.findall("\d+", shoe_class_id))

price=int(re.findall("\d+", shoe_class_id)[0])

if (price < 1400):
    print("Right time to buy your shoe is today/Now :-) ",price )
    msg='Right time to buy your shoe is today/Now :-) '+str(price)
else:
    print ("wait... don't buy as your shoe price is high: :-( ",price)
    msg = "wait... don't buy as your shoe price is high: :-( " + str(price)


ctypes.windll.user32.MessageBoxW(0, msg, "Alert", 0x1000)

"""