# Zadanie 1
# Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak,
# aby pierwsze 5 liczb zostało w oryginalnej liście a pozostałe 5
# znalazło się w nowej liście.

# tworzenie listy
lista = list(range(1, 11))

# dzielenie na dwie listy
lista1 = lista[:5]
lista2 = lista[5:]

# wyświetlenie list
print(lista1)
print(lista2)
