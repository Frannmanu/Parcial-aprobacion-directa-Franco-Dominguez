def ingresar_contrasena() -> str:
    """
    Solicita al usuario el ingreso de una contraseña por consola y aplica 
    validaciones secuenciales obligatorias para asegurar su calidad.
    
    Validaciones:
        - No puede estar vacía.
        - Debe tener al menos 8 caracteres de longitud.
        - No puede iniciar con un espacio.
        - Debe tener como mínimo un carácter alfabético (letra).

    Returns:
        str: La contraseña válida que cumple con todos los requisitos.
    """
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

def validar_nivel_seguridad(contrasena : str) -> None:
    """
    Realiza un análisis de los componentes de la contraseña con
    un recorrido manual y clasifica su nivel de seguridad en Débil, Media o Fuerte.
    
    Criterios de clasificación:
        - Débil: Longitud de 8 a 9 caracteres compuestos únicamente por letras.
        - Media: Contiene letras y números (sin importar el largo o símbolos).
        - Fuerte: Al menos 12 caracteres, con letras, números y símbolos permitidos.
        - No clasificado: No encaja estrictamente en los grupos anteriores.

    Args:
        contrasena (str): La contraseña que se va a evaluar.
    """
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