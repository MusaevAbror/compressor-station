import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from window.avariya import WindowAvar
from models import *







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
        self.combo.setEditable(False)
        
        self.combo_c = QComboBox(self) # Combobox curerni rejimini tanlash 
        self.combo_c.setGeometry(350, 500, 100, 30)
        self.combo_c.addItem("Вручной", 1)
        self.combo_c.addItem("Авто", 2)
        self.combo_c.currentIndexChanged.connect(self.onCurer)

        self.btn_o = QPushButton("Открывать", self) # Button 
        self.btn_o.move(140, 30)
        self.btn_o.clicked.connect(self.onOpen)

        self.btn_c = QPushButton("Закрывать", self)
        self.btn_c.move(250, 30)
        self.btn_c.clicked.connect(self.onClose)

        self.btn_s = QPushButton("Стоп", self)
        self.btn_s.move(360, 30)

        self.btn_p = QPushButton("Запуск", self)
        self.btn_p.move(470 ,30)

        self.tem_M1_Bar = QProgressBar(self) # M1 Mator uchun temperatura Bar
        self.tem_M1_Bar.setGeometry(50, 120, 50, 270)
        self.tem_M1_Bar.setOrientation(QtCore.Qt.Vertical)
        self.tem_M1_Bar.setMaximum(150)
        self.tem_M1_Bar.setValue(52)
        

        self.tem_M1_sb = QSpinBox(self)   # M1 Matorning Temperaturasini SpinBox
        self.tem_M1_sb.setGeometry(50, 400, 50, 30)
        self.tem_M1_sb.setMaximum(self.tem_M1_Bar.maximum())
        self.tem_M1_sb.setValue(100)
        self.tem_M1_sb.valueChanged.connect(self.onSpin_M1)

        self.tem1_ch = QCheckBox(self) # M1 SpinBox uchun CheckBox
        self.tem1_ch.setGeometry(110, 400, 50, 30)
        self.tem1_ch.clicked.connect(self.onCheck_mt1)
        self.tem1_ch.setChecked(True)

        self.tem1_l = QLabel(self)   # M1 Mator Temperaturasining Labeli
        self.tem1_l.setFrameShape(QFrame.WinPanel)
        self.tem1_l.setFrameShadow(QFrame.Raised)
        self.tem1_l.setGeometry(5, 435, 140, 30)
        self.tem1_l.setText('''<html><head/><body><p><span style=" font-family:'Consolas,Courier New,monospace'; font-size:10pt; font-weight:600; color:#000000;">Температура М1</span></p></body></html>''')

        self.tem1_lf = QLabel(self) # M1 Matorning temperaturasini C da ifodalovchi Label
        self.tem1_lf.setGeometry(60, 85, 40, 30)
        self.tem1_lf.setText(str(self.tem_M1_Bar.value()) + " ℃ ")

        
        

        self.tem_M2_Bar = QProgressBar(self)  # M2 Matorning temperaturasi uchun ProgressBar 
        self.tem_M2_Bar.setGeometry(250, 120, 50, 270)
        self.tem_M2_Bar.setOrientation(QtCore.Qt.Vertical)
        self.tem_M2_Bar.setMaximum(150)
        self.tem_M2_Bar.setValue(22)

        self.tem_M2_sb = QSpinBox(self) # M2 matorning temperaturasi uchun SpinBox 
        self.tem_M2_sb.setGeometry(250, 400, 50, 30)
        self.tem_M2_sb.setMaximum(self.tem_M2_Bar.maximum())
        self.tem_M2_sb.setValue(100)
        self.tem_M2_sb.valueChanged.connect(self.onSpin_M2)

        self.tem2_ch = QCheckBox(self) # M2 matorning spinBoxi uchun CheckBox
        self.tem2_ch.setGeometry(310, 400, 50, 30)
        self.tem2_ch.setChecked(True)
        self.tem2_ch.clicked.connect(self.onCheck_mt2)

        self.tem2_l = QLabel(self)  # M2 Matorning temperaturasini Labeli
        self.tem2_l.setFrameShape(QFrame.WinPanel)
        self.tem2_l.setFrameShadow(QFrame.Raised)
        self.tem2_l.setGeometry(205, 435, 140, 30)
        self.tem2_l.setText('''<html><head/><body><p><span style=" font-family:'Consolas,Courier New,monospace'; font-size:10pt; font-weight:600; color:#000000;">Температура М2</span></p></body></html>''')

        self.tem2_lf = QLabel(self) # M2 mator temperaturasini C da ifodalovchi Label
        self.tem2_lf.setGeometry(255, 85, 40, 30)
        self.tem2_lf.setText(str(self.tem_M2_Bar.value()) + " ℃ ")



        self.tem_T1_Bar = QProgressBar(self) # T1 tranzistorning temperaturasini ko`rsatuvchi ProgressBar
        self.tem_T1_Bar.setGeometry(450, 120, 50, 270)
        self.tem_T1_Bar.setOrientation(QtCore.Qt.Vertical)
        self.tem_T1_Bar.setMaximum(200)
        self.tem_T1_Bar.setValue(122)

        self.tem_T1_sb = QSpinBox(self) # T1 Tranzistor Temperaturasi uchun SpinBox
        self.tem_T1_sb.setGeometry(450, 400, 50, 30)
        self.tem_T1_sb.setMaximum(self.tem_M2_Bar.maximum())
        self.tem_T1_sb.setValue(120)
        self.tem_T1_sb.valueChanged.connect(self.onSpin_T1)

        self.temt1_ch = QCheckBox(self)
        self.temt1_ch.setGeometry(510, 400, 50, 30)
        self.temt1_ch.setChecked(True)
        self.temt1_ch.clicked.connect(self.onCheck_t1)


        self.tem1_t1 = QLabel(self)  # T1 tranzistorning temperaturasini Labeli
        self.tem1_t1.setFrameShape(QFrame.WinPanel)
        self.tem1_t1.setFrameShadow(QFrame.Raised)
        self.tem1_t1.setGeometry(405, 435, 140, 30)
        self.tem1_t1.setText('''<html><head/><body><p><span style=" font-family:'Consolas,Courier New,monospace'; font-size:10pt; font-weight:600; color:#000000;">Температура Т1</span></p></body></html>''')

        self.tem_T1_Bar_L = QLabel(self)  # T1 Tranzistorning temperaturasini C da ifodalovchi Tabel
        self.tem_T1_Bar_L.setGeometry(455, 85, 40, 30)
        self.tem_T1_Bar_L.setText(str(self.tem_T1_Bar.value()) + " ℃ ")



        self.tem_T2_Bar = QProgressBar(self) # T2 Tranzistorning temperaturasi uchun ProgressBar 
        self.tem_T2_Bar.setGeometry(650, 120, 50, 270)
        self.tem_T2_Bar.setOrientation(QtCore.Qt.Vertical)
        self.tem_T2_Bar.setMaximum(200)
        self.tem_T2_Bar.setValue(99)

        self.tem_T2_sb = QSpinBox(self)  # T2 Tranzistor uchun SpinBox
        self.tem_T2_sb.setGeometry(650, 400, 50, 30)
        self.tem_T2_sb.setMaximum(self.tem_T2_Bar.maximum())
        self.tem_T2_sb.setValue(120)
        self.tem_T2_sb.valueChanged.connect(self.onSpin_T2)

        self.temt2_ch = QCheckBox(self) # T2 SpinBox ovhun CheckBox
        self.temt2_ch.setGeometry(710, 400, 50, 30)
        self.temt2_ch.setChecked(True)
        self.temt2_ch.clicked.connect(self.onCheck_t2)

        self.tem1_t2 = QLabel(self) # T2 Tranzistorning Temperaturasining Labeli
        self.tem1_t2.setFrameShape(QFrame.WinPanel)
        self.tem1_t2.setFrameShadow(QFrame.Raised)
        self.tem1_t2.setGeometry(605, 435, 140, 30)
        self.tem1_t2.setText('''<html><head/><body><p><span style=" font-family:'Consolas,Courier New,monospace'; font-size:10pt; font-weight:600; color:#000000;">Температура T2</span></p></body></html>''')

        self.tem1_lf = QLabel(self)  # T2 tranzistorning temperturasini C da ifodalovchi Label
        self.tem1_lf.setGeometry(655, 85, 40, 30)
        self.tem1_lf.setText(str(self.tem_T2_Bar.value()) + " ℃ ")


        self.slider_M1 = QSlider(self)
        self.slider_M1.setOrientation(QtCore.Qt.Vertical)
        self.slider_M1.setGeometry(65, 500, 70, 250)
        self.slider_M1.setMaximum(255)
        self.slider_M1.setTickPosition(QSlider.TicksBothSides)
        self.slider_M1.setSingleStep(50)
        self.slider_M1.setCursor(Qt.SplitVCursor)
        self.slider_M1.valueChanged.connect(self.onMator_1)

        self.M1_l = QLabel(self)
        self.M1_l.setFrameShape(QFrame.WinPanel)
        self.M1_l.setFrameShadow(QFrame.Raised)
        self.M1_l.setGeometry(40, 760, 120, 30)
        self.M1_l.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Скорость М1</span></p></body></html>')

        self.slider_M2 = QSlider(self)
        self.slider_M2.setOrientation(QtCore.Qt.Vertical)
        self.slider_M2.setGeometry(215, 500, 70, 250)
        self.slider_M2.setMaximum(255)
        self.slider_M2.setTickPosition(QSlider.TicksBothSides)
        self.slider_M2.setSingleStep(50)
        self.slider_M2.setCursor(Qt.SplitVCursor)
        self.slider_M2.valueChanged.connect(self.onMator_2)

        self.M2_l = QLabel(self)
        self.M2_l.setFrameShape(QFrame.WinPanel)
        self.M2_l.setFrameShadow(QFrame.Raised)
        self.M2_l.setGeometry(185, 760, 120, 30)
        self.M2_l.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Скорость М2</span></p></body></html>')


        if self.combo_c.currentData() == 1:
            self.slider_Curer = QSlider(self)
            self.slider_Curer.setOrientation(QtCore.Qt.Vertical)
            self.slider_Curer.setGeometry(365, 550, 70, 200)
            self.slider_Curer.setMaximum(255)
            self.slider_Curer.setTickPosition(QSlider.TicksBothSides)
            self.slider_Curer.setSingleStep(50)
            self.slider_Curer.valueChanged.connect(self.onDataCurer)


            self.c_l = QLabel(self)
            self.c_l.setFrameShape(QFrame.WinPanel)
            self.c_l.setFrameShadow(QFrame.Raised)
            self.c_l.setGeometry(320, 760, 160, 30)
            self.c_l.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Скорость Сурера</span></p></body></html>')

        
        self.qlcd_o_m1 = QLCDNumber(self)
        self.qlcd_o_m1.setGeometry(800, 120, 250, 100)
        self.qlcd_o_m1.display("12000")

        self.lcd_o_m1 = QLabel(self)
        self.lcd_o_m1.setFrameShape(QFrame.WinPanel)
        self.lcd_o_m1.setFrameShadow(QFrame.Raised)
        self.lcd_o_m1.setGeometry(820, 230, 200, 30)
        self.lcd_o_m1.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Оборот М1 (об/мин)</span></p></body></html>')
        

        self.qlcd_0_m2 = QLCDNumber(self)
        self.qlcd_0_m2.setGeometry(800, 290, 250, 100)
        
        self.lcd_0_m2 = QLabel(self)
        self.lcd_0_m2.setFrameShape(QFrame.WinPanel)
        self.lcd_0_m2.setFrameShadow(QFrame.Raised)
        self.lcd_0_m2.setGeometry(820, 400, 200, 30)
        self.lcd_0_m2.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Оборот М2 (об/мин)</span></p></body></html>')

        self.qlcd_G = QLCDNumber(self)
        self.qlcd_G.setGeometry(800, 460, 250, 100)

        self.lcd_G = QLabel(self)
        self.lcd_G.setFrameShape(QFrame.WinPanel)
        self.lcd_G.setFrameShadow(QFrame.Raised)
        self.lcd_G.setGeometry(830, 570, 180, 30)
        self.lcd_G.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Степен Газа (ppm)</span></p></body></html>')
        
    
        self.green_led_p = QLabel(self)
        self.green_led_p.setStyleSheet("QLabel {background-color : green; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.green_led_p.move(870, 650)
        
        self.red_led_p = QLabel(self)
        self.red_led_p.setStyleSheet("QLabel {background-color : red; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.red_led_p.move(870, 650)

        self.l_y = QLabel(self)
        self.l_y.setFrameShape(QFrame.WinPanel)
        self.l_y.setFrameShadow(QFrame.Raised)
        self.l_y.setGeometry(810, 700, 220, 30)
        self.l_y.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Информация о пожаре </span></p></body></html>')

        self.green_led_v = QLabel(self)
        self.green_led_v.setStyleSheet("QLabel {background-color : green; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.green_led_v.move(870, 780)

        self.red_led_v = QLabel(self)
        self.red_led_v.setStyleSheet("QLabel {background-color : red; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.red_led_v.move(870, 780)

        self.l_v = QLabel(self)
        self.l_v.setFrameShape(QFrame.WinPanel)
        self.l_v.setFrameShadow(QFrame.Raised)  
        self.l_v.setGeometry(810, 820, 235, 30)
        self.l_v.setText('<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#0000ff;">Информация о выбрации </span></p></body></html>')

    def initAction(self):
        self.information = QAction("&Аварии", self)
        self.information.triggered.connect(self.onAvar)

    
    def initMenu(self):
        menubar = self.menuBar()
        self.setMenuBar(menubar)

        serviceMenu = menubar.addMenu("&Service")
        serviceMenu.addAction(self.information)

    def onAvar(self):
        self.avariya = WindowAvar()
        self.avariya.showMaximized()
        
    def avariya(self):
        pass



    
    def onCheck_mt1(self, onOff):
        if onOff is False:
            self.currentVal1 = self.tem_M1_sb.value()
            self.tem_M1_sb.setVisible(False)
            self.tem_M1_sb.setValue(self.tem_M1_Bar.maximum())
           
        else :
            self.tem_M1_sb.setValue(self.currentVal1)
            self.tem_M1_sb.setVisible(True)


    def onCheck_mt2(self, onOff):
        if onOff is False:
            self.currentVal2 = self.tem_M2_sb.value()
            self.tem_M2_sb.setVisible(False)
            self.tem_M2_sb.setValue(self.tem_M2_Bar.maximum())
        else : 
            self.tem_M2_sb.setValue(self.currentVal2)
            self.tem_M2_sb.setVisible(True)


    def onCheck_t1(self, onOff):
        if onOff is False:
            self.currentVal3 = self.tem_T1_sb.value()
            self.tem_T1_sb.setVisible(False)
            self.tem_T1_sb.setValue(self.tem_T1_Bar.maximum())
        else:
            self.tem_T1_sb.setValue(self.currentVal3)
            self.tem_T1_sb.setVisible(True)

    def onCheck_t2(self, onOff):
        if onOff is False:
            self.currentVal4 = self.tem_T2_sb.value()
            self.tem_T2_sb.setVisible(False)
            self.tem_T2_sb.setValue(self.tem_T2_Bar.maximum())
        else:
            self.tem_T2_sb.setValue(self.currentVal4)
            self.tem_T2_sb.setVisible(True)

    def onSpin_M1(self, val):
        if val <= self.tem_M1_Bar.value():
            self.qmsg.setIcon(QMessageBox.Critical)
            self.qmsg.setWindowTitle("AVARIYA")
            self.qmsg.setText("Birinchi Matorning Temperturasi oshib ketdi")
            self.qmsg.show()

    def onSpin_M2(self, val):
        if val <= self.tem_M2_Bar.value():
            tem_m1 = str(self.tem_M1_Bar.value())
            tem_m2 = str(self.tem_M2_Bar.value())
            tem_t1 = str(self.tem_T1_Bar.value())
            tem_t2 = str(self.tem_T2_Bar.value())
            

            TableAvariy(tem_m1, tem_m2, tem_t1, tem_t2, )
            self.qmsg.setIcon(QMessageBox.Critical)
            self.qmsg.setWindowTitle("AVARIYA")
            self.qmsg.setText("M2 Matorning temperaturasi oshib ketti")
            self.qmsg.show()

    def onSpin_T1(self, val):
        if val <= self.tem_T1_Bar.value():
            self.qmsg.setIcon(QMessageBox.Critical)
            self.qmsg.setWindowTitle("AVARIYA")
            self.qmsg.setText("T1 Tranzistorning temperaturasi oshib ketti")
            self.qmsg.show()

    def onSpin_T2(self, val):
        if val <= self.tem_T2_Bar.value():
            self.qmsg.setIcon(QMessageBox.Critical)
            self.qmsg.setWindowTitle("AVARIYA")
            self.qmsg.setText("T2 Tranzistorning Temperaturasi oshib ketti")
            self.qmsg.show()

    
    
    
    
    
    def onCurer(self):
        if self.combo_c.currentData() == 1:
            self.slider_Curer.setVisible(True)
            self.c_l.setVisible(True)
            self.slider_Curer.setEnabled(True)
            self.slider_Curer.valueChanged.connect(self.onDataCurer)

        elif self.combo_c.currentData() == 2:
            self.slider_Curer.setEnabled(False)
            self.slider_Curer.setValue(21)
            

    def onDataCurer(self, a):
        self.SerialSend([3, a])

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
                print(self.data)
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




app = QApplication(sys.argv)
win = ArduinoPython()

win.show()
app.exec()