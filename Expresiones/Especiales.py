from Abstract.NodoAST import NodoAST


class Especiales(NodoAST):
    def __init__(self, identificador, expresion_uno, expresion_dos, expresioness, tipo_dato, fila, columna):
        self.identificador = identificador
        self.expresion_uno = expresion_uno
        self.expresion_dos = expresion_dos
        self.expresioness = expresioness
        self.tipo_dato = tipo_dato
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
