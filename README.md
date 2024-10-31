# Analizador Sintáctico

Este proyecto es un **analizador sintáctico** para un subconjunto del lenguaje de programación Python. El objetivo es analizar código Python que utiliza construcciones básicas y proporcionar un informe detallado del análisis sintáctico en un archivo de texto.

## Características

El analizador es capaz de procesar las siguientes construcciones de Python:

- **Definición de funciones** con parámetros y anotaciones de tipo simples.
- **Anotaciones de tipo** en parámetros y retornos de funciones utilizando `:` y `->`.
- **Estructuras de control**:
  - Sentencias `if`, `elif` y `else`.
  - Bucles `while` y `for`.
- **Sentencias simples**:
  - `return`, `pass`, `break`, `continue`.
- **Asignaciones y expresiones aritméticas** con operadores `+`, `-`, `*`, `/`.
- **Llamadas a funciones** con uno o múltiples argumentos.
- **Listas** y acceso a elementos de listas.
- **Importación de módulos** utilizando `import`.
- **Manejo de cadenas de texto** y literales numéricos.
- **Acceso a atributos y métodos** utilizando el operador punto `.`.

## Limitaciones

Actualmente, el analizador tiene las siguientes limitaciones:

- **No maneja la indentación real** de Python; no reconoce tokens `indent` y `dedent`.
- **No soporta clases** ni programación orientada a objetos.
- **No maneja** excepciones (`try`, `except`, `finally`, `raise`).
- **No soporta** funciones lambda, decoradores, ni comprensiones de listas.
- **No maneja operadores lógicos** (`and`, `or`, `not`) ni operadores bit a bit.
- **No soporta operadores de asignación compuesta** (`+=`, `-=`, `*=`, `/=`, etc.).
- **No maneja tipos de datos avanzados** como tuplas, conjuntos, diccionarios, ni tipos personalizados.

## Requisitos

- Python 3.x instalado en el sistema.

## Instrucciones de Uso

### 1. Preparar el Código a Analizar

- Crea un archivo Python (`.py`) con el código que deseas analizar.
- Asegúrate de que el código utilice únicamente las construcciones soportadas por el analizador.

### 2. Ejecutar el Analizador

Abre una terminal en el directorio donde se encuentra `lexer_parser.py` y ejecuta el siguiente comando:

```bash
python3 lexer_parser.py [nombre_del_archivo.py]
```

Reemplaza `nombre_del_archivo.py` con el nombre de tu archivo Python.

### 3. Revisar los Resultados

El analizador generará dos archivos de salida:

- **`analisis_tokens.txt`**: Contiene la lista de tokens generados durante el análisis léxico.
- **`analisis_sintactico.txt`**: Contiene el resultado del análisis sintáctico. Si el análisis es exitoso, verás el mensaje:

```
El análisis sintáctico ha finalizado exitosamente.
```

Si se detectan errores, el archivo mostrará detalles sobre el tipo de error, la línea y columna donde ocurrió, y el token involucrado.

## Ejemplo

Supongamos que tienes un archivo `codigo_prueba.py` con el siguiente contenido:

```python
def sumar(a: int, b: int) -> int:
  resultado = a + b
  return resultado

print("La suma es:", sumar(10, 20))
```

Ejecuta el analizador con:

```bash
python3 lexer_parser.py codigo_prueba.py
```

Después de la ejecución, revisa los archivos `analisis_tokens.txt` y `analisis_sintactico.txt` para ver los resultados.

## Estructura del Proyecto

- **`lexer_parser.py`**: Script principal que realiza el análisis léxico y sintáctico.
- **`analisis_tokens.txt`**: Archivo de salida con los tokens generados.
- **`analisis_sintactico.txt`**: Archivo de salida con el resultado del análisis sintáctico.
- **`codigo_prueba.py`**: (Opcional) Archivo de código de ejemplo para pruebas.

## Autores
- Mateo Fonseca
- Santiago Garzón
- Sebastián Barros
- Karol Guerrero
