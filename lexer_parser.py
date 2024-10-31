import sys

# Definición de caracteres especiales y tokens
character_special = {
    ")": "tk_par_der",
    "(": "tk_par_izq",
    "]": "tk_sqb_der",
    "[": "tk_sqb_izq",
    ":": "tk_dos_puntos",
    ",": "tk_comma",
    ";": "tk_punto_comma",
    "+": "tk_plus",
    "-": "tk_minus",
    "*": "tk_star",
    "/": "tk_slash",
    "|": "tk_vbar",
    "&": "tk_amper",
    "<": "tk_less",
    ">": "tk_greater",
    "=": "tk_assign",
    ".": "tk_punto",
    "%": "tk_percent",
    "}": "tk_brace_der",
    "{": "tk_brace_izq",
    "==": "tk_equal",
    "!=": "tk_no_equal",
    "<=": "tk_less_equal",
    ">=": "tk_greate_equal",
    "^": "tk_circumflex",
    "<<": "tk_shift_izq",
    ">>": "tk_shift_der",
    "**": "tk_double_star",
    "+=": "tk_plus_equal",
    "-=": "tk_mine_equal",
    "*=": "tk_star_equal",
    "/=": "tk_slash_equal",
    "%=": "tk_percent_equal",
    "&=": "tk_amper_equal",
    "|=": "tk_vabar_equal",
    "^=": "tk_circum_flex_equal",
    "<<=": "tk_shift_equal_izq",
    ">>=": "tk_shift_equal_der",
    "**=": "tk_double_start_equal",
    "//": "tk_double_slash",
    "//=": "tk_double_slash_equal",
    "@": "tk_at",
    "@=": "tk_at_equal",
    "->": "tk_ejecuta",
    "...": "tk_ellipsis",
    ":=": "tk_dos_puntos_equal",
}

# Palabras reservadas
word_reserved = {
    "open": "open",
    "False": "False",
    "None": "None",
    "True": "True",
    "and": "and",
    "as": "as",
    "assert": "assert",
    "async": "async",
    "await": "await",
    "break": "break",
    "class": "class",
    "continue": "continue",
    "def": "def",
    "del": "del",
    "elif": "elif",
    "else": "else",
    "except": "except",
    "finally": "finally",
    "for": "for",
    "from": "from",
    "global": "global",
    "if": "if",
    "import": "import",
    "in": "in",
    "is": "is",
    "lambda": "lambda",
    "nonlocal": "nonlocal",
    "not": "not",
    "or": "or",
    "pass": "pass",
    "raise": "raise",
    "return": "return",
    "try": "try",
    "while": "while",
    "with": "with",
    "yield": "yield",
    "object": "object",
    "self": "self",
    "print": "print",
    "input": "input",
}

