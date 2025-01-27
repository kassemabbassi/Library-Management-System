# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'affichage_emprunt_etudiant.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import csv
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_affichage_emprunt_etudiant(object):
    def setupUi(self, affichage_emprunt_etudiant):
        affichage_emprunt_etudiant.setObjectName("affichage_emprunt_etudiant")
        affichage_emprunt_etudiant.resize(1300, 870)
        self.label = QtWidgets.QLabel(affichage_emprunt_etudiant)
        self.label.setGeometry(QtCore.QRect(0, 0, 1300, 870))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/ressources/23.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(affichage_emprunt_etudiant)
        self.tableWidget.setGeometry(QtCore.QRect(240, 240, 751, 441))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(188)
        self.label_2 = QtWidgets.QLabel(affichage_emprunt_etudiant)
        self.label_2.setGeometry(QtCore.QRect(230, 110, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius:10px")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(affichage_emprunt_etudiant)
        self.lineEdit.setGeometry(QtCore.QRect(570, 120, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid white;\n"
"border-radius:10px")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(affichage_emprunt_etudiant)
        self.pushButton.setGeometry(QtCore.QRect(550, 760, 161, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid white;\n"
"border-radius:10px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load_csv)

        self.retranslateUi(affichage_emprunt_etudiant)
        QtCore.QMetaObject.connectSlotsByName(affichage_emprunt_etudiant)
    def load_csv(self):
        numero=self.lineEdit.text()
        if not(numero.isdecimal() and len(numero)==8):
                QMessageBox.critical(None, "Erreur", "Le numéro d'inscription doit contenir 8 chiffres")
                return
        csv_file = "emprunt.csv"
        with open(csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            header = next(reader)
            self.tableWidget.setColumnCount(len(header))
            self.tableWidget.setHorizontalHeaderLabels(header)
            self.tableWidget.setRowCount(0)
            found = False
            for row_data in reader:
                if row_data[0] == numero:
                    found = True
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    for column, item in enumerate(row_data):
                        self.tableWidget.setItem(row, column, QTableWidgetItem(item))
            if not found:
                QMessageBox.information(None, "Erreur", f" il n y aucun emprunt avec Le numero inscription {numero}  dans notre base de données.")


    def retranslateUi(self, affichage_emprunt_etudiant):
        _translate = QtCore.QCoreApplication.translate
        affichage_emprunt_etudiant.setWindowTitle(_translate("affichage_emprunt_etudiant", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("affichage_emprunt_etudiant", "Numéro_inscription"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("affichage_emprunt_etudiant", "Référence_livre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("affichage_emprunt_etudiant", "Date_emprunt"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("affichage_emprunt_etudiant", "Date_retour"))
        self.label_2.setText(_translate("affichage_emprunt_etudiant", " Numéro d\'inscription"))
        self.pushButton.setText(_translate("affichage_emprunt_etudiant", "Afficher"))
import ressources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    affichage_emprunt_etudiant = QtWidgets.QWidget()
    ui = Ui_affichage_emprunt_etudiant()
    ui.setupUi(affichage_emprunt_etudiant)
    affichage_emprunt_etudiant.show()
    sys.exit(app.exec_())
