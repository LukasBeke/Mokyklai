#nenaudoti min ir max
# duoti 4 skaiciai, rasti didziausia ir maziausia

a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
d = int(input('d= '))

if a>=b and a>=c and a>=d:
    did = a
elif b>=c and b>=d:
    did = b
elif c>=d:
    did = c 
else:
    did = d

print(f'Didziausias skaicius = {did}')

