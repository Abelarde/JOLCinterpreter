import re
import sys
import ply.lex as lex
import ply.yacc as yacc
from TS.Excepcion import Excepcion

sys.setrecursionlimit(3000)

errores = []
input = ''

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

    'push': 'PUSH',
    'pop': 'POP',
    'length': 'LENGTH',

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

    #'DOLAR',
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

#t_DOLAR = r'\$'
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
    errores.append(Excepcion("LEXICO", "Error lexico ", t.value[0], t.lexer.lineno, find_column(input, t)))
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def find_column(entrada, token):
    line_start = entrada.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

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
#ABSTRACTAS

from Instrucciones.Asignacion import Asignacion
from Instrucciones.BreakInstr import BreakInst
from Instrucciones.ContinueInstr import ContinueInstr
from Instrucciones.Declaracion import Declaracion
from Instrucciones.DeclaracionAsignacion import DeclaracionAsignacion
from Instrucciones.ForInstr import ForInst
from Instrucciones.Funcion import Funcion
from Instrucciones.FuncionParametros import FuncionParametros
from Instrucciones.IfInstr import IfInstr
from Instrucciones.Imprimir import Imprimir
from Instrucciones.LlamadaFuncion import LlamadaFuncion
from Instrucciones.ReturnInstr import ReturnInstr
from Instrucciones.StructInstr import StructInst
from Instrucciones.StructParametros import StructParametros
from Instrucciones.WhileInstr import WhileInst
from Instrucciones.ElseIfInstr import ElseIfInstr
from Instrucciones.ForCondicionInstr import ForCondicionInstr

from Expresiones.Aritmetica import Aritmetica
from Expresiones.Constante import Constante
from Expresiones.Especiales import Especiales
from Expresiones.Identificador import Identificador
from Expresiones.Logica import Logica
from Expresiones.Nativas import Nativas
from Expresiones.Relacional import Relacional

from TS.Tipo import TIPO, Instrucciones, TiposEspeciales, OperadorLogico, OperadorAritmetico, OperadorRelacional, FuncionesPrimitivas



# DEFINICION DE GRAMATICA======================
def p_init(t):
    'inicio             : instrucciones'
    t[0] = t[1]

def p_instrucciones_s1(t):
    'instrucciones      : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_s2(t):
    'instrucciones      : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instruccion_s1(t):
    '''instruccion      : print_instr
                        | declaracion_instr
                        | structs_instr
                        | asignacion_instr
                        | declaracion_asignacion_instr
                        | llamadaFuncion_instr
                        | funcion_instr
                        | if_instr
                        | while_instr
                        | for_instr
                        | break_instr
                        | continue_instr
                        | return_instr'''
                        # se puede validar que el break, continue, venga solo dentro de bucles y en cualquier
                        # otro lado es error
                        # return = solo dentro de una funcion (si viene, ahi se acaba la ejecucion y retorna
                        # de una ese valor)
    t[0] = t[1]

def p_instruccion_s2(t):
    'instruccion        : error PUNTOYCOMA'
    errores.append(Excepcion("SINTACTICO","Error Sintactico:" + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""

def p_print_instr_s1(t): # TODO: agregar el simbolo $
    'print_instr            : PRINTLN PARIZQ expresiones PARDER PUNTOYCOMA'
    t[0] = Imprimir(Instrucciones.PRINT_LN, t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_print_instr_s2(t):
    'print_instr            : PRINT PARIZQ expresiones PARDER PUNTOYCOMA'
    t[0] = Imprimir(Instrucciones.PRINT, t[3], t.lineno(1), find_column(input, t.slice[1]))


def p_declaracion_instr_s1(t): # VARIABLE
    '''declaracion_instr    : LOCAL ID IGUAL expresion PUNTOYCOMA
                            | GLOBAL ID IGUAL expresion PUNTOYCOMA'''
    if t[1] == 'LOCAL':   # TODO: ver si se puede validar por el nombre del terminal y no por un string
        t[0] = Declaracion(TIPO.LOCAL, t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'GLOBAL':
        t[0] = Declaracion(TIPO.GLOBAL, t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))

def p_declaracion_instr_s2(t): # VARIABLE
    '''declaracion_instr    : LOCAL ID PUNTOYCOMA
                            | GLOBAL ID PUNTOYCOMA'''
    if t[1] == 'LOCAL':
        t[0] = Declaracion(TIPO.LOCAL, t[2], None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'GLOBAL':
        t[0] = Declaracion(TIPO.GLOBAL, t[2], None, t.lineno(1), find_column(input, t.slice[1]))

def p_declaracion_instr_s3(t): # STRUCT
    '''structs_instr        : STRUCT ID struct_variables END PUNTOYCOMA
                            | MUTABLE STRUCT ID struct_variables END PUNTOYCOMA'''
    if t[1] == 'STRUCT':
        t[0] = StructInst(TIPO.STRUCT_NO_MUTABLE, t[2], t[3], t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'MUTABLE':
        t[0] = StructInst(TIPO.STRUCT_MUTABLE, t[2], t[3], t.lineno(1), find_column(input, t.slice[1]))


def p_struct_variables_instr_s1(t):
    'struct_variables      : struct_variables struct_variable'
    t[1].append(t[2])
    t[0] = t[1]

def p_struct_variables_instr_s2(t):
    'struct_variables      : struct_variable'
    t[0] = [t[1]]

def p_struct_variable(t):
    '''struct_variable      : ID DOSPUNTOSDOSPUNTOS tipoDato PUNTOYCOMA
                            | ID PUNTOYCOMA'''
    if len(t) == 5:
        t[0] = StructParametros(Instrucciones.STRUCT_VARIABLE_TIPO, t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))
    elif len(t) == 3:
        t[0] = StructParametros(Instrucciones.STRUCT_VARIABLE, t[1], None, t.lineno(1), find_column(input, t.slice[1]))


def p_asignacion_instr_s1(t): # VARIABLE Y ARRAY  antes=[ID IGUAL CORIZQ expresiones CORDER expresion PUNTOYCOMA]
    'asignacion_instr       : expresion IGUAL expresion PUNTOYCOMA'
                            # validar que la expresion que viene es de tipo:
                            # ID
                            # arreglo
                            # arr = [1,2,3,4,5,6];  x[3][2]=55; x[1] = 3;  variable = 3;
    t[0] = Asignacion(t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))

def p_declaracion_asignacion_instr_s1(t):
    'declaracion_asignacion_instr   :  ID IGUAL expresion DOSPUNTOSDOSPUNTOS tipoDato PUNTOYCOMA'
    t[0] = DeclaracionAsignacion(t[1], t[3], t[5], t.lineno(1), find_column(input, t.slice[1]))


def p_llamadaFuncion_instr_s1(t):
    'llamadaFuncion_instr   : ID PARIZQ expresiones PARDER PUNTOYCOMA'
    t[0] = LlamadaFuncion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_funcion_instr_s1(t):  #VALIDAR EL RETURN EN EL SEMANTICO TODO:siempre retornar 'nothing'
    'funcion_instr          : FUNCTION ID PARIZQ parametros PARDER instrucciones END PUNTOYCOMA'
    t[0] = Funcion(t[2], t[4], t[6], t.lineno(1), find_column(input, t.slice[1]))

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
                        # TODO: se permitira un id como parametro
    if len(t) == 4:
        t[0] = FuncionParametros(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))
    elif len(t) == 2:
        t[0] = FuncionParametros(t[1], None, t.lineno(1), find_column(input, t.slice[1]))

# ==========================
def p_if_instr(t):
    '''if_instr        : IF expresion instrucciones END PUNTOYCOMA
                        | IF expresion instrucciones elseifs ELSE instrucciones END PUNTOYCOMA
                        | IF expresion instrucciones ELSE instrucciones END PUNTOYCOMA'''
    if len(t) == 6:
        t[0] = IfInstr(Instrucciones.IF_1, t[2], t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif len(t) == 9:
        t[0] = IfInstr(Instrucciones.IF_2, t[2], t[3], t[6], t[4], t.lineno(1), find_column(input, t.slice[1]))
    elif len(t) == 8:
        t[0] = IfInstr(Instrucciones.IF_3, t[2], t[3], t[5], None, t.lineno(1), find_column(input, t.slice[1]))

def p_elseifs_s1(t):
    'elseifs            : elseifs COMA elseif_instr'
    t[1].append(t[3])
    t[0] = t[1]
def p_elseif_s2(t):
    'elseifs            : elseif_instr'
    t[0] = [t[1]]
def p_elseif_instr(t):
    'elseif_instr       : ELSEIF expresion instrucciones'
    t[0] = ElseIfInstr(t[2], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_while_instr(t):
    'while_instr        : WHILE expresion instrucciones END PUNTOYCOMA'
    t[0] = WhileInst(t[2], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_for_instr(t): # EN EL SEMANTICO VALIDAR QUE TIPO ES LO QUE ITERARA Y DE AHI PROGRAMAR LA ACCION
    'for_instr          : FOR ID IN for_instr_opciones instrucciones END PUNTOYCOMA'
    t[0] = ForInst(t[2], t[4], t[5], t.lineno(1), find_column(input, t.slice[1]))

def p_for_instr_opciones(t):
    '''for_instr_opciones   : expresion DOSPUNTOS expresion
                            | expresion'''
                        # ENTERO :: ENTERO
                        # id, string, arreglo, variable === expresion
                        # TODO: validar estos parametros
    if len(t) == 4:
        t[0] = ForCondicionInstr(Instrucciones.FOR_RANGO, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif len(t) == 2:
        t[0] = ForCondicionInstr(Instrucciones.FOR_VARIABLE, t[1], None, t[1].fila, t[1].columna) # TODO: verificarq que esto no produzca error alguno

def p_break_instr_s1(t):
    'break_instr            : BREAK PUNTOYCOMA'
    t[0] = BreakInst(t.lineno(1), find_column(input, t.slice[1]))

def p_return_instr_s1(t):
    'return_instr            : RETURN expresion PUNTOYCOMA'
    t[0] = ReturnInstr(t[2], t.lineno(1), find_column(input, t.slice[1]))

def p_continue_instr_s1(t):
    'continue_instr            : CONTINUE PUNTOYCOMA'
    t[0] = ContinueInstr(t.lineno(1), find_column(input, t.slice[1]))
# ==========================



# ==========================
def p_expresiones_s1(t):
    'expresiones        : expresiones COMA expresion'
    t[1].append(t[2])
    t[0] = t[1]
def p_expresiones_s2(t):
    'expresiones        : expresion'
    t[0] = [t[1]]
def p_expresion_s1(t): # TODO: unario
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
                        | expresion AND expresion'''
    if t[2] == '+':
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/':
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '^':
        t[0] = Aritmetica(OperadorAritmetico.POTENCIA, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(OperadorAritmetico.MODULO, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(OperadorRelacional.MENORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(OperadorRelacional.MENORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(OperadorRelacional.IGUALIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '!=':
        t[0] = Relacional(OperadorRelacional.DIFERENTE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(OperadorLogico.OR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))


def p_expresion_s2(t): # TODO: unario
    '''expresion        : MENOS expresion %prec UMENOS
                        | NOT expresion'''
    if len(t) == 3:
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[2], None, t.lineno(1), find_column(input, t.slice[1]))
    else:
        t[0] = Logica(OperadorLogico.NOT, t[2], None, t.lineno(1), find_column(input, t.slice[1]))


def p_expresion_s3(t): # TODO: unario
    '''expresion        : DECIMAL
                        | ENTERO
                        | CARACTER
                        | CADENA
                        | TRUE
                        | FALSE
                        | NULO'''

def p_expresion_s4(t):
    '''expresion        : SQRT PARIZQ expresion PARDER
                        | TAN PARIZQ expresion PARDER
                        | COS PARIZQ expresion PARDER
                        | SIN PARIZQ expresion PARDER
                        | LOG PARIZQ expresion COMA expresion PARDER
                        | LOG10 PARIZQ expresion PARDER
                        | PARSE PARIZQ tipoDato COMA expresion PARDER
                        | TRUNC PARIZQ tipoDato COMA expresion PARDER
                        | FLOAT PARIZQ expresion PARDER
                        | STRING PARIZQ expresion PARDER
                        | TYPEOF PARIZQ expresion PARDER
                        | PUSH NOT PARIZQ expresion COMA expresion PARDER
                        | POP NOT PARIZQ expresion PARDER
                        | LENGTH PARIZQ expresion PARDER
                        | UPPERCASE PARIZQ expresion PARDER
                        | LOWERCASE PARIZQ expresion PARDER'''
    if t[1] == 'SQRT':
        t[0] = Nativas(FuncionesPrimitivas.SQRT, t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'TAN':
        t[0] = Nativas(FuncionesPrimitivas.TAN, t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'COS':
        t[0] = Nativas(FuncionesPrimitivas.COS, t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'SIN':
        t[0] = Nativas(FuncionesPrimitivas.SIN, t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'LOG':
        t[0] = Nativas(FuncionesPrimitivas.LOG, t[3], t[5], None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'LOG10':
        t[0] = Nativas(FuncionesPrimitivas.LOG10, t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'PARSE':
        t[0] = Nativas(FuncionesPrimitivas.PARSE, t[5], None, t[3], t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'TRUNC':
        t[0] = Nativas(FuncionesPrimitivas.TRUNC, t[5], None, t[3], t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'FLOAT':
        t[0] = Nativas(FuncionesPrimitivas.FLOAT, t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'STRING':
        t[0] = Nativas(FuncionesPrimitivas.STRING, t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'TYPEOF':
        t[0] = Nativas(FuncionesPrimitivas.TYPEOF, t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'PUSH':
        t[0] = Nativas(FuncionesPrimitivas.PUSH, t[4], t[6], None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'POP':
        t[0] = Nativas(FuncionesPrimitivas.POP, t[4], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'LENGTH':
        t[0] = Nativas(FuncionesPrimitivas.LENGTH, t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'UPPERCASE':
        t[0] = Nativas(FuncionesPrimitivas.UPPERCASE, t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'LOWERCASE':
        t[0] = Nativas(FuncionesPrimitivas.LOWERCASE, t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))


def p_expresion_s5(t):
    '''expresion        : expresion PUNTO expresion
                        | ID PARIZQ expresiones PARDER
                        | ID expresion
                        | ID
                        | CORIZQ expresion DOSPUNTOS expresion CORDER
                        | CORIZQ expresiones CORDER
                        | PARIZQ expresiones PARDER'''
                        # x[1] = 3;
                        # x[3][2]=55;
                        # TODO: arreglo = [32, 21, 7, 89, 56, 909, 109, 2, 9, 1, 44, 3, 8200, 11, 8, 10];
                        # copiaArreglo = arreglo[:];

                        #PUEDE SER LA LLAMDA A UNA FUNCION || PUEDE SER LA CREACION DE UN STRUCT COMO EXPRESION

def p_tipoDatos(t):
    '''tipoDato         : NULO
                        | FLOAT64
                        | INT64
                        | BOOL
                        | CHAR
                        | STRING
                        | ID'''
                        # POR EJEMPLO ALGUN STRUCT
    if t[1] == 'NULO':
        t[0] = TIPO.NULO
    elif t[1] == 'FLOAT64':
        t[0] = TIPO.FLOAT64
    elif t[1] == 'INT64':
        t[0] = TIPO.INT64
    elif t[1] == 'BOOL':
        t[0] = TIPO.BOOL
    elif t[1] == 'CHAR':
        t[0] = TIPO.CHAR
    elif t[1] == 'STRING':
        t[0] = TIPO.STRING
    elif t[1] == 'ID':
        t[0] = TIPO.ID

def p_error(t):
    print("Error sintáctico en '%s'" % str(t))

# CONSTRUYENDO EL ANALIZADOR SINTACTICO========
from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos

parser = yacc.yacc()

def getErrores():
    return errores

def parse(inp):
    global errores  # reference to global variables
    global lexer
    global parser

    lexer.input(inp)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

    cad = parser.parse(inp)  # TODO: porque ingresar al cad[x]?
    for item in cad:
        print(item)


    errores = []
    lexer = lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()

    global input
    input = inp

    instrucciones = parser.parse(inp)
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolos()
    ast.setTSglobal(TSGlobal)

    # TODO: captura de errores lexicos y sintacticos

    for instruccion in ast.getInstrucciones():
        if isinstance(instruccion, Funcion):
            ast.addFuncion(instruccion)
        elif isinstance(instruccion, ReturnInstr):
            errores.append(Excepcion("SINTACTICO", "instruccion return en lugar no valido" , instruccion.fila, instruccion.columna))
        elif isinstance(instruccion, BreakInst):
            errores.append(Excepcion("SINTACTICO", "instruccion break en lugar no valido" , instruccion.fila, instruccion.columna))
        elif isinstance(instruccion, ContinueInstr):
            errores.append(Excepcion("SINTACTICO", "instruccion contine en lugar no valido" , instruccion.fila, instruccion.columna))
        else:
            instruccion.interpretar(ast, TSGlobal)

    return ast



"""
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