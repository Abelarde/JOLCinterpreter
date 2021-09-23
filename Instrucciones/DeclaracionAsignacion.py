from Abstract.NodoAST import NodoAST
from Abstract.Objeto import TipoObjeto
from TS.Excepcion import Excepcion, TipoError
from TS.Simbolo import Simbolo
from TS.Tipo import Instrucciones


class DeclaracionAsignacion(NodoAST):
    def __init__(self, id, expresion, tipo, fila, columna):
        self.id = id
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        if self.expresion is None:
            return Excepcion(TipoError.SEMANTICO, f"Error al obtener el valor de la asignacion", self.fila,
                             self.columna)

        valor = self.expresion.interpretar(tree, table)
        if valor.tipo == TipoObjeto.ERROR:
            return valor

        '''if valor.tipo != self.tipo:
            return Excepcion(TipoError.SEMANTICO, f"Tipo de dato incorrecto con el valor que esta asignando", self.fila,
                             self.columna)
'''
        simbolo = Simbolo(self.id, self.fila, self.columna, valor)
        result = table.actualizarTabla(simbolo)  # actualiza o crea un nuevo simbolo
        if isinstance(result, Excepcion): return result
        return None

    def getNodo(self):
        return None
