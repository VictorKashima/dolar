#CAPTAR DATA EM TEMPO REAL
from requests import get
from bs4 import BeautifulSoup as bs
import html5lib

h = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 OPR/85.0.4341.18'}

url = get('https://www.wikidates.org/br/data-de-hoje.html', headers=h)
page = bs(url.content, 'html5lib')
d = page.find('p')
da = d.text
dat = da.replace('• A data de hoje: ', '')
data = dat.replace('.', '')


diaid = page.find(id="dmenudate")
dias = diaid.text
diase = dias[:3]

if diase == 'seg':
    diasemana = 'Segunda'
elif diase == 'ter':
    diasemana = 'Terça'
elif diase == 'qua':
    diasemana = 'Quarta'
elif diase == 'qui':
    diasemana = 'Quinta'
elif diase == 'sex':
    diasemana = 'Sexta'
elif diase == 'sab':
    diasemana = 'Sábado'
elif diase == 'dom':
    diasemana = 'Domingo'
else:
    diasemana = 'Não identificado'