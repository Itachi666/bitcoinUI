# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/generate.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ui_details

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


class details(ui_details.QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = ui_details.Ui_details()  # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)

class Ui_Generated(object):
    def setupUi(self, Generated):
        Generated.setObjectName(_fromUtf8("Generated"))
        Generated.resize(399, 492)
        self.label_2 = QtGui.QLabel(Generated)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 321, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(Generated)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 361, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(Generated)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 210, 361, 161))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label = QtGui.QLabel(Generated)
        self.label.setGeometry(QtCore.QRect(20, 0, 261, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Generated)
        self.label_3.setGeometry(QtCore.QRect(20, 370, 361, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(Generated)
        self.pushButton.setGeometry(QtCore.QRect(80, 450, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit_3 = QtGui.QTextEdit(Generated)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 400, 361, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.pushButton_2 = QtGui.QPushButton(Generated)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 450, 93, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_2.clicked.connect(self.moredetail)

        self.retranslateUi(Generated)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Generated.accept)
        QtCore.QMetaObject.connectSlotsByName(Generated)

    def retranslateUi(self, Generated):
        Generated.setWindowTitle(_translate("Generated", "Successfully Generated！", None))
        self.label_2.setText(_translate("Generated", "Here is your Private key(Important)：", None))
        self.textEdit.setHtml(_translate("Generated",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">cV2tkAFehDQjHXbnJZCpVPeqtB3v7RwGVUPSCVeTwvbCS9hwvm3W</span></p></body></html>",
                                         None))
        self.textEdit_2.setHtml(_translate("Generated",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">03c5940c90925467eedc8809fa03088258edc4fe33150bb2010daee5c11c10b57b</p></body></html>",
                                           None))
        self.label.setText(_translate("Generated", "Here is your Public key：", None))
        self.label_3.setText(_translate("Generated", "Here is your Hash salt(Important)：", None))
        self.pushButton.setText(_translate("Generated", "Ok", None))
        self.textEdit_3.setHtml(_translate("Generated",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">cb62f3ea</span></p></body></html>",
                                           None))
        self.pushButton_2.setText(_translate("Generated", "Details", None))

    def putdata(self, p, q, n, h, salt, sk, Wifsk, pk, com_pk, address):
        self.textEdit.setHtml(_translate("Generated",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">%s</span></p></body></html>" % Wifsk,
                                         None))
        self.textEdit_2.setHtml(_translate("Generated",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</p></body></html>" % com_pk,
                                           None))
        self.textEdit_3.setHtml(_translate("Generated",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">%s</span></p></body></html>" % salt,
                                           None))
        self.h = h
        self.p = p
        self.q = q
        self.sk = sk
        self.pk = pk
        self.address = address

    def moredetail(self):
        myapp = details()
        myapp.ui.putdata(self.p, self.q, self.h, self.sk, self.pk, self.address)
        myapp.show()
        myapp.exec_()
