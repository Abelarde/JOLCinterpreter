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
        res_right = self.operadorDer.interpretar(tree, table)

        if res_right.tipo == TipoObjeto.ERROR:
            return res_right

        res_left = None
        if self.operadorIzq is not None:
            res_left = self.operadorIzq.interpretar(tree, table)
            if res_left.tipo == TipoObjeto.ERROR:
                return res_left

        if res_right.tipo == TipoObjeto.BOOL:
            if self.operador == OperadorLogico.OR or self.operador == OperadorLogico.AND:
                if res_left is not None and res_left.tipo == TipoObjeto.BOOL:
                    if self.operador == OperadorLogico.OR:
                        return Primitivo(TipoObjeto.BOOL, res_left.getValue() or res_right.getValue())
                    elif self.operador == OperadorLogico.AND:
                        return Primitivo(TipoObjeto.BOOL, res_left.getValue() and res_right.getValue())
                else:
                    return Exception("Semantico", f"Tipo error al obtener el valor izq", self.fila, self.columna)
            elif self.operador == OperadorLogico.NOT:
                return Primitivo(TipoObjeto.BOOL, not bool(str(res_right.getValue())))
            else:
                return Exception("Semantico", f"Operador desconocido: {self.operador}", self.fila, self.columna)
        else:
            return Exception("Semantico", f"Tipo de datos invalidos para una operacion logica der{res_right.tipo}", self.fila, self.columna)



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
