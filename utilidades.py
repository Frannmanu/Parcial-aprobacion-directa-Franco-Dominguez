def mostrar_menu():
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

def mostrar_contrasena_invertida(contrasena):
    largo = len(contrasena)
    invertida = ""
    
    for indice in range(largo - 1, -1, -1):
        invertida = invertida + contrasena[indice]
        
    print("\nContraseña invertida:", invertida)