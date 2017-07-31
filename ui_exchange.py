# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/exchange.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket
#import server
import socket
import time
import threading
from ouretc import IP

global a
a=[]

def tcplink(sock, addr, da):
    print("Accept new connection from %s:%s..." % addr)
    sock.send(b'Welcome')
    i = 0
    while True:
        data = sock.recv(1024)
        #time.sleep(1)
        if data == 'exit' or not data:
            break
        a.append(data)
        sock.send('%s' % da[i].encode("utf8"))
        i = i + 1
    sock.close()
    print("Connection from %s: %s closed." % addr)


def setserver(da):
    host = socket.gethostname()
    ip=IP
    global a
    print host
    print ip
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    print("1")
    s.listen(5)
    while True:
        # 接受一个新连接：
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=tcplink, args=(sock, addr, da))
        t.start()
        t.join()

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


class Ui_exchange(object):
    def setupUi(self, exchange):
        exchange.setObjectName(_fromUtf8("exchange"))
        exchange.resize(632, 805)
        self.label = QtGui.QLabel(exchange)
        self.label.setGeometry(QtCore.QRect(10, 0, 351, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(exchange)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 611, 61))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(exchange)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 351, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit_2 = QtGui.QTextEdit(exchange)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 130, 611, 61))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label_3 = QtGui.QLabel(exchange)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 351, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit_3 = QtGui.QTextEdit(exchange)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 230, 611, 61))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.label_4 = QtGui.QLabel(exchange)
        self.label_4.setGeometry(QtCore.QRect(10, 410, 351, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.name = QtGui.QTextEdit(exchange)
        self.name.setGeometry(QtCore.QRect(250, 410, 371, 31))
        self.name.setObjectName(_fromUtf8("name"))
        self.label_5 = QtGui.QLabel(exchange)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 351, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.textEdit_4 = QtGui.QTextEdit(exchange)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 330, 611, 61))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.label_6 = QtGui.QLabel(exchange)
        self.label_6.setGeometry(QtCore.QRect(10, 460, 441, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.money = QtGui.QTextEdit(exchange)
        self.money.setGeometry(QtCore.QRect(450, 460, 171, 31))
        self.money.setObjectName(_fromUtf8("money"))
        self.pushButton = QtGui.QPushButton(exchange)
        self.pushButton.setGeometry(QtCore.QRect(10, 550, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(exchange)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 610, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_7 = QtGui.QLabel(exchange)
        self.label_7.setGeometry(QtCore.QRect(220, 510, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_3 = QtGui.QPushButton(exchange)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 670, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(exchange)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 770, 611, 31))
        self.pushButton_5 = QtGui.QPushButton(exchange)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 720, 611, 41))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_4"))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.money_2 = QtGui.QTextEdit(exchange)
        self.money_2.setGeometry(QtCore.QRect(260, 510, 171, 31))
        self.money_2.setObjectName(_fromUtf8("money_2"))
        self.newdata = []

        self.pushButton.clicked.connect(self.set_a_server)
        self.pushButton_2.clicked.connect(self.connect_ip)
        self.pushButton_3.clicked.connect(self.exchangedata)
        self.pushButton_5.clicked.connect(self.checking)

        self.retranslateUi(exchange)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), exchange.accept)
        QtCore.QMetaObject.connectSlotsByName(exchange)

    def retranslateUi(self, exchange):
        exchange.setWindowTitle(_translate("exchange", "Exchange Data", None))
        self.label.setText(_translate("exchange", "Here is your sk of your contract：", None))
        self.label_2.setText(_translate("exchange", "Here is your pk of your contract：", None))
        self.label_3.setText(_translate("exchange", "Here is the pk of your partner\'s contract：", None))
        self.textEdit_3.setHtml(_translate("exchange",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Null</p></body></html>",
                                           None))
        self.label_4.setText(_translate("exchange", "Input your partner\'s name：", None))
        self.label_5.setText(_translate("exchange", "Here is the your partner\'s bitcoin PK：", None))
        self.textEdit_4.setHtml(_translate("exchange",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Null</p></body></html>",
                                           None))
        self.name.setHtml(_translate("exchange",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Alice</p></body></html>",
                                     None))
        self.money.setHtml(_translate("exchange",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>",
                                      None))
        self.label_6.setText(_translate("exchange", "Input the bitcoin that you want to pay (temporary)：", None))
        self.pushButton.setText(
            _translate("exchange", "Set a Server (Create a server to let your partner connect)", None))
        self.pushButton_2.setText(_translate("exchange", "Connect your partner\'s server(Need input IP)", None))
        self.label_7.setText(_translate("exchange", "IP:", None))
        self.pushButton_3.setText(_translate("exchange", "Data Exchange", None))
        self.pushButton_4.setText(_translate("exchange", "OK", None))
        self.pushButton_5.setText(_translate("exchange", "Checking Data", None))

    def showHint(self):
        hint_msg = QtGui.QMessageBox()
        hint_msg.setWindowTitle('Get connect')
        hint_msg.setText('Welcome!')
        hint_msg.addButton(QtGui.QMessageBox.Ok)
        hint_msg.exec_()

    def showHint_2(self):
        hint_msg = QtGui.QMessageBox()
        hint_msg.setWindowTitle('Verification Passed')
        hint_msg.setText('Your partner is honesty!')
        hint_msg.addButton(QtGui.QMessageBox.Ok)
        hint_msg.exec_()

    def showHint_3(self):
        hint_msg = QtGui.QMessageBox()
        hint_msg.setWindowTitle('Exchange')
        hint_msg.setText('Exchange Over!')
        hint_msg.addButton(QtGui.QMessageBox.Ok)
        hint_msg.exec_()

    def putindata(self, p, q, n, h, salt, sk, pk, compk, bitpk, bitsk, wifsk):
        self.mydata = [p, q, n, h, salt, sk, pk, compk, bitpk, bitsk]
        self.textEdit.setHtml(_translate("exchange",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</p></body></html>" % wifsk,
                                         None))
        self.textEdit_2.setHtml(_translate("exchange",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</p></body></html>" % compk,
                                           None))

    def set_a_server(self):
        host = socket.gethostname()
        ip = IP
        self.money_2.setHtml(_translate("exchange",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</p></body></html>" % ip,
                                        None))
        self.k = Worker()
        self.k.render(self.mydata)

    def connect_ip(self):
        host = 'Lancelot'  # socket.gethostname()
        ip = unicode(self.money_2.toPlainText())
        print 'ip=', ip
        port = 12345
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 建立链接
        s.connect((ip, port))
        # 接受欢迎消息
        if s.recv(1024) == 'Welcome':
            self.showHint()
        s.send('exit')
        s.close()

    def exchangedata(self):
        ip = unicode(self.money_2.toPlainText())
        port = 12345
        print 'ip=', ip
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        newdata = []
        print s.recv(1024)
        for data in self.mydata:
            s.send(data.encode())
            newdata.append(s.recv(1024))
        s.send('exit')
        s.close()
        self.newdata = newdata
        self.textEdit_3.setHtml(_translate("exchange",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</p></body></html>" %
                                           newdata[7],
                                           None))
        self.textEdit_4.setHtml(_translate("exchange",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</p></body></html>" %
                                           newdata[8],
                                           None))
        self.showHint_3()

    def getdata(self):
        name = unicode(self.name.toPlainText())
        money = unicode(self.money.toPlainText())
        if len(self.newdata) == 0:
            self.newdata = a

        self.newdata.insert(0, money)
        self.newdata.insert(0, name)
        return self.newdata

    def checking(self):
        self.showHint_2()
        # self.textEdit_3.setText('asdf\nasdf\nasdf')


class Worker(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def render(self, data):
        self.data = data
        self.start()

    def run(self):
        global a
        setserver(self.data)
