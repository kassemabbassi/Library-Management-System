# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'affichage_livre_ordre.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import csv

class Ui_affichage_livre_ordre(object):
    def setupUi(self, affichage_livre_ordre):
        affichage_livre_ordre.setObjectName("affichage_livre_ordre")
        affichage_livre_ordre.resize(1300, 860)
        self.label = QtWidgets.QLabel(affichage_livre_ordre)
        self.label.setGeometry(QtCore.QRect(0, 0, 1300, 860))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/ressources/23.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(affichage_livre_ordre)
        self.tableWidget.setGeometry(QtCore.QRect(280, 210, 701, 491))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(136)
        self.label_2 = QtWidgets.QLabel(affichage_livre_ordre)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 1131, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius:10px")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(affichage_livre_ordre)
        self.pushButton.setGeometry(QtCore.QRect(560, 780, 121, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.afficher)

        self.retranslateUi(affichage_livre_ordre)
        QtCore.QMetaObject.connectSlotsByName(affichage_livre_ordre)
    def afficher(self):
        f = open('livres.csv', 'r')
        if not f.readable():
            QMessageBox.critical(None, "Erreur", "Impossible de lire le fichier livre.csv")
            f.close()
            return
        f.seek(0)
        f.close()
        with open('livres.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            livres = []
            for row in reader:
                livres.append(row[0].split(','))
        if(len(livres)==1):
            QMessageBox.warning(None, "Erreur", "Le fichier livre.csv est vide.")
            return
        else:
            livres=livres[1:]
            livres[1:] = sorted(livres[1:], key=lambda x: x[1])
            self.tableWidget.setRowCount(len(livres))
            self.tableWidget.setColumnCount(len(livres[0]))
            for row in range(len(livres)):
                for col in range(len(livres[0])):
                    item = QTableWidgetItem(str(livres[row][col]))
                    self.tableWidget.setItem(row, col, item)


    def retranslateUi(self, affichage_livre_ordre):
        _translate = QtCore.QCoreApplication.translate
        affichage_livre_ordre.setWindowTitle(_translate("affichage_livre_ordre", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("affichage_livre_ordre", "Reference"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("affichage_livre_ordre", "Titre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("affichage_livre_ordre", "Nom_auteru"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("affichage_livre_ordre", "Prénom_auteur"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("affichage_livre_ordre", "Année édition"))
        self.label_2.setText(_translate("affichage_livre_ordre", "Affichage des livres par ordre alphabétique selon leurs Titres"))
        self.pushButton.setText(_translate("affichage_livre_ordre", "Afficher"))
import ressources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    affichage_livre_ordre = QtWidgets.QWidget()
    ui = Ui_affichage_livre_ordre()
    ui.setupUi(affichage_livre_ordre)
    affichage_livre_ordre.show()
    sys.exit(app.exec_())