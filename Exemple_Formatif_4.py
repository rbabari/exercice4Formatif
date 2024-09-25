# importer pyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QGridLayout

# Data
listeInputs = []
listeNoms = []
listeScores = []

#Actions
def charger():
    print("== Charger ==")
    f = open("Resultat.txt", "r")
    for l in listeInputs:
        l.setText(f.readline())
    f.close()

def sauver():
    print("== Sauver ==")
    f = open("Resultat.txt","w")
    for l in listeInputs:
        f.write(l.text() + "\n")
    f.close()
def analyser():
    print("== Analyser ==")
    listeNoms.append(listeInputs[0].text())
    listeScores.append(int(listeInputs[1].text()))

    listeNoms.append(listeInputs[2].text())
    listeScores.append(int(listeInputs[3].text()))

    listeNoms.append(listeInputs[4].text())
    listeScores.append(int(listeInputs[5].text()))

    listeNoms.append(listeInputs[6].text())
    listeScores.append(int(listeInputs[7].text()))

    total = listeScores[0] + listeScores[1]+listeScores[2]+listeScores[3]
    moyenne = total /4

    lblTotal.setText("Total : " + str(total))
    lblMoyenne.setText("Moyenne" + str(moyenne))

    # IDENTIFIER LES LE GAGNANT ...


# Interface

app = QApplication([])
fen = QWidget()
fen.setGeometry(50, 50, 500, 250)
#fen.setStyleSheet("background-color: gray;")
fen.setWindowTitle("Formatif Exercice 4")

#---------GRID LAYOUT
grid = QGridLayout()
fen.setLayout(grid)

#------JOUEURS 1
lbl1 = QLabel(fen)
lbl1.setText("Joueur 1")
grid.addWidget(lbl1, 0, 0)

edit11 = QLineEdit(fen)
grid.addWidget(edit11, 0, 1)
listeInputs.append(edit11)

edit12 = QLineEdit(fen)
grid.addWidget(edit12, 0, 2)
listeInputs.append(edit12)
#------JOUEURS 2

lbl2 = QLabel(fen)
lbl2.setText("Joueur 2")
grid.addWidget(lbl2, 1, 0)

edit21 = QLineEdit(fen)
grid.addWidget(edit21, 1, 1)
listeInputs.append(edit21)

edit22 = QLineEdit(fen)
grid.addWidget(edit22, 1, 2)
listeInputs.append(edit22)

#------JOUEURS 3

grid.addWidget(QLabel("Joueur3",fen), 2, 0)

listeInputs.append(QLineEdit(fen)) # input du joueur 3 ... position 4 de la liste
grid.addWidget(listeInputs[4], 2, 1)

listeInputs.append(QLineEdit(fen)) # input du joueur 3 ... position 5 de la liste
grid.addWidget(listeInputs[5], 2, 2)

#------JOUEURS 3

grid.addWidget(QLabel("Joueur4",fen), 3, 0)

listeInputs.append(QLineEdit(fen))
grid.addWidget(listeInputs[6], 3, 1)

listeInputs.append(QLineEdit(fen))
grid.addWidget(listeInputs[7], 3, 2)

#-------
lblTotal = QLabel(fen)
lblTotal.setText(" Total")
grid.addWidget(lblTotal, 4, 0)

lblMoyenne = QLabel(fen)
lblMoyenne.setText(" Moyenne")
grid.addWidget(lblMoyenne, 4, 1)

lblGagnant = QLabel(fen)
lblGagnant.setText(" Gagnant")
grid.addWidget(lblGagnant, 4, 2)


#---- QPushButton
btn1 = QPushButton(fen)
btn1.setText("Charger")
grid.addWidget(btn1, 5, 0)
btn1.clicked.connect(charger)

btn2 = QPushButton(fen)
btn2.setText("Sauver")
grid.addWidget(btn2, 5, 1)
btn2.clicked.connect(sauver)

btn3 = QPushButton(fen)
btn3.setText("Analyser")
grid.addWidget(btn3, 5, 2)
btn3.clicked.connect(analyser)

charger()


fen.show()
app.exec()


