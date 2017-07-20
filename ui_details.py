# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/details.ui'
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


class Ui_details(object):
    def setupUi(self, details):
        details.setObjectName(_fromUtf8("details"))
        details.resize(663, 564)
        self.label = QtGui.QLabel(details)
        self.label.setGeometry(QtCore.QRect(10, 0, 261, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(details)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 261, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(details)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 641, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(details)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 150, 641, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label_3 = QtGui.QLabel(details)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 261, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(details)
        self.label_4.setGeometry(QtCore.QRect(10, 310, 261, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEdit_3 = QtGui.QTextEdit(details)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 270, 641, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QTextEdit(details)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 340, 641, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.label_5 = QtGui.QLabel(details)
        self.label_5.setGeometry(QtCore.QRect(10, 380, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.textEdit_5 = QtGui.QTextEdit(details)
        self.textEdit_5.setGeometry(QtCore.QRect(10, 410, 641, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_6 = QtGui.QTextEdit(details)
        self.textEdit_6.setGeometry(QtCore.QRect(10, 480, 641, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.label_6 = QtGui.QLabel(details)
        self.label_6.setGeometry(QtCore.QRect(10, 450, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(details)
        self.pushButton.setGeometry(QtCore.QRect(190, 520, 291, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(details)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), details.accept)
        QtCore.QMetaObject.connectSlotsByName(details)

    def retranslateUi(self, details):
        details.setWindowTitle(_translate("details", "Details", None))
        self.label.setText(_translate("details", "Here is your prime P：", None))
        self.label_2.setText(_translate("details", "Here is your prime Q：", None))
        self.textEdit.setHtml(_translate("details",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">asdf</span></p></body></html>",
                                         None))
        self.textEdit_2.setHtml(_translate("details",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">asdf</span></p></body></html>",
                                           None))
        self.label_3.setText(_translate("details", "Here is your File Hash：", None))
        self.label_4.setText(_translate("details", "Here is your SK(hex)：", None))
        self.textEdit_3.setHtml(_translate("details",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdf</p></body></html>",
                                           None))
        self.textEdit_4.setHtml(_translate("details",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdf</p></body></html>",
                                           None))
        self.label_5.setText(_translate("details", "Here is your PK(Uncompressed)：", None))
        self.textEdit_5.setHtml(_translate("details",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdf</p></body></html>",
                                           None))
        self.textEdit_6.setHtml(_translate("details",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdf</p></body></html>",
                                           None))
        self.label_6.setText(_translate("details", "Here is your Address:", None))
        self.pushButton.setText(_translate("details", "Close", None))

    def putdata(self, p, q, h, sk, pk, address):
        self.textEdit.setHtml(_translate("details",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">%s</span></p></body></html>"%p,
                                         None))
        self.textEdit_2.setHtml(_translate("details",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">%s</span></p></body></html>"%q,
                                           None))
        self.textEdit_3.setHtml(_translate("details",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</span></p></body></html>"%h,
                                           None))
        self.textEdit_4.setHtml(_translate("details",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</span></p></body></html>"%sk,
                                           None))
        self.textEdit_5.setHtml(_translate("details",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</span></p></body></html>"%pk,
                                           None))
        self.textEdit_6.setHtml(_translate("details",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</span></p></body></html>"%address,
                                           None))