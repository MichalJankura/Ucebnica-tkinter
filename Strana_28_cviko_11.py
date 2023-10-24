"""Pomocou for cyklu napíšte do okna shell tieto čísla:
a) 1, 2, 4, 8, 16, 32, 64, 128, 256, 512,
b) 3, 2, 1, 0, -1, -2, -3"""

"""RIEŠENIE PRE VÝPIS NA JEDEN RIADOK AKO JE V ZADANÍ MOŽNÉ + ALEBO 1TKA"""

print("a)",end=' ')
for i in range(1, 10):
    print(2 ** i, end=' ,')

print("\nb)",end=' ')
for i in range(3, -4, -1):
    print(i,end=' ,')

"""RIEŠENIE PRE VÝPIS POD SEBA JEDNODUCHÁ METÓDA"""
for i in range(1, 10):
    print(2 ** i)

for i in range(3, -4, -1):
    print(i)


