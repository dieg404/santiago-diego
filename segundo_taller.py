import random

# primera funcion: Mostrar el menú de las opciones de lista
def ml(): #ml -> "Menú Lista"
   print('1. "Contar los elementos totales que tiene una lista.')
   print('2. "Mostrar un elemento de una posicione en especifica de la lista."')
   print('4. "Verificar si la variable ingresada está en la lista."')
   print('5. "Mostrar todos los elemntos de la lista."')
   print('6. "Agregar nuevo elemento a una lista."')
   print('7. "Sacar un elemento especifico de la lista."')
   print('8. "Sacar un elemento de una posicion en especifico."')
   print('9. "Concantenar dos listas."')
   print('10."Remplazar algun elemento de la lista."')    

# segunda funcion: Contar cuantos elementos se encunetran en una lista
def contador(lista_a):
   return len(lista_a)

#tercera funcion: Identificar en que posicion se encuentra un elemento
def posicion(lista_a,n):
   i=0
   if n<= len(lista_a):
        for i in range(len(lista_a)):
            if i==n:
              return f"fue encontrando en posicion {lista_a[n]}"
   else:
       return "se encuentra fuera de rango"
        
# Cuarta funcion: Verificar si la variable ingresada está en la lista
def elemento(lista,m):
  i=1
  for i in lista: 
    if (i==m):
      return "fue encontrado en la lista"
  return "no se encuentra en la lista"    

# Quinta Funcion: Imprimir elementos de una lista        
def impresion(lista):
   return lista

# Sexta Funcion: Agregar elementos a una lista
def agregar(lista,n):
  i=1
  for i in range(n):
    m=int(input("Ingrese el nuevo elemento a la lista: "))
    lista.append(m)
  return lista  

# Septima Funcion: Eliminar elemento de un lista
def eliminar_elemento(lista,x):
  i=1
  for i in lista: 
    if i==x:
      lista.remove(i)
      return  f"fue borrado {lista}"
  return "no fue encontrado"

# Octava Funcion: Eliminar elemento de una lista por su posicion
def eliminacion_posicion(lista,x):
   if x<=len(lista):
      del lista[x]
      return f"fue eliminada {lista}"
   else:
      return "se encuentra fuera del rango"

# Novena Funcion: Concatenacion de dos listas
def concatenar(lista_a,lista_b):
   lista_a.extend(lista_b)
   return lista_a

# Decima Funcion: Remover elemento y agregar elemento nuevo
def remover_añadir(lista,a):
   if a<=len(lista):


    b=int(input("Ingrese el elemento que desea añadir: "))
    lista[a]= b
    return lista
   else:
      return "Posicion fuera de rango"
   
# Onceava Funcion: Implementacion de todas las funciones
def implementacion(x):
   if x==1:
      print(f"El numero de elementos que se encuentran en la lista A son {contador(lista_a)}")
   if x==2:
      n=int(input("Ingrese la posicion del elemento que desea saber: "))
      print(f"El elemento {n} {posicion(lista_a,n)}")




# Inicio de codigo
lista_a=[]
lista_b=[]
a=int(input("Ingrese cuantos datos desea ingresar para la lista A: "))
b=int(input("Ingrese cuantos datos desea ingresar para la lista B: "))
#Bucles para la creacion de las listas con numeros asignados por el sistema
for i in range(a+1):
   x=random.randint(1,20)
   lista_a.append(x)
for i in range(b+1):
   x=random.randint(1,20)
   lista_b.append(x)
#Fin de bucles creacion de listas

ml()
x=int(input("Ingrese la opcion que desea: ")) 
implementacion(x)          