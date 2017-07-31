# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/showtxid.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_showtxid(object):
    def setupUi(self, showtxid):
        showtxid.setObjectName(_fromUtf8("showtxid"))
        showtxid.resize(663, 414)
        self.pushButton = QtGui.QPushButton(showtxid)
        self.pushButton.setGeometry(QtCore.QRect(500, 370, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(showtxid)
        self.label.setGeometry(QtCore.QRect(10, 10, 581, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(showtxid)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(showtxid)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(showtxid)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 581, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_3 = QtGui.QLineEdit(showtxid)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 180, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_3 = QtGui.QLabel(showtxid)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 581, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_4 = QtGui.QLineEdit(showtxid)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 250, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_4 = QtGui.QLabel(showtxid)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 581, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_5 = QtGui.QLineEdit(showtxid)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 320, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_5 = QtGui.QLabel(showtxid)
        self.label_5.setGeometry(QtCore.QRect(10, 290, 581, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(showtxid)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), showtxid.accept)
        QtCore.QMetaObject.connectSlotsByName(showtxid)

    def retranslateUi(self, showtxid):
        showtxid.setWindowTitle(_translate("showtxid", "Show Txid", None))
        self.pushButton.setText(_translate("showtxid", "OK", None))
        self.label.setText(_translate("showtxid", "Funding Transaction txid:", None))
        self.label_2.setText(_translate("showtxid", "Commitment Transaction txid:", None))
        self.label_3.setText(_translate("showtxid", "Timeout Commitment Transaction txid:", None))
        self.label_4.setText(_translate("showtxid", "Delivery Transaction txid:", None))
        self.label_5.setText(_translate("showtxid", "Timeout Delivery Transaction txid:", None))

    def putin2data(self,txid):
        self.lineEdit.setText(txid[0])
        self.lineEdit_2.setText(txid[1])
        self.lineEdit_3.setText(txid[2])
        self.lineEdit_4.setText(txid[3])
        self.lineEdit_5.setText(txid[4])

