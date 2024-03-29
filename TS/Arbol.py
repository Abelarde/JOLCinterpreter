
# NOTE: CLASE PARA MANEJAR NUESTRO ANALISIS
# CLASE PARA CONSTRUIR NUESTRO ARBOL CON EL ANALISIS
class Arbol:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.funciones = []
        self.excepciones = []
        self.consola = ""
        self.TSglobal = None   # DE TIPO TablaSimbolos() con sus metodos
        self.dot = ""
        self.contador = 0

    def getInstrucciones(self):
        return self.instrucciones

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones

    def getExcepciones(self):
        return self.excepciones

    def setExcepciones(self, excepciones):
        self.excepciones = excepciones

    def getConsola(self):
        return  self.consola

    def setConsola(self, consola):
        self.consola = consola

    def updateConsola(self, cadena):
        self.consola += str(cadena) + '\n'

    def getTSGlobal(self):
        return self.TSglobal

    def setTSglobal(self, TSglobal):
        self.TSglobal = TSglobal

    def getFunciones(self):
        return self.funciones

    def getFuncion(self, nombre):
        for funcion in self.funciones:
            if funcion.nombre == nombre:
                return funcion
        return None

    # TODO: quizas validar que no exista dos funciones con el mismo nombre
    def addFuncion(self, funcion):
        self.funciones.append(funcion)

    def getDot(self, raiz):
        self.dot = ""
        self.dot += "digraph {\n"
        self.dot += "n0[label=\"" + raiz.getValor().replace("\"", "\\\"") + "\"];\n"
        self.contador = 1
        self.recorrerAST("n0", raiz)
        self.dot += "}"
        return self.dot

    def recorrerAST(self, idPadre, nodoPadre):
        for hijo in nodoPadre.getHijos():
            nombreHijo = "n" + str(self.contador)
            self.dot += nombreHijo + "[label=\"" + hijo.getValor().replace("\"", "\\\"") + "\"];\n"
            self.dot += idPadre + "->" + nombreHijo + ";\n"
            self.contador += 1
            self.recorrerAST(nombreHijo, hijo)