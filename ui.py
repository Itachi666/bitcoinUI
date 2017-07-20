# -*- coding: utf-8 -*-
from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic
import sqlite3
import ui_input
import ui_generate
import ui_anotherinput
import ui_sign

qtCreatorFile = "bitcoin.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class input(ui_input.QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=ui_input.Ui_input()    # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)





class sign(ui_sign.QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=ui_sign.Ui_Dialog()    # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)

class LoginDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowTitle(u'登录')
        self.resize(300, 150)

        self.leName = QtGui.QLineEdit(self)
        self.leName.setPlaceholderText(u'用户名')

        self.lePassword = QtGui.QLineEdit(self)
        self.lePassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lePassword.setPlaceholderText(u'密码')

        self.pbLogin = QtGui.QPushButton(u'登录', self)
        self.pbCancel = QtGui.QPushButton(u'取消', self)

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
        if self.leName.text() == 'admin' and self.lePassword.text() == 'admin':
            self.accept()  # 关闭对话框并返回1
        else:
            QtGui.QMessageBox.critical(self, u'错误', u'用户名密码不匹配')


def login():
    """返回True或False"""
    dialog = LoginDialog()
    return True
    if dialog.exec_():
        return True
    else:
        return False


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        # self.initToolbar()
        self.setupUi(self)
        self.set_table()
        self.initDB()
        self.current_row = 0
        self.AddSqlData()

        self.statusBar().showMessage('Your Bitcoin Address: mgN94Z7hRWy4UfZHTj2T8hZd1BctusLkps')
        self.newprojectbut.clicked.connect(self.newproject)
        self.oldprojectbut.clicked.connect(self.oldproject)
        self.haveprojectbut.clicked.connect(self.haveproject)
        self.nowprojectbut.clicked.connect(self.nowproject)

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

    def set_table(self):
        self.grid.setColumnCount(5)
        self.grid.setRowCount(0)

        column_width = [75, 125, 125, 125, 125]
        for column in range(5):
            self.grid.setColumnWidth(column, column_width[column])
        headerlabels = ['Id', 'Private', 'Public', 'Address', 'Wif']
        self.grid.setHorizontalHeaderLabels(headerlabels)
        self.grid.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.grid.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

    def initDB(self):
        self.conn = sqlite3.connect('accounts.db')
        self.conn.isolation_level = None

    def AddSqlData(self):
        cursor = self.conn.execute("SELECT * from account")
        for row in cursor:
            #print row, '    ', self.current_row
            self.current_row += 1
            self.grid.insertRow(self.current_row - 1)
            a = '%d' %row[0]
            a = unicode(a, 'utf-8')
            new_item = QtGui.QTableWidgetItem(a)
            self.grid.setItem(self.current_row - 1, 0, new_item)
            for i in range(4):
                new_item = QtGui.QTableWidgetItem(row[i + 1])
                self.grid.setItem(self.current_row - 1, i + 1, new_item)

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

    def oldproject(self):
        myapp = input()
        myapp.show()
        myapp.exec_()
        #print myapp.ui.getdata_p()
        #print myapp.ui.getdata_q()
        #print myapp.ui.getdata_inverse()
        #print myapp.ui.getdata_filepath()

    def nowproject(self):
        data = self.showDialog()
        if data[0]:
            self.current_row += 1
            self.grid.insertRow(self.current_row - 1)
            for i in range(5):
                new_item = QtGui.QTableWidgetItem(data[i + 1])
                self.grid.setItem(self.current_row - 1, i, new_item)

    def newproject(self):
        myapp = generate()
        myapp.show()
        myapp.exec_()
        print myapp.ui.getdata()

    def haveproject(self):
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    if login():
        Window = MyApp()
        Window.show()
    sys.exit(app.exec_())
