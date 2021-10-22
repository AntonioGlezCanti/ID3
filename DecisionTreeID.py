import ID3
import numpy as np
import pandas as pd
import math

class DecisionTreeID :
    
    def __init__(self):
        self.tabla = [] #tabla con los datos (tipo dataFrame)
        self.etiquetas = {} #diccionario con los posibles valores/etiquetas de cada columna
        self.id3 = None #arbol de decision

    def learnDT(self,ficheroCVS):
        self._readCSV(ficheroCVS) 
        self._obtenerEtiquetas()
        filas = list(range(len(self.tabla))) #array con las filas permitidas (tipo np.array)
        columnas = self.tabla.columns.to_list() #array con las columnas permitidas (tipo np.array)
        self.id3 = ID3.ID3(filas,columnas,self.tabla,self.etiquetas) #Creamos el arbol, con altura 1

    def drawDecisionTree(self):
        print(self.id3.pintarArbol(1,[]))
    
    def prediction (self,registroCSV):
        None

    def _readCSV(self,ficheroCSV):
        self.tabla = pd.read_csv(ficheroCSV)

    def _obtenerEtiquetas (self):
        for c in self.tabla.columns:
            self.etiquetas.update({c:pd.unique(self.tabla[c]).tolist()})


main = DecisionTreeID()
main.learnDT(r"C:\Users\gonza\Documents\Informática\Aprendizaje\ID3\ejemplo.csv")
main.drawDecisionTree()




