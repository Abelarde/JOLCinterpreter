import ply.lex as lex
import ply.yacc as yacc

reservadas = {
    # PALABRAS RESERVADAS
    'nothing': 'NULO',
    'Int64': 'INT64',
    'Float64': 'FLOAT64',
    'Bool': 'BOOL',
    'true': 'TRUE',
    'false': 'FALSE',
    'Char': 'CHAR',
    'String': 'STRING',
    'Struct': 'STRUCT', # TODO: minuscula o mayuscula (incial)
    'Mutable': 'MUTABLE',
    'end': 'END',

    'println': 'PRINTLN',
    'print': 'PRINT',
    'uppercase': 'UPPERCASE',
    'lowercase': 'LOWERCASE',
    'log10': 'LOG10',
    'log': 'LOG',
    'sin': 'SIN',
    'cos': 'COS',
    'tan': 'TAN',
    'sqrt': 'SQRT',

    'global': 'GLOBAL',
    'local': 'LOCAL',

    'function': 'FUNCTION',

    'parse': 'PARSE',
    'trunc': 'TRUNC',
    'float': 'FLOAT',
    # 'string': 'STRING',   # TODO: ver si ya no es necesaria esta por la que esta arriba
    'typeof': 'TYPEOF',

    'if': 'IF',
    'elseif': 'ELSEIF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',

    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN'
}

tokens = [
    'PUNTOYCOMA',
    'CORIZQ',
    'CORDER',
    'COMA',
    'DOSPUNTOSDOSPUNTOS',
    'DOSPUNTOS',

    'PARIZQ',
    'PARDER',

    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'POTENCIA',
    'MODULO',

    'MAYOR',
    'MENOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALIGUAL',
    'DIFERENTE',
    'IGUAL',

    'OR',
    'AND',
    'NOT',

    'DOLAR',
    'PUNTO',

    'DECIMAL',
    'ENTERO',
    'CARACTER',
    'CADENA',
    'ID'
] + list(reservadas.values())

# HACEMOS USO DE r
t_PUNTOYCOMA = r'\;'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_COMA = r'\,'
t_DOSPUNTOSDOSPUNTOS = r'\::'
t_DOSPUNTOS = r'\:'

t_PARIZQ = r'\('
t_PARDER = r'\)'

t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIV = r'\/'
t_POTENCIA = r'\^'
t_MODULO = r'\%'

t_MAYOR = r'\>'
t_MENOR = r'\<'
t_MAYORIGUAL = r'\>='
t_MENORIGUAL = r'\<='
t_IGUALIGUAL = r'\=='
t_DIFERENTE = r'\!='
t_IGUAL = r'\='

t_OR = r'\|\|'
t_AND = r'\&&'
t_NOT = r'\!'

t_DOLAR = r'\$'
t_PUNTO = r'\.'


# MAS PATRONES
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CARACTER(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas simples
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_COMENTARIO_MULTI(t):
    r'\#\=(.|\n)*?\\=\#'
    t.lexer.lineno += t.value.count('\n')

def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# CARACTERES IGNORADOS
t_ignore = "[ \t\r\f\v]"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# CONSTRUYENDO EL ANALIZADOR LEXICO==========
lexer = lex.lex()

# ASOCIACION DE OPERADORES Y PRECEDENCIA
precedence = (
    # ('right', IGUAL),
    # ('right', TERNARIO),
    ('right', 'OR'),  # TODO: el OR y AND son left pero en Julia aparecen right
    ('right', 'AND'),
    ('nonassoc', 'DIFERENTE', 'IGUALIGUAL', 'MENORIGUAL', 'MAYORIGUAL', 'MENOR', 'MAYOR'),
    # (left, DOSPUNTOS),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIV', 'MODULO'),
    # ('right', 'UMENOS'),
    ('right', 'POTENCIA'),
    ('right', 'NOT'),
    ('right','UMENOS')
    # ('left', 'PUNTO', 'DOSPUNTODOSPUNTOS'),
)

# DEFINICION DE GRAMATICA======================
def p_init(t):
    'inicio             : instrucciones'
    t[0] = t[1]

def p_instrucciones_s1(t):
    'instrucciones      : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_s2(t):
    'instrucciones      : instruccion'
    t[0] = [t[1]]

def p_instruccion_s1(t):
    '''instruccion      : print_instr
                        | declaracion_instr
                        | asignacion_instr
                        | declaracion_asignacion_instr
                        | llamadaFuncion_instr
                        | funcion_instr
                        | if_instr
                        | while_instr
                        | for_instr
                        | BREAK
                        | CONTINUE
                        | RETURN
                        | parse
                        | trunc
                        | float
                        | string
                        | typeof
                        | push
                        | pop
                        | length
                        | raizCuadrada
                        | tangente
                        | coseno
                        | seno
                        | logaritmoBaseDiferente
                        | logaritmoComun'''

def p_print_instr_s1(t): # TODO: agregar el simbolo $
    'print_instr            : PRINTLN PARIZQ expresiones PARDER PUNTOYCOMA'
def p_print_instr_s2(t):
    'print_instr            : PRINT PARIZQ expresiones PARDER PUNTOYCOMA'
def p_declaracion_instr_s1(t): # VARIABLE
    '''declaracion_instr    : LOCAL ID PUNTOYCOMA
                            | GLOBAL ID PUNTOYCOMA'''
def p_declaracion_instr_s2(t): # STRUCT
    '''declaracion_instr    : STRUCT ID instrucciones END PUNTOYCOMA
                            | MUTABLE STRUCT ID instrucciones END PUNTOYCOMA'''
def p_asignacion_instr_s1(t): # VARIABLE Y ARRAY  antes=[ID IGUAL CORIZQ expresiones CORDER expresion PUNTOYCOMA]
    'asignacion_instr       : ID IGUAL expresion PUNTOYCOMA'
def p_declaracion_asignacion_instr_s1(t):
    'declaracion_asignacion_instr:  ID IGUAL expresion DOSPUNTOSDOSPUNTOS tipoDato PUNTOYCOMA'
def p_llamadaFuncion_instr_s1(t):
    'llamadaFuncion_instr   : ID PARIZQ expresiones PARDER PUNTOYCOMA'
def p_funcion_instr_s1(t):  #VALIDAR EL RETURN EN EL SEMANTICO TODO:siempre retornar 'nothing'
    'funcion_instr          : FUNCTION ID PARIZQ parametros PARDER instrucciones END PUNTOYCOMA'

# ==========================
def p_parametros_s1(t):
    'parametros        : parametros COMA parametro'
    t[1].append(t[2])
    t[0] = t[1]
def p_parametros_s2(t):
    'parametros        : parametro'
    t[0] = [t[1]]
def p_parametro_s1(t):
    '''parametro        : ID DOSPUNTOSDOSPUNTOS tipoDato
                        | ID'''

# ==========================
def p_if_instr(t):
    '''if_instr:        : IF expresion instrucciones END PUNTOYCOMA
                        | IF expresion instrucciones elseif_instr ELSE instrucciones END PUNTOYCOMA
                        | IF expresion instrucciones ELSE instrucciones END PUNTOYCOMA'''
def p_elseifs_s1(t):
    'elseifs            : elseifs COMA elseif_instr'
    t[1].append(t[2])
    t[0] = t[1]
def p_elseif_s2(t):
    'elseifs            : elseif_instr'
    t[0] = [t[1]]
def p_elseif_instr(t):
    'elseif_instr       : ELSEIF expresion instrucciones'

def p_while_instr(t):
    'while_instr        : WHILE expresion instrucciones END PUNTOYCOMA'

def p_for_instr(t): # EN EL SEMANTICO VALIDAR QUE TIPO ES LO QUE ITERARA Y DE AHI PROGRAMAR LA ACCION
    'for_instr          : FOR ID IN for_instr_opciones instrucciones END PUNTOYCOMA'
def p_for_instr_opciones(t):
    '''for_instr_opciones: ENTERO DOSPUNTOS ENTERO 
                        | expresion'''  # TODO: validar estos parametros

# ==========================



# ==========================
def p_expresiones_s1(t):
    'expresiones        : expresiones COMA expresion'
    t[1].append(t[2])
    t[0] = t[1]
def p_expresiones_s2(t):
    'expresiones        : expresion'
    t[0] = [t[1]]
def p_expresion(t): # TODO: unario
    '''expresion        : expresion MAS expresion
                        | expresion MENOS expresion
                        | expresion POR expresion
                        | expresion DIV expresion
                        | expresion POTENCIA expresion
                        | expresion MODULO expresion
                        | expresion MAYOR expresion
                        | expresion MENOR expresion
                        | expresion MAYORIGUAL expresion
                        | expresion MENORIGUAL expresion
                        | expresion IGUALIGUAL expresion
                        | expresion DIFERENTE expresion
                        | expresion OR expresion
                        | expresion AND expresion
                        | MENOS expresion %prec UMENOS
                        | NOT expresion
                        | DECIMAL
                        | ENTERO
                        | CARACTER
                        | CADENA
                        | TRUE
                        | FALSE
                        | NULO
                        | expresion PUNTO expresion
                        | ID PARDER expresiones PARIZQ
                        | ID expresion
                        | ID
                        | CORIZQ expresiones CORDER'''
                        # x[1] = 3;
                        # x[3][2]=55;

def p_tipoDatos(t):
    '''tipoDato         : NULO
                        | FLOAT64
                        | INT64
                        | BOOL
                        | CHAR
                        | STRING
                        | ID'''   # POR EJEMPLO ALGUN STRUCT

def p_error(t):
    print("Error sintáctico en '%s'" % str(t))

# CONSTRUYENDO EL ANALIZADOR SINTACTICO========
parser = yacc.yacc()

def parse(input):
    # Give the lexer some input
    lexer.input(input)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

    cad = parser.parse(input)  # TODO: porque ingresar al cad[x]?
    return str(cad)

"""
def parse(input):
    global contTemp
    global contEtq
    contTemp = 1
    contEtq = 1
    cad = parser.parse(input)
    return str(cad[2]) + '\n' + str(cad[0]) + ':\r\n' + 'ETIQUETA_VERDADERA' + '\r\n\n' + str(
        cad[1]) + ':\r\n' + 'ETIQUETA_FALSA\r\n'


x[1] = 3;
x[3][2]=55;

"""
# TODO: dejarlo mas completo en el sentido que recupere mas informacion. Y empezar a ver como sera la TDS
# TODO: hacer pruebas con los numeros, expresiones bien escritas