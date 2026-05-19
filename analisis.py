def contar_tipos_caracteres(contrasena : str) -> None:
    """
    Realiza un escaneo y conteo manual carácter por carácter sobre la contraseña
    para clasificar y mostrar cuántas letras, números, símbolos específicos y
    espacios en blanco tiene.

    Args:
        contrasena (str): La contraseña que se va a analizar.
    """
    cant_letras = 0
    cant_numeros = 0
    cant_simbolos = 0
    cant_espacios = 0
    
    simbolos_validos = '!“#$%&()*+,-./'
    
    for caracter in contrasena:
        if ("a" <= caracter <= "z") or ("A" <= caracter <= "Z"):
            cant_letras = cant_letras + 1
            
        elif "0" <= caracter <= "9":
            cant_numeros = cant_numeros + 1
            
        elif caracter == " ":
            cant_espacios = cant_espacios + 1
            
        else:
            for simbolo in simbolos_validos:
                if caracter == simbolo:
                    cant_simbolos = cant_simbolos + 1

    print("\n--- Resultados del Análisis ---\n")
    print(f"Cantidad de letras:{cant_letras}")
    print(f"Cantidad de números:{cant_numeros}")
    print(f"Cantidad de símbolos:{cant_simbolos}")
    print(f"Cantidad de espacios:{cant_espacios}\n")


def buscar_caracter_especifico(contrasena : str) -> None:
    """
    Solicita al usuario un carácter por teclado y realiza una búsqueda manual
    carácter por carácter dentro de la contraseña, informando la cantidad total de apariciones
    y una secuencia de una cadena con los índices exactos de sus posiciones.

    Args:
        contrasena (str): La contraseña sobre la cual realizar la búsqueda.
    """
    caracter_buscado = input("Ingrese el carácter que desea buscar: ")

    cant_veces = 0
    posiciones = ""
    indice = 0 

    for caracter in contrasena:
        if caracter == caracter_buscado:
            cant_veces = cant_veces + 1
            posiciones = posiciones + str(indice) + " "
            
        indice = indice + 1

    print("\n--- Resultado de la búsqueda ---\n")
    print(f"\nAparece: {cant_veces} veces.\n")
    
    if cant_veces > 0:
        print(f"Posiciones: {posiciones}\n")
    else:
        print("\nNo se encontraron coincidencias.\n")
        

def verificar_palindromo(contrasena : str) -> None:
    """
    Verifica si la contraseña es un palíndromo (se lee igual
    de izquierda a derecha que de derecha a izquierda), invirtiendo la cadena
    y comparando secuencialmente cada uno de sus componentes indexados.

    Args:
        contrasena (str): La contraseña que se va a evaluar.
    """
    largo = len(contrasena)
    invertida = ""

    for i in range(largo):

        caracter = contrasena[i]
        invertida = caracter + invertida
    letras_iguales = 0

    for i in range(largo):
        if contrasena[i] == invertida[i]:
            letras_iguales = letras_iguales + 1

    if letras_iguales == largo:
        print("\nLa contraseña es un palíndromo.\n")
    else:
        print("\nLa contraseña NO es un palíndromo.\n")

def ordenar_contrasena(contrasena: str) -> None:
    """
    Convierte la contraseña en una lista de caracteres de manera manual,
    se utiliza el Bubble Sort (Burbuja) para ordenar
    los caracteres de mayor a menor según su valor e imprime el resultado.

    Args:
        contrasena (str): La contraseña que se va a ordenar.
    """
    lista_caracteres = []
    for caracter in contrasena:
        lista_caracteres = lista_caracteres + [caracter]
        
    n = len(lista_caracteres)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_caracteres[j] < lista_caracteres[j + 1]: # ordena Mayor a Menor
                auxiliar = lista_caracteres[j]
                lista_caracteres[j] = lista_caracteres[j + 1]
                lista_caracteres[j + 1] = auxiliar
                
    contrasena_ordenada = ""
    for caracter in lista_caracteres:
        contrasena_ordenada = contrasena_ordenada + caracter
        
    print(f"\n Contraseña ordenada (Mayor a Menor): {contrasena_ordenada}\n")