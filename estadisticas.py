def reporte_estadistico(contrasena : str) -> None:
    """
    Genera y muestra por consola un informe detallado con las métricas
    de la contraseña, incluyendo su longitud total y el desglose
    por cantidad de letras, números y símbolos válidos.

    Args:
        contrasena (str): La contraseña activa en el sistema que se va a evaluar.
    """
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
    print(f"El porcentaje de letras es: {cant_letras / largo * 100}%\n")
    print(f"El porcentaje de numeros es: {cant_numeros / largo * 100}%\n")
    print(f"El porcentaje de simbolos es: {cant_simbolos / largo * 100}%\n")