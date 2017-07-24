# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/up2bit.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from time import strftime,gmtime
import socket
import time
import threading

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_send2bit(object):
    def setupUi(self, send2bit):
        send2bit.setObjectName(_fromUtf8("send2bit"))
        send2bit.resize(603, 417)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        send2bit.setFont(font)
        self.pushButton = QtGui.QPushButton(send2bit)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(send2bit)
        self.lineEdit.setGeometry(QtCore.QRect(400, 50, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(send2bit)
        self.label.setGeometry(QtCore.QRect(300, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(send2bit)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 10, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(send2bit)
        self.label_2.setGeometry(QtCore.QRect(290, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(send2bit)
        self.groupBox.setGeometry(QtCore.QRect(10, 170, 581, 231))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 90, 541, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 541, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 160, 541, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.groupBox_2 = QtGui.QGroupBox(send2bit)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 170, 581, 161))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 20, 541, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 90, 541, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_3 = QtGui.QLabel(send2bit)
        self.label_3.setGeometry(QtCore.QRect(80, 80, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_7 = QtGui.QPushButton(send2bit)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 130, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(send2bit)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 130, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(send2bit)
        self.pushButton_9.setGeometry(QtCore.QRect(520, 130, 71, 31))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.groupBox_2.raise_()
        self.label_3.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.groupBox.raise_()

        self.pushButton.clicked.connect(self.checking)
        self.pushButton_2.clicked.connect(self.sendfunding)
        self.pushButton_3.clicked.connect(self.sendcommit)
        self.pushButton_4.clicked.connect(self.sendtcommit)
        self.pushButton_5.clicked.connect(self.senddelivery)
        self.pushButton_6.clicked.connect(self.sendtdelivery)
        self.count = 0

        self.retranslateUi(send2bit)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.groupBox.close)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_3.close)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_7.close)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_3.close)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_8.close)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_8.close)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_7.close)
        QtCore.QMetaObject.connectSlotsByName(send2bit)

    def retranslateUi(self, send2bit):
        send2bit.setWindowTitle(_translate("send2bit", "up2bit", None))
        self.pushButton.setText(_translate("send2bit", "Checking Progress", None))
        self.lineEdit.setText(_translate("send2bit", "1 day", None))
        self.label.setText(_translate("send2bit", "Deadline:", None))
        self.lineEdit_2.setText(_translate("send2bit", "Null", None))
        self.label_2.setText(_translate("send2bit", "StartTime:", None))
        self.pushButton_3.setText(_translate("send2bit", "Sign and Send Commitment Transaction", None))
        self.pushButton_2.setText(_translate("send2bit", "Send Funding Transaction", None))
        self.pushButton_6.setText(_translate("send2bit", "Send Timeoutdelivery Transaction", None))
        self.pushButton_5.setText(_translate("send2bit", "Sign and Send Delivery Transaction", None))
        self.pushButton_4.setText(_translate("send2bit", "Send TimeoutCommitment Transaction", None))
        self.label_3.setText(_translate("send2bit", "Are you going to send Funding Transaction?", None))
        self.pushButton_7.setText(_translate("send2bit", "Yes", None))
        self.pushButton_8.setText(_translate("send2bit", "No", None))
        self.pushButton_9.setText(_translate("send2bit", "Refresh", None))

    def showHint(self):
        hint_msg = QtGui.QMessageBox()
        hint_msg.setWindowTitle('Congratulation!')
        hint_msg.setText('Sent successfully')
        hint_msg.addButton(QtGui.QMessageBox.Ok)
        hint_msg.exec_()

    def checking(self):
        pass

    def sendfunding(self):
        self.count = 1
        t = strftime("%Y-%m-%d %H:%M")
        self.time = unicode(t)
        self.lineEdit_2.setText(_translate("send2bit", self.time, None))
        self.showHint()

    def sendcommit(self):
        self.count = 2
        self.showHint()
        t = strftime("%Y-%m-%d %H:%M")
        self.time = unicode(t)
        self.lineEdit_2.setText(_translate("send2bit", self.time, None))

    def sendtcommit(self):
        self.count = 3
        self.showHint()

    def senddelivery(self):
        self.count = 4
        self.showHint()

    def sendtdelivery(self):
        self.count = 5
        self.showHint()

    def connect_ip(self):
        ip = '192.168.75.1'
        port = 12345
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        newdata = [self.time,'1']
        print(s.recv(1024))
        for data in newdata:
            s.send(data.encode())
            newdata.append(s.recv(1024))
        s.send('exit')
        s.close()

