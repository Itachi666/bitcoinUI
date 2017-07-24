# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/send.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ui_createtx
import ui_signtx
import ui_up2bit

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


class create(ui_createtx.QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = ui_createtx.Ui_Dialog()  # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)


class sign(ui_signtx.QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = ui_signtx.Ui_signtx()  # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)

class up2bit(ui_up2bit.QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = ui_up2bit.Ui_send2bit()  # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)


class Ui_send(object):
    def setupUi(self, send):
        send.setObjectName(_fromUtf8("send"))
        send.resize(340, 347)
        self.groupBox = QtGui.QGroupBox(send)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 331))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 180, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 260, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.pushButton.clicked.connect(self.create)
        self.pushButton_2.clicked.connect(self.sign)
        self.pushButton_3.clicked.connect(self.exchange)
        self.pushButton_4.clicked.connect(self.uptx)

        self.retranslateUi(send)
        QtCore.QMetaObject.connectSlotsByName(send)

    def retranslateUi(self, send):
        send.setWindowTitle(_translate("send", "Create and send Transaction", None))
        self.pushButton.setText(_translate("send", "Create raw transactions", None))
        self.pushButton_2.setText(_translate("send", "Sign raw transactions", None))
        self.pushButton_3.setText(_translate("send", "Exchange raw transactions", None))
        self.pushButton_4.setText(_translate("send", "Send raw transactions", None))

    def create(self):
        myapp = create()
        myapp.ui.putin2data(self.mydata)
        myapp.show()
        myapp.exec_()
        self.a, self.b, self.c, self.d, self.e = myapp.ui.getcreatedata()

    def sign(self):
        myapp = sign()
        myapp.ui.putin2data(self.mydata, self.a, self.b, self.c, self.d, self.e)
        myapp.show()
        myapp.exec_()
        self.sigtx, self.siga, self.sigb = myapp.ui.getsigndata()

    def showHint(self):
        hint_msg = QtGui.QMessageBox()
        hint_msg.setWindowTitle('Finish!')
        hint_msg.setText('Get Transactions')
        hint_msg.addButton(QtGui.QMessageBox.Ok)
        hint_msg.exec_()

    def exchange(self):
        self.showHint()

    def uptx(self):
        myapp = up2bit()
        myapp.show()
        myapp.exec_()

    def putin2data(self, data):
        self.mydata = data
