from Abstract.NodoAST import NodoAST


class Constante(NodoAST):
    def __init__(self, valor, fila, columna):
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
