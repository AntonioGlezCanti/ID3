import ID3
import numpy as np
import pandas as pd
import math

class DecisionTreeID :
    
    def __init__(self):
        self.tabla = [] #tabla con los datos (tipo dataFrame)
        self.filas = [] #array con las filas permitidas (tipo np.array)
        self.columnas = [] #array con las columnas permitidas (tipo np.array)
        self.etiquetas = {} #diccionario con los posibles valores/etiquetas de cada columna

    def learnDT(self,ficheroCVS):
        self._readCSV(ficheroCVS) 
        self._obtenerEtiquetas()
        self.filas = list(range(len(self.tabla)))
        self.columnas = self.tabla.columns

    def drawDecisionTree(self):
        None
    
    def prediction (self,registroCSV):
        None

    def _readCSV(self,ficheroCSV):
        self.tabla = pd.read_csv(ficheroCSV)

    def _obtenerEtiquetas (self):
        for c in self.tabla.columns:
            self.etiquetas.update({c:pd.unique(self.tabla[c]).tolist()})
            
    def _getAtributos(self):
        return self.filas,self.columnas,self.tabla,self.etiquetas

main = DecisionTreeID()
main.learnDT(r"C:\Users\gonza\Documents\Informática\Aprendizaje\ID3\ejemplo.csv")
f,c,t,e = main._getAtributos()

#print(t)
col = ['azucar sangre','indice col','alergia ant', 'otras alergias', 'administrar farmaco']
fil = [0,1,6,7,8,11]
#print(t.loc()[fil,col])

#print(-1*(4/6*math.log2(4/6) + 2/6*math.log2(2/6)))

id3 = ID3.ID3(fil,col,t,e)
id3.calcularNodo()


