import sys
class fab:
    '''Clase para la FAB'''
    def __init__ (self):
        self.periodos={}
        self.equipos={}

    def tanper(self, f):
        for linea in f:
            #crear equipos y crear periodos
            lili=linea.split(',')
            evento=lili[0]
            if evento=='eq':
                idEq=int(lili[1])
                nomEq=lili[2]
                self.equipos[idEq]=nomEq.strip()
            if evento[0]=='Q':
                idcuar=int(evento[1])
                tparcial={}
                for equipo in self.equipos:
                    tparcial[equipo]=0
                self.periodos[idcuar]=tparcial
            if evento=='b': 
                idEq=int(lili[1].split('#')[0])
                puntos=int(lili[2])
                if self.periodos[idcuar][idEq]==0:
                    self.periodos[idcuar][idEq]=puntos
                else:
                    self.periodos[idcuar][idEq]+=puntos         
        return self.periodos, self.equipos