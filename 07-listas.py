lista1 = ["Daniel", 25, 9, True, "Nachez", 20.7]

print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])
print(lista1[0:3])
print(lista1[3:])

lista1.append("Vargas") #agregar 1
print(lista1)

lista1.insert(2, "Nadia") #agregar 2 veces el valor
print(lista1)

lista1.extend(["uno", 1.1, False]) #agregar varias 
print(lista1)

lista1.remove(25) #borrar el seleccionado
print(lista1)

lista1.pop() #borrar el ultimo
print(lista1)

lista2 = ["tres", "cuatro"]
lista3 = lista1 + lista2 #sumar listas
print(lista3)

print(lista2 * 4)
lista4 = [2, 1, 5, 4, 3]
print(lista4)
lista4.sort()
print(lista4)