# Métodos (Aquí se incluyen los métodos de Python que desees reconocer)
methods = {
    "append": "append",
    "extend": "extend",
    "insert": "insert",
    "remove": "remove",
    "pop": "pop",
    "clear": "clear",
    "index": "index",
    "count": "count",
    "sort": "sort",
    "reverse": "reverse",
    "copy": "copy",
    "keys": "keys",
    "values": "values",
    "items": "items",
    "get": "get",
    "update": "update",
    "fromkeys": "fromkeys",
    "setdefault": "setdefault",
    "format": "format",
    "lower": "lower",
    "upper": "upper",
    "split": "split",
    "join": "join",
    "replace": "replace",
    "find": "find",
    "startswith": "startswith",
    "endswith": "endswith",
    "strip": "strip",
    "lstrip": "lstrip",
    "rstrip": "rstrip",
    "isdigit": "isdigit",
    "isalpha": "isalpha",
    "isalnum": "isalnum",
    "isnumeric": "isnumeric",
    "capitalize": "capitalize",
    "title": "title",
    "center": "center",
    "count": "count",
    "encode": "encode",
    "decode": "decode",
    "replace": "replace",
    "len": "len",
    "abs": "abs",
    "all": "all",
    "any": "any",
    "bin": "bin",
    "bool": "bool",
    "bytearray": "bytearray",
    "bytes": "bytes",
    "callable": "callable",
    "chr": "chr",
    "classmethod": "classmethod",
    "compile": "compile",
    "complex": "complex",
    "delattr": "delattr",
    "dict": "dict",
    "dir": "dir",
    "divmod": "divmod",
    "enumerate": "enumerate",
    "eval": "eval",
    "exec": "exec",
    "filter": "filter",
    "float": "float",
    "format": "format",
    "frozenset": "frozenset",
    "getattr": "getattr",
    "globals": "globals",
    "hasattr": "hasattr",
    "hash": "hash",
    "help": "help",
    "hex": "hex",
    "id": "id",
    "input": "input",
    "int": "int",
    "isinstance": "isinstance",
    "issubclass": "issubclass",
    "iter": "iter",
    "len": "len",
    "list": "list",
    "locals": "locals",
    "map": "map",
    "max": "max",
    "memoryview": "memoryview",
    "min": "min",
    "next": "next",
    "object": "object",
    "oct": "oct",
    "open": "open",
    "ord": "ord",
    "pow": "pow",
    "print": "print",
    "property": "property",
    "range": "range",
    "repr": "repr",
    "reversed": "reversed",
    "round": "round",
    "set": "set",
    "setattr": "setattr",
    "slice": "slice",
    "sorted": "sorted",
    "staticmethod": "staticmethod",
    "str": "str",
    "sum": "sum",
    "super": "super",
    "tuple": "tuple",
    "type": "type",
    "vars": "vars",
    "zip": "zip",
    "__init__": "__init__",
    "__str__": "__str__",
    "__repr__": "__repr__",
}

DOCSTRING_MULTI = ""


class Token:
    def __init__(self, nombre, fila, columna, valor=None):
        self.nombre = nombre
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def __str__(self):
        if self.valor is not None:
            return f"<{self.nombre}, {self.valor}, {self.fila}, {self.columna}>"
        else:
            return f"<{self.nombre}, {self.fila}, {self.columna}>"

    def __repr__(self):
        return self.__str__()


class Error:
    def __init__(self, nombre, fila, columna, mensaje=">>>Error léxico"):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.mensaje = mensaje

    def __str__(self):
        return f"{self.mensaje} (línea: {self.fila}, posición: {self.columna}, token: {self.nombre})"

    def __repr__(self):
        return self.__str__()


def read_file(file_name):
    lines = []
    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            lines.append(line)
        if lines and lines[-1][-1] != "\n":
            lines[-1] += "\n"
    return lines


def scannerFunction(cadena, i=0):
    global DOCSTRING_MULTI
    textoEscaneado = []
    subcadena_actual = ""
    indice_inicial = 1
    ignorar = False
    if '"""' in cadena or "'''" in cadena:
        docstring = True
    else:
        docstring = False
    while i < len(cadena):
        if cadena[i] == "\n":
            i += 1
            ignorar = False
            continue
        elif cadena[i] == "#":
            ignorar = True
            i += 1
            continue
        elif ignorar:
            i += 1
            continue
        found_special = False
        if docstring:
            if (cadena[i : i + 3] == '"""' and DOCSTRING_MULTI == ""):
                end_quote_index = cadena.find('"""', i + 3)
                if end_quote_index != -1:
                    i = end_quote_index + 3
                else:
                    ignorar = True
                    DOCSTRING_MULTI = '"""'
                    continue
            elif cadena[i : i + 3] == "'''" and DOCSTRING_MULTI == "":
                end_quote_index = cadena.find("'''", i + 3)
                if end_quote_index != -1:
                    i = end_quote_index + 3
                else:
                    ignorar = True
                    DOCSTRING_MULTI = "'''"
                    continue
            elif DOCSTRING_MULTI == '"""':
                end_quote_index = cadena.find('"""', i + 3)
                if end_quote_index != -1:
                    i = end_quote_index + 3
                    DOCSTRING_MULTI = ""
                    ignorar = False
                else:
                    ignorar = True
                    break
            elif DOCSTRING_MULTI == "'''":
                end_quote_index = cadena.find("'''", i + 3)
                if end_quote_index != -1:
                    i = end_quote_index + 3
                    DOCSTRING_MULTI = ""
                    ignorar = False
                else:
                    ignorar = True
                    break
        if cadena[i] == '"':
            end_quote_index = cadena.find('"', i + 1)
            if end_quote_index != -1:
                textoEscaneado.append([cadena[i : end_quote_index + 1], i + 1])
                i = end_quote_index
                found_special = True
        if cadena[i] == "'":
            end_quote_index = cadena.find("'", i + 1)
            if end_quote_index != -1:
                textoEscaneado.append([cadena[i : end_quote_index + 1], i + 1])
                i = end_quote_index
                found_special = True
        if not found_special:
            if cadena[i].isdigit():
                k = i
                subcadena_siguiente = ""
                while (
                    k < len(cadena) - 1
                    and " " not in subcadena_siguiente
                    and sum(
                        1 for key in character_special if key in subcadena_siguiente
                    )
                    == 0
                ):
                    k += 1
                    if k < len(cadena) - 1:
                        subcadena_siguiente += cadena[k]
                        if cadena[k] == "j" and cadena[k + 1] == " ":
                            break
                if "j" in subcadena_siguiente:
                    subcadena_actual += cadena[i] + subcadena_siguiente
                    textoEscaneado.append(
                        [subcadena_actual, k + 2 - len(subcadena_actual)]
                    )
                    i += len(subcadena_siguiente) + 1
                    subcadena_actual = ""
                    found_special = True
            for j in range(3, 0, -1):
                if i + j <= len(cadena) and cadena[i : i + j] in character_special:
                    if cadena[i : i + j] == ".":
                        if subcadena_actual.isdigit():
                            if cadena[i + 1 : i + j + 1].isdigit():
                                subcadena_actual += cadena[i]
                                found_special = True
                                break
                    if subcadena_actual:
                        textoEscaneado.append([subcadena_actual, indice_inicial])
                        subcadena_actual = ""
                    textoEscaneado.append([cadena[i : i + j], i + 1])
                    i += j - 1
                    found_special = True
                    break
            if not found_special:
                if cadena[i] == " ":
                    if subcadena_actual:
                        textoEscaneado.append([subcadena_actual, indice_inicial])
                        subcadena_actual = ""
                elif cadena[i : i + 3] in character_special:
                    if subcadena_actual:
                        textoEscaneado.append([subcadena_actual, indice_inicial])
                        subcadena_actual = ""
                    textoEscaneado.append((cadena[i : i + 3], i + 1))
                    i += 2
                else:
                    if not subcadena_actual:
                        indice_inicial = i + 1
                    subcadena_actual += cadena[i]
        i += 1
    if subcadena_actual:
        textoEscaneado.append([subcadena_actual, indice_inicial])
    return textoEscaneado


def generadorTokensSinProcesar(texto):
    global DOCSTRING_MULTI
    tokensFinales = []
    for i in range(len(texto)):
        if DOCSTRING_MULTI == '"""':
            end_quote_index = texto[i].find('"""')
            if end_quote_index != -1:
                DOCSTRING_MULTI = ""
                tokensImperfectos = scannerFunction(texto[i], end_quote_index + 3)
                tokensFinales.append(tokensImperfectos)
            else:
                tokensFinales.append([])
                continue
        elif DOCSTRING_MULTI == "'''":
            end_quote_index = texto[i].find("'''")
            if end_quote_index != -1:
                DOCSTRING_MULTI = ""
                tokensImperfectos = scannerFunction(texto[i], end_quote_index + 3)
                tokensFinales.append(tokensImperfectos)
            else:
                tokensFinales.append([])
                continue
        else:
            tokensImperfectos = scannerFunction(texto[i])
            tokensFinales.append(tokensImperfectos)
    return tokensFinales


