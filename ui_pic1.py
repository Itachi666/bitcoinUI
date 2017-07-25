# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/pic1.ui'
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

class Ui_pic1(object):
    def setupUi(self, pic1):
        pic1.setObjectName(_fromUtf8("pic1"))
        pic1.resize(815, 901)
        self.label = QtGui.QLabel(pic1)
        self.label.setGeometry(QtCore.QRect(-10, 0, 831, 901))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("pic1.png")))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(pic1)
        QtCore.QMetaObject.connectSlotsByName(pic1)

    def retranslateUi(self, pic1):
        pic1.setWindowTitle(_translate("pic1", "No Send", None))

