sk = int(input('Skaicius'))

laimingas = (sk>=5 and sk<=10) or (sk>=20 and sk<=25)
if laimingas :
    print(f'skaicius {sk} laimingas')
else :
    print(f'skaicius {sk} nelaimingas')
