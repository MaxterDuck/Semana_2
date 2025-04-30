Taller Investigativo: Arrays en Python
1. *¿Qué es un array o lista en Python?*
- Son un tipo de dato fundamental que permite almacenar una colección ordenada de elementos de cualquier tipo  donde se pueden crear listas utilizando 
corchetes [] o la funcion list ().

-¿Cómo se declara una lista vacía?
Una lista vacia se puede declarar de 2 formas una solo utilizando los corchetes [] y otra utilizando la funcion list () dejandola vacia. 

-¿Cómo se crea una lista con valores iniciales? 
Una  lista con valores iniciales se puede declarar de la siguiente manera; la primera utilizando los corchetes [] y agregando contenido a esta como por 
*ejemplo* [1,2,3,4].Tambien de la siguiente manera se puede valores de diferentes tipos *ejemplo* ["manzana", 3.14, True, 42], Y si se quiere generar una lista de numeros de forma automatica se utiliza range() junto con list (): *ejemplo* list(range(1, 6)). 

2. *¿Cómo accedemos a los elementos de una lista?*
-¿Cómo se accede al primer elemento de una lista?
En python se puede acceder al primer elemento de una lista utilizando el indice 0 *ejemplo*
mi_lista = [10, 20, 30, 40]
primer_elemento = mi_lista[0]
print(primer_elemento)  # Salida: 10

-¿Qué significa usar un índice negativo?
Usar el indice negativo conlleva a mostrar el ultimo y el penultimo elemento; de tal manera esto sirve si no se sabe cuantos elementos hay y se  necesita trabajar con los ultimos. *Ejemplo* 
mi_lista = ['a', 'b', 'c', 'd']
print(mi_lista[-1])  # 'd' (último elemento)
print(mi_lista[-2])  # 'c' (penúltimo elemento)

-¿Qué pasa si intento acceder a un índice que no existe?
Si se intenta acceder a un elemento que no existe saldria el siguiente error llamado *INDEXERROR*. *Ejemplo* 
mi_lista = [1, 2, 3]
print(mi_lista[5])  # Esto genera un IndexError

3. *¿Qué es el "slicing" o rebanado de listas?*
- ¿Qué significa "slicing" en listas?
Slicing en listas de Python significa obtener una sublista a partir de una porción de la lista original. *Ejemplo* 
mi_lista = [10, 20, 30, 40, 50]
sublista = mi_lista[1:4]
print(sublista)  # [20, 30, 40]

-¿Cómo se obtiene una sublista usando slicing?
Para obtener una sublista usando slicing en Python, utilizas la sintaxis [inicio:fin], donde:
*inicio* es el índice donde comienza la sublista (incluido).
*fin* es el índice donde termina la sublista (no incluido).
*Ejemplo*
mi_lista = [10, 20, 30, 40, 50]
sublista = mi_lista[1:4]  # Desde el índice 1 hasta el 3 (índice 4 no incluido)
print(sublista)  # Salida: [20, 30, 40]

-¿Qué significa dejar vacío el inicio o el final en el slicing?
Dejar vacío el inicio ([ :fin]):
Si dejas vacío el índice de inicio en el slicing, se considera que quieres empezar desde el inicio de la lista.*Ejemplo*
mi_lista = [10, 20, 30, 40, 50]
sublista = mi_lista[:3]  # Desde el principio hasta el índice 2
print(sublista)  # Salida: [10, 20, 30]

Dejar vacío el final ([inicio:]):
Dejar vacío el final ([inicio:]):Si dejas vacío el índice final, se considera que quieres tomar los elementos desde el índice de inicio hasta el final de la lista.*Ejemplo*
mi_lista = [10, 20, 30, 40, 50]
sublista = mi_lista[2:]  # Desde el índice 2 hasta el final
print(sublista)  # Salida: [30, 40, 50]

4. *¿Cómo modificamos los elementos de una lista?*
-¿Cómo se cambia el valor de un elemento de la lista?
Para cambiar el valor de un elemento de una lista en Python, simplemente accedes a ese elemento utilizando su índice y le asignas un nuevo valor. *Ejemplo*
mi_lista = [10, 20, 30, 40, 50]
# Cambiar el valor del tercer elemento (índice 2)
mi_lista[2] = 99
print(mi_lista)  # Salida: [10, 20, 99, 40, 50]

