from Abstract.Objeto import Objeto, TipoObjeto
from enum import Enum

# NOTE: ERRORES DE CUALQUIER TIPO Y PODER USAR ESTA CLASE DONDE LA NECESITEMOS
# CLASE HIJA DE OBJETO
# PARA MANEJAR LOS ERRORES: LEXICOS, SINTACTICOS, SEMANTICOS.


# NOTE: ENUM'S PARA LA GRAMATICA
class TipoError(Enum):
    LEXICO = 1
    SINTACTICO = 2
    SEMANTICO = 3


class Excepcion(Objeto):
    def __init__(self, tipo, descripcion, fila, columna):
        self.tipoError = tipo
        self.descripcion = descripcion
        self.fila = fila
        self.columna = columna
        self.tipo = TipoObjeto.ERROR

    def toString(self):
        return self.tipoError + " - " + self.descripcion + " [" + str(self.fila) + "," + str(self.columna) + "]"

    def getValue(self):
        return "";