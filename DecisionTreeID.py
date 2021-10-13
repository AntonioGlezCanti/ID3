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

