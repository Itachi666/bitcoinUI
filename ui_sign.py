# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/sign.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(633, 203)
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 160, 151, 28))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 60, 151, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 421, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 451, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 421, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 160, 151, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 10, 151, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Sign Transaction", None))
        self.pushButton_4.setText(_translate("Dialog", "No", None))
        self.pushButton_3.setText(_translate("Dialog", "See more", None))
        self.label_3.setText(_translate("Dialog", "Now you can sign them with your private key:", None))
        self.label.setText(_translate("Dialog", "Here is your partner\'s  Commitment Transaction:", None))
        self.label_2.setText(_translate("Dialog", "Here is your partner\'s Delivery Transaction:", None))
        self.pushButton.setText(_translate("Dialog", "Ok", None))
        self.pushButton_2.setText(_translate("Dialog", "See more", None))

