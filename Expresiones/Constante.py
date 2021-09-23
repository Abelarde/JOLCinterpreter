from Abstract.NodoAST import NodoAST
from Abstract.NodoReporteArbol import NodoReporteArbol, Expresion


class Constante(NodoAST):
    def __init__(self, valor, fila, columna):
        self.valor = valor  # NOTE: PRIMITIVO(OBJETO)
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return self.valor

    def getNodo(self):
        nodo = NodoReporteArbol(Expresion.CONSTANTES)
        nodo.agregarhijo(str(self.valor))
        return nodo


