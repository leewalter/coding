# very simple code to scrape Wells Fargo Mortgage Rates from html table
# ref - https://github.com/engineer-man/youtube/tree/master/042
import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('https://www.wellsfargo.com/mortgage/rates/')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

# XPath //*[@id="PurchaseRatesTable"]
mortgagetable = soup.find('table', { 'id': 'PurchaseRatesTable' })
tbody = mortgagetable.find('tbody')
print ("%-30s %10s %10s" % ("productName", "intRate", "AprRate"))

for tr in tbody.find_all('tr'):
    try:
        productName = tr.find_all('th')[0].find_all('a')[0].text.strip()
        intRate = tr.find_all('td')[0].text.strip()
        AprRate = tr.find_all('td')[1].text.strip()
        # print(productName,"\t\t", intRate,"\t", AprRate)
        print ("%-30s %10s %10s" % (productName, intRate, AprRate))
    except IndexError:
        pass

'''
output: 
(base) D:\github\walter-repo\python\web-scape\>python wf-rates1.py
productName                       intRate    AprRate
30-Year Fixed Rate                 4.375%      4.48%
30-Year Fixed-Rate VA              4.375%     4.696%
20-Year Fixed Rate                  4.25%     4.394%
15-Year Fixed Rate                 3.875%     4.038%
7/1 ARM                             4.25%     4.879%
5/1 ARM                            4.125%     4.947%
30-Year Fixed-Rate Jumbo             4.0%     4.064%
15-Year Fixed-Rate Jumbo            3.75%     3.827%
7/1 ARM Jumbo                      3.375%     4.415%
10/1 ARM Jumbo                      3.75%     4.347%
'''