-¿Cómo invertir una lista usando slicing?
Para invertir una lista en Python usando slicing, puedes usar la sintaxis [::-1], que significa:
:: Seleccionar toda la lista.
-1: El paso negativo indica que los elementos deben tomarse en orden inverso.
*Ejemplo*
mi_lista = [10, 20, 30, 40, 50]
lista_invertida = mi_lista[::-1]
print(lista_invertida)  # Salida: [50, 40, 30, 20, 10]

5. *¿Cómo agregamos nuevos elementos a una lista?*
-¿Cómo se agrega un elemento al final de la lista?
Para agregar un elemento al final de una lista en Python, puedes se puede usar  el método append(). Este método agrega un solo elemento al final de la lista sin modificar el orden de los elementos ya existentes.*Ejemplo*
mi_lista = [1, 2, 3]
mi_lista.append(4)  # Agrega 4 al final de la lista
print(mi_lista)  # Salida: [1, 2, 3, 4]

-¿Cómo se inserta un elemento en una posición específica?
Para insertar un elemento en una posición específica de una lista en Python, utilizamos el método insert(). Este método te permite especificar el índice donde deseas insertar el elemento, y lo hace desplazando los elementos que estaban en esa posición y en las posteriores.*Ejemplo*
mi_lista = [1, 2, 3, 5]
mi_lista.insert(3, 4)  # Inserta el número 4 en la posición 3
print(mi_lista)  # Salida: [1, 2, 3, 4, 5]

-¿Cómo se combinan dos listas en una sola?
Se pueden utilzar varias formas como por ejemplo utilizando el operador + *Ejemplo*.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_combinada = lista1 + lista2
print(lista_combinada)  # Salida: [1, 2, 3, 4, 5, 6]

Otra manera a utilzar es con el metodo extend() *Ejemplo*
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)  # Salida: [1, 2, 3, 4, 5, 6]

Y otra manera es utilizando un bucle. *Ejemplo*
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
for item in lista2:
    lista1.append(item)
print(lista1)  # Salida: [1, 2, 3, 4, 5, 6]
Esta ultima se utiliza cuando se quiere ser mas especifico. 

6. *¿Cómo eliminamos elementos de una lista?*
-Para eliminar un valor específico de una lista en Python, se puede utilizar el método remove(). Este método elimina la primera aparición del valor especificado. Si el valor no se encuentra en la lista, se lanza un ValueError.*Ejemplo*
mi_lista = [10, 20, 30, 40, 50]
# Eliminar el valor 30 de la lista
mi_lista.remove(30)
print(mi_lista)  # Salida: [10, 20, 40, 50]

-¿Qué hace el método pop()?
El método pop() en Python se usa para eliminar un elemento de una lista en una posición específica y devolverlo. Es útil cuando necesitas tanto remover un elemento como guardar su valor.*Ejemplo*
mi_lista = [10, 20, 30]
valor = mi_lista.pop()
print(valor)      # Salida: 30
print(mi_lista)   # Salida: [10, 20]

*Ejemplo 2* Eliminar un elemento especifico 
mi_lista = ['a', 'b', 'c', 'd']
letra = mi_lista.pop(1)  # Elimina el elemento en el índice 1
print(letra)      # Salida: 'b'
print(mi_lista)   # Salida: ['a', 'c', 'd']

-¿Cómo se elimina un elemento usando del?
Para eliminar un elemento de una lista usando la palabra clave del en Python, simplemente indicas el índice del elemento que deseas eliminar.*Ejemplo*
mi_lista = [10, 20, 30, 40, 50]
del mi_lista[2]  # Elimina el elemento en el índice 2 (valor 30)
print(mi_lista)  # Salida: [10, 20, 40, 50]

7. *¿Cómo buscamos elementos dentro de una lista?*
-¿Cómo se verifica si un elemento está presente en una lista?
Para verificar si un elemento está presente en una lista en Python, se utiliza el operador in. Este operador devuelve True si el elemento está en la lista, y False si no lo está.*Ejemplo*
frutas = ['manzana', 'banana', 'naranja']
# Verificar si 'banana' está en la lista
print('banana' in frutas)  # Salida: True
# Verificar si 'pera' está en la lista
print('pera' in frutas)    # Salida: False

-¿Cómo encontrar el índice de un elemento?
Para encontrar el índice de un elemento en una lista en Python, se utiliza el método index(). Este método devuelve el índice (posición) de la primera aparición del valor en la lista.*Ejemplo*
nombres = ['Ana', 'Luis', 'Carlos', 'Ana']
posicion = nombres.index('Ana')
print(posicion)  # Salida: 0 (porque 'Ana' aparece primero en el índice 0)
En caso tal de que se agregue un elemento que no exista este mandara un error 

-¿Cómo contar cuántas veces aparece un valor en la lista?
Para contar cuántas veces aparece un valor en una lista en Python, puedes usar el método count(). Este método devuelve el número de veces que un valor específico aparece en la lista.*Ejemplo*
numeros = [1, 2, 3, 2, 4, 2, 5]
veces = numeros.count(2)
print(veces)  # Salida: 3

8. *¿Cómo ordenamos los elementos de una lista?*
-¿Cómo se ordena una lista de manera ascendente?
Para ordenar una lista de manera ascendente en Python (de menor a mayor o alfabéticamente de A a Z),se puede usar:
✅ Opción 1: sort() – modifica la lista original
numeros = [5, 2, 9, 1]
numeros.sort()  # Ordena de menor a mayor
print(numeros)  # Salida: [1, 2, 5, 9]

✅ Opción 2: sorted() – devuelve una nueva lista ordenada
numeros = [5, 2, 9, 1]
ordenada = sorted(numeros)
print(ordenada)  # Salida: [1, 2, 5, 9]
print(numeros)   # La original sigue igual: [5, 2, 9, 1]

*Tambien funciona con cadenas de texto* 
nombres = ['Carlos', 'Ana', 'Luis']
nombres.sort()
print(nombres)  # Salida: ['Ana', 'Carlos', 'Luis']

-¿Cómo se ordena en orden descendente?
Para ordenar una lista en orden descendente (de mayor a menor o de Z a A), puedes usar los mismos métodos que para orden ascendente, pero agregando el parámetro reverse=True.
✅ Opción 1: sort(reverse=True) – modifica la lista original
numeros = [3, 1, 4, 2]
numeros.sort(reverse=True)
print(numeros)  # Salida: [4, 3, 2, 1]

✅ Opción 2: sorted(..., reverse=True) – crea una nueva lista ordenada
numeros = [3, 1, 4, 2]
descendente = sorted(numeros, reverse=True)
print(descendente)  # Salida: [4, 3, 2, 1]
print(numeros)      # La original no cambia: [3, 1, 4, 2]

-¿Qué diferencia hay entre sort() y sorted()?
La diferencia principal entre sort() y sorted() radica en cómo afectan a la lista original y el tipo de valor que devuelven.

✅ sort():
Modifica la lista original en su lugar.
No devuelve nada (devuelve None).
Solo se puede usar en listas.

*Ejemplo*
numeros = [3, 1, 4, 2]
numeros.sort()  # Ordena la lista original
print(numeros)  # Salida: [1, 2, 3, 4]

✅ sorted():
No modifica la lista original.
Devuelve una nueva lista ordenada, dejando la lista original sin cambios.
Se puede usar en cualquier objeto iterable (no solo listas), como tuplas, diccionarios, y cadenas de texto.

numeros = [3, 1, 4, 2]
ordenados = sorted(numeros)  # Devuelve una nueva lista ordenada
print(ordenados)  # Salida: [1, 2, 3, 4]
print(numeros)    # La lista original no cambia: [3, 1, 4, 2]

9. ¿Cómo invertimos el orden de los elementos de una lista?
-¿Cómo invertir una lista usando reverse()?
Para invertir una lista en Python, puedes usar el método reverse(). Este método modifica la lista original invirtiendo su orden de manera in-place, es decir, no devuelve una nueva lista, sino que cambia la lista existente. 
*Ejemplo* 
numeros = [1, 2, 3, 4, 5]
numeros.reverse()  # Invierte la lista
print(numeros)  # Salida: [5, 4, 3, 2, 1]

