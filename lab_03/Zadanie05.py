# Zadanie 5
# Stwórz podobny słownik jak w zadaniu 1, ale z angielskimi nazwami miesięcy.
# Połącz teraz słowniki tak, żeby przykładowo dla kwietnia, dostać się poprzez
# wyrażenie: months['pl'][4] a dla wersji angielskiej poprzez months['en'][4].

from Zadanie04 import miesiace

# stworzenie słownika z angielskimi nazwami miesięcy
miesiace_en = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

# połączenie słowników
miesiace_polaczone = {'pl': miesiace, 'en': miesiace_en}
# print(miesiace_polaczone)

# wyświetlenie przykładowych wartości
print(miesiace_polaczone['pl'][4])
print(miesiace_polaczone['en'][4])
