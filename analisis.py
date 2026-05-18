def contar_tipos_caracteres(contrasena):
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
    print(f"Cantidad de espacios:{cant_espacios}")


def buscar_caracter_especifico(contrasena):
    caracter_buscado = input("Ingrese el carácter que desea buscar: ")

    cant_veces = 0
    posiciones = ""
    indice = 0 

    for caracter in contrasena:
        if caracter == caracter_buscado:
            cant_veces = cant_veces + 1
            posiciones = posiciones + str(indice) + " "
            
        indice = indice + 1

    print("\n--- Resultado de la búsqueda ---")
    print(f"\nAparece: {cant_veces} veces.")
    
    if cant_veces > 0:
        print(f"Posiciones: {posiciones}\n")
    else:
        print("No se encontraron coincidencias.")