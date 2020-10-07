#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:50:53 2020

@author: shinhojung814
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon

class MyWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout)
        self.time = QTime(0, 0 ,0)
        self.setWindowTitle('QTimer')
        self.setGeometry(100, 100, 600, 280)
        layout = QVBoxLayout()
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(8)
        self.lcd.display(self.time.toString("hh:mm:ss"))
        subLayout = QHBoxLayout()
        self.btnStart = QPushButton("시작")
        self.btnStart.clicked.connect(self.onStartButtonClicked)
        self.btnStop = QPushButton("멈춤")
        self.btnStop.clicked.connect(self.onStopButtonClicked)
        self.btnInput = QPushButton("입력")
        self.btnInput.clicked.connect(self.onInputButtonClicked)
        layout.addWidget(self.lcd)
        subLayout.addWidget(self.btnStart)
        subLayout.addWidget(self.btnStop)
        subLayout.addWidget(self.btnInput)
        layout.addLayout(subLayout)
        self.btnStop.setEnabled(False)
        self.setLayout(layout)
        
    def onStartButtonClicked(self):
         self.timer.start()
         self.btnStop.setEnabled(True)
         self.btnStart.setEnabled(False)
         self.btnInput.setEnabled(False)
         
    def onStopButtonClicked(self):
        self.timer.stop()
        self.btnStop.setEnabled(False)
        self.btnStart.setEnabled(True)
        self.btnInput.setEnabled(True)
        
    def onInputButtonClicked(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        hour, minute, second = text.split(":")
        self.time = QTime(int(hour), int(minute) , int(second))
        self.lcd.display(self.time.toString("hh:mm:ss"))
        
    def timeout(self):
        sender = self.sender()
        self.time = self.time.addSecs(-1)
        currentTime = self.time.toString("hh:mm:ss")
        if id(sender) == id(self.timer):
            self.lcd.display(currentTime)
        if QTime(0, 0, 0) == self.time:
            self.onStopButtonClicked()
            self.time = QTime(0, 0 ,0)
            self.lcd.display(self.time.toString("hh:mm:ss"))
            buttonReply = QMessageBox.information(self, 'PyQt5', "타임 아웃")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())