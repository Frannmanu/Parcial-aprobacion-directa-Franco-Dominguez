# Sistema de Procesamiento de Contraseñas
Este proyecto es un sistema de análisis y validación de contraseñas por consola desarrollado en **Python** para la materia **Programación I**.

El objetivo principal es implementar estructuras lógicas fundamentales, condicionales, ciclos y modularización en múltiples archivos, aplicando técnicas de recorrido y procesamiento manual de cadenas de caracteres.

## Datos del proyecto

**Integrante:** Franco Dominguez.
**Materia:** Programacion I.
**Instancia:** Primer parcial de aprobacion directa.

**Lenguaje utilizado:** Python

## Descripción del codigo:

El programa está modularizado en archivos independientes siguiendo las prácticas vistas en la cursada:
* **main.py**: Punto de entrada del sistema. Contiene el bucle principal y la lógica del menú con **match-case**.
* **validaciones.py**: Contiene las funciones asociadas a la carga obligatoria de la contraseña y la verificación de su nivel de seguridad.
* **analisis.py**: Implementa las búsquedas de caracteres, conteos específicos y la verificación de palíndromos.
* **estadisticas.py**: Encargado de compilar el reporte integral sobre las características físicas de la cadena.
* **utilidades.py**: Contiene el renderizado estético del menú de opciones y la lógica de inversión de la cadena.

## Funcionalidades Desarrolladas:

El sistema cuenta con un menú interactivo que ofrece las siguientes opciones:

1. **Ingresar contraseña:** Solicita una contraseña aplicando filtros obligatorios (no vacía, mínimo 8 caracteres, no iniciar con espacio, poseer al menos una letra).
2. **Validar nivel de seguridad:** Clasifica la contraseña en tres niveles posibles (*Débil*, *Media* o *Fuerte*) basándose en su longitud y la combinación de tipos de caracteres.
3. **Contar tipos de caracteres:** Informa por pantalla la cantidad total de letras, números, símbolos específicos (`!“#$%&()*+,-./`) y espacios en blanco.
4. **Buscar carácter específico:** Permite la búsqueda manual de un carácter indicando la cantidad de apariciones y listando secuencialmente sus posiciones.
5. **Mostrar contraseña invertida:** Reconstruye e imprime la contraseña al revés.
6. **Generar reporte estadístico:** Presenta un resumen de la longitud total y el conteo de los componentes.
7. **Verificar si es palíndromo:** Verifica si la contraseña se lee igual en ambos sentidos.
8. **Ordenar caracteres de la contraseña:** (Próxima implementación) Ordenamiento de elementos mediante algoritmos como *Bubble Sort*.
9. **Salir:** Termina el ciclo del programa y al usuario.

---
## Restricciones de Cursada Aplicadas

Para cumplir con las consignas del examen, el código se diseñó con las siguientes limitaciones:
* **Recorrido manual estricto:** Todas las evaluaciones se realizan carácter por carácter indexando el string o utilizando ciclos controlados por rangos numéricos (`range(len(...))`).
* **Sin métodos de Strings:** se excluyen los usos de `.isalpha()`, `.isdigit()`, `.find()`, `.count()`, `.index()`, `.lower()`, `.upper()` o slicing del tipo `[::-1]`.
* **Sin funciones de ordenamiento integradas:** se excluye el ordenamiento con `sorted()` o `.sort()`.
* **Funciones integradas autorizadas:** Solo se utilizan las funciones `len()`, `input()`, `print()`, `int()`, `float()`, `str()`, `type()` y `range()`.