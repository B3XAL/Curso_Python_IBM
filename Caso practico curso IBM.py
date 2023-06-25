"""
Nombre del programa: Programa IBM Matriz
Autor: B3XAL
Versión: 1.0
Fecha de creación: 24/06/2023
"""
# Importamos random para usarlo en el relleno de la matriz
import random 

# Creamos la funcion para solicitar un numero para definir la matriz
def solicitar_entero():
    # Cremo un bucle que solicite un numero, hast qu sea válido.
    while True:
        try:
            # Solicitamos al usuario un numero
            numero = int(input("Defina un numero para crear una matriz cuadrada: "))
            # Si el numero es menor de 0
            if numero < 0:
                # Podemos utilizar el valor absoluto como definición de la matriz
                respuesta = input("El número ingresado es negativo. ¿Desea utilizar el valor absoluto? (S/N): ")
                if respuesta.upper() == 'S' or respuesta.upper() == 'SI' or respuesta.upper() == 'Y' or respuesta.upper() == 'YES':
                    numero = abs(numero)
                #Si no queremos usar el valor absoluto, volvemos a solicitarlo. 
                else:
                    continue
            # Si el valor es 0, se lo volvemos a solicitar.
            elif numero ==0:
                print("Si definimos una matriz de 0 columnas y filas, no tendría gracia.","\nPrueba otra vez")
                continue
            else:
                return numero
        
        except ValueError:
            print("Error: ¡Debe ingresar un número entero válido!")
            return numero
        
# Definimos una funcion para la creación de la matriz proporcionando el numero de definición
# La matriz está inicializada en 0 a proposito, simplemente es educativo.
def crear_matriz_cuadrada(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            # numero_aleatorio = random.randint(0, 9)
            # fila.append(numero_aleatorio)
            # Deberiamos escribir este codigo para crearla directamente con los numeros aleatorios.
            fila.append(0)  # Puedes cambiar este valor de inicialización.
        matriz.append(fila)
    return matriz


# Creamos una funcion que me rellena con numeros aletarios entre el 0 y el 9 la matriz que le pasemos.
def rellenar_matriz_aleatoriamente(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            numero_aleatorio = random.randint(0, 9)
            matriz[i][j] = numero_aleatorio

# Creamos el Main 
def main():
    # Introducción al programa.
    print("\nBienvenido a la práctica de IBM\n")

    # Solicitamos el numero para definir la matriz
    numero_matriz = solicitar_entero()
    # Pasaremos el valor desedo para crear la matriz
    print(crear_matriz_cuadrada(numero_matriz))
  
main()
