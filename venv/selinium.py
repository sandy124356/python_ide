from selenium import webdriver
import re
import ctypes
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
#driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)


browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.myntra.com/sports-shoes/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-blue--black-colourblocked-running-shoes/2524413/buy?mini=true&qty=1&size=8')

#shoe= browser.find_element_by_xpath('//*[@id="mountRoot"]/div/div/main/div[2]/div[2]/div[1]/p[1]/span[1]/strong/').text

shoe_class_id=browser.find_element_by_class_name('pdp-price').text

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