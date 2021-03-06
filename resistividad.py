# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#Cambio


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 701, 521))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btnCalcular = QtWidgets.QPushButton(self.groupBox)
        self.btnCalcular.setGeometry(QtCore.QRect(200, 270, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnCalcular.setFont(font)
        self.btnCalcular.setObjectName("btnCalcular")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber.setGeometry(QtCore.QRect(430, 90, 151, 101))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setObjectName("lcdNumber")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(30, 60, 242, 87))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.txtLongitud = QtWidgets.QLineEdit(self.widget)
        self.txtLongitud.setObjectName("txtLongitud")
        self.gridLayout.addWidget(self.txtLongitud, 0, 2, 1, 1)
        self.txtArea = QtWidgets.QLineEdit(self.widget)
        self.txtArea.setObjectName("txtArea")
        self.gridLayout.addWidget(self.txtArea, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnCalcular.clicked.connect(self.calcularResistencia)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def calcularResistencia(self):
        area = float(self.txtArea.text())
        longitud = float(self.txtLongitud.text())
        text = self.comboBox.currentText()
        resistividad=0;
        if text == "Hule":
            resistividad=1e13
        elif text == "Cobre":
            resistividad=1.68e-8
        elif text == "Germanio":
            resistividad=4.6e-1
        else:
            resistividad=0
        resistecia = (resistividad*longitud)/area
        self.lcdNumber.display(resistecia)
        print("calcularestencia")
        print("end")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resistividad"))
        self.groupBox.setTitle(_translate("MainWindow", "Resistencia"))
        self.btnCalcular.setText(_translate("MainWindow", "Calcular"))
        self.label.setText(_translate("MainWindow", "Longitud m"))
        self.label_2.setText(_translate("MainWindow", "Area m"))
        self.comboBox.setItemText(0, _translate("MainWindow", "--None--"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cobre"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Hule"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Germanio"))
        self.label_3.setText(_translate("MainWindow", "Material"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
