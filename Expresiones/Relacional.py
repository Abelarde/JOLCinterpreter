from Abstract.NodoAST import NodoAST
from Abstract.NodoReporteArbol import NodoReporteArbol, Expresion
from Abstract.Objeto import TipoObjeto
from Objeto.Primitivo import Primitivo
from TS.Excepcion import Excepcion, TipoError
from TS.Tipo import OperadorRelacional


class Relacional(NodoAST):
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

        if (res_left.tipo == TipoObjeto.INT64 or res_left.tipo == TipoObjeto.FLOAT64 or res_left.tipo == TipoObjeto.STRING or res_left.tipo == TipoObjeto.BOOL) and (res_right.tipo == TipoObjeto.INT64 or res_right.tipo == TipoObjeto.FLOAT64 or res_right.tipo == TipoObjeto.STRING or res_right.tipo == TipoObjeto.BOOL):
            if self.operador == OperadorRelacional.MAYORIGUAL:
                return Primitivo(TipoObjeto.BOOL, float(str(res_left.getValue())) >= float(str(res_right.getValue())));

            elif self.operador == OperadorRelacional.MAYORQUE:
                return Primitivo(TipoObjeto.BOOL, float(str(res_left.getValue())) > float(str(res_right.getValue())));

            elif self.operador == OperadorRelacional.MENORIGUAL:
                return Primitivo(TipoObjeto.BOOL, float(str(res_left.getValue())) <= float(str(res_right.getValue())));

            elif self.operador == OperadorRelacional.MENORQUE:
                return Primitivo(TipoObjeto.BOOL, float(str(res_left.getValue())) < float(str(res_right.getValue())));

            elif self.operador == OperadorRelacional.IGUALIGUAL:
                if res_left.tipo == TipoObjeto.STRING or res_right.tipo == TipoObjeto.STRING:
                    return Primitivo(TipoObjeto.BOOL, str(res_left.getValue()) == str(res_right.getValue()))
                elif res_left.tipo == TipoObjeto.BOOL or res_right.tipo == TipoObjeto.BOOL:
                    return Primitivo(TipoObjeto.BOOL, bool(res_left.getValue()) == bool(res_right.getValue()))
                else:
                    return Primitivo(TipoObjeto.BOOL, float(str(res_left.getValue())) == float(str(res_right.getValue())));

            elif self.operador == OperadorRelacional.DIFERENTE:
                if res_left.tipo == TipoObjeto.STRING or res_right.tipo == TipoObjeto.STRING:
                    return Primitivo(TipoObjeto.BOOL, str(res_left.getValue()) != str(res_right.getValue()));
                elif res_left.tipo == TipoObjeto.BOOL or res_right.tipo == TipoObjeto.BOOL:
                    return Primitivo(TipoObjeto.BOOL, bool(res_left.getValue()) != bool(res_right.getValue()))
                else:
                    return Primitivo(TipoObjeto.BOOL, float(str(res_left.getValue())) != float(str(res_right.getValue())));

            return Excepcion(TipoError.SEMANTICO, f"Operador desconocido: {self.operador}", self.fila, self.columna);
        else:
            return Excepcion(TipoError.SEMANTICO, f"Tipo de dato invalido en operacion relacional izq:{res_left.tipo} der: {res_right.tipo}", self.fila, self.columna);



    def getNodo(self):
        nodo = NodoReporteArbol(Expresion.RELACIONAL)
        nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
        nodo.agregarHijo(str(self.operador))
        nodo.agregarHijoNodo(self.OperacionDer.getNodo())
        return nodo
