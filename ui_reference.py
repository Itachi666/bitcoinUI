# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/reference.ui'
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

class Ui_Reference(object):
    def setupUi(self, Reference):
        Reference.setObjectName(_fromUtf8("Reference"))
        Reference.resize(720, 761)
        self.label = QtGui.QLabel(Reference)
        self.label.setGeometry(QtCore.QRect(0, 0, 721, 761))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("transaction.png")))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Reference)
        QtCore.QMetaObject.connectSlotsByName(Reference)

    def retranslateUi(self, Reference):
        Reference.setWindowTitle(_translate("Reference", "Reference", None))

