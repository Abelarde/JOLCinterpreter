from Abstract.NodoAST import NodoAST


class Asignacion(NodoAST):
    def __init__(self, expresion_variable, expresion_valor, fila, columna):
        self.expresion_variable = expresion_variable
        self.expresion_valor = expresion_valor
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
