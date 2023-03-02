# Przejdź na stronę https://pyformat.info/ a następnie zapisz w oddzielnym
# pliku .py i wykonaj 5 wybranych przykładów formatowania ciągów oznaczonego
# jako „New”, których nie było w przykładach z tego podrozdziału
# (np. z wyrównaniem do prawej lub lewej strony, ilością pozycji liczby,
# znakiem, wypełnieniem spacji itp.). Przerób zaprezentowane tam przykłady
# tak, żeby korzystały z zapisu w postaci f-string.

napis = "DOMINIK"
liczba = 42

print(f"{napis:>10}")  # 1
print(f"{liczba:-<10}")  # 2
print(f"{napis:^11}")  # 3
print(f"{liczba:=^10}")  # 4
print(f"{napis:!^15}")  # 5
