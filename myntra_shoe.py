import lxml.html as LH
import requests
import ctypes
import xlwt
from datetime import datetime
import openpyxl
from selenium import webdriver

from xlwt import Workbook
#from xlutils.copy import copy
#import pandas as pd
def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')


headers = {
    'User-Agent': 'Mozilla/5.0',
    'From': 'santhoshpiggychops@gmail.com'  # This is another valid field
}



browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
url = 'https://www.myntra.com/sports-shoes/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-blue--black-colourblocked-running-shoes/2524413/buy?mini=true&qty=1&size=8'
rr = browser.get(url) #navigate to the page


r = requests.get(url,headers=headers)
print(r.content)
root = LH.fromstring(rr.content)

print("root is",root)



print(type(root))
print("before finding tr_elements")
tr_elements = root.xpath('//*[@id="mountRoot"]/div/div/main/div[2]/div[2]/div[1]/p[1]/span[1]/strong/text()')



print("tr elemts are ",tr_elements)

col=[]
i=0
#For each row, store each first element (header) and an empty list
for t in tr_elements:
    print("in loop")
    rate=t.text_content().replace(u'\xa0', u' ')
    msg='cost of my shoe is'+rate
    print ('cost of my shoe is"%s"'%(msg))

ctypes.windll.user32.MessageBoxW(0, 222, "Alert", 0x1000)