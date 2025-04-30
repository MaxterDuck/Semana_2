#Ejemplo12 de taller investigativo.py
cantidad = int(input("¿Cuántos datos quieres ingresar? "))
datos = []
for i in range(cantidad):
    dato = input(f"Ingrese el dato {i+1}: ") 
    datos.append(dato)  
print (datos)