# Converte da Fahrenheit a Celsius e Kelvin
#
# versione 0.2 - Pietro IZ2RPN 2022
#
# use: python3 convert.py 12.4 50.9
# converte più di un valore alla volta.

import sys

temperatura = sys.argv[1:]
i=0

def convert(temp):
    c = 5/9*(temp-32)
    k = c + 273.15
    risultato = (f'Celsius: {round(c,2)} Kelvin: {round(k,2)}')
    return risultato

while i < len(temperatura):
    try:
        float(temperatura[i])
        print(f"{temperatura[i]} Fahrenheit = " + convert(float(temperatura[i])))
        i += 1
    except ValueError:
        print(f"'{temperatura[i]}' This is not a number")
        i += 1
