# Napisz fragment kodu, który wczyta trzy zmienne z klawiatury:
# linię danych rozdzielonych jakimś separatorem (spacja, średnik, itd.)
# separator źródłowy
# separator docelowy
# Następnie zaimplementuj z użyciem metod split oraz join podzielenie wejścia
# pierwszym separatorem, połączenie i wypisanie danych połączonych drugim
# separatorem. Czy można to zrobić prościej?

print("Pierwsza wersja z split() oraz join()")

line1 = input("Podaj linię danych: ")
source_sep1 = input("Podaj separator źródłowy: ")
target_sep1 = input("Podaj separator docelowy: ")

data1 = line1.split(source_sep1)
result1 = target_sep1.join(data1)
print(result1)


# Można prościej. Można np wykorzystać instrukcję replace()
print("Druga wersja Uproszczona")

line2 = input("Wprowadź linię danych: ")
source_sep2 = input("Wprowadź separator źródłowy: ")
target_sep2 = input("Wprowadź separator docelowy: ")

result2 = line2.replace(source_sep2, target_sep2)
print(result2)
