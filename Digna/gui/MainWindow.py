# -*- coding: utf-8 -*-

# Copyright © 2020 baneon - MIT License
# See `LICENSE` included in the source distribution for details.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self):
        self.width = 610
        self.height = 443


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 443)

        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setObjectName("CentralWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.CentralWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableWidget = QtWidgets.QTableWidget(self.CentralWidget)
        #self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        #self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setHorizontalHeaderItem(0, item)
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setHorizontalHeaderItem(1, item)
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.radioButton = QtWidgets.QRadioButton(self.CentralWidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton, 0, QtCore.Qt.AlignHCenter)
        self.radioButton_2 = QtWidgets.QRadioButton(self.CentralWidget)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2, 0, QtCore.Qt.AlignHCenter)
        self.radioButton_3 = QtWidgets.QRadioButton(self.CentralWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.CentralWidget)

        # MenuBar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuConfiguraci_n = QtWidgets.QMenu(self.menubar)
        self.menuConfiguraci_n.setObjectName("menuConfiguraci_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionEditItem = QtWidgets.QAction(MainWindow)
        self.actionEditItem.setObjectName("actionEditItem")
        self.actionFilas_3 = QtWidgets.QAction(MainWindow)
        self.actionFilas_3.setObjectName("actionFilas_3")
        self.actionActivar_modo_sorteo = QtWidgets.QAction(MainWindow)
        self.actionActivar_modo_sorteo.setCheckable(True)
        self.actionActivar_modo_sorteo.setObjectName("actionActivar_modo_sorteo")
        self.actionRestaurar_Configuraci_n = QtWidgets.QAction(MainWindow)
        self.actionRestaurar_Configuraci_n.setObjectName("actionRestaurar_Configuraci_n")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionEditItem)
        self.menuEdit.addAction(self.actionFilas_3)
        self.menuConfiguraci_n.addAction(self.actionActivar_modo_sorteo)
        self.menuConfiguraci_n.addSeparator()
        self.menuConfiguraci_n.addAction(self.actionRestaurar_Configuraci_n)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuConfiguraci_n.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(True)
        #item = self.tableWidget.horizontalHeaderItem(0)
        #item.setText(_translate("MainWindow", "ID"))
        #item = self.tableWidget.horizontalHeaderItem(1)
        #item.setText(_translate("MainWindow", "Cedula"))
        #item = self.tableWidget.horizontalHeaderItem(2)
        #item.setText(_translate("MainWindow", "Apellidos y Nombre"))
        self.radioButton.setText(_translate("MainWindow", "1er Lapso"))
        self.radioButton_2.setText(_translate("MainWindow", "2do Lapso"))
        self.radioButton_3.setText(_translate("MainWindow", "3er Lapso"))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEdit.setTitle(_translate("MainWindow", "Editar"))
        self.menuConfiguraci_n.setTitle(_translate("MainWindow", "Configuración"))
        self.actionSave.setText(_translate("MainWindow", "Guardar"))
        self.actionEditItem.setText(_translate("MainWindow", "Editar Items"))
        self.actionFilas_3.setText(_translate("MainWindow", "Filas"))
        self.actionActivar_modo_sorteo.setText(_translate("MainWindow", "Activar modo sorteo"))
        self.actionRestaurar_Configuraci_n.setText(_translate("MainWindow", "Restaurar Configuración"))
        self.actionExit.setText(_translate("MainWindow", "Salir"))
