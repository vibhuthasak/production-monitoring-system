# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import psycopg2

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

class Ui_Dialog2(object):
    ip_add = '127.0.0.1'
    dbname = 'dsisppms'
    uname = 'postgres'
    pwd = '123456'

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(360, 310)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"Cantarell\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Password)
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/connector.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.connection)
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.lineEdit_2.setText(Ui_Dialog2.ip_add)
        self.lineEdit.setText(Ui_Dialog2.dbname)
        self.lineEdit_3.setText(Ui_Dialog2.uname)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Log-In", None))
        self.label.setText(_translate("Dialog", "Database Connection Settings", None))
        self.label_2.setText(_translate("Dialog", "Database Name", None))
        self.label_3.setText(_translate("Dialog", "IP Address ", None))
        self.label_4.setText(_translate("Dialog", "Username", None))
        self.label_6.setText(_translate("Dialog", "Password", None))
        self.pushButton.setText(_translate("Dialog", "Connect", None))
        #self.label_5.setText(_translate("Dialog", "Connection Sucess", None))

    def connection(self):
        Ui_Dialog2.ip_add = self.lineEdit_2.text()
        Ui_Dialog2.dbname = self.lineEdit.text()
        Ui_Dialog2.uname = self.lineEdit_3.text()
        Ui_Dialog2.pwd = self.lineEdit_4.text()

        # self.data_connection_string =("database=%s, user=%s, password=%s, host=%s, port=5432" % (self.dbname,self.uname,self.pwd, self.ip_add))
        # print(type(database="plottest", user="postgres",password="*",host="localhost", port="5432"))
        try:
            conn_test = psycopg2.connect(database="%s" % (Ui_Dialog2.dbname), user="%s" % (Ui_Dialog2.uname),
                                           password="%s" % (Ui_Dialog2.pwd), host="%s" % (Ui_Dialog2.ip_add), port="5432")
            self.label_5.setText(_translate("Dialog", "Connection Success", None))

        except psycopg2.ProgrammingError:
            self.label_5.setText(_translate("Dialog", "Connection Failed", None))

        except psycopg2.OperationalError:
            self.label_5.setText(_translate("Dialog", "Connection Failed", None))

import rersource_rc
