from Abstract.NodoAST import NodoAST


class ForCondicionInstr(NodoAST):
    def __init__(self, tipo, expresion_uno, expresion_dos, fila, columna):
        self.tipo = tipo
        self.expresion_uno = expresion_uno
        self.expresion_dos = expresion_dos
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
