# Zadanie 2
# Połącz te listy ponownie. Dodaj do listy wartość „0” na początku.
# Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.

from Zadanie01 import lista1, lista2

# połączenie list i dodanie 0 na początku
nowa_lista = [0] + lista1 + lista2
print(nowa_lista)
# utworzenie kopii połączonej listy i posortowanie malejąco
kopia_lista = nowa_lista.copy()
kopia_lista.sort(reverse=True)

# wyświetlenie posortowanej listy
print(kopia_lista)
