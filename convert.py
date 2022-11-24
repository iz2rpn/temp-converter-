import sys

temperatura = sys.argv[1]

def convert(temp):
    c = 5/9*(temp-32)
    k = c + 273.15
    risultato = (f'Celsius: {round(c,2)} Kelvin: {round(k,2)}')
    return risultato
try:
    float(temperatura)
    print(convert(float(temperatura)))
except ValueError:
    print("This is not a number")
