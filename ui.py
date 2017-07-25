# -*- coding: utf-8 -*-
from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic
import os
import sqlite3
import ui_input
import ui_exchange
import SkPk
import ui_send
from ouretc import *

qtCreatorFile = "bitcoin.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class input(ui_input.QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = ui_input.Ui_input()  # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)


class send(ui_send.QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = ui_send.Ui_send()  # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)


class exchange(ui_exchange.QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = ui_exchange.Ui_exchange()  # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)


class LoginDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowTitle(u'Loading')
        self.resize(300, 150)

        self.leName = QtGui.QLineEdit(self)
        self.leName.setPlaceholderText(u'Address')

        self.lePassword = QtGui.QLineEdit(self)
        self.lePassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lePassword.setPlaceholderText(u'Sk')

        self.pbLogin = QtGui.QPushButton(u'OK', self)
        self.pbCancel = QtGui.QPushButton(u'Cancel', self)

        self.pbLogin.clicked.connect(self.login)
        self.pbCancel.clicked.connect(self.reject)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.leName)
        layout.addWidget(self.lePassword)

        # 放一个间隔对象美化布局
        spacerItem = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)

        # 按钮布局
        buttonLayout = QtGui.QHBoxLayout()
        # 左侧放一个间隔
        spancerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        buttonLayout.addItem(spancerItem2)
        buttonLayout.addWidget(self.pbLogin)
        buttonLayout.addWidget(self.pbCancel)

        layout.addLayout(buttonLayout)

        self.setLayout(layout)

    def login(self):
        if SkPk.checking(unicode(self.leName.text()), unicode(self.lePassword.text())):
            self.accept()  # 关闭对话框并返回1
        else:
            QtGui.QMessageBox.critical(self, u'Error', u'The address and Sk do not match')


def login():
    """返回True或False"""
    dialog = LoginDialog()
    if dbg:
        return True, 'mhqNzF5fQGpeVHpestNbxz8mPDyjzUcSuJ', 'cNUz3hRMLEq2BXNyG1RunyrFXhYeucdC2sg5buxsWcu2AAG3Gd6q'
    if dialog.exec_():
        return True, dialog.leName.text(), dialog.lePassword.text()
    else:
        return False, 'Null', 'Null'


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        # self.initToolbar()
        self.setupUi(self)
        self.set_table()
        self.initDB()
        self.AddSqlData()
        self.setWindowIcon(QtGui.QIcon('h19.ico'))
        self.setFixedSize(self.width(),self.height())
        self.newprojectbut.clicked.connect(self.createandsendTransaction)
        self.translatebut.clicked.connect(self.translate)
        self.delprojectbut.clicked.connect(self.deltranslate)
        self.nowprojectbut.clicked.connect(self.exchangedata)

    def initToolbar(self):
        newAction = QtGui.QAction(QtGui.QIcon('new.png'), 'New', self)
        editAction = QtGui.QAction(QtGui.QIcon('edit.png'), 'New', self)
        delAction = QtGui.QAction(QtGui.QIcon('del.png'), 'New', self)
        newAction.setShortcut('Ctrl+N')
        editAction.setShortcut('Ctrl+E')
        delAction.setShortcut('Delete')
        # newAction.triggered.connect(self.newAction_def)
        # editAction.triggered.connect(self.editAction_def)
        # delAction.triggered.connect(self.delAction_def)
        self.tb_new = self.addToolBar('New')
        self.tb_edit = self.addToolBar('Edit')
        self.tb_del = self.addToolBar('Del')
        self.tb_new.addAction(newAction)
        self.tb_edit.addAction(editAction)
        self.tb_del.addAction(delAction)

    def login(self, address, sk):
        self.address = address
        self.sk = sk
        self.statusBar().showMessage('Bitcoin Address: %s, Private Key: %s' % (address, sk))

    def set_table(self):
        self.grid.setColumnCount(5)
        self.grid.setRowCount(0)

        column_width = [100, 150, 150, 150, 100]
        for column in range(5):
            self.grid.setColumnWidth(column, column_width[column])
        headerlabels = ['Contract', 'SecretKey', 'PublicKey', 'Partername', 'Money(BTC)']
        self.grid.setHorizontalHeaderLabels(headerlabels)
        self.grid.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.grid.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

    def initDB(self):
        # self.conn = sqlite3.connect('accounts.db')
        # self.conn.isolation_level = None
        if os.path.exists('INFO.db'):
            self.conn = sqlite3.connect('INFO.db')
            self.conn.isolation_level = None
        else:
            self.conn = sqlite3.connect('INFO.db')
            self.conn.isolation_level = None
            self.conn.execute('''CREATE TABLE INFO
                        (ID int PRIMARY KEY NOT NULL,
                        Contract char(255),
                        SecretKey char(255),
                        PublicKey char(255),
                        Partername char(255),
                        Money char(255),
                        myp char(255),
                        myq char(255),
                        myn char(255),
                        myh char(255),
                        mysalt char(255),
                        myhexsk char(255),
                        mypk char(255),
                        mybitsk char(255),
                        mybitpk char(255),
                        hisbitpk char(255),
                        hisbitsk char(255),
                        hisSecretKey char(255),
                        hisPublicKey char(255),
                        hisp char(255),
                        hisq char(255),
                        hisN char(255),
                        hish char(255))''')
        '''
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM INFO')
        self.displayData = cur.fetchall()
        cur.close()
        self.current_row = len(self.displayData)
        '''

    def AddSqlData(self):
        self.current_row = 0
        cursor = self.conn.execute("SELECT * from INFO")
        for row in cursor:
            self.current_row += 1
            self.grid.insertRow(self.current_row - 1)
            for i in range(5):
                new_item = QtGui.QTableWidgetItem(row[i + 1])
                self.grid.setItem(self.current_row - 1, i, new_item)

    def showDialog(self, Id='', Pr='', Pu='', Ad='', Wif=''):

        edit_dialog = QtGui.QDialog(self)
        group = QtGui.QGroupBox('Edit Info', edit_dialog)

        lbl_id = QtGui.QLabel('Id:', group)
        le_id = QtGui.QLineEdit(group)
        le_id.setText(Id)
        lbl_Private = QtGui.QLabel('Private:', group)
        le_Private = QtGui.QLineEdit(group)
        le_Private.setText(Pr)
        lbl_Public = QtGui.QLabel('Public:', group)
        le_Public = QtGui.QLineEdit(group)
        le_Public.setText(Pu)
        lbl_Address = QtGui.QLabel('Address:', group)
        le_Address = QtGui.QLineEdit(group)
        le_Address.setText(Ad)
        lbl_Wif = QtGui.QLabel('Wif:', group)
        le_Wif = QtGui.QLineEdit(group)
        le_Wif.setText(Wif)
        ok_button = QtGui.QPushButton('OK', edit_dialog)
        cancel_button = QtGui.QPushButton('CANCEL', edit_dialog)

        ok_button.clicked.connect(edit_dialog.accept)
        ok_button.setDefault(True)
        cancel_button.clicked.connect(edit_dialog.reject)

        group_layout = QtGui.QVBoxLayout()
        group_item = [lbl_id, le_id,
                      lbl_Private, le_Private,
                      lbl_Public, le_Public,
                      lbl_Address, le_Address,
                      lbl_Wif, le_Wif]
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
            Id = le_id.text()
            Private = le_Private.text()
            Public = le_Public.text()
            Address = le_Address.text()
            Wif = le_Wif.text()
            return True, Id, Private, Public, Address, Wif
        return False, None, None, None, None, None

    def showHint(self):
        hint_msg = QtGui.QMessageBox()
        hint_msg.setWindowTitle('Error')
        hint_msg.setText('No selected row!')
        hint_msg.addButton(QtGui.QMessageBox.Ok)
        hint_msg.exec_()

    def translate(self):
        myapp = input()
        myapp.show()
        myapp.exec_()
        data = myapp.ui.getdata_all()
        pk=SkPk.fromsk2compk(self.sk)

        self.current_row += 1
        self.conn.execute(
            "INSERT INTO INFO VALUES(%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
            % (self.current_row, data[0], data[1], data[2], '', '', data[3], data[4], data[5], data[6], data[7], data[8], data[9], self.sk, pk, '', '', '', '', '', '', '', ''))
        self.grid.insertRow(self.current_row - 1)
        d = [data[0], data[1], data[2], '', '']
        for i in range(5):
            new_item = QtGui.QTableWidgetItem(d[i])
            self.grid.setItem(self.current_row - 1, i, new_item)

    def exchangedata(self):
        selected_row = self.grid.selectedItems()
        if selected_row:
            edit_row = self.grid.row(selected_row[0])

            cursor = self.conn.execute('SELECT * from INFO')
            mydata = cursor.fetchall()[edit_row]
            myapp = exchange()
            myapp.ui.putindata(mydata[6], mydata[7], mydata[8], mydata[9], mydata[10], mydata[11], mydata[12],
                               mydata[3], SkPk.fromsk2compk(self.sk), self.sk, mydata[2])
            myapp.show()
            myapp.exec_()
            new_data = myapp.ui.getdata()
            print new_data
            if len(new_data) == 2:
                self.conn.execute('''UPDATE INFO SET
                                             Partername = '%s', Money = '%s'
                                            WHERE ID = '%d' '''
                                  % (new_data[0], new_data[1], edit_row + 1))
            else:
                self.conn.execute('''UPDATE INFO SET
                                        Partername = '%s', Money = '%s', hisp='%s', hisq='%s', hisN='%s', hish='%s',hisSecretKey='%s',hisPublicKey='%s',hisbitpk='%s',hisbitsk='%s'
                                        WHERE ID = '%d' '''
                                  % (new_data[0], new_data[1], new_data[2], new_data[3], new_data[4], new_data[5],
                                     new_data[7], new_data[9], new_data[10], new_data[11], edit_row + 1))
            for i in range(2):
                new_item = QtGui.QTableWidgetItem(new_data[i])
                self.grid.setItem(edit_row, i + 3, new_item)
        else:
            self.showHint()

    def deltranslate(self):
        selected_row = self.grid.selectedItems()
        if selected_row:
            del_row = self.grid.row(selected_row[0])
            self.grid.removeRow(del_row)
            self.conn.execute("DELETE FROM INFO WHERE ID = %d" % (del_row + 1))
            for index in range(del_row + 2, self.current_row + 1):
                self.conn.execute("UPDATE INFO SET ID = %d WHERE ID = %d" % ((index - 1), index))
            self.current_row -= 1
        else:
            self.showHint()

    def createandsendTransaction(self):
        selected_row = self.grid.selectedItems()
        if selected_row:
            edit_row = self.grid.row(selected_row[0])
            cursor = self.conn.execute('SELECT * from INFO')
            mydata = cursor.fetchall()[edit_row]
            myapp = send()
            myapp.ui.putin2data(mydata)
            myapp.show()
            myapp.exec_()
        else:
            self.showHint()

    def haveproject(self):
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    t, address, sk = login()
    if t:
        address = unicode(address)
        sk = unicode(sk)
        Window = MyApp()
        Window.login(address, sk)
        Window.show()
    sys.exit(app.exec_())
