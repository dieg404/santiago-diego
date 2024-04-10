import random

# primera funcion: Mostrar el menú de las opciones de lista
def ml(lista_a,lista_b): #ml -> "Menú Lista"
   print('\n1. Contar los elementos totales que tiene una lista.')
   print('2. Mostrar un elemento de una posicion especifica de la lista.')
   print('3. Verificar si la variable ingresada está en la lista.')
   print('4. Mostrar todos los elementos de la lista.')
   print('5. Agregar nuevo elemento a una lista.')
   print('6. Sacar un elemento especifico de la lista.')
   print('7. Sacar un elemento de una posicion en especifico.')
   print('8. Concantenar dos listas.')
   print('9. Remplazar algun elemento de la lista.\n')
   print(f"Lista A\t\t\t\tLista B\n{lista_a}\t\t{lista_b}")    

# segunda funcion: Contar cuantos elementos se encunetran en una lista
def contador(lista_a):
   return len(lista_a)

#tercera funcion: Identificar en que posicion se encuentra un elemento
def posicion(lista_a,n):
   i=0
   if n<= len(lista_a):
        for i in range(len(lista_a)):
            if i==n:
              return f"fue encontrando el elemento {lista_a[n]}"
   else:
       return "se encuentra fuera de rango"
        
# Cuarta funcion: Verificar si la variable ingresada está en la lista
def elemento(lista_a,n):
  i=1
  for i in lista_a: 
    if (i==n):
      return "fue encontrado en la lista"
  return "no se encuentra en la lista"    

# Quinta Funcion: Imprimir elementos de una lista        
def impresion(lista_a):
   return lista_a

# Sexta Funcion: Agregar elementos a una lista
def agregar(lista_a,n):
  for i in range(n):
    m=int(input("Ingrese el nuevo elemento a la lista: "))
    lista_a.append(m)
  return lista_a  

# Septima Funcion: Eliminar elemento de un lista
def eliminar_elemento(lista,n):
  i=1
  for i in lista_a: 
    if i==n:
      lista.remove(i)
      return  f"fue borrado {lista_a}"
  return "no fue encontrado"

# Octava Funcion: Eliminar elemento de una lista por su posicion
def eliminacion_posicion(lista_a,n):
   if n<=len(lista_a):
      del lista_a[n]
      return f"fue eliminada {lista_a}"
   else:
      return "se encuentra fuera del rango"

# Novena Funcion: Concatenacion de dos listas
def concatenar(lista_a,lista_b,lista_nueva):
   lista_nueva=lista_a+lista_b
   return sorted(lista_nueva)

# Decima Funcion: Remover elemento y agregar elemento nuevo
def remover_añadir(lista_a,n):
   if n<=len(lista_a):
    b=int(input("Ingrese el elemento que desea añadir: "))
    lista_a[n]= b
    return lista_a
   else:
      return "Posicion fuera de rango"
   
# Onceava Funcion: Implementacion de todas las funciones
def implementacion(x):
   if x==1:
      print(f"El numero de elementos que se encuentran en la lista A son {contador(lista_a)}")
   elif x==2:
      n=int(input("Ingrese la posicion del elemento que desea saber: "))
      print(f"En la posicion {n} {posicion(lista_a,n)}")
   elif x==3:
      n=int(input("Ingrese el elemento que desea saber si se encuentra en la lista: "))
      print(f"El elemento {n} {elemento(lista_a,n)}")
   elif x==4:
      print(impresion(lista_a))
   elif x==5:
      n=int(input("¿Cuantos elementos desea ingresar?: "))
      print(f"Los elementos fueron ingresados {agregar(lista_a,n)}")
   elif x==6:
      n=int(input("Ingrese el elemento que desea eliminar de la lista: "))
      print(f"El elemento {n} {eliminar_elemento(lista_a,n)}")
   elif x==7:
      n=int(input("Ingrese la posicion del elemento que desea eliminar de la lista: "))
      print(f"La posicion {n} {eliminacion_posicion(lista_a,n)}")
   elif x==8:
      print(f"La concatenacion de las listas A y B generaron {concatenar(lista_a,lista_b,lista_nueva)}")
   elif x==9:
      n=int(input("Ingrese la posicion que desea remplazar de la lista: "))
      print(f"El elemento en la posicion {n} fue remplazado {remover_añadir(lista_a,n)} ")


# Inicio de codigo
lista_a=[]
lista_b=[]
lista_nueva=[]
opcion=int(input("Desea rellenar la lista manualmente '1' o automaticamente '2': "))
if (opcion==1):
   a=int(input("Ingrese cuantos datos desea ingresar para la lista A: "))
   b=int(input("Ingrese cuantos datos desea ingresar para la lista B: "))
    #Bucles para la creacion de las listas con numeros asignados por el sistema
   for i in range(a):
      lista1=int(input("Ingrese el elemento a la lista A: "))
      lista_a.append(lista1)
   for i in range(b):
      lista2=int(input("Ingrese el elemento a la lista B: "))
      lista_b.append(lista2)
   #Fin de bucles creacion de listas
elif (opcion==2):
   a=int(input("Ingrese cuantos datos desea ingresar para la lista A: "))
   b=int(input("Ingrese cuantos datos desea ingresar para la lista B: "))
   #Bucles para la creacion de las listas con numeros asignados por el sistema
   for i in range(a):
      x=random.randint(1,20)
      lista_a.append(x)
   for i in range(b):
      x=random.randint(1,20)
      lista_b.append(x)
   #Fin de bucles creacion de listas

ml(lista_a,lista_b)
x=int(input("Ingrese la opcion que desea: "))
while x<=0 or x>9:
   print("Opcion no valida")
   x=int(input("Ingrese la opcion que desea: "))
        
implementacion(x)         