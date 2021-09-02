from Abstract.NodoAST import NodoAST
from Abstract.NodoReporteArbol import NodoReporteArbol, Expresion
from Abstract.Objeto import TipoObjeto
from Objeto.Primitivo import Primitivo
from TS.Excepcion import Excepcion
from TS.Tipo import OperadorRelacional


class Relacional(NodoAST):
    def __init__(self, operador, operadorIzq, operadorDer, fila, columna):
        self.operador = operador
        self.operadorIzq = operadorIzq
        self.operadorDer = operadorDer
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        res_left = self.OperacionIzq.interpretar(tree, table)
        res_right = self.OperacionDer.interpretar(tree, table)

        if res_left.tipo == TipoObjeto.ERROR:
            return res_left

        if res_right.tipo == TipoObjeto.ERROR:
            return res_right

        if self.operador == OperadorRelacional.MAYORIGUAL:
            return Primitivo(TipoObjeto.BOOLEANO, int(str(res_left.getValue())) >= int(str(res_right.getValue())));

        if self.operador == OperadorRelacional.MAYORQUE:
            return Primitivo(TipoObjeto.BOOLEANO, int(str(res_left.getValue())) > int(str(res_right.getValue())));

        if self.operador == OperadorRelacional.MENORIGUAL:
            return Primitivo(TipoObjeto.BOOLEANO, int(str(res_left.getValue())) <= int(str(res_right.getValue())));

        if self.operador == OperadorRelacional.MENORQUE:
            return Primitivo(TipoObjeto.BOOLEANO, int(str(res_left.getValue())) < int(str(res_right.getValue())));

        if self.operador == OperadorRelacional.IGUALIGUAL:
            return Primitivo(TipoObjeto.BOOLEANO, int(str(res_left.getValue())) == int(str(res_right.getValue())));

        if self.operador == OperadorRelacional.DIFERENTE:
            return Primitivo(TipoObjeto.BOOLEANO, int(str(res_left.getValue())) != int(str(res_right.getValue())));

        return Excepcion("Semantico", f"Operador desconocido: {self.operador}", self.fila, self.columna);


    def getNodo(self):
        nodo = NodoReporteArbol(Expresion.RELACIONAL)
        nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
        nodo.agregarHijo(str(self.operador))
        nodo.agregarHijoNodo(self.OperacionDer.getNodo())
        return nodo
