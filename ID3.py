import math
import numpy as np

class ID3 :

    def __init__(self,filas,columnas,tabla,etiquetas):
        self.filas = filas
        self.columnas = columnas
        self.tabla = tabla
        self.etiquetas = etiquetas
        self.entropia = 0

    def _calcularEntropia(self):
        atrDec = self.tabla.columns[len(self.tabla.columns)-1] #index del atributo de decision (el último atributo)
        cont = self.tabla.groupby(atrDec)[atrDec].count().tolist()
        total = sum(cont)
        for c in cont:
            self.entropia -= c/total*math.log2(c/total)  #aplicamos la formula de la entropia           
        return self.entropia
        
        