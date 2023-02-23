# Przygotuj 4 przykłady kodu, który będzie wykorzystywał operatory bitowe.

# Przykład 1: operator &, AND
and_a = 60  # 0011 1100
and_b = 13  # 0000 1101
and_c = and_a & and_b  # 0000 1100
print("Operator AND", and_c)

# Przykład 2: operator |, OR
or_a = 60  # 0011 1100
or_b = 13  # 0000 1101
or_c = or_a | or_b  # 0011 1101
print("Operator OR", or_c)

# Przykład 3: operator ^, XOR
xor_a = 60  # 0011 1100
xor_b = 13  # 0000 1101
xor_c = xor_a ^ xor_b  # 0011 0001
print("Operator XOR", xor_c)

# Przykład 4: operator <<, przesunięcie w lewo
leftBit_a = 60  # 0011 1100
leftBit_b = leftBit_a << 2  # 1111 0000
print("Operator << (Przesuniecie bitowe w lewo)", leftBit_b)
