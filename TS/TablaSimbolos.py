from TS.Excepcion import Excepcion

# CLASE QUE SERA CUALQUIER VARIBLES (OBJETOS),
# FUNCIONES DENTRO DEL ANALISIS
class TablaSimbolos:
    def __init__(self, anterior=None):
        self.tabla = {}  # DICCIONARIO VACIO
        self.anterior = anterior

    def setTabla(self, simbolo):    # AGREGA UNA NUEVA VARIABLE
        if simbolo.id.lower() in self.tabla:
            return Excepcion("Semantico", "Variable " + simbolo.id + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id.lower()] = simbolo
            return None

    def getTabla(self, id):     #OBTIENE UNA VARIABLE
        tablaActual = self
        while tablaActual != None:
            if id.lower() in tablaActual.tabla:
                return tablaActual.tabla[id.lower()]  # RETORNA SIMBOLO
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarTabla(self, simbolo):     # actualiza o crea el valor para un simbolo
        tablaActual = self
        while tablaActual != None:
            if simbolo.id.lower() in tablaActual.tabla:
                tablaActual.tabla[simbolo.id.lower()].setValor(simbolo.getValor())
                return None  # EL VALOR DEL SIMBOLO ACTUALIZADO ('OBJETO')
            else:
                tablaActual = tablaActual.anterior
        self.tabla[simbolo.id.lower()] = simbolo
        return None # SIMBOLO AGREGADO
