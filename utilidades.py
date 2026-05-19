def mostrar_menu() -> str:
    """
    Muestra en la consola el menú principal con las 8 opciones disponibles
    y solicita al usuario que ingrese una opción.
    
    Returns:
        str: El número de la opción seleccionada por el usuario en formato de texto.
    """
    print("Sistema de Procesamiento de Contraseñas")
    print("Seleccione una opción con la tecla numeral:")
    print("1. Ingresar contraseña")
    print("2. Validar nivel de seguridad")
    print("3. Contar tipos de caracteres")
    print("4. Buscar carácter específico")
    print("5. Mostrar contraseña invertida")
    print("6. Generar reporte estadístico")
    print("7. Verificar si es palindromo")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")
    return opcion

def mostrar_contrasena_invertida(contrasena: str) -> None:
    """
    Recorre de forma manual la contraseña
    para reconstruirla de manera invertida e imprimirla por pantalla.
    
    Args:
        contrasena (str): La cadena de caracteres que se desea invertir.
    """
    largo = len(contrasena)
    invertida = ""
    
    for i in range(largo - 1, -1, -1):
        invertida = invertida + contrasena[i]
        
    print("\nContraseña invertida:", invertida)