import csv

class DecisionTreeID :
    
    def __init__(self):
        self.tabla = []
        self.filas = []
        self.columnas = []

    def learnDT(self,ficheroCVS):
        self._readCSV(ficheroCVS)
    
    def drawDecisionTree(self):
        None
    
    def prediction (self,registroCSV):
        None

    def _readCSV(self,ficheroCSV):
        file = open(ficheroCSV)
        reader = csv.reader(file)
        for row in reader:
            self.tabla.append(row)
        print(self.tabla)

    def _obtenerEtiquetas (self):
        et = []
        for j in range(len(self.tabla[0])-1):
            for i in range(1,len(self.tabla)-1):
                val = self.tabla[i][j]
                if val not in et:
                    et.append(val)
            self.etiquetas.append(et)
            et = []
