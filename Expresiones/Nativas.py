from Abstract.NodoAST import NodoAST


class Nativas(NodoAST):
    def __init__(self, funcion_nativa, expresion_uno, expresion_dos, tipo_dato, fila, columna):
        self.funcion_nativa = funcion_nativa
        self.expresion_uno = expresion_uno
        self.expresion_dos = expresion_dos
        self.tipo_dato = tipo_dato
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
