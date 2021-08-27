from Abstract.NodoAST import NodoAST


class FuncionParametros(NodoAST):
    def __init__(self, identificador, tipo, fila, columna):
        self.identificador = identificador
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
