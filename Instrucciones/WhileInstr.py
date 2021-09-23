from Abstract.NodoAST import NodoAST
from Abstract.Objeto import TipoObjeto
from Instrucciones.ContinueInstr import ContinueInstr
from Instrucciones.BreakInstr import BreakInst
from Instrucciones.ReturnInstr import ReturnInstr
from TS.Excepcion import Excepcion, TipoError
from TS.TablaSimbolos import TablaSimbolos


class WhileInst(NodoAST):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        while True:
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Excepcion): return condicion

            if condicion.tipo == TipoObjeto.BOOL:
                if bool(condicion.valor):   # VERIFICA SI ES VERDADERA LA CONDICION
                    nuevaTabla = TablaSimbolos(table)       #NUEVO ENTORNO
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla)
                        if isinstance(result, Excepcion): return result
                        if isinstance(result, BreakInst): return None
                        if isinstance(result, ContinueInstr): continue
                        if isinstance(result, ReturnInstr): return result
                else:
                    break
            else:
                return Excepcion(TipoError.SEMANTICO, "Tipo de dato no booleano en while.", self.fila, self.columna)

    def getNodo(self):
        return None


""""
function main(){
    a=0;
    c=1;
    println("-olc2-N");
    while(a<4+c){
        a=a+1;
        b=0;
        while(b<4+c){
            b=b+1;
            println(a+" * "+b+" = "+a * b);
        }
        println("----------------");
    }
}
a=0;
c=1;
println("-olc2-N");
while a<4+c
a=a+1;
b=0;
    while b<4+c
    b=b+1;
    println(a+" * "+b+" = "+a * b);
    end;
println("----------------");
end;

var1 = 0;
while var1 < 10
println(var1);
var1 = var1 + 1;
end;

main();
"""