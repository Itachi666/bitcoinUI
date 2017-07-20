# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/anotherinput.ui'
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
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(60, 50, 501, 61))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 250, 151, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 250, 151, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 371, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit_2 = QtGui.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 160, 501, 61))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "AnotherInput", None))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">02486f11079cf6c386fab19cfb8bf9dcda7b98070b3dadbbce3ab00a102769e3b6</span></p></body></html>", None))
        self.pushButton.setText(_translate("Dialog", "Ok", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancel", None))
        self.label_2.setText(_translate("Dialog", "Enter the private key of your file:", None))
        self.label.setText(_translate("Dialog", "Enter the public key of your file:", None))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">9afdb8c1572ccc025be325f8736b836519c64a4d2016a2e576907d2f387ae6a2</span></p></body></html>", None))

