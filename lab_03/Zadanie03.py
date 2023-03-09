# Zadanie 3
# Napisz skrypt, który pobierze dowolny tekst ze standardowego wejścia
# poprzez funckję input(). Następnie wyświetl ciąg unikalnych znaków
# z wczytanego zdania, zapisanych alfabetycznie małymi literami.

# pobranie tekstu
tekst = input("Wprowadź dowolny tekst: ")

# stworzenie zbioru unikalnych znaków
unikalne_znaki = sorted(set(tekst.lower()))

# wyświetlenie unikalnych znaków
print(unikalne_znaki)
