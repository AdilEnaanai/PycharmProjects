import sys

from PyQt5 import QtWidgets,uic

class Fenetre(QtWidgets.QMainWindow):
    def __init__(self):
        super(Fenetre,self).__init__()
        uic.loadUi("ui/FEN_Addition.ui",self)
        self.show()
        self.addition.clicked.connect(self.calculer)
        self.operation.currentTextChanged.connect(self.choisirOp)

    def calculer(self):
        if self.operation.currentText()=='+':r=int(self.nombre1.text())+int(self.nombre2.text())
        elif self.operation.currentText()=='-':r=int(self.nombre1.text())-int(self.nombre2.text())
        elif self.operation.currentText() == 'x': r=int(self.nombre1.text())*int(self.nombre2.text())
        else:
            try:
                r=int(self.nombre1.text())/int(self.nombre2.text())
            except ZeroDivisionError:
                print("Division par Zéro")

        self.resultat.setText(str(r))

    def choisirOp(self):
        if self.operation.currentText()=='+':self.resultat.setText("Addition")
        elif self.operation.currentText()=='-':self.resultat.setText("soustraction")
        elif self.operation.currentText() == 'x': self.resultat.setText("Multiplication")
        else: self.resultat.setText("Division")

app=QtWidgets.QApplication(sys.argv)
fen=Fenetre()
app.exec()