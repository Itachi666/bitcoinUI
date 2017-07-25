# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/pic4.ui'
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

class Ui_pic4(object):
    def setupUi(self, pic4):
        pic4.setObjectName(_fromUtf8("pic4"))
        pic4.resize(815, 901)
        self.label = QtGui.QLabel(pic4)
        self.label.setGeometry(QtCore.QRect(-10, 0, 831, 901))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("pic4.png")))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(pic4)
        QtCore.QMetaObject.connectSlotsByName(pic4)

    def retranslateUi(self, pic4):
        pic4.setWindowTitle(_translate("pic4", "Send all", None))

