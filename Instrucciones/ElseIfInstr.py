from Abstract.NodoAST import NodoAST


class ElseIfInstr(NodoAST):
    def __init__(self, condicion, instrucciones_if, fila, columna):
        self.condicion = condicion
        self.instrucciones_if = instrucciones_if
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
