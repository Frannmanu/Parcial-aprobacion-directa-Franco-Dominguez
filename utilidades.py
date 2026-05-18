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

def ingresar_contrasena():
    contrasena = input("Ingrese la contraseña: ")

    if contrasena == "":
        print("La contraseña no puede estar vacía")
        contrasena = ingresar_contrasena()

    elif len(contrasena) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        contrasena = ingresar_contrasena()

    elif contrasena [0] == " ":
        print("La contraseña no puede comenzar con un espacio en blanco")
        contrasena = ingresar_contrasena()
    else: 
        for caracter in contrasena:
            if ("a" <= caracter <= "z") or ("A" <= caracter <= "Z"):
                break
        else:
            print("La contraseña debe contener al menos un caracter alfabetico")
            contrasena = ingresar_contrasena()
    return contrasena