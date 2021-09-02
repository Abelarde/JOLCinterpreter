from Abstract.NodoAST import NodoAST
from Abstract.NodoReporteArbol import NodoReporteArbol, Expresion
from Abstract.Objeto import TipoObjeto
from Objeto.Primitivo import Primitivo
from TS.Excepcion import Excepcion
from TS.Tipo import OperadorAritmetico


class Aritmetica(NodoAST):
    def __init__(self, operador, operadorIzq, operadorDer, fila, columna):
        self.operador = operador
        self.operadorIzq = operadorIzq
        self.operadorDer = operadorDer
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        res_left = self.operadorIzq.interpretar(tree, table)
        res_right = self.operadorDer.interpretar(tree, table)

        if res_left.tipo == TipoObjeto.ERROR:
            return res_left
        if res_right.tipo == TipoObjeto.ERROR:
            return res_right

        if self.operador == OperadorAritmetico.MAS:
            if res_left.tipo != TipoObjeto.ERROR and res_right.tipo != TipoObjeto.STRING:
                return Primitivo(TipoObjeto.INT64, int(str(res_left.getValue())) + int(str(res_right.getValue())))
            return Primitivo(TipoObjeto.STRING, str(res_left.getValue()) + str(res_right.getValue()))

        if self.operador == OperadorAritmetico.MENOS:
            return Primitivo(TipoObjeto.INT64, int(str(res_left.getValue())) - int(str(res_right.getValue())));

        if self.operador == OperadorAritmetico.POR:
            return Primitivo(TipoObjeto.INT64, int(str(res_left.getValue())) * int(str(res_right.getValue())));

        if self.operador == OperadorAritmetico.DIV:
            return Primitivo(TipoObjeto.INT64, int(str(res_left.getValue())) / int(str(res_right.getValue())));

        if self.operador == OperadorAritmetico.POTENCIA:
            return Primitivo(TipoObjeto.INT64, int(pow(str(res_left.getValue())), int(str(res_right.getValue()))));

        if self.operador == OperadorAritmetico.MODULO:
            return Primitivo(TipoObjeto.INT64, int(str(res_left.getValue())) % int(str(res_right.getValue())));

        return Excepcion("Semantico", f"Operador desconocido: {self.operador}", self.fila, self.columna)


    def getNodo(self):
        nodo = NodoReporteArbol(Expresion.ARITMETICA)
        if self.operadorDer is not None:
            nodo.agregarHijoNodo(self.operadorIzq.getNodo())
            nodo.agregarHijoNodo(self.operador)
            nodo.agregarHijoNodo(self.operadorDer.getNodo())
        else:
            nodo.agregarHijo(self.operador)
            nodo.agregarHijoNodo(self.operadorIzq.getNodo())
        return nodo
