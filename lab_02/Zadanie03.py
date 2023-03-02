# Korzystając ze zmiennej z zadania 2 wyświetl na konsoli tekst postaci:
# „W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter
# {litera_2}”. W miejsca {liczba_liter1} oraz {liczba_liter2} podstaw zmienne,
# które będą przechowywały liczbę wystąpień danych liter (poszukaj odpowiedniej
# metody dla typu str). Litery, które należy wyszukać to 4-ta litera nazwiska
# oraz 3-cia litera imienia osoby wykonującej ćwiczenie, np. imie = „Jan”,
# nazwisko = „Kowalski”, litera_1 = imie[2], litera_2 = nazwisko[3].

# Importuje zmienna `tekst` z pliku Zadanie02.py
from Zadanie02 import tekst

# Utworzenie zmiennych przechowujących imię i nazwisko
imie = "Dominik"
nazwisko = "Lewczyński"

# Utworzenie zmiennych przechowujących 3-cią literę imienia oraz 4-tą literę nazwiska
litera_1 = imie[2]
litera_2 = nazwisko[3]

# Utworzenie zmiennych które przechowują ilość wystąpień litera_1 i litera_2
liczba_liter1 = tekst.count(litera_1)
liczba_liter2 = tekst.count(litera_2)

# wypisanie wyniku
print(f'W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}')
