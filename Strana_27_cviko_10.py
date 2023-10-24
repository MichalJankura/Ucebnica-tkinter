"""Pomocou for cyklu napíšte do okna shell:
a) všetky párne čísla od 20 do 40,
b) všetky nepárne čísla od 20 do 40."""

"""a) všetky párne čísla od 20 do 40"""
print("---Začiatok párnych čísel---")
for i in range(20, 41):
    if i % 2 == 0:
        print(i)
print("---Koniec párnych čísel---\n")
"""b) všetky nepárne čísla od 20 do 40"""

print("---Začiatok nepárnych čísel---")
for i in range(20, 41):
    if i % 2 != 0:
        print(i)
print("---Koniec nepárnych čísel---")
