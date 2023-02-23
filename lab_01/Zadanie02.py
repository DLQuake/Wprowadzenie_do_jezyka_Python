# Napisz kod, w którym wykorzystasz poniższe metody dla typów:
# int.bit_count()
# float.is_integer()

# Wykorzystanie metody bit_count() dla typu int
int_obj = 100 # 0110 0100
print(int_obj.bit_count())  # 3

# Wykorzystanie metody is_integer() dla typu float
float_obj1 = 3.0
float_obj2 = 3.14
print(float_obj1.is_integer())  # True
print(float_obj2.is_integer())  # False