def clasificadorDeTokens(tokensFinales):
    tokenClasificado = []
    for i in range(len(tokensFinales)):
        for j in range(len(tokensFinales[i])):
            lexema = tokensFinales[i][j][0]
            fila = i + 1
            columna = tokensFinales[i][j][1]

            if lexema in character_special:
                objeto = Token(
                    character_special[lexema],
                    fila,
                    columna,
                    lexema  # Guardamos el lexema
                )
                tokenClasificado.append(objeto)
            elif lexema in word_reserved:
                objeto = Token(
                    word_reserved[lexema],
                    fila,
                    columna,
                    lexema  # Guardamos el lexema
                )
                tokenClasificado.append(objeto)
            elif (
                lexema[-1] == "j"
                and (
                    lexema.count(".") == 0
                    or lexema.count(".") == 1
                )
                and all(
                    char.isdigit() or char in (".", "j")
                    for char in lexema
                )
                and len(lexema) > 1
            ):
                objeto = Token(
                    "tk_complejo",
                    fila,
                    columna,
                    lexema  # Guardamos el lexema
                )
                tokenClasificado.append(objeto)
            elif all(caracter.isdigit() for caracter in lexema):
                objeto = Token(
                    "tk_entero",
                    fila,
                    columna,
                    lexema  # Guardamos el lexema
                )
                tokenClasificado.append(objeto)
            elif (
                lexema.count(".") == 1
                and all(
                    char.isdigit() or char == "." for char in lexema
                )
            ):
                objeto = Token(
                    "tk_float",
                    fila,
                    columna,
                    lexema  # Guardamos el lexema
                )
                tokenClasificado.append(objeto)
            elif lexema.startswith('"') and lexema.endswith('"'):
                objeto = Token(
                    "tk_cadena",
                    fila,
                    columna,
                    lexema
                )
                tokenClasificado.append(objeto)
            elif lexema.startswith("'") and lexema.endswith("'"):
                objeto = Token(
                    "tk_cadena",
                    fila,
                    columna,
                    lexema
                )
                tokenClasificado.append(objeto)
            elif lexema.startswith("__") and lexema.endswith("__"):
                objeto = Token(
                    lexema,
                    fila,
                    columna,
                    lexema
                )
                tokenClasificado.append(objeto)
            elif (
                j != 0
                and lexema in methods
                and tokensFinales[i][j - 1][0] == "."
            ):
                objeto = Token(
                    methods[lexema],
                    fila,
                    columna,
                    lexema
                )
                tokenClasificado.append(objeto)
            elif (
                any(
                    caracter.isalpha()
                    or (caracter.isdigit() and not caracter.isalnum())
                    for caracter in lexema
                )
                and lexema[0].isalpha()
            ):
                objeto = Token(
                    "id",
                    fila,
                    columna,
                    lexema
                )
                tokenClasificado.append(objeto)
            else:
                objeto = Error(lexema, fila, columna)
                tokenClasificado.append(objeto)
                return tokenClasificado
    return tokenClasificado


def parser(tokens):
    index = 0
    length = len(tokens)

    comparison_operators = [
        "tk_equal", "tk_no_equal", "tk_less", "tk_less_equal",
        "tk_greater", "tk_greate_equal"
    ]

    # Abrimos el archivo para escribir los resultados del análisis sintáctico
    output_file = open("analisis_sintactico.txt", "w", encoding="utf-8")

    def current_token():
        if index < length:
            return tokens[index]
        else:
            return None

    def match(expected_types):
        nonlocal index
        token = current_token()
        if token and any(
            token.nombre == expected_type or token.nombre.startswith(expected_type + ",")
            for expected_type in expected_types
        ):
            index += 1
            return token
        else:
            if token:
                expected_lexemes = []
                for expected_type in expected_types:
                    expected_lexeme = invert_token_lookup(expected_type)
                    expected_lexemes.append(expected_lexeme)
                expected = '", "'.join(expected_lexemes)
                lexema = token.valor if token.valor is not None else token.nombre
                error_message = f'<{token.fila},{token.columna}> Error sintactico: se encontro: "{lexema}"; se esperaba: "{expected}".'
                output_file.write(error_message + "\n")
            else:
                error_message = "Error sintáctico: fin de entrada inesperado"
                output_file.write(error_message + "\n")
            output_file.close()
            sys.exit(1)

    def invert_token_lookup(token_name):
        for lex, name in character_special.items():
            if name == token_name:
                return lex
        for lex, name in word_reserved.items():
            if name == token_name:
                return lex
        return token_name

    # [Implementación de las funciones de parsing]

    def parse_program():
        while current_token():
            parse_statement()

    def parse_statement():
        token = current_token()
        if token.nombre == "def":
            parse_function_def()
        elif token.nombre == "if":
            parse_if_statement()
        elif token.nombre == "while":
            parse_while_statement()
        elif token.nombre == "for":
            parse_for_statement()
        elif token.nombre == "import":
            parse_import_statement()
        elif token.nombre == "print":
            parse_print_statement()
        elif token.nombre == "return":
            parse_return_statement()
        elif token.nombre == "pass":
            parse_pass_statement()
        elif token.nombre == "break":
            parse_break_statement()
        elif token.nombre == "continue":
            parse_continue_statement()
        elif token.nombre == "id":
            parse_assignment_or_expression()
        else:
            expected_tokens = ["def", "if", "while", "for", "import", "print", "return", "pass", "break", "continue", "id"]
            expected_lexemes = [invert_token_lookup(t) for t in expected_tokens]
            expected = '", "'.join(expected_lexemes)
            lexema = token.valor if token.valor is not None else token.nombre
            print(f'<{token.fila},{token.columna}> Error sintactico: se encontro: "{lexema}"; se esperaba: "{expected}".')
            sys.exit(1)

    def parse_import_statement():
        match(["import"])
        parse_module_name()
        token = current_token()
        if token and token.nombre == "as":
            match(["as"])
            match(["id"])

    def parse_module_name():
        match(["id"])
        while current_token() and current_token().nombre == "tk_punto":
            match(["tk_punto"])
            match(["id"])

    def parse_function_def():
        match(["def"])
        match(["id"])
        match(["tk_par_izq"])
        if current_token().nombre != "tk_par_der":
            parse_parameters()
        match(["tk_par_der"])
        if current_token() and current_token().nombre == "tk_ejecuta":
            match(["tk_ejecuta"])
            parse_type()
        match(["tk_dos_puntos"])
        parse_block()

    def parse_parameters():
        parse_parameter()
        while current_token() and current_token().nombre == "tk_comma":
            match(["tk_comma"])
            parse_parameter()

    def parse_parameter():
        match(["id"])
        if current_token() and current_token().nombre == "tk_dos_puntos":
            match(["tk_dos_puntos"])
            parse_type()

    def parse_type():
        token = current_token()
        if token.nombre == "id":
            match(["id"])
            if current_token() and current_token().nombre == "tk_sqb_izq":
                match(["tk_sqb_izq"])
                parse_type()
                match(["tk_sqb_der"])
        else:
            expected_tokens = ["id"]
            expected_lexemes = [invert_token_lookup(t) for t in expected_tokens]
            expected = '", "'.join(expected_lexemes)
            lexema = token.valor if token.valor is not None else token.nombre
            print(f'<{token.fila},{token.columna}> Error sintactico: se encontro: "{lexema}"; se esperaba: "{expected}".')
            sys.exit(1)

    def parse_block():
        while current_token():
            if current_token().nombre in ["else", "elif", "except", "finally", "dedent"]:
                break
            parse_statement()

    def parse_if_statement():
        match(["if"])
        parse_comparison_expression()
        match(["tk_dos_puntos"])
        parse_block()
        while current_token() and current_token().nombre in ["elif", "else"]:
            if current_token().nombre == "elif":
                match(["elif"])
                parse_comparison_expression()
                match(["tk_dos_puntos"])
                parse_block()
            elif current_token().nombre == "else":
                match(["else"])
                match(["tk_dos_puntos"])
                parse_block()

    def parse_while_statement():
        match(["while"])
        parse_comparison_expression()
        match(["tk_dos_puntos"])
        parse_block()

    def parse_for_statement():
        match(["for"])
        match(["id"])
        match(["in"])
        parse_expression()
        match(["tk_dos_puntos"])
        parse_block()

    def parse_print_statement():
        match(["print"])
        match(["tk_par_izq"])
        if current_token().nombre != "tk_par_der":
            parse_arguments()
        match(["tk_par_der"])

    def parse_return_statement():
        match(["return"])
        if current_token() and current_token().nombre not in ["tk_dos_puntos", "dedent"]:
            parse_expression()

    def parse_pass_statement():
        match(["pass"])

    def parse_break_statement():
        match(["break"])

    def parse_continue_statement():
        match(["continue"])

    def parse_assignment_or_expression():
        match(["id"])
        if current_token() and current_token().nombre == "tk_assign":
            match(["tk_assign"])
            parse_expression()
        else:
            # Manejo de posibles llamadas a funciones o acceso a atributos
            if current_token() and current_token().nombre == "tk_par_izq":
                parse_function_call()
            else:
                parse_expression_prime()

    def parse_expression():
        parse_term()
        parse_expression_prime()

    def parse_expression_prime():
        while current_token() and current_token().nombre in ("tk_plus", "tk_minus"):
            match([current_token().nombre])
            parse_term()

    def parse_term():
        parse_factor()
        parse_term_prime()

    def parse_term_prime():
        while current_token() and current_token().nombre in ("tk_star", "tk_slash"):
            match([current_token().nombre])
            parse_factor()

    def parse_factor():
        token = current_token()
        if token.nombre.startswith("tk_entero") or token.nombre.startswith("tk_float"):
            match([token.nombre.split(",")[0]])
        elif token.nombre == "tk_par_izq":
            match(["tk_par_izq"])
            parse_expression()
            match(["tk_par_der"])
        elif token.nombre == "tk_sqb_izq":
            parse_list()
        elif token.nombre == "id":
            match(["id"])
            # Manejo de llamadas a funciones
            if current_token() and current_token().nombre == "tk_par_izq":
                parse_function_call()
            # Manejo de acceso a atributos o métodos
            while current_token() and current_token().nombre == "tk_punto":
                match(["tk_punto"])
                match(["id"])
                if current_token() and current_token().nombre == "tk_par_izq":
                    parse_function_call()
        elif token.nombre == "tk_cadena":
            match(["tk_cadena"])
        else:
            expected_tokens = ["tk_entero", "tk_float", "(", "id", "[", "tk_cadena"]
            expected_lexemes = [invert_token_lookup(t) for t in expected_tokens]
            expected = '", "'.join(expected_lexemes)
            lexema = token.valor if token.valor is not None else token.nombre
            print(
                f'<{token.fila},{token.columna}> Error sintactico: se encontro: "{lexema}"; se esperaba: "{expected}".'
            )
            sys.exit(1)

    def parse_function_call():
        match(["tk_par_izq"])
        if current_token().nombre != "tk_par_der":
            parse_arguments()
        match(["tk_par_der"])

    def parse_arguments():
        parse_expression()
        while current_token() and current_token().nombre == "tk_comma":
            match(["tk_comma"])
            parse_expression()

    def parse_list():
        match(["tk_sqb_izq"])
        if current_token().nombre != "tk_sqb_der":
            parse_expression()
            while current_token() and current_token().nombre == "tk_comma":
                match(["tk_comma"])
                parse_expression()
        match(["tk_sqb_der"])

    def parse_comparison_expression():
        parse_expression()
        while current_token() and current_token().nombre in comparison_operators:
            match([current_token().nombre])
            parse_expression()

    parse_program()
    output_file.write("El analisis sintactico ha finalizado exitosamente.\n")
    output_file.close()


def main():
    try:
        path = sys.argv[1]
        texto = read_file(path)
    except Exception:
        print("Error al leer el archivo")
        exit(0)

    tokens = generadorTokensSinProcesar(texto)
    salida = clasificadorDeTokens(tokens)

    # Filtrar errores léxicos antes de proceder
    for token in salida:
        if isinstance(token, Error):
            # Escribimos el error en el archivo de análisis sintáctico
            with open("analisis_sintactico.txt", "w", encoding="utf-8") as output_file:
                output_file.write(str(token) + "\n")
            sys.exit(1)

    # Implementar el parser utilizando los tokens
    parser(salida)

    # Guardar los tokens en un archivo (opcional)
    output_file_tokens = "analisis_tokens.txt"

    with open(output_file_tokens, "w", encoding="UTF-8") as file:
        for token in salida:
            file.write(str(token) + "\n")


if __name__ == "__main__":
    main()
