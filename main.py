# -*- coding: utf-8 -*-

import sys
import pathlib

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot, Qt, QVariant

from data.gui.principal import Ui_MainWindow
from data.gui.testDialog import Ui_Dialog


# === AlignCenterText ===
class AlignDelegate(QtWidgets.QStyledItemDelegate):

    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter
# === AlignCenterText ===


class Dialog(QtWidgets.QDialog):

    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class main(QtWidgets.QMainWindow):

    def __init__(self):
        super(main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(None))
                item = QtWidgets.QTableWidgetItem()
                item.setData(Qt.EditRole, QVariant(row + 1))
                item.setFlags(Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, 0, item)

        item = QtWidgets.QTableWidgetItem()
        self.ui.tableWidget.setHorizontalHeaderItem(0, item)
        item = self.ui.tableWidget.horizontalHeaderItem(0)
        item.setText('ID')

        # === AlignCenterText ===
        delegate = AlignDelegate(self.ui.tableWidget)
        self.ui.tableWidget.setItemDelegate(delegate)
        # === AlignCenterText ===

        # Acomoda el ancho de las columnas.
        self.ui.tableWidget.resizeColumnsToContents()

        self.ui.actionColumnas.triggered['bool'].connect(self.openFileSaveDialog)
        self.ui.tableWidget.cellChanged['int', 'int'].connect(self.get_tableWidget_values)


    @pyqtSlot(bool)
    def openFileSaveDialog(self, q):
        title = 'Guardar Archivo'
        accept = 'Documento de Evaluación (*.digna)'
        files, _ = QtWidgets.QFileDialog.getSaveFileName(self, title, '', accept)
        print(files, _)


    @pyqtSlot(int, int)
    def get_tableWidget_values(self, x, y):
        self.ui.tableWidget.resizeColumnsToContents()
        print(x, y)
        print(self.ui.tableWidget.item(x, y).text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = main()
    application.show()
    sys.exit(app.exec())
