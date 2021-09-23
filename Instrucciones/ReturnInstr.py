from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion


class ReturnInstr(NodoAST):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.result = None
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        result = self.expresion.interpretar(tree, table)
        if isinstance(result, Excepcion): return result
        self.result = result            #VALOR DEL RESULT
        return self

    def getNodo(self):
        return None
