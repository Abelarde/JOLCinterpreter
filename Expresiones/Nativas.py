import math

from Abstract.NodoAST import NodoAST
from Abstract.NodoReporteArbol import NodoReporteArbol, Expresion
from Abstract.Objeto import TipoObjeto
from Objeto.Primitivo import Primitivo
from TS.Excepcion import Excepcion
from TS.Tipo import FuncionesPrimitivas


class Nativas(NodoAST):
    def __init__(self, funcion_nativa, expresion_uno, expresion_dos, tipo_dato, fila, columna):
        self.funcion_nativa = funcion_nativa
        self.expresion_uno = expresion_uno
        self.expresion_dos = expresion_dos
        self.tipo_dato = tipo_dato
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        res_uno = self.expresion_uno.interpretar(tree, table)
        res_dos = self.expresion_dos.interpretar(tree, table)

        if res_uno.tipo == TipoObjeto.ERROR:
            return res_uno

        if res_dos.tipo == TipoObjeto.ERROR:
            return res_dos

        # TODO: validaciones o try except: https://www.geeksforgeeks.org/python-math-function-sqrt/

        if self.funcion_nativa == FuncionesPrimitivas.SQRT:
            return Primitivo(TipoObjeto.FLOAT64, math.sqrt(int(str(res_uno.getValue()))))

        if self.funcion_nativa == FuncionesPrimitivas.TAN:
            return Primitivo(TipoObjeto.FLOAT64, math.tan(int(str(res_uno.getValue()))))

        if self.funcion_nativa == FuncionesPrimitivas.COS:
            return Primitivo(TipoObjeto.FLOAT64, math.cos(int(str(res_uno.getValue()))))

        if self.funcion_nativa == FuncionesPrimitivas.SIN:
            return Primitivo(TipoObjeto.FLOAT64, math.sin(int(str(res_uno.getValue()))))

        if self.funcion_nativa == FuncionesPrimitivas.LOG:
            return Primitivo(TipoObjeto.FLOAT64, math.log(int(str(res_uno.getValue())), int(str(res_dos.getValue()))))

        if self.funcion_nativa == FuncionesPrimitivas.LOG10:
            return Primitivo(TipoObjeto.FLOAT64, math.log10(int(str(res_uno.getValue()))))

        if self.funcion_nativa == FuncionesPrimitivas.PARSE:
            if self.tipo_dato == TipoObjeto.FLOAT64:
                return Primitivo(TipoObjeto.FLOAT64, float(str(res_uno.getValue())))
            elif self.tipo_dato == TipoObjeto.INT64:
                return Primitivo(TipoObjeto.INT64, int(str(res_uno.getValue())))

        if self.funcion_nativa == FuncionesPrimitivas.TRUNC:
            if self.tipo_dato == TipoObjeto.INT64:
                return Primitivo(TipoObjeto.INT64, int(str(res_uno.getValue())))

        if self.funcion_nativa == FuncionesPrimitivas.FLOAT:
            return Primitivo(TipoObjeto.FLOAT64, float(str(res_uno.getValue())))

        if self.funcion_nativa == FuncionesPrimitivas.STRING:
            return Primitivo(TipoObjeto.STRING, str(res_uno.getValue()))

        if self.funcion_nativa == FuncionesPrimitivas.TYPEOF:
            return Primitivo(TipoObjeto.STRING, str("en alguna clase programarle el toString")) # TODO: en alguna clase programarle el toString
        """
                if self.funcion_nativa == FuncionesPrimitivas.PUSH:
                    return Primitivo(TipoObjeto.FLOAT64, math.sqrt(int(str(res_uno.getValue()))))

                if self.funcion_nativa == FuncionesPrimitivas.POP:
                    return Primitivo(TipoObjeto.FLOAT64, math.sqrt(int(str(res_uno.getValue()))))

                if self.funcion_nativa == FuncionesPrimitivas.LENGTH:
                    return Primitivo(TipoObjeto.FLOAT64, math.sqrt(int(str(res_uno.getValue()))))
        """
        if self.funcion_nativa == FuncionesPrimitivas.UPPERCASE:
            return Primitivo(TipoObjeto.STRING, str(res_uno.getValue()).upper())

        if self.funcion_nativa == FuncionesPrimitivas.LOWERCASE:
            return Primitivo(TipoObjeto.STRING, str(res_uno.getValue()).lower())

        return Excepcion("Semantico", f"Funcion nativa desconocida: {self.funcion_nativa}", self.fila, self.columna);

    def getNodo(self):
        nodo = NodoReporteArbol(Expresion.NATIVA)

        nodo.agregarHijoNodo(self.funcion_nativa)
        nodo.agregarHijoNodo(self.expresion_uno.getNodo())

        if self.expresion_dos is not None:
            nodo.agregarHijoNodo(self.expresion_dos.getNodo())
        elif self.tipo_dato is not None:
            nodo.agregarHijoNodo(self.tipo_dato)
        return nodo
