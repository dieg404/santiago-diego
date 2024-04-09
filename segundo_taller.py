# primera funcion: Mostrar el menú de las opciones de lista

def ml(): #ml -> "Menú Lista"
   print('1. "Imprimir menú de las opciones de lista.')
   print('2. "Contar los elementos totales que tiene una lsita.')
   print('3. "Mostrar un elemento de una posicione en especifica de la lista."')
   print('4. "Verificar si la variable ingresada está en la lista."')
   print('5. "Mostrar todos los elemntos de la lista."')
   print('6. "Agregar nuevo elemento a una lista."')
   print('7. "Sacar un elemento especifico de la lista."')
   print('8. "Sacar un elemento de una posicion en especifico."')
   print('9. "Concantenar dos listas."')
   print('10. "Remplazar algun elemento de la lista."')    

# segunda funcion: Contar cuantos elementos se encunetran en una lista
def contador(lista):
    return len(lista)

#tercera funcion: Identificar en que posicion se encuentra un elemento
def posicion(lista,n):
   i=0
   if n<= len(lista):
        for i in range(len(lista)):
            if i==n:
              return lista[n]
   else:
       return "Posicion fuera de rango"
        
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

# Novena Funcion:         