from Abstract.NodoAST import NodoAST
from Abstract.NodoReporteArbol import NodoReporteArbol, Expresion
from Abstract.Objeto import TipoObjeto
from Objeto.Primitivo import Primitivo
from TS.Tipo import OperadorLogico


class Logica(NodoAST):
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

        if self.operador == OperadorLogico.OR:
            return Primitivo(TipoObjeto.BOOL, bool(str(res_left.getValue())) or bool(str(res_right.getValue())))

        if self.operador == OperadorLogico.AND:
            return Primitivo(TipoObjeto.BOOL, bool(str(res_left.getValue())) and bool(str(res_right.getValue())))

        if self.operador == OperadorLogico.NOT:
            return Primitivo(TipoObjeto.BOOL, not bool(str(res_right.getValue())))

        return Exception("Semantico", f"Operador desconocido: {self.operador}", self.fila, self.columna)


    def getNodo(self):
        nodo = NodoReporteArbol(Expresion.LOGICA)
        if self.operadorDer is not None:
            nodo.agregarHijoNodo(self.operadorIzq.getNodo())
            nodo.agregarHijoNodo(self.operador)
            nodo.agregarHijoNodo(self.operadorDer.getNodo())
        else:
            nodo.agregarHijo(self.operador)
            nodo.agregarHijoNodo(self.operadorIzq.getNodo())
        return nodo
