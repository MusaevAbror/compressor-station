from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import datetime

from models import TableAvariy

class WindowAvar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Avariya Haqida Maylumotlar")
        self.initUi()
        self.fillTable()
      

    def initUi(self):
        self.cal = QDateEdit(self, calendarPopup=True)
        self.cal.setGeometry(1500, 30, 100, 30)
        self.cal.setDate(QDate.currentDate())
        self.cal.dateChanged.connect(self.onDate)
       

        
        self.table = QTableWidget(self)
        self.table.setGeometry(30, 50, 1450, 800)
        self.table.setColumnCount(12)
        self.table.setHorizontalHeaderLabels(["ID", "Температура М1", "Температура М2", "Температура Т1", "Температура Т2", "Выбрация M1", "Выбрация M2", "Степен Газа", "Пожар", "Время аварии"])
        self.table.hideColumn(0)
        
        



    def fillTable(self):
        self.table.clear()
        self.table.setColumnCount(12)
        self.table.hideColumn(0)
        self.table.setHorizontalHeaderLabels(["ID", "Температура М1 ℃", "Температура М2 (℃)", "Температура Т1 ℃", "Температура Т2 ℃ ", "Обород М1 (об/мин)", "Обород М2 (об/мин)", "Выбрация_M1", "Выбрация_M2", "Степен Газа", "Пожар", "Время аварии"])
        self.table.setRowCount(0)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.resizeColumnsToContents()

        for item in TableAvariy.objects():
            row_count = self.table.rowCount()
            self.table.setRowCount(row_count + 1)
            self.table.setItem(row_count, 0, QTableWidgetItem(str(item.id)))
            self.table.setItem(row_count, 1, QTableWidgetItem(item.temM1))
            self.table.setItem(row_count, 2, QTableWidgetItem(item.temM2))
            self.table.setItem(row_count, 3, QTableWidgetItem(item.temT1))
            self.table.setItem(row_count, 4, QTableWidgetItem(item.temT2))
            self.table.setItem(row_count, 5, QTableWidgetItem(item.obM1))
            self.table.setItem(row_count, 6, QTableWidgetItem(item.obM2))
            self.table.setItem(row_count, 7, QTableWidgetItem(item.vib_M1))
            self.table.setItem(row_count, 8, QTableWidgetItem(item.vib_M2))
            self.table.setItem(row_count, 9, QTableWidgetItem(item.gaz))
            self.table.setItem(row_count, 10, QTableWidgetItem(item.pojar))
            self.table.setItem(row_count, 11, QTableWidgetItem(item.date))
            self.table.resizeColumnsToContents()





    def onDate(self):
        year = self.cal.date().year()
        month = self.cal.date().month()
        day = self.cal.date().day()
        print(year, month, day)
                    


