# para rodar em https://app.quickcode.io/

import scraperwiki
import csv
import requests
import urllib2
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import sys

sys.getdefaultencoding()
'utf-8'

url = "http://www.ibge.gov.br/home/estatistica/indicadores/pib/pib-vol-val_201604_1.shtm"


response = requests.get(url)
html = response.content

soup = BeautifulSoup(html.decode('UTF-8','ignore'))
table = soup.find('table', attrs={'class': 'tabela_acessivel'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;&nbsp;', '')
        text = cell.text.replace(',', '.')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("pib.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
