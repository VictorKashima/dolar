#CAPTAR VALOR DO DOLAR EM TEMPO 
from requests import get
from bs4 import BeautifulSoup as bs
import html5lib 

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

link = get('https://www.melhorcambio.com/dolar-hoje', headers=headers)
page = bs(link.content, 'html5lib')

dol = page.find('input', attrs={'id': 'comercial'})
doleta = (dol['value'])
dolar = float(doleta.replace(',', '.'))