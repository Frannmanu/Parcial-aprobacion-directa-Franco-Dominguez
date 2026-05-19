def reporte_estadistico(contrasena):
    largo = len(contrasena)
    print("\n--- Reporte Estadístico ---\n")
    print(f"Longitud de la contraseña: {largo} caracteres\n")

    cant_letras = 0
    cant_numeros = 0
    cant_simbolos = 0
    simbolos_validos = '!“#$%&()*+,-./'

    for caracter in contrasena:
        if ("a" <= caracter <= "z") or ("A" <= caracter <= "Z"):
            cant_letras = cant_letras + 1

        elif "0" <= caracter <= "9":
            cant_numeros = cant_numeros + 1

        else:
            for simbolo in simbolos_validos:
                if caracter == simbolo:
                    cant_simbolos = cant_simbolos + 1

    print(f"Cantidad de letras: {cant_letras}")
    print(f"Cantidad de números: {cant_numeros}")
    print(f"Cantidad de símbolos: {cant_simbolos}\n")