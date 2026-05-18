from utilidades import mostrar_menu as menu, mostrar_contrasena_invertida as invertir
from validaciones import ingresar_contrasena as ingresar, validar_nivel_seguridad as validar
from analisis import contar_tipos_caracteres as contador, buscar_caracter_especifico as buscar

contraseña_nueva = ""
continuar = "si"
while continuar == "si":
    opcion = menu()

    match opcion:
        case "1":
            contraseña_nueva = ingresar()
            print("\n---La contraseña fue creada con exito!---\n")
        case "2":
            print("\n---Analizando la contraseña nueva!---\n")
            validar(contraseña_nueva)
        case "3":
            if contraseña_nueva == "":
                print("\n---Primero debe ingresar una contraseña en opcion 1!---\n")
            else:
                contador(contraseña_nueva)
        case "4":
            if contraseña_nueva == "":
                print("\n---Primero debe ingresar una contraseña en opcion 1!---\n")
            else:
                buscar(contraseña_nueva)
        case "5":
            if contraseña_nueva == "":
                print("\n---Primero debe ingresar una contraseña en opcion 1!---\n")
            else:
                invertir(contraseña_nueva)
        case "6":
            pass
        case "7":
            pass
        case "8":
            print("\n---Gracias por usar el programa!---\n")
            continuar = "no"