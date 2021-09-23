import math

from Abstract.NodoAST import NodoAST
from Abstract.NodoReporteArbol import NodoReporteArbol, Expresion
from Abstract.Objeto import TipoObjeto
from Objeto.Primitivo import Primitivo
from TS.Excepcion import Excepcion, TipoError
from TS.Tipo import OperadorAritmetico

#TODO: VERIFICAR TODOS LOS ELSE*, LOGICAS*, RELACIONALES*, NATIVAS*, VARIABLES, INSTRUCCIONES BASICAS
#TODO: VER LOS EJEMPLOS DEL PROYECTO ANTERIOR DONDE USO FLOAT O COSAS ASI*

class Aritmetica(NodoAST):
    def __init__(self, operador, operadorIzq, operadorDer, fila, columna):
        self.operador = operador
        self.operadorIzq = operadorIzq
        self.operadorDer = operadorDer
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        res_right = self.operadorDer.interpretar(tree, table)   # NOTE: CONSTANTE (NODOAST)- PRIMITIVO (OBJETO)

        if res_right.tipo == TipoObjeto.ERROR:
            return res_right

        res_left = None
        if self.operadorIzq is not None:
            res_left = self.operadorIzq.interpretar(tree, table)
            if res_left.tipo == TipoObjeto.ERROR:
                return res_left

        if self.operador == OperadorAritmetico.MAS:

            if res_right.tipo == TipoObjeto.INT64 or res_right.tipo == TipoObjeto.FLOAT64 or res_right.tipo == TipoObjeto.STRING:
                if res_left is not None:
                    if res_left.tipo == TipoObjeto.INT64 or res_left.tipo == TipoObjeto.FLOAT64 or res_left.tipo == TipoObjeto.STRING:

                        if res_left.tipo == TipoObjeto.STRING or res_right.tipo == TipoObjeto.STRING: # DOMINA STRING
                            return Primitivo(TipoObjeto.STRING, str(res_left.getValue()) + str(res_right.getValue()))
                        else:
                            if res_left.tipo == TipoObjeto.INT64: # IZQ INT64
                                if res_right.tipo == TipoObjeto.INT64:
                                    return Primitivo(TipoObjeto.INT64, res_left.getValue() + res_right.getValue())
                                elif res_right.tipo == TipoObjeto.FLOAT64:
                                    return Primitivo(TipoObjeto.FLOAT64, res_left.getValue() + res_right.getValue())
                            elif res_left.tipo == TipoObjeto.FLOAT64: # IZQ FLOAT54
                                return Primitivo(TipoObjeto.FLOAT64, res_left.getValue() + res_right.getValue())
                    else:
                        return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador izq para la operacion [+]", self.fila, self.columna)
                else:
                    return Primitivo(res_right.tipo, res_right.getValue())
            else:
                return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador der para la operacion [+]", self.fila, self.columna)

        elif self.operador == OperadorAritmetico.MENOS:

            if res_right.tipo == TipoObjeto.INT64 or res_right.tipo == TipoObjeto.FLOAT64:
                if res_left is not None:
                    if res_left.tipo == TipoObjeto.INT64 or res_left.tipo == TipoObjeto.FLOAT64:

                        if res_left.tipo == TipoObjeto.FLOAT64 or res_right.tipo == TipoObjeto.FLOAT64: # DOMINA FLOAT64
                            return Primitivo(TipoObjeto.FLOAT64, res_left.getValue() - res_right.getValue())
                        else:
                            if res_left.tipo == TipoObjeto.INT64: # IZQ INT64
                                if res_right.tipo == TipoObjeto.INT64:
                                    return Primitivo(TipoObjeto.INT64, res_left.getValue() - res_right.getValue())
                                elif res_right.tipo == TipoObjeto.FLOAT64:
                                    return Primitivo(TipoObjeto.FLOAT64, res_left.getValue() - res_right.getValue())
                            else:
                                return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no permitido para la operacion [-]", self.fila, self.columna)
                    else:
                        return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador izq para la operacion [-]", self.fila, self.columna)
                else:
                    return Primitivo(res_right.tipo, -1 * res_right.getValue())
            else:
                return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador der para la operacion [-]", self.fila, self.columna)

        elif self.operador == OperadorAritmetico.POR:

            if res_right.tipo == TipoObjeto.INT64 or res_right.tipo == TipoObjeto.FLOAT64:
                if res_left is not None:
                    if res_left.tipo == TipoObjeto.INT64 or res_left.tipo == TipoObjeto.FLOAT64:

                        if res_left.tipo == TipoObjeto.FLOAT64 or res_right.tipo == TipoObjeto.FLOAT64: # DOMINA FLOAT64
                            return Primitivo(TipoObjeto.FLOAT64, res_left.getValue() * res_right.getValue())
                        else:
                            if res_left.tipo == TipoObjeto.INT64: # IZQ INT64
                                if res_right.tipo == TipoObjeto.INT64:
                                    return Primitivo(TipoObjeto.INT64, res_left.getValue() * res_right.getValue())
                                elif res_right.tipo == TipoObjeto.FLOAT64:
                                    return Primitivo(TipoObjeto.FLOAT64, res_left.getValue() * res_right.getValue())
                            else:
                                return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no permitido para la operacion [*]", self.fila, self.columna)
                    else:
                        return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador izq para la operacion [*]", self.fila, self.columna)
                else:
                    return Primitivo(res_right.tipo, res_right.getValue())
            else:
                return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador der para la operacion [*]", self.fila, self.columna)

        elif self.operador == OperadorAritmetico.DIV:

            if res_right.tipo == TipoObjeto.INT64 or res_right.tipo == TipoObjeto.FLOAT64:
                if res_left is not None:
                    if res_left.tipo == TipoObjeto.INT64 or res_left.tipo == TipoObjeto.FLOAT64:
                        return Primitivo(TipoObjeto.FLOAT64, res_left.getValue() / res_right.getValue())
                    else:
                        return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador izq para la operacion [/]", self.fila, self.columna)
                else:
                    return Primitivo(res_right.tipo, res_right.getValue())
            else:
                return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador der para la operacion [/]", self.fila, self.columna)

        elif self.operador == OperadorAritmetico.POTENCIA:

            if res_right.tipo == TipoObjeto.INT64 or res_right.tipo ==  TipoObjeto.FLOAT64:
                if res_left is not None:
                    if res_left.tipo == TipoObjeto.INT64 or res_left.tipo == TipoObjeto.FLOAT64 or res_left.tipo == TipoObjeto.STRING:

                        if res_left.tipo == TipoObjeto.FLOAT64 or res_right.tipo == TipoObjeto.FLOAT64 : # DOMINA FLOAT64
                            if res_left.tipo != TipoObjeto.STRING or res_right.tipo != TipoObjeto.STRING:
                                return Primitivo(TipoObjeto.FLOAT64, math.pow(res_left.getValue(), res_right.getValue()))
                            else:
                                return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador izq para la operacion [^]", self.fila, self.columna)
                        else:
                            if res_left.tipo == TipoObjeto.INT64 and res_right.tipo == TipoObjeto.INT64: # LOS DOS INT
                                return Primitivo(TipoObjeto.INT64, int(math.pow(res_left.getValue(), res_right.getValue())))
                            elif res_left.tipo == TipoObjeto.STRING and res_right.tipo == TipoObjeto.INT64: # IZQ STRING
                                return Primitivo(TipoObjeto.STRING, str(res_left.getValue() * res_right.getValue()))

                    else:
                        return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador izq para la operacion [^]", self.fila, self.columna)
                else:
                    return Primitivo(res_right.tipo, res_right.getValue())
            else:
                return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador der para la operacion [^]", self.fila, self.columna)

        elif self.operador == OperadorAritmetico.MODULO:

            if res_right.tipo == TipoObjeto.INT64 or res_right.tipo == TipoObjeto.FLOAT64:
                if res_left is not None:
                    if res_left.tipo == TipoObjeto.INT64 or res_left.tipo == TipoObjeto.FLOAT64:

                        if res_left.tipo == TipoObjeto.FLOAT64 or res_right.tipo == TipoObjeto.FLOAT64: # DOMINA FLOAT64
                            return Primitivo(TipoObjeto.FLOAT64, res_left.getValue() % res_right.getValue())
                        else:
                            if res_left.tipo == TipoObjeto.INT64 and res_right.tipo == TipoObjeto.INT64: # IZQ INT64
                                return Primitivo(TipoObjeto.INT64, res_left.getValue() % res_right.getValue())

                    else:
                        return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador izq para la operacion [%]", self.fila, self.columna)
                else:
                    return Primitivo(res_right.tipo, res_right.getValue())
            else:
                return Excepcion(TipoError.SEMANTICO, f"Tipo de dato no valido del operador der para la operacion [%]", self.fila, self.columna)

        return Excepcion(TipoError.SEMANTICO, f"Operador desconocido: {self.operador}", self.fila, self.columna)


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
