import lxml.html as LH
import requests
import pandas as pd
def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')

url = 'http://www.sify.com/finance/gold-rates-in-hyderabad/'
r = requests.get(url)
root = LH.fromstring(r.content)

for table in root.xpath('//*[@id="middle"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[1]/td[2]'):

    header = [text(tbody) for tbody in table.xpath('//tbody')]        # 1
    data = [[text(td) for td in tr.xpath('td')]
            for tr in table.xpath('//tr')]                   # 2
    data = [row for row in data[0] if len(row)==len(header)]    # 3
    data = pd.DataFrame(data, columns=header)                # 4

    print(data)