-¿Cómo invertir una lista usando slicing?
Para invertir una lista usando slicing en Python, puedes utilizar la siguiente sintaxis:
mi_lista[::-1]
Este slicing crea una nueva lista que contiene los elementos de la lista original, pero en orden inverso.
*Ejemplo*
numeros = [1, 2, 3, 4, 5]
inverso = numeros[::-1]
print(inverso)  # Salida: [5, 4, 3, 2, 1]

10. ¿Cómo hacemos una copia de una lista?
-¿Cómo copiar una lista usando slicing?
Para copiar una lista usando slicing en Python, se puede utilizar la siguiente sintaxis: 
*Ejemplo*
lista_original = [1, 2, 3, 4, 5]
lista_copiada = lista_original[:]

-¿Cómo copiarla usando list()?
Para copiar una lista usando la función list(), simplemente puedes pasar la lista original como argumento a list(). Esto crea una nueva lista con los mismos elementos de la lista original.
*Ejemplo*
lista_original = [1, 2, 3, 4, 5]
lista_copiada = list(lista_original)

-¿Cómo copiarla usando copy()?
Para copiar una lista usando el método copy(), simplemente puedes llamar a este método en la lista original. El método copy() crea una copia superficial de la lista, similar al slicing o a la función list().
*Ejemplo*
lista_original = [1, 2, 3, 4, 5]
lista_copiada = lista_original.copy()

11. ¿Cómo comprobamos si una lista está vacía?
- ¿Cómo podemos saber si una lista no tiene elementos?
Para saber si una lista esta vacia hay 2 formas de hacerlo invirtiendo la logica. 
La primera es usando una comprobación directa con if:
Para verificar que la lista no tiene elementos, simplemente puedes usar la negación (not), ya que si la lista está vacía, su valor es considerado False en un contexto booleano. Entonces, al usar not, puedes verificar si la lista está vacía.
*Ejemplo*
lista = []
if not lista:
    print("La lista está vacía, no tiene elementos.")
else:
    print("La lista tiene elementos.")

La segunda es usar len(). Si la longitud de la lista es igual a 0, significa que la lista no tiene elementos.
*Ejemplo*
lista = []
if len(lista) == 0:
    print("La lista no tiene elementos.")
else:
    print("La lista tiene elementos.")

     
12. ¿Cómo pedir varios datos al usuario y almacenarlos en una lista?
- ¿Cómo pedimos al usuario la cantidad de datos que quiere ingresar?
Para pedir al usuario la cantidad de datos que quiere ingresar, puedes usar la función input() para recibir una entrada del usuario, y luego convertir esa entrada a un número (usualmente a un entero) utilizando la función int().
*Ejemplo*
# Pedir al usuario la cantidad de datos que quiere ingresar
cantidad = int(input("¿Cuántos datos quieres ingresar? "))
# Mostrar la cantidad de datos que el usuario quiere ingresar
print(f"Vas a ingresar {cantidad} datos.")

-¿Cómo almacenamos esos datos en una lista usando un ciclo for?
Para almacenar los datos que el usuario ingresa en una lista usando un ciclo for, puedes seguir estos pasos:
Primero, pides la cantidad de datos que el usuario quiere ingresar.
Luego, usas un ciclo for que se repita esa cantidad de veces.
Dentro del ciclo, pides al usuario que ingrese cada dato y lo agregas a una lista.
*Ejemplo*
# Pedir al usuario la cantidad de datos que quiere ingresar
cantidad = int(input("¿Cuántos datos quieres ingresar? "))
# Crear una lista vacía para almacenar los datos
datos = []
# Usar un ciclo for para pedir y almacenar los datos
for i in range(cantidad):
    dato = input(f"Ingrese el dato {i+1}: ")  # Pedir el dato al usuario
    datos.append(dato)  # Agregar el dato a la lista
# Mostrar la lista de datos ingresados
print("Los datos ingresados son:", datos)


