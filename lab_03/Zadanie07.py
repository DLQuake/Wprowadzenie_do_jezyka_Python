# Zadanie 7
# Wykorzystaj moduł string i następnie:
# - wczytaj ze standardowego wejścia dowolny łańcuch znaków,
# - używając formatowania znaków wyświetl ile oraz jaki % znaków
# (zamienionych na małe litery) z wprowadzonego tekstu pokrywa się
# z: string.ascii_lowercase, string.digits.

import string

input_string = input("Wprowadź dowolny tekst: ")

lowercase_set = set(string.ascii_lowercase)
digit_set = set(string.digits)

formatted_input = input_string.lower()

formatted_set = set(formatted_input)

lowercase_matches = formatted_set & lowercase_set
digit_matches = formatted_set & digit_set

lowercase_percent = len(lowercase_matches) / len(formatted_set) * 100
digit_percent = len(digit_matches) / len(formatted_set) * 100

print("Znaków małych liter jest {:.2f}% ({}/{})".format(lowercase_percent, len(lowercase_matches), len(formatted_set)))
print("Znaków cyfr jest {:.2f}% ({}/{})".format(digit_percent, len(digit_matches), len(formatted_set)))
