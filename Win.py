# -*- coding: utf-8 -*-
import os
# Form implementation generated from reading ui file 'UITEST.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#TODO:idf安装过程
#TODO:PyCharm连接功能
#TODO:shell输入功能以及代码上传测试功能
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import UITEST
import Serial
import threading
import time
import varity
import pyboard
import subprocess

import subprocess
from queue import Queue


Port = ""
Click = 0
Serial = Serial.Serial()
PortList = []
LastPortList = []

def comBoxSelected():
    global Port
    global pyb
    print(Serial.comports[Ui.comboBox.currentIndex()])
    Port = Serial.comports[Ui.comboBox.currentIndex()]

def Earse_Flash():
    global Click
    while True:
        if Click == 1:
            CMD = "esptool.py --port "+Port+" erase_flash"
            print(time.asctime())
            Ui.lineEdit.setText("Earsing Flash")
            os.system(CMD)
            OutPut = time.asctime()+"   Erasing complete"
            Ui.lineEdit.setText(OutPut)
            Click = 0


def Clicked():
    global Click
    Click = 1
    os.system("exit")



def Window():#WindowReFlash
    global LastPortList
    while True:
        PortList = varity.q.get()
        if (PortList == LastPortList) == False:
            Ui.comboBox.clear()
            Ui.comboBox.addItems(PortList)
            LastPortList = PortList

def ConnectToESPDevice():#如果可以连接到板子，并且成功执行代码，就不显示窗口，否则显示窗口让用户选择Port
    osStaues = print(os.system("python pyboard.py -d COM21 app.py"))  # 连接+直接执行
    if osStaues !=0:
        MainWndow.show()

# def RecordFiles():
#


# _QTWindows_#
app = QtWidgets.QApplication(sys.argv)
MainWndow = QtWidgets.QMainWindow()
Ui = UITEST.Ui_Dialog()
Ui.setupUi(MainWndow)



Ui.comboBox.currentIndexChanged.connect(comBoxSelected)
Ui.pushButton_3.clicked.connect(Clicked)
Ui.pushButton_2.clicked.connect(ConnectToESPDevice)
Ui.lineEdit.setReadOnly(True)
# _QTWindows_#

#_Thread_
GetSerial = threading.Thread(target=Serial.UpDatePortList)
WindowProc = threading.Thread(target=Window)
ClickProc = threading.Thread(target=Earse_Flash)
CTD = threading.Thread(target=ConnectToESPDevice)
ConnectToESPDevice()
#_Thread_

#CTD.start()
GetSerial.start()
ClickProc.start()
WindowProc.start()


sys.exit(app.exec())


