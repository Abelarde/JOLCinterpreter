from Abstract.NodoAST import NodoAST


class BreakInst(NodoAST):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return self

    def getNodo(self):
        return None
