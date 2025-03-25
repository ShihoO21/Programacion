# Datos con mas informacion

# Lista class list
# Son conjutos de datos ordenados y mutables
# Pueden almacenar distintos tipos de datos (str, bool, int, float, etc)
# Se puede acceder a los valores de la lista por su indice, comenzando por el 0

# Todos los elementos de una lista van dentro de corchetes
print("tipos de datos LISTA")
lista = ["Aquiles Baeza", True, 45]
print(lista)
print(type(lista))

#Para cada elemento de manera individual usar valores numericos, primero siempre es 0
print(lista[0])
print(lista[1])
print(lista[2])
# se pueden modificar los datos de las listas
lista[1] = False
print(lista)

# Diccionarios
# son pares de datos ordenados, nombres de un dato y valor de un dato class dic
# se pueden acceder a las listas por su nombre
print("tipos de datos DICCIONARIO")
diccionario = {
    "nombre" : "Alan Brito Delgado", 
    "estudiante" : False,
    "edad" : 21
}
print(diccionario)
print(type(diccionario))
print(diccionario["edad"])

diccionario["edad"] = 22
print(diccionario["edad"])

# Conjuntos, set de datos que tiene elementos pero no tiene orden y no se pueden cambiar, pero se pueden agregar elementos class set
# Son conjuntos de pares de datos desordenador
# podemos agregar nuevos elementos 
print("tipos de datos CONJUNTO")
conjunto = {2, "Sebastian Parra", True}
print(conjunto)
print(type(conjunto))

conjunto.add("Jaime Rios")
print(conjunto)
conjunto.pop() #eliminar ultimo elemento
print(conjunto)

# Tuplas, es un set de datos inmutable, estan ordenas y no se pueden agregar ni cambiar los elementos class tuple
print("tipos de datos TUPLA")
tupla = ("Armando Casas", False, 45)
print(tupla)
print(type(tupla))

# tupla[0] = "Jose Feliciano"
# print(tupla)

