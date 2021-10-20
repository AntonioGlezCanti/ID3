import math
import numpy as np

class ID3 :

    def __init__(self,filas,columnas,tabla,etiquetas):
        self.filas = filas
        self.columnas = columnas
        self.tabla = tabla
        self.etiquetas = etiquetas
        self.atrDec = self.tabla.columns[len(self.tabla.columns)-1] 
        self.etDec = self.etiquetas[self.atrDec]
        self.entropia = 0

    def _calcularEntropia(self):
        cont = self.tabla.groupby(self.atrDec)[self.atrDec].count().tolist()
        self.entropia = self._entropia(cont)
        return(self.entropia)
    
    def _calcularGanancia(self,atributo):
        entropias = {}
        etAtr = self.etiquetas[atributo]
        cont = self.tabla.groupby([self.atrDec,atributo])[atributo].count()
        for et in etAtr:
            val = []
            for ed in self.etDec:
                val.append(cont.get(ed,0).get(et,0))                
            e = self._entropia(val)
            entropias.update({et:e})

        ganancia = self.entropia
        cont = self.tabla.groupby(atributo)[self.atrDec].count()
        for et in etAtr:
            ganancia -= cont[et]/len(self.tabla)*entropias[et]
        return ganancia

    def _entropia(self, cont):
        entropia = 0
        total = sum(cont)
        for c in cont:
            if c != 0:
                entropia -= c/total*math.log2(c/total)  #aplicamos la formula de la entropia           
        return entropia
        
        