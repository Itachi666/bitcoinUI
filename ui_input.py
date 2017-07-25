# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/input.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import SkPk
import ui_generate

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


class generate(ui_generate.QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = ui_generate.Ui_Generated()  # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)


class Ui_input(QtGui.QWidget):
    def setupUi(self, input):
        input.setObjectName(_fromUtf8("input"))
        input.resize(952, 424)
        self.setFixedSize(self.width(), self.height())
        self.textEdit = QtGui.QTextEdit(input)
        self.textEdit.setGeometry(QtCore.QRect(260, 20, 641, 91))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(input)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 140, 641, 91))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.pushButton_4 = QtGui.QPushButton(input)
        self.pushButton_4.setGeometry(QtCore.QRect(760, 360, 131, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.textEdit_3 = QtGui.QTextEdit(input)
        self.textEdit_3.setGeometry(QtCore.QRect(260, 300, 591, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.label_3 = QtGui.QLabel(input)
        self.label_3.setGeometry(QtCore.QRect(30, 310, 181, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(input)
        self.label.setGeometry(QtCore.QRect(30, 20, 261, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_3 = QtGui.QPushButton(input)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 300, 31, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_2 = QtGui.QLabel(input)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 261, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(input)
        self.pushButton.setGeometry(QtCore.QRect(260, 360, 121, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(input)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 360, 121, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_6 = QtGui.QPushButton(input)
        self.pushButton_6.setGeometry(QtCore.QRect(260, 250, 261, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_5 = QtGui.QPushButton(input)
        self.pushButton_5.setGeometry(QtCore.QRect(640, 250, 261, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.textEdit_4 = QtGui.QTextEdit(input)
        self.textEdit_4.setGeometry(QtCore.QRect(2000, 4000, 361, 41))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))

        self.pushButton_5.clicked.connect(self.getpandq)
        self.pushButton_6.clicked.connect(self.Require)
        self.pushButton_3.clicked.connect(self.file_click)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), input.accept)
        self.pushButton.clicked.connect(self.createkey)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), input.accept)

        self.retranslateUi(input)
        QtCore.QMetaObject.connectSlotsByName(input)

    def retranslateUi(self, input):
        input.setWindowTitle(_translate("input", "Input", None))
        self.textEdit.setHtml(_translate("input",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                         None))
        self.textEdit_2.setHtml(_translate("input",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                           None))
        self.pushButton_4.setText(_translate("input", "Another way", None))
        self.textEdit_3.setHtml(_translate("input",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">C:/Users/Niujx/Documents/GitHub/Imtest/1.pdf</span></p></body></html>",
                                           None))
        self.label_3.setText(_translate("input", "Input your file path:", None))
        self.label.setText(_translate("input", "Input a prime number p：", None))
        self.pushButton_3.setText(_translate("input", "...", None))
        self.label_2.setText(_translate("input", "Input a prime number q：", None))
        self.pushButton.setText(_translate("input", "Ok", None))
        self.pushButton_2.setText(_translate("input", "Cancel", None))
        self.pushButton_6.setText(_translate("input", "See Require", None))
        self.pushButton_5.setText(_translate("input", "Get Random Number", None))

    def getdata_p(self):
        return self.textEdit.toPlainText()

    def getdata_q(self):
        return self.textEdit_2.toPlainText()

    def getdata_inverse(self):
        return self.textEdit_4.toPlainText()

    def getdata_filepath(self):
        return self.textEdit_3.toPlainText()

    def getdata_all(self):
        return self.data

    def getpandq(self):
        p, q, inverse3 = SkPk.generate_pq()
        i = hex(p)[2:len(hex(p)) - 1]
        j = hex(q)[2:len(hex(q)) - 1]
        self.textEdit.setHtml(_translate("input",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%s</span></p></body></html>" % i,
                                         None))
        self.textEdit_2.setHtml(_translate("input",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%s</span></p></body></html>" % j,
                                           None))
        self.textEdit_4.setHtml(_translate("input",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%s</span></p></body></html>" % str(
                                               inverse3),
                                           None))

    def Require(self):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)

        msg.setText("P&Q should be a prime.")
        msg.setInformativeText("and should not less than 1024 bits")
        msg.setWindowTitle("Require")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)

        msg.exec_()

    def file_click(self):
        # absolute_path is a QString object
        absolute_path = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        if absolute_path:
            cur_path = QtCore.QDir('.')
            relative_path = cur_path.relativeFilePath(absolute_path)
            self.textEdit_3.setHtml(_translate("input",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">%s</span></p></body></html>" % absolute_path,
                                               None))

    def createkey(self):
        p = unicode(self.getdata_p())
        q = unicode(self.getdata_q())
        inverse3 = unicode(self.getdata_inverse())
        p = int(p, 16)
        q = int(q, 16)
        inverse3 = int(inverse3)

        path = self.getdata_filepath()
        path = unicode(path)
        filename = path[path.rindex("/") + 1:]
        i, j, n, h, salt, sk, Wifsk, pk, com_pk, final_pk = SkPk.getall(p, q, inverse3, path)

        hexi = hex(i)[2:len(hex(i)) - 1]
        hexj = hex(j)[2:len(hex(j)) - 1]
        hexn = hex(n)[2:len(hex(n)) - 1]
        hexsalt = hex(salt)[2:len(hex(salt)) - 1]
        hexsk = hex(sk)[2:len(hex(sk)) - 1]
        self.data = [filename, Wifsk, com_pk, hexi, hexj, hexn, h, hexsalt, hexsk, pk, final_pk]
        myapp = generate()
        myapp.ui.putdata(hexi, hexj, hexn, h, hexsalt, hexsk, Wifsk, pk, com_pk, final_pk)
        myapp.show()
        myapp.exec_()
