#lista
lista = ["David","Salomon","Juan"] #crea lista, posiciones empieza en 0
print(lista) #impprime
lista.append("Pedro") #agrega al final de la lista
print(lista)
lista.pop() #elimina el ultimos, es decir, pedro
print(lista)
personaje_biblico=input("Digite un persona biblico: ") #agrega una variable agregada por el usuario
lista.append(personaje_biblico)
lista.append(200000) #se pueden agregar varios tipos de variables en una lista
print(lista) 
lista.pop(2) #pop segun el indice, borra al de la posicion 3
print(lista)
lista.remove("Salomon") #remove segun una variable
print(lista) 

#lista borra ejemplo con input
personajes_biblicos = ["Juan", "Job","Pedro","Jonas"]
for personaje in personajes_biblicos:
   print(personaje)
borrar=input("Digite el personaje que desea borrar: ")
if borrar in personajes_biblicos:
   personajes_biblicos.remove(borrar)
   print(personajes_biblicos)
else:
   print("No conozco ese personaje")


#practica
productos=[]
cantidades=[]
opcion=""
while opcion != "4":
   print("Bienvenido al supermercado")
   print("1. Agregar producto")
   print("2. Ver inventario")
   print("3. Remover producto")
   print("4. Salir")
   opcion=input("Digite su opcion: ")
   match opcion:
      case "1":
         producto=input("Digite el producto: ").upper()
         if producto != "SALIR":
            cantidad=int(input("Digite la cantidad de dicho producto: "))
            productos.append(producto)
            cantidades.append(cantidad)
      case "2":
         for producto in productos:
            indice=productos.index(producto)
            print(producto,cantidades[indice])
      case "3":
         producto=input("Digite el producto a eliminar: ").upper()
         if producto in productos:
            indice=productos.index(producto)
            productos.remove(producto)
            cantidades.pop(indice)
         else:
            print("Por favor valide el inventario no encontre el producto")
      case "4":
         print("Hasta luego...")
      case _:
         print("Opcion invalida")

