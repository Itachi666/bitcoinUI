# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/createtx.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ui_reference
import tx
import common
import json

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


class reference(ui_reference.QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = ui_reference.Ui_Reference()  # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(969, 739)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(430, 100, 521, 611))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 230, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 470, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 590, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 0, 641, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 350, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 240, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 360, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 480, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 600, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 680, 131, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(230, 680, 131, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.textEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.textEdit.setFontPointSize(15)

        self.txidfundingtx=0
        self.redeemscripta=0
        self.fundingtx_1=0
        self.fundingtx_2=0
        self.fundingtx_3=0
        self.txidcommitmenttx=0
        self.redeemscriptb=0
        self.commitmenttx_1=0
        self.commitmenttx_2=0
        self.txidtimeoutcommmitmenttx=0
        self.timeoutcommmitmenttx_1=0
        self.timeoutcommmitmenttx_2=0
        self.txiddeliverytx=0
        self.deliverytx_1=0
        self.deliverytx_2=0
        self.txidtimeoutdeliverytx=0
        self.timeoutdeliverytx_1=0
        self.timeoutdeliverytx_2=0

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.FundingTransaction)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton.close)

        self.pushButton_2.clicked.connect(self.CommitmentTransaction)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_2.close)

        self.pushButton_5.clicked.connect(self.TimeCommitmentTransaction)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_5.close)

        self.pushButton_3.clicked.connect(self.DeliveryTransaction)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_3.close)

        self.pushButton_4.clicked.connect(self.TimeDeliveryTransaction)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_4.close)

        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reference)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Transactions", None))
        self.pushButton.setText(_translate("Dialog", "Create Funding Transaction", None))
        self.pushButton_2.setText(_translate("Dialog", "Create Commitment Transaction", None))
        self.pushButton_3.setText(_translate("Dialog", "Create Delivery Transaction", None))
        self.pushButton_4.setText(_translate("Dialog", "Create Timeout Delivery Transaction", None))
        self.label.setText(_translate("Dialog", "Create Raw Transactions", None))
        self.pushButton_5.setText(_translate("Dialog", "Create Timeout Commitment Transaction", None))
        self.label_2.setText(_translate("Dialog", "Completed", None))
        self.label_3.setText(_translate("Dialog", "Completed", None))
        self.label_4.setText(_translate("Dialog", "Completed", None))
        self.label_5.setText(_translate("Dialog", "Completed", None))
        self.label_6.setText(_translate("Dialog", "Completed", None))
        self.pushButton_6.setText(_translate("Dialog", "Ok", None))
        self.pushButton_7.setText(_translate("Dialog", "See Reference", None))
        self.textEdit.setHtml(_translate("Dialog",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"> </span></p></body></html>",
                                         None))

    def showDialog(self):

        edit_dialog = QtGui.QDialog()
        group = QtGui.QGroupBox('Edit Info', edit_dialog)

        lbl_txid1 = QtGui.QLabel('txid1:', group)
        le_txid1 = QtGui.QLineEdit(group)
        le_txid1.setText('a0e8fd53509411af0f8fe0c22d0fdf9ba6bb5a3897a4398533b92a1382cd7335')
        lbl_vout1 = QtGui.QLabel('vout:', group)
        le_vout1 = QtGui.QLineEdit(group)
        le_vout1.setText('1')
        lbl_txid2 = QtGui.QLabel('txid2:', group)
        le_txid2 = QtGui.QLineEdit(group)
        le_txid2.setText('3edd403baa19cde1696b348f712196e2438ebc909163e817c419f0ccd824ff13')
        lbl_vout2 = QtGui.QLabel('vout:', group)
        le_vout2 = QtGui.QLineEdit(group)
        le_vout2.setText('0')
        ok_button = QtGui.QPushButton('OK', edit_dialog)
        cancel_button = QtGui.QPushButton('CANCEL', edit_dialog)

        ok_button.clicked.connect(edit_dialog.accept)
        ok_button.setDefault(True)
        cancel_button.clicked.connect(edit_dialog.reject)

        group_layout = QtGui.QVBoxLayout()
        group_item = [lbl_txid1, le_txid1,
                      lbl_vout1, le_vout1,
                      lbl_txid2, le_txid2,
                      lbl_vout2, le_vout2]
        for item in group_item:
            group_layout.addWidget(item)
        group.setLayout(group_layout)
        group.setFixedSize(group.sizeHint())

        button_layout = QtGui.QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        dialog_layout = QtGui.QVBoxLayout()
        dialog_layout.addWidget(group)
        dialog_layout.addLayout(button_layout)
        edit_dialog.setLayout(dialog_layout)
        edit_dialog.setFixedSize(edit_dialog.sizeHint())

        if edit_dialog.exec_():
            txid1 = le_txid1.text()
            vout1 = le_vout1.text()
            txid2 = le_txid2.text()
            vout2 = le_vout2.text()
            return True, unicode(txid1), unicode(vout1), unicode(txid2), unicode(vout2)
        return False, None, None, None, None, None

    def FundingTransaction(self):
        data = self.showDialog()
        if data[0]:
            pre_txid1 = data[1]
            voutx1 = data[2]
            pre_txid2 = data[3]
            voutx2 = data[4]
            z = float(self.mydata[5])
            ha = self.mydata[9]
            pkb = self.mydata[15]
            pkam = self.mydata[3]
            pka=self.mydata[14]
            nsequence = 'ffffffff'
            fundingtx, self.txidfundingtx, self.redeemscripta, self.fundingtx_1, self.fundingtx_2, self.fundingtx_3 = tx.createfundingtx(
                pre_txid1, voutx1, pre_txid2, voutx2, z, ha, pkb, pka, nsequence)
            jsontxt = common.raw2json(fundingtx)
            k = json.dumps(jsontxt)
            self.textEdit.setText('Hex= '+fundingtx)

    def CommitmentTransaction(self):
        z = float(self.mydata[5])
        pka = self.mydata[14]
        pkb = self.mydata[15]
        h = self.mydata[9]
        pkam = self.mydata[3]
        pkbm = self.mydata[18]
        nsequence = 'ffffffff'
        commitmenttx, self.txidcommitmenttx, self.redeemscriptb, self.commitmenttx_1, self.commitmenttx_2 = tx.createcommitmenttx(
            self.txidfundingtx, 0, z, pkam, h, pka, pkb, nsequence)
        jsontxt = common.raw2json(commitmenttx)
        k = json.dumps(jsontxt)
        self.textEdit.setText('Hex= '+commitmenttx)

    def TimeCommitmentTransaction(self):
        z = float(self.mydata[5])
        pkb = self.mydata[15]
        timeoutcommmitmenttx, self.txidtimeoutcommmitmenttx, self.timeoutcommmitmenttx_1, self.timeoutcommmitmenttx_2 = tx.createone2onetx(
            self.txidfundingtx, 0, z, pkb)
        jsontxt = common.raw2json(timeoutcommmitmenttx)
        k = json.dumps(jsontxt)
        self.textEdit.setText('Hex= '+timeoutcommmitmenttx)

    def DeliveryTransaction(self):
        z = float(self.mydata[5])
        pkbm = self.mydata[18]
        deliverytx, self.txiddeliverytx, self.deliverytx_1, self.deliverytx_2 = tx.createone2onetx(
            self.txidtimeoutcommmitmenttx, 1, z, pkbm)
        jsontxt = common.raw2json(deliverytx)
        k = json.dumps(jsontxt)
        self.textEdit.setText('Hex= '+deliverytx)

    def TimeDeliveryTransaction(self):
        z = float(self.mydata[5])
        pka = self.mydata[14]
        timeoutdeliverytx, self.txidtimeoutdeliverytx, self.timeoutdeliverytx_1, self.timeoutdeliverytx_2 = tx.createone2onetx(
            self.txidtimeoutcommmitmenttx, 1, z, pka)
        jsontxt = common.raw2json(timeoutdeliverytx)
        k = json.dumps(jsontxt)
        self.textEdit.setText('Hex= '+timeoutdeliverytx)

    def reference(self):
        myapp = reference()
        myapp.show()
        myapp.exec_()

    def putin2data(self, data):
        self.mydata = data

    def getcreatedata(self):
        return [self.txidfundingtx, self.redeemscripta, self.fundingtx_1, self.fundingtx_2, self.fundingtx_3], \
               [self.txidcommitmenttx, self.redeemscriptb, self.commitmenttx_1, self.commitmenttx_2], \
               [self.txidtimeoutcommmitmenttx, self.timeoutcommmitmenttx_1, self.timeoutcommmitmenttx_2], \
               [self.txiddeliverytx, self.deliverytx_1, self.deliverytx_2], \
               [self.txidtimeoutdeliverytx, self.timeoutdeliverytx_1, self.timeoutdeliverytx_2]
