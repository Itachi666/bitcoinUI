# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/signtx.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ui_reference
import tx
import common
import json
import SkPk

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


class Ui_signtx(object):
    def setupUi(self, signtx):
        signtx.setObjectName(_fromUtf8("signtx"))
        signtx.resize(969, 739)
        font = QtGui.QFont()
        font.setPointSize(10)
        signtx.setFont(font)
        self.textEdit = QtGui.QTextEdit(signtx)
        self.textEdit.setGeometry(QtCore.QRect(430, 100, 521, 611))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(signtx)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(signtx)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 230, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(signtx)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 470, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(signtx)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 590, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(signtx)
        self.label.setGeometry(QtCore.QRect(40, 0, 641, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_5 = QtGui.QPushButton(signtx)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 350, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_2 = QtGui.QLabel(signtx)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(signtx)
        self.label_3.setGeometry(QtCore.QRect(100, 240, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(signtx)
        self.label_4.setGeometry(QtCore.QRect(100, 360, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(signtx)
        self.label_5.setGeometry(QtCore.QRect(100, 480, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(signtx)
        self.label_6.setGeometry(QtCore.QRect(100, 600, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_6 = QtGui.QPushButton(signtx)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 680, 131, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(signtx)
        self.pushButton_7.setGeometry(QtCore.QRect(230, 680, 131, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
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

        self.retranslateUi(signtx)
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

        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), signtx.accept)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reference)
        QtCore.QMetaObject.connectSlotsByName(signtx)

    def retranslateUi(self, signtx):
        signtx.setWindowTitle(_translate("signtx", "Sign Raw Transacthins", None))
        self.pushButton.setText(_translate("signtx", "Sign Funding Transaction", None))
        self.pushButton_2.setText(_translate("signtx", "Sign Commitment Transaction", None))
        self.pushButton_3.setText(_translate("signtx", "Sign Delivery Transaction", None))
        self.pushButton_4.setText(_translate("signtx", "Sign Timeout Delivery Transaction", None))
        self.label.setText(_translate("signtx", "Sign Raw Transactions", None))
        self.pushButton_5.setText(_translate("signtx", "Sign Timeout Commitment Transaction", None))
        self.label_2.setText(_translate("signtx", "Completed", None))
        self.label_3.setText(_translate("signtx", "Completed", None))
        self.label_4.setText(_translate("signtx", "Completed", None))
        self.label_5.setText(_translate("signtx", "Completed", None))
        self.label_6.setText(_translate("signtx", "Completed", None))
        self.pushButton_6.setText(_translate("signtx", "Ok", None))
        self.pushButton_7.setText(_translate("signtx", "See Reference", None))

    def putin2data(self, data, f, c, tc, d, td):
        self.mydata = data
        self.ft = f
        self.ct = c
        self.tct = tc
        self.dt = d
        self.tdt = td

    def reference(self):
        myapp = reference()
        myapp.show()
        myapp.exec_()

    def FundingTransaction(self):
        fundingtx_1 = self.ft[2]
        fundingtx_2 = self.ft[3]
        fundingtx_3 = self.ft[4]
        pka = self.mydata[14]
        ska = self.mydata[13]
        pkb = self.mydata[15]
        skb = self.mydata[16]
        sign_fundingtransaction, siga, sigb = tx.sign_fundingtransaction(fundingtx_1, fundingtx_2, fundingtx_3, pka,
                                                                         ska, pkb, skb)
        self.tx1 = sign_fundingtransaction
        self.sa1 = siga
        self.sb1 = sigb
        jsontxt = common.raw2json(sign_fundingtransaction)
        k = json.dumps(jsontxt)
        self.textEdit.setText('Hex= ' + sign_fundingtransaction + '\n' + 'Siga= ' + siga + '\n' + 'Sigb= ' + sigb)

    def CommitmentTransaction(self):
        commitmenttx_1 = self.ct[2]
        commitmenttx_2 = self.ct[3]
        ska = self.mydata[13]
        skb = self.mydata[16]
        redeemscripta = self.ft[1]
        ha = self.mydata[9]
        sign_commitmenttransaction, sigam, sigb1 = tx.sign_commitmenttransaction(commitmenttx_1, commitmenttx_2, ska,
                                                                                 skb, redeemscripta, ha)
        self.tx2 = sign_commitmenttransaction
        self.sa2 = sigam
        self.sb2 = sigb1
        jsontxt = common.raw2json(sign_commitmenttransaction)
        k = json.dumps(jsontxt)
        self.textEdit.setText('Hex= ' + sign_commitmenttransaction + '\n' + 'Sigb1= ' + sigb1)

    def TimeCommitmentTransaction(self):
        one2onetx_1 = self.tct[1]
        one2onetx_2 = self.tct[2]
        skb = self.mydata[16]
        redeemscripta = self.ft[1]
        ha1 = '6' + self.mydata[9][1:]
        sign_timeoutcommitmenttransaction, sigb2 = tx.sign_timeoutcommitmenttransaction(one2onetx_1, one2onetx_2, skb,
                                                                                        redeemscripta, ha1)
        self.tx3 = sign_timeoutcommitmenttransaction
        self.sb3 = sigb2
        jsontxt = common.raw2json(sign_timeoutcommitmenttransaction)
        k = json.dumps(jsontxt)
        self.textEdit.setText('Hex= ' + sign_timeoutcommitmenttransaction + '\n' + 'Sigb2= ' + sigb2)

    def DeliveryTransaction(self):
        one2onetx_1 = self.dt[1]
        one2onetx_2 = self.dt[2]
        ska = self.mydata[13]
        skb = self.mydata[16]
        redeemscriptb = self.ct[1]
        hb = self.mydata[22]
        sign_deliverytransaction, siga1, sigbm = tx.sign_deliverytransaction(one2onetx_1, one2onetx_2, ska, skb,
                                                                             redeemscriptb, hb)
        self.tx4 = sign_deliverytransaction
        self.sa4 = siga1
        self.sb4 = sigbm
        jsontxt = common.raw2json(sign_deliverytransaction)
        k = json.dumps(jsontxt)
        self.textEdit.setText('Hex= ' + sign_deliverytransaction + '\n' + 'Siga1= ' + siga1)

    def TimeDeliveryTransaction(self):
        one2onetx_1 = self.tdt[1]
        one2onetx_2 = self.tdt[2]
        ska = self.mydata[13]
        skb = self.mydata[16]
        redeemscriptb = self.ct[1]
        hb1 = '6' + self.mydata[22][1:]
        sign_timeoutdeliverytransaction, siga2 = tx.sign_timeoutdeliverytransaction(one2onetx_1, one2onetx_2, ska,
                                                                                    redeemscriptb, hb1)
        self.tx5 = sign_timeoutdeliverytransaction
        self.sa5 = siga2

        jsontxt = common.raw2json(sign_timeoutdeliverytransaction)
        k = json.dumps(jsontxt)
        self.textEdit.setText('Hex= ' + sign_timeoutdeliverytransaction + '\n' + 'Siga2= ' + siga2)

    def getsigndata(self):
        return [self.tx1, self.tx2, self.tx3, self.tx4, self.tx5], \
               [self.sa1, self.sa2, self.sa4, self.sa5], \
               [self.sb1, self.sb2, self.sb3, self.sb4]
