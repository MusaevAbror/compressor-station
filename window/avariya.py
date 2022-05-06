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
        print(self.cal.date().day())
        print(self.cal.date().month())
        print(self.cal.date().year())

        


        
      

        self.table = QTableWidget(self)
        self.table.setGeometry(30, 50, 1450, 800)
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels(["ID", "Температура М1", "Температура М2", "Температура Т1", "Температура Т2", "Выбрация", "Степен Газа","Пожар" "Время аварии"])
        self.table.hideColumn(0)
        
        



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
            



    def onDate(self):
        year = self.cal.date().year()
        month = self.cal.date().month()
        day = self.cal.date().day()
        print(year, month, day)
                    


