from Abstract.NodoAST import NodoAST


class Declaracion(NodoAST):
    def __init__(self, local_global, identificador, expresion, fila, columna):
        self.local_global = local_global
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
