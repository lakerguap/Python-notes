import random
def genera_numero_casuale():
    return random.random()

numero_casuale = genera_numero_casuale()
print(f"numero casuale generato: {numero_casuale}")

import random

def genera_numeri_random_compresi():
    a = float(input("inserisci a: "))
    b = float(input("inserisci b: "))
    return random.uniform(a, b)

numeri_random_compresi = genera_numeri_random_compresi()
print(numeri_random_compresi)

import random

def genera_numeri_randomici_range():
    return random.randrange(0, 10 ,2)
