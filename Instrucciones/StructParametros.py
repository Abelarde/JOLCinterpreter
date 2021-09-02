from Abstract.NodoAST import NodoAST


class StructParametros(NodoAST):
    def __init__(self, var_tipo, identificador, tipo, fila, columna):
        self.var_tipo = var_tipo
        self.identificador = identificador
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
