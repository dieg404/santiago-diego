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

# segunda funcion
def contador(lista):
    return len(lista)


#tercera funcion
def posicion(lista,n):
   i=0
   if n<= len(lista):
        for i in range(len(lista)):
            if i==n:
              return lista[n]
   else:
       return "Posicion fuera de rango"
        

# Cuarta funcion: Verificar si la variable ingresada está en la lista





