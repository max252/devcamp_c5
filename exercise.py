#!/usr/bin/python3

# Exercise 1
# Cree un bucle For de Python.
for x in range(100):
    print(x)


# Exercise 2
# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def sum(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


# Exercise 3
sum_l = lambda arg1, arg2, arg3: arg1 + arg2 + arg3

# Exercise 4
nombre = "Enrique"
# nombre = "Paul"
lista_nombre = "Jessica", "Paul", "George", "Henry", "Adán"

if nombre in lista_nombre:
    have = "in"
else:
    have = "not in"

print(f"Nomber: {nombre} {have} list: {lista_nombre}")
