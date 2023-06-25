"""
Nombre del programa: Programa IBM Matriz
Autor: B3XAL
Versión: 1.0
Fecha de creación: 24/06/2023
"""
# Importamos random para usarlo en el relleno de la matriz
import random 
# Importame time para el uso de las pausas
import time

# Creamos la funcion para solicitar un numero para definir la matriz
def solicitar_entero():
    # Creamos un bucle que solicite un numero, hasta que sea válido.
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
                print("Si definimos una matriz de 0 columnas y 0 filas, no tendría gracia.","\nPrueba otra vez")
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

# Creamos una función para imprimir la matriz de forma bonita
def print_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")  # Imprime cada elemento separado por un tabulador
        print()  # Imprime un salto de línea después de cada fila

# Creamos una función para sumar los números de cada fila de la matriz
def sumar_filas(matriz):
    # Creamos una lista para guardar los resultados
    sumas = []
    for fila in matriz:
        suma_fila = sum(fila)
        sumas.append(suma_fila)
    return sumas

# Creamos una función para sumar los números de cada columna de la matriz
def sumar_columnas(matriz):
    # Calculamos la longitud de la matriz
    n = len(matriz)
    # Creamos una lista para guardar los resultados
    sumas = []
    for j in range(n):
        suma_columna = sum(matriz[i][j] for i in range(n))
        sumas.append(suma_columna)
    return sumas




# Creamos el Main 
def main():
    # Introducción al programa.
    print("\nBienvenido a la práctica de IBM\n")

    # Solicitamos el numero para definir la matriz
    numero_matriz = solicitar_entero()
    # Pasaremos el valor desedo para crear la matriz, inicilizada en 0
    matriz=crear_matriz_cuadrada(numero_matriz)
    # Rellenamos con numeros aleatorios todos los huecos de la matriz
    rellenar_matriz_aleatoriamente(matriz)
    # Imprimimos la matriz generadacon los numeros aleatorios
    print("Matriz generada:")
    print_matriz(matriz)
    # Generamos un poco de intriga para el calculo de las sumas
    print("Calculando las sumas de cada fila y columna")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)

    # Calculamos las sumas de las filas y nos lo devuelve en una lista.
    sumas_filas = sumar_filas(matriz)

    # Calculamos las sumas de las columnas y nos lo devuelve en una lista.
    sumas_columnas = sumar_columnas(matriz)

    # Imprimimos la matriz junto con las sumas de filas y columnas
    print("Matriz generada:")
    for i, fila in enumerate(matriz):
        for elemento in fila:
            print(elemento, end="\t")
        print("\t =", sumas_filas[i])
    print("---------------------------------------")
    for j, suma_columna in enumerate(sumas_columnas):
        print(suma_columna, end="\t")
    print()

# Llamamos a la función main para ejecutar el programa
main()
