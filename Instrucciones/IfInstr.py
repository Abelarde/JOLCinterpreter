from Abstract.NodoAST import NodoAST


class IfInstr(NodoAST):
    def __init__(self, tipo_if, condicion, instrucciones_if, instrucciones_else, instrucciones_else_if, fila, columna):
        self.tipo_if = tipo_if
        self.condicion = condicion
        self.instrucciones_if = instrucciones_if
        self.instrucciones_else = instrucciones_else
        self.instrucciones_else_if = instrucciones_else_if
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
