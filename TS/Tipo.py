from enum import Enum


# TODO: averiguar la diferencia entre este tipo y el tipo dentro de Objeto
class TIPO(Enum):
    NULO = 1
    FLOAT64 = 2
    INT64 = 3
    BOOL = 4
    CHAR = 5
    STRING = 6
    ID = 7  # algun tipo de algun struct o variable
    ARRAY = 8
    STRUCT_MUTABLE = 9  # cuando se declara
    STRUCT_NO_MUTABLE = 10  # cuando se declara
    FUNCTION = 11  # cuando se declara
    LOCAL = 12  # cuando se declara
    GLOBAL = 13  # cuando se declara
    ERROR = 14

class OperadorAritmetico(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIV = 4
    POTENCIA = 5
    MODULO = 6

class OperadorRelacional(Enum):
    MENORQUE = 1
    MAYORQUE = 2
    MENORIGUAL = 3
    MAYORIGUAL = 4
    IGUALIGUAL = 5
    DIFERENTE = 6

class OperadorLogico(Enum):
    NOT = 1
    AND = 2
    OR = 3

class FuncionesPrimitivas(Enum):
    SQRT = 1
    TAN = 2
    COS = 3
    SIN = 4
    LOG = 5
    LOG10 = 6
    PARSE = 7
    TRUNC = 8
    FLOAT = 9
    STRING = 10
    TYPEOF = 11
    PUSH = 12
    POP = 13
    LENGTH = 14
    UPPERCASE = 15
    LOWERCASE = 16

class TiposEspeciales(Enum):
    ACCESO_OBJETO = 1
    LLAMADA_FUNCION = 2
    ARREGLO_ARMADO = 3
    ARREGLO_DOSPUNTOS = 4
    ARREGLO_CORCHETES = 5

class Instrucciones(Enum):
    IF_1 = 1
    IF_2 = 2
    IF_3 = 3
    PARAMETRO_TIPO = 4
    PARAMETRO_VARIABLE = 5
    STRUCT_VARIABLE_TIPO = 7
    STRUCT_VARIABLE = 8
    PRINT = 9
    PRINT_LN = 10
    FOR_VARIABLE = 11
    FOR_RANGO = 12