from Abstract.NodoAST import NodoAST


class Logica(NodoAST):
    def __init__(self, operador, operadorIzq, operadorDer, fila, columna):
        self.operador = operador
        self.operadorIzq = operadorIzq
        self.operadorDer = operadorDer
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
