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
                respuesta = input("El número ingresado es negativo. ¿Desea utilizar el valor absoluto? (S/N): ").upper()
                if respuesta in ['S', 'SI', 'Y', 'YES']:
                    # Usamos el absoluto
                    numero = abs(numero)
                    # Retornamos el valor y salimos del while
                    return numero
                #Si no queremos usar el valor absoluto, volvemos a solicitarlo. 
                else:
                    # Conitnuamos solicitandolo en el while
                    continue
            # Si el valor es 0, se lo volvemos a solicitar.
            elif numero ==0:
                print("Si definimos una matriz de 0 columnas y 0 filas, no tendría gracia.","\nPrueba otra vez")
                continue
            # Puede que el numero que nos de este bien, retornamos ese valor.
            else:
                return numero
        # En caso de que el numero introducido no sea valido de ninguna de las opciones, saltaráun error para volver a introducirlo.
        # Ejemplos de error: string, bool.
        except ValueError:
            print("Error: ¡Debe ingresar un número entero válido!")
        
        
# Definimos una funcion para la creación de la matriz proporcionando el numero de definición
# La matriz está inicializada en 0 a proposito, simplemente es educativo.
def crear_matriz_cuadrada(n):
    # Creamos una lista vacia en la que crearemos la matriz, en ella se almacenarás las filas.
    matriz = []
    # Se inicia un bucle que recorrerá todas las filas desde 0 hasta n-1 dado por el usuario.
    for i in range(n):
        fila = []
        # Se inicia un bucle que recorrera todas las columnas ( elementos dentro de cada fila)desde 0 hasta n-1 dado por el usuario, en este caso asi ya que es cuadrada.
        for j in range(n):
            # numero_aleatorio = random.randint(0, 9)
            # fila.append(numero_aleatorio)
            # Deberiamos escribir este codigo para crearla directamente con los numeros aleatorios.
            # Inicializamos cada elemento de la columna en 0
            fila.append(0)  # Puedes cambiar este valor de inicialización.
        # Una vez completemos toda la columna tendremos una fila, y la añadiremos a la lista "matriz"
        matriz.append(fila)
    # Cuando tengamos toda la matriz, devolveremos la lista completa.
    return matriz


# Creamos una funcion que me rellena con numeros aletarios entre el 0 y el 9 la matriz que le pasemos.
def rellenar_matriz_aleatoriamente(matriz):
    # Reiniciar la semilla de generación de números aleatorios
    random.seed()
    # Definimos n como la longitud maxima de nuetra matriz. ( numeor maximo definido por el usuario)
    n = len(matriz)
    # Inicializamos un bucle el cual recorre todas las filas
    for i in range(n):
        # Inicializamos un bucle el cual recorre todos los elementos de cada columna.
        for j in range(n):
            # Definimos un numero aleatorio cualquiera
            numero_aleatorio = random.randint(0, 9)
            # Le asociamos ese numero aleatorio generado al elemento de la fila 'i', de la columna 'j'
            matriz[i][j] = numero_aleatorio
            

# Creamos una función para imprimir la matriz de forma bonita
def print_matriz(matriz):
    # Creamos un bucle que recorre cada fila de la matriz
    for fila in matriz:
        # Creamos un bucle que recorre cada columna todos los elementos.
        for elemento in fila:
            # Imprimimos cada elementos y lo separamos por una tabulacion para que se vean bien.
            print(elemento, end="\t") 
        # Imprime un salto de línea después del final de cada fila
        # Es el equivalente a print('\n')
        print()  

# Creamos una función para sumar los números de cada fila de la matriz
def sumar_filas(matriz):
    # Creamos una lista para guardar los resultados
    sumas = []
    # Creamos un bucle que recorra cada fila
    for fila in matriz:
        # Al indicar que estamos en cada fila, realizamos la suma de todos los elementos de cada fila.
        # Es decir en la fila 0, sumaremos los elementos 0 de cada columan, en la fila 1 sumaremos todos los elementos 1 de cada columna
        suma_fila = sum(fila)
        # Añadiremos el resultado a una lista la cual retornaremos
        sumas.append(suma_fila)
    return sumas

# Creamos una funcion que sume todos los resultados de las filas
def totalizar_filas(lista):
    # Hacemos un sumatorio de todos los resultados de esa lista.
    suma = sum(lista)
    return suma

# Creamos una función para sumar los números de cada columna de la matriz
def sumar_columnas(matriz):
    # Calculamos la longitud de la matriz y lo asignamos a una variable
    n = len(matriz)
    # Creamos una lista para guardar los resultados
    sumas = []
    # Cremoa un bucle el cual recorre los elementos de las columnas
    for j in range(n):
        # Cremoas una variable que suma todos los elementos j de cada fila.
        # Es decir, suma todos los elementos 0 de cada fila,la columna 0. todos los elementos 1 de cada fila, es decir la columna 1...
        suma_columna = sum(matriz[i][j] for i in range(n))
        # Añadimos la suma a la lista y lo retornamos.
        sumas.append(suma_columna)
    return sumas

# Creamos una funcion que sume todos los resultados de las columnas
def totalizar_columnas(lista):
    # Hacemos un sumatorio de todos los resultados de esa lista.
    suma = sum(lista)
    return suma





# Creamos el Main, el cuerpo principal del programa, desde donde llamaremos a todas las funciones. 
def main():
    # Introducción al programa.
    print("\nBienvenido a la práctica de IBM\n")

    # Solicitamos el numero para definir la matriz y lo guardamos en una variable.
    numero_matriz = solicitar_entero()

    # Pasaremos el valor desedo para crear la matriz, e inicializamos la matriz en 0
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
    time.sleep(1)
    print("...")
    time.sleep(0.5)

    # Calculamos las sumas de las filas y nos lo devuelve en una lista.
    sumas_filas = sumar_filas(matriz)

    # Calculamos el total de todos resultados de las filas
    total_filas = totalizar_filas(sumas_filas)

    # Calculamos las sumas de las columnas y nos lo devuelve en una lista.
    sumas_columnas = sumar_columnas(matriz)

    # Calculamos el total de todos resultados de las columnas
    total_columnas = totalizar_columnas(sumas_columnas)

    
    # Imprimimos la matriz junto con las sumas de filas y columnas
    print("Matriz generada:")
    # Creamos un bucle que recorre la matriz y nos devuelve el indice y el valor de ese indice en la matriz.
    for i, fila in enumerate(matriz):
        # Creamos un bucle que recorre cada elemento de cada fila.
        for elemento in fila:
            # Imprimimos cada elementos separado por una tabulacion.
            print(elemento, end="\t")
        # Al final de cada fila impresa, imprimiremos el valor de toda su suma anteriormeten guardada.
        print("\t =", sumas_filas[i])
    # Imprimimios una linea separatoria para mostrar los resultados de las sumas de las columnas.
    print("-" * (len(matriz[0]) * 8 + 15))
    # Creamos un bucle el cual recorre los resultados de las sumas de las columna.
    for suma in sumas_columnas:
        # Va imprimiento cada suma de las columnas separadas por una tabulacion
        print(suma, end="\t")
    # Imprimimos una separacion variable para intentar ajustar los resultados de las sumas de todas las filas y todas las columnas, y queden todo lo centrado que podamos.
    print(" " * (len(matriz[0])-6) + f"     = {total_columnas}|{total_filas}")

# Llamamos a la función main para iniciar el programa
main()


