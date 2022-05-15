import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from window.avariya import WindowAvar
from models import TableAvariy
import datetime
print(datetime.datetime)






class ArduinoPython(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.initAction()
        self.initMenu()
        self.qmsg = QMessageBox()

    def initUi(self):
        self.setGeometry(400, 100, 1100, 900)
        self.serial = QSerialPort(self)
        self.serial.setBaudRate(9600)
        self.ports = QSerialPortInfo.availablePorts()
        self.serial.readyRead.connect(self.onRead)
        self.portlist = []
        
        for port in self.ports:
            self.portlist.append(port.portName())

        self.combo = QComboBox(self) # combobox Portni tanlash uchun 
        self.combo.move(30, 30)
        self.combo.addItems(self.portlist)
        
        self.btn_o = QPushButton("Открывать", self) # Button 
        self.btn_o.move(140, 30)
        self.btn_o.clicked.connect(self.onOpen)

        self.btn_c = QPushButton("Закрывать", self)
        self.btn_c.move(250, 30)
        self.btn_c.clicked.connect(self.onClose)
        
        self.refresh = QPushButton("Обновить", self)
        self.refresh.move(360, 30)
        self.refresh.clicked.connect(self.onRef)

        self.btn_s = QPushButton("Стоп", self)
        self.btn_s.move(470, 30)
        self.btn_s.clicked.connect(self.onStop)

        self.btn_p = QPushButton("Запуск", self)
        self.btn_p.move(580 ,30)
        self.btn_p.clicked.connect(self.onStart)





        self.tem_M1_Bar = QProgressBar(self) # M1 Mator uchun temperatura Bar
        self.tem_M1_Bar.setGeometry(50, 120, 50, 270)
        self.tem_M1_Bar.setOrientation(QtCore.Qt.Vertical)
        self.tem_M1_Bar.setMaximum(80)

        self.tem1_l = QLabel(self)   # M1 Mator Temperaturasining Labeli
        self.tem1_l.setFrameShape(QFrame.WinPanel)
        self.tem1_l.setFrameShadow(QFrame.Raised)
        self.tem1_l.setGeometry(5, 435, 140, 30)
        self.tem1_l.setText('''<html><head/><body><p><span style=" font-family:'Consolas,Courier New,monospace'; font-size:10pt; font-weight:600; color:#000000;">Температура М1</span></p></body></html>''')

        self.tem1_lf = QLabel(self) # M1 Matorning temperaturasini C da ifodalovchi Label
        self.tem1_lf.setGeometry(50, 85, 50, 30)
        self.tem1_lf.setText(str(self.tem_M1_Bar.value()) + " ℃ ")

        

        self.tem_M2_Bar = QProgressBar(self)  # M2 Matorning temperaturasi uchun ProgressBar 
        self.tem_M2_Bar.setGeometry(250, 120, 50, 270)
        self.tem_M2_Bar.setOrientation(QtCore.Qt.Vertical)
        self.tem_M2_Bar.setMaximum(80)
        
        self.tem2_l = QLabel(self)   # M2 Matorning temperaturasini Labeli
        self.tem2_l.setFrameShape(QFrame.WinPanel)
        self.tem2_l.setFrameShadow(QFrame.Raised)
        self.tem2_l.setGeometry(205, 435, 140, 30)
        self.tem2_l.setText('''<html><head/><body><p><span style=" font-family:'Consolas,Courier New,monospace'; font-size:10pt; font-weight:600; color:#000000;">Температура М2</span></p></body></html>''')

        self.tem2_lf = QLabel(self) # M2 mator temperaturasini C da ifodalovchi Label
        self.tem2_lf.setGeometry(250, 85, 50, 30)
        self.tem2_lf.setText(str(self.tem_M2_Bar.value()) + " ℃ ")



        self.tem_T1_Bar = QProgressBar(self) # T1 tranzistorning temperaturasini ko`rsatuvchi ProgressBar
        self.tem_T1_Bar.setGeometry(450, 120, 50, 270)
        self.tem_T1_Bar.setOrientation(QtCore.Qt.Vertical)
        self.tem_T1_Bar.setMaximum(125)

        self.tem1_t1 = QLabel(self)  # T1 tranzistorning temperaturasini Labeli
        self.tem1_t1.setFrameShape(QFrame.WinPanel)
        self.tem1_t1.setFrameShadow(QFrame.Raised)
        self.tem1_t1.setGeometry(405, 435, 140, 30)
        self.tem1_t1.setText('''<html><head/><body><p><span style=" font-family:'Consolas,Courier New,monospace'; font-size:10pt; font-weight:600; color:#000000;">Температура Т1</span></p></body></html>''')

        self.tem3_lf = QLabel(self)  # T1 Tranzistorning temperaturasini C da ifodalovchi Tabel
        self.tem3_lf.setGeometry(450, 85, 50, 30)
        self.tem3_lf.setText(str(self.tem_T1_Bar.value()) + " ℃ ")



        self.tem_T2_Bar = QProgressBar(self) # T2 Tranzistorning temperaturasi uchun ProgressBar 
        self.tem_T2_Bar.setGeometry(650, 120, 50, 270)
        self.tem_T2_Bar.setOrientation(QtCore.Qt.Vertical)
        self.tem_T2_Bar.setMaximum(125)
       
        self.tem1_t2 = QLabel(self) # T2 Tranzistorning Temperaturasining Labeli
        self.tem1_t2.setFrameShape(QFrame.WinPanel)
        self.tem1_t2.setFrameShadow(QFrame.Raised)
        self.tem1_t2.setGeometry(605, 435, 140, 30)
        self.tem1_t2.setText('''<html><head/><body><p><span style=" font-family:'Consolas,Courier New,monospace'; font-size:10pt; font-weight:600; color:#000000;">Температура T2</span></p></body></html>''')

        self.tem4_lf = QLabel(self)  # T2 tranzistorning temperturasini C da ifodalovchi Label
        self.tem4_lf.setGeometry(650, 85, 50, 30)
        self.tem4_lf.setText(str(self.tem_T2_Bar.value()) + " ℃ ")



        self.slider_M1 = QSlider(self) # M1 matorning slideri tezlik uchun
        self.slider_M1.setOrientation(QtCore.Qt.Vertical)
        self.slider_M1.setGeometry(65, 500, 70, 250)
        self.slider_M1.setMinimum(150)
        self.slider_M1.setMaximum(255)
        self.slider_M1.setTickPosition(QSlider.TicksBothSides)
        self.slider_M1.setSingleStep(50)
        self.slider_M1.setCursor(Qt.SplitVCursor)
        self.slider_M1.valueChanged.connect(self.onMator_1)

        self.M1_l = QLabel(self) # M1 mator Qlabel li 
        self.M1_l.setFrameShape(QFrame.WinPanel)
        self.M1_l.setFrameShadow(QFrame.Raised)
        self.M1_l.setGeometry(40, 760, 120, 30)
        self.M1_l.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Скорость М1</span></p></body></html>')



        self.slider_M2 = QSlider(self)  # M2 matorning slideri tezlik uchun
        self.slider_M2.setOrientation(QtCore.Qt.Vertical)
        self.slider_M2.setGeometry(215, 500, 70, 250)
        self.slider_M2.setMinimum(150)
        self.slider_M2.setMaximum(255)
        self.slider_M2.setTickPosition(QSlider.TicksBothSides)
        self.slider_M2.setSingleStep(50)
        self.slider_M2.setCursor(Qt.SplitVCursor)
        self.slider_M2.valueChanged.connect(self.onMator_2)

        self.M2_l = QLabel(self) # M2 mator Qlabel li 
        self.M2_l.setFrameShape(QFrame.WinPanel)
        self.M2_l.setFrameShadow(QFrame.Raised)
        self.M2_l.setGeometry(185, 760, 120, 30)
        self.M2_l.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Скорость М2</span></p></body></html>')


              
        self.qlcd_o_m1 = QLCDNumber(self) # display M1 mator oborodi uchun 
        self.qlcd_o_m1.setGeometry(800, 120, 250, 100)
        self.qlcd_o_m1.display("12000")

        self.lcd_o_m1 = QLabel(self) # label display M1 mator oborodi uchun 
        self.lcd_o_m1.setFrameShape(QFrame.WinPanel)
        self.lcd_o_m1.setFrameShadow(QFrame.Raised)
        self.lcd_o_m1.setGeometry(820, 230, 200, 30)
        self.lcd_o_m1.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Оборот М1 (об/мин)</span></p></body></html>')
        


        self.qlcd_o_m2 = QLCDNumber(self) # display M2 mator oborodi uchun 
        self.qlcd_o_m2.setGeometry(800, 290, 250, 100)
        
        self.lcd_o_m2 = QLabel(self) # Label display M2 mator oborodi uchun 
        self.lcd_o_m2.setFrameShape(QFrame.WinPanel)
        self.lcd_o_m2.setFrameShadow(QFrame.Raised)
        self.lcd_o_m2.setGeometry(820, 400, 200, 30)
        self.lcd_o_m2.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Оборот М2 (об/мин)</span></p></body></html>')



        self.qlcd_G = QLCDNumber(self) # display gaz uchun 
        self.qlcd_G.setGeometry(800, 460, 250, 100)

        self.lcd_G = QLabel(self) # label displey gaz uchun 
        self.lcd_G.setFrameShape(QFrame.WinPanel)
        self.lcd_G.setFrameShadow(QFrame.Raised)
        self.lcd_G.setGeometry(830, 570, 180, 30)
        self.lcd_G.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Степен Газа (ppm)</span></p></body></html>')
        


        self.green_led_p = QLabel(self)
        self.green_led_p.setStyleSheet("QLabel {background-color : green; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.green_led_p.move(870, 650)
        
        self.l_y = QLabel(self)
        self.l_y.setFrameShape(QFrame.WinPanel)
        self.l_y.setFrameShadow(QFrame.Raised)
        self.l_y.setGeometry(810, 700, 220, 30)
        self.l_y.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Информация о пожаре </span></p></body></html>')

        
        
        self.green_led_v = QLabel(self)
        self.green_led_v.setStyleSheet("QLabel {background-color : green; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.green_led_v.move(870, 780)

        self.l_v = QLabel(self)
        self.l_v.setFrameShape(QFrame.WinPanel)
        self.l_v.setFrameShadow(QFrame.Raised)  
        self.l_v.setGeometry(810, 820, 235, 30)
        self.l_v.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Информация о выбрации </span></p></body></html>')

    

    
    

    
        
    def avariya(self):
        obo_M1 = self.qlcd_o_m1.value()
        obo_M2 = self.qlcd_o_m2.value()
        tem_M1 = self.tem1_lf.text()
        tem_M2 = self.tem2_lf.text()
        tem_T1 = self.tem3_lf.text()
        tem_T2 = self.tem4_lf.text()
        vib_M1 = self.data[7]
        vib_M2 = self.data[8]
        

    def onStop(self):
        self.M1_val = self.slider_M1.value()
        self.M2_val = self.slider_M2.value()
        self.slider_M1.setEnabled(False)
        self.slider_M2.setEnabled(False)
        self.SerialSend([1, 0])
        self.SerialSend([2, 0])

    
    def onStart(self):
        self.slider_M1.setEnabled(True)
        self.slider_M2.setEnabled(True)
        self.slider_M1.setValue(self.M1_val)
        self.slider_M2.setValue(self.M2_val)
        self.SerialSend([1, self.M1_val])
        self.SerialSend([2, self.M2_val])

    
    def onMator_1(self, b):
        self.SerialSend([1, b])

    def onMator_2(self, a):
        self.SerialSend([2, a])

    def onRead(self):
        if not self.serial.canReadLine():
            return
        else :
            rx = self.serial.readLine()
            try:
                rxs = str(rx, 'utf-8').strip()
                self.data = rxs.split(',') 
               
                self.tem_M1_Bar.setValue(round(float(self.data[0])))
                self.tem1_lf.setText(str(float(self.data[0])) +" ℃ ")
                
                self.tem_M2_Bar.setValue(round(float(self.data[1])))
                self.tem2_lf.setText(str(float(self.data[1])) + " ℃ ")
                
                self.tem_T1_Bar.setValue(round(float(self.data[2])))
                self.tem3_lf.setText(str(float(self.data[2])) + " ℃ ")
                
                self.tem_T2_Bar.setValue(round(float(self.data[3])))
                self.tem4_lf.setText(str(float(self.data[3])) + " ℃ ")
                
                self.qlcd_o_m1.display(self.data[5])
                self.qlcd_o_m2.display(self.data[4])
                self.qlcd_G.display(self.data[6])
                a = True
                
                if self.data[9]:
                    print(self.data[9])    
                    self.red_led_p = QLabel(self)
                    self.red_led_p.setStyleSheet("QLabel {background-color : red; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
                    self.red_led_p.move(870, 650)
                else :
                    print(self.data[9])    

                    self.green_led_p = QLabel(self)
                    self.green_led_p.setStyleSheet("QLabel {background-color : green; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
                    self.green_led_p.move(870, 650)
                    a = False

                if (self.data[7] or self.data[8]) and a:
                
                    self.red_led_v = QLabel(self)
                    self.red_led_v.setStyleSheet("QLabel {background-color : red; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
                    self.red_led_v.move(870, 780)
                else:
                    self.green_led_v = QLabel(self)
                    self.green_led_v.setStyleSheet("QLabel {background-color : green; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
                    self.green_led_v.move(870, 780)


            except:
                self.qmsg.setIcon(QMessageBox.Information)
                self.qmsg.setWindowTitle("Xatolik")
                self.qmsg.setText("Port bilan bog`lanishda hatolik")
                self.qmsg.show()
           
    def SerialSend(self, data):
        self.txs = ""
        for item in data:
            self.txs += str(item)
            self.txs += ','
        self.txs = self.txs[:-1]
        self.txs += ';'
        self.serial.write(self.txs.encode())

    def onOpen(self):
       self.serial.setPortName(self.combo.currentText())
       self.serial.open(QIODevice.ReadWrite)

    def onClose(self):
        self.serial.close()

    def onRef(self):
        self.combo.clear()
        self.portlist = []
        ports = QSerialPortInfo.availablePorts()
        for item in ports :
            self.portlist.append(item.portName())
        self.combo.addItems(self.portlist)



    def initMenu(self):
        menubar = self.menuBar()
        self.setMenuBar(menubar)

        serviceMenu = menubar.addMenu("&Service")
        serviceMenu.addAction(self.information)

    def onAvar(self):
        self.avariya = WindowAvar()
        self.avariya.showMaximized()

    def initAction(self):
        self.information = QAction("&Аварии", self)
        self.information.triggered.connect(self.onAvar)


app = QApplication(sys.argv)
win = ArduinoPython()

win.show()
app.exec()