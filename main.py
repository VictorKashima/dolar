#ARQUIVO PRINCIPAL.
#EXECUTE ESTE ARQUIVO.
from DataCerta import data, diasemana
from DolarCerto import dolar
from HoraCerta import hora

sett = ''

def linha():
    print('- '*20)

while True:
    linha()
    print('$ COTAÇÃO DO DÓLAR EM TEMPO REAL $')
    linha()

    sett = int(input('DIGITE 1 PARA COTAÇÃO DO DÓLAR.\nDIGITE 2 PARA CONVERTER DÓLAR.\nDIGITE 3 PARA SAIR.\n'))
    linha()

    if sett == 1:
        print(f'COTAÇÃO DO DÓLAR DIA {data}, {diasemana}-feira.')
        print(f'HORÁRIO: {hora}')
        print(f'1$ = R${dolar}')

    elif sett == 2:
        set2 = int(input('DIGITE 1 PARA CONVERTER DÓLAR PARA REAL.\nDIGITE 2 PARA CONVERTER REAL PARA DÓLAR.\n'))
        linha()
        if set2 == 1:
            dol = float(input('DIGITE O VALOR EM DÓLAR:'))
            dr = dol*dolar
            linha()
            print(f'{dol}$ equivale a R${dr:.2f}.')
        elif set2 == 2:
            r = float(input('DIGITE O VALOR EM REAIS:'))
            rd = r/dolar
            linha()
            print(f'R${r} equivale a {rd:.2f}$')
        else:
            print('POR FAVOR, DIGITE 1 OU 2')
    elif sett == 3:
        print('PROGRAMA ENCERRADO')
        break
    else:
        print('POR FAVOR, DIGITE 1 OU 2')