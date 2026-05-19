from utilidades import mostrar_menu as menu, mostrar_contrasena_invertida as invertir
from validaciones import ingresar_contrasena as ingresar, validar_nivel_seguridad as validar
from analisis import contar_tipos_caracteres as contador, buscar_caracter_especifico as buscar, verificar_palindromo as verificar, ordenar_contrasena as ordenar
from estadisticas import reporte_estadistico as estadistica

contraseña_nueva = ""
continuar = "si"

while continuar == "si":
    opcion = menu()

    match opcion:
        case "1": # Ingresar contraseña
            contraseña_nueva = ingresar()
            print("\n---La contraseña fue creada con exito!---\n")
        case "2": # Validar nivel de seguridad
            if contraseña_nueva == "":
                print("\n---Primero debe ingresar una contraseña en opcion 1!---\n")
            else:
                print("\n---Analizando la contraseña nueva!---\n")
            validar(contraseña_nueva)
        case "3": # Contar tipos de caracteres
            if contraseña_nueva == "":
                print("\n---Primero debe ingresar una contraseña en opcion 1!---\n")
            else:
                contador(contraseña_nueva)
        case "4": # Buscar carácter específico
            if contraseña_nueva == "":
                print("\n---Primero debe ingresar una contraseña en opcion 1!---\n")
            else:
                buscar(contraseña_nueva)
        case "5": # Mostrar contraseña invertida
            if contraseña_nueva == "":
                print("\n---Primero debe ingresar una contraseña en opcion 1!---\n")
            else:
                invertir(contraseña_nueva)
        case "6": # Generar reporte estadístico
            if contraseña_nueva == "":
                print("\n---Primero debe ingresar una contraseña en opcion 1!---\n")
            else:
                estadistica(contraseña_nueva)
        case "7": # Verificar si es palindromo
            if contraseña_nueva == "":
                print("\n---Primero debe ingresar una contraseña en opcion 1!---\n")
            else:
                verificar(contraseña_nueva)
        case "8": # Ordenar caracteres de la contraseña
            if contraseña_nueva == "":
                print("\n---Primero debe ingresar una contraseña en opcion 1!---\n")
            else:
                ordenar(contraseña_nueva)
        case "9": # Salir
            print("\n---Gracias por usar el programa!---\n")
            continuar = "no"
        case _:
            print("\n---Opcion no valida!---\n")