
karosuvienetai=int(input('Karosu vienetai'))
karosusvoris=float(input('Vieneto svoris'))
bendraskarosusvoris=karosuvienetai * karosusvoris
print('Bendras karosu svoris'f'{bendraskarosusvoris}''kg')

eseriuvienetai=int(input('Eseriu vienetai'))
eseriusvoris=float(input('Vieneto svoris'))
bendraseseriusvoris=eseriuvienetai * eseriusvoris
print('Bendras eseriu svoris'f'{bendraseseriusvoris}''kg')

auksliuvienetai=int(input('Auksliu vienetai'))
auksliusvoris=float(input('Vieneto svoris'))
bendrasauksliusvoris=auksliuvienetai * auksliusvoris
print('Bendras auksliu svoris'f'{bendrasauksliusvoris}')

z = bendraskarosusvoris + bendraseseriusvoris + bendrasauksliusvoris
print('Bendras svoris'f'{z}''kg')