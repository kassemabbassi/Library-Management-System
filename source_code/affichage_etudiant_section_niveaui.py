# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'affichage_etudiant_section_niveaui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import csv
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_affichage_etudiant_section_niveaui(object):
    def setupUi(self, affichage_etudiant_section_niveaui):
        affichage_etudiant_section_niveaui.setObjectName("affichage_etudiant_section_niveaui")
        affichage_etudiant_section_niveaui.resize(1300, 870)
        self.label = QtWidgets.QLabel(affichage_etudiant_section_niveaui)
        self.label.setGeometry(QtCore.QRect(0, -20, 1300, 870))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/ressources/23.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(affichage_etudiant_section_niveaui)
        self.tableWidget.setGeometry(QtCore.QRect(20, 230, 1261, 491))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(136)
        self.label_2 = QtWidgets.QLabel(affichage_etudiant_section_niveaui)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius:10px")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(affichage_etudiant_section_niveaui)
        self.label_3.setGeometry(QtCore.QRect(190, 130, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius:10px")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(affichage_etudiant_section_niveaui)
        self.comboBox.setGeometry(QtCore.QRect(500, 61, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid white;\n"
"border-radius:10px")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(affichage_etudiant_section_niveaui)
        self.comboBox_2.setGeometry(QtCore.QRect(500, 131, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid white;\n"
"border-radius:10px")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(affichage_etudiant_section_niveaui)
        self.pushButton.setGeometry(QtCore.QRect(550, 757, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid white;\n"
"border-radius:10px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load_csv)

        self.retranslateUi(affichage_etudiant_section_niveaui)
        QtCore.QMetaObject.connectSlotsByName(affichage_etudiant_section_niveaui)
    def load_csv(self):
        section=self.comboBox.currentText()
        niveau=self.comboBox_2.currentText()
        csv_file = "students.csv"
        with open(csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            header = next(reader)
            self.tableWidget.setColumnCount(len(header))
            self.tableWidget.setHorizontalHeaderLabels(header)
            self.tableWidget.setRowCount(0)
            found = False
            for row_data in reader:
                if (row_data[7] == section and row_data[8] == niveau):
                    found = True
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    for column, item in enumerate(row_data):
                        self.tableWidget.setItem(row, column, QTableWidgetItem(item))
            if not found:
                QMessageBox.warning(None, "Erreur", f" aucun étudiant trouvé avec Le niveau d'étude {niveau} et la section {section} dans notre base de données.")


    def retranslateUi(self, affichage_etudiant_section_niveaui):
        _translate = QtCore.QCoreApplication.translate
        affichage_etudiant_section_niveaui.setWindowTitle(_translate("affichage_etudiant_section_niveaui", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("affichage_etudiant_section_niveaui", "Numero inscription"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("affichage_etudiant_section_niveaui", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("affichage_etudiant_section_niveaui", "Prenom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("affichage_etudiant_section_niveaui", "Date Naissance"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("affichage_etudiant_section_niveaui", "Adresse"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("affichage_etudiant_section_niveaui", "Mail"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("affichage_etudiant_section_niveaui", "Telephone"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("affichage_etudiant_section_niveaui", "Section"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("affichage_etudiant_section_niveaui", "Niveau Etude"))
        self.label_2.setText(_translate("affichage_etudiant_section_niveaui", "Section"))
        self.label_3.setText(_translate("affichage_etudiant_section_niveaui", "Niveau d\'étude"))
        self.comboBox.setItemText(0, _translate("affichage_etudiant_section_niveaui", "Cycle Préparatoire intégrée"))
        self.comboBox.setItemText(1, _translate("affichage_etudiant_section_niveaui", "License Info"))
        self.comboBox.setItemText(2, _translate("affichage_etudiant_section_niveaui", "License Tic"))
        self.comboBox.setItemText(3, _translate("affichage_etudiant_section_niveaui", "License électronique"))
        self.comboBox.setItemText(4, _translate("affichage_etudiant_section_niveaui", "Ingénieur électronique"))
        self.comboBox.setItemText(5, _translate("affichage_etudiant_section_niveaui", "Ingénieur Informatique"))
        self.comboBox_2.setItemText(0, _translate("affichage_etudiant_section_niveaui", "1 ére année"))
        self.comboBox_2.setItemText(1, _translate("affichage_etudiant_section_niveaui", "2 éme année"))
        self.comboBox_2.setItemText(2, _translate("affichage_etudiant_section_niveaui", "3 éme année"))
        self.pushButton.setText(_translate("affichage_etudiant_section_niveaui", "Afficher"))
import ressources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    affichage_etudiant_section_niveaui = QtWidgets.QWidget()
    ui = Ui_affichage_etudiant_section_niveaui()
    ui.setupUi(affichage_etudiant_section_niveaui)
    affichage_etudiant_section_niveaui.show()
    sys.exit(app.exec_())
