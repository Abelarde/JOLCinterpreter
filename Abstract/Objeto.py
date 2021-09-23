from abc import ABC, abstractmethod
from enum import Enum

# NOTE: TIPO DE LOS OBJETOS EN EL LENGUAGE
# TIPO DE LAS VARIABLES (OBJETOS) QUE VOY A CREAR


class TipoObjeto(Enum):
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

# NOTE: VALOR DE LOS SIMBOLOS
# INTERFAZ PARA LOS OBJETOS QUE VOY A CREAR
class Objeto(ABC):
    def __init__(self, tipo):
        self.tipo = tipo
        super().__init__()

    @abstractmethod
    def toString(self):
        pass

    @abstractmethod
    def getValue(self):
        pass
