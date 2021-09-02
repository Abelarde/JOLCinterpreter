from Abstract.Objeto import Objeto, TipoObjeto

# CLASE PARA MANEJAR LOS ERRORES: LEXICOS, SINTACTICOS, SEMANTICOS.

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