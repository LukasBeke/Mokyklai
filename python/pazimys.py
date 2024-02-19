# Reikia patikrinti ar ivestas blogas(neegzistuojantis) pazimys.
# -beg - 0 ir nuo 11 iki BEG

pazimys = int(input('Pazimys'))
if pazimys <=0 or pazimys >=11:
    print(f'{pazimys} negalimas, kartokite ivedima')
    pazimys = int(input('pazimys = '))
print('pazimys = ' +str(pazimys))