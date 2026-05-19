def ingresar_contrasena():
    contrasena = input("Ingrese la contrasena: ")
    
    if contrasena == "":
        print("La contraseña no puede estar vacía\n")
        contrasena = ingresar_contrasena()
        
    elif len(contrasena) < 8:
        print("La contraseña debe tener al menos 8 caracteres\n")
        contrasena = ingresar_contrasena()
        
    elif contrasena[0] == " ":
        print("La contraseña no puede comenzar con un espacio en blanco\n")
        contrasena = ingresar_contrasena()
        
    else:
        cant_letras = 0
        for caracter in contrasena:
            if ("a" <= caracter <= "z") or ("A" <= caracter <= "Z"):
                cant_letras = cant_letras + 1
                
        if cant_letras == 0:
            print("\nLa contraseña debe contener al menos un caracter alfabetico\n")
            contrasena = ingresar_contrasena()
            
    return contrasena

def validar_nivel_seguridad(contrasena):
    largo = len(contrasena)
    cant_letras = 0
    cant_numeros = 0
    cant_simbolos = 0
    simbolos_validos = '!“#$%&()*+,-./'
    
    for i in contrasena:
        if ("a" <= i <= "z") or ("A" <= i <= "Z"):
            cant_letras = cant_letras + 1
            
        elif "0" <= i <= "9":
            cant_numeros = cant_numeros + 1
            
        else:
            for simbolo in simbolos_validos:
                if i == simbolo:
                    cant_simbolos = cant_simbolos + 1

    
    if largo >= 12 and cant_letras > 0 and cant_numeros > 0 and cant_simbolos > 0:
        print("\nLa contraseña es de nivel: Fuerte\n")
        
    elif cant_letras > 0 and cant_numeros > 0:
        print("\nLa contraseña es de nivel: Media\n")
        
    elif (largo >= 8 and largo <= 9) and cant_letras == largo:
        print("\nLa contraseña es de nivel: Débil\n")
        
    else:
        print("\nLa contraseña es de nivel: No clasificado\n")