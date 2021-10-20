import csv
import ID3
import numpy as np
import pandas as pd

class DecisionTreeID :
    
    def __init__(self):
        self.tabla = []
        self.filas = []
        self.columnas = []
        self.etiquetas = []

    def learnDT(self,ficheroCVS):
        self._readCSV(ficheroCVS)
        self._obtenerEtiquetas()
        #self.filas = np.ones(len(self.tabla))
        #self.columnas = np.ones(len(self.tabla[0]))

    def drawDecisionTree(self):
        None
    
    def prediction (self,registroCSV):
        None

    def _readCSV(self,ficheroCSV):
        self.tabla = pd.read_csv(ficheroCSV)

    def _obtenerEtiquetas (self):
        for c in self.tabla.columns:
            self.etiquetas.append(pd.unique(self.tabla[c]).tolist())
            
    def _getAtributos(self):
        return self.filas,self.columnas,self.tabla,self.etiquetas

main = DecisionTreeID()
main.learnDT(r"C:\Users\gonza\Documents\Informática\Aprendizaje\ID3\ejemplo.csv")
#f,c,t,e = main._getAtributos()
#id3 = ID3.ID3(f,c,t,e)
#print(id3._calcularEntropia())




