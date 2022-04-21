from operator import setitem
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from datetime import date
from models import TableAvariy

class WindowAvar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Avariya Haqida Maylumotlar")
        self.initUi()
        self.fillTable()

    def initUi(self):
        self.cal = QCalendarWidget(self)
        self.cal.setGeometry(1500, 30, 400, 350)
        self.dat = QDate(date.today())
        self.cal.setSelectedDate(self.dat)
        self.cal.clicked.connect(self.onDat)


        self.table = QTableWidget(self)
        self.table.setGeometry(30, 50, 1450, 800)
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels(["ID", "Температура М1", "Температура М2", "Температура Т1", "Температура Т2", "Выбрация", "Степен Газа","Пожар" "Время аварии"])
        self.table.hideColumn(0)
        \
        



    def fillTable(self):
        self.table.clear()
        self.table.setColumnCount(11)
        self.table.hideColumn(0)
        self.table.setHorizontalHeaderLabels(["ID", "Температура М1 ℃", "Температура М2 (℃)", "Температура Т1 ℃", "Температура Т2 ℃ ", "Обород М1 (об/мин)", "Обород М2 (об/мин)", "Выбрация", "Степен Газа", "Пожар", "Время аварии"])
        self.table.setRowCount(0)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)

        for item in TableAvariy.objects():
            rowCount = self.table.rowCount()
            self.table.setRowCount(rowCount + 1)
            print(item.id)
            self.table.setItem(rowCount, 0, QTableWidgetItem(str(item.id)))
            self.table.setItem(rowCount, 1, QTableWidgetItem(str(item.temM1)))
            self.table.setItem(rowCount, 2, QTableWidgetItem(str(item.temM2)))
            self.table.setItem(rowCount, 3, QTableWidgetItem(str(item.temT1)))
            self.table.setItem(rowCount, 4, QTableWidgetItem(str(item.temT2)))
            self.table.setItem(rowCount, 5, QTableWidgetItem(str(item.obM1)))
            self.table.setItem(rowCount, 6, QTableWidgetItem(str(item.obM2)))
            self.table.setItem(rowCount, 7, QTableWidgetItem(str(item.vib)))
            self.table.setItem(rowCount, 8, QTableWidgetItem(str(item.gaz)))
            self.table.setItem(rowCount, 9, QTableWidgetItem(str(item.pojar)))
            self.table.setItem(rowCount, 10, QTableWidgetItem(str(item.date)))
            self.table.resizeColumnsToContents()
            



    def onDat(self, a):
        sana = a.toString()
        self.d = 0
        if sana[3:6] == 'янв':
            self.d = 1
        elif sana[3:6] == 'фев':
            self.d = 2
        elif sana[3:6] == 'мар':
            self.d = 3
        elif sana[3:6] == 'апр':
            self.d = 4
        elif sana[3:6] == 'май':
            self.d = 5
        elif sana[3:6] == 'июн':
            self.d = 6
        elif sana[3:6] == 'июл':
            self.d = 7
        elif sana[3:6] == 'авг':
            self.d = 8
        elif sana[3:6] == 'сен':
            self.d = 9
        elif sana[3:6] == 'окт':
            self.d = 10
        elif sana[3:6] == 'ноя':
            self.d = 11
        else :
            self.d = 12
                    


