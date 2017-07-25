# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/pic3.ui'
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

class Ui_pic3(object):
    def setupUi(self, pic3):
        pic3.setObjectName(_fromUtf8("pic3"))
        pic3.resize(815, 901)
        self.label = QtGui.QLabel(pic3)
        self.label.setGeometry(QtCore.QRect(-10, 0, 831, 901))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("pic3.png")))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(pic3)
        QtCore.QMetaObject.connectSlotsByName(pic3)

    def retranslateUi(self, pic3):
        pic3.setWindowTitle(_translate("pic3", "No Send", None))

