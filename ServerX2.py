import rersource_rc
import datetime
import psycopg2
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
    ip_add = 'localhost'
    dbname = 'dsisppms'
    uname = 'postgres'
    pwd = '123456'

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(350, 272)
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
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Password)
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_3)

        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_6)

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
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.variable = "LOVE"

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Server Login", None))
        self.label.setText(_translate("Dialog", "Database Connection Settings", None))
        self.label_2.setText(_translate("Dialog", "IP Address", None))
        self.label_3.setText(_translate("Dialog", "User Name", None))
        self.label_4.setText(_translate("Dialog", "Password", None))
        self.pushButton.setText(_translate("Dialog", "Connect", None))
        self.label_6.setText(_translate("Dialog", "Database Name", None))

    def connection(self):
        Ui_Dialog.ip_add = self.lineEdit.text()
        Ui_Dialog.dbname = self.lineEdit_6.text()
        Ui_Dialog.uname = self.lineEdit_2.text()
        Ui_Dialog.pwd = self.lineEdit_3.text()
        # self.data_connection_string =("database=%s, user=%s, password=%s, host=%s, port=5432" % (self.dbname,self.uname,self.pwd, self.ip_add))
        # print(type(database="plottest", user="postgres",password="*",host="localhost", port="5432"))
        try:
            conn_test = psycopg2.connect(database="%s" % (Ui_Dialog.dbname), user="%s" % (Ui_Dialog.uname),
                                           password="%s" % (Ui_Dialog.pwd), host="%s" % (Ui_Dialog.ip_add), port="5432")
            self.label_5.setText(_translate("Dialog", "Connection Success", None))

        except psycopg2.ProgrammingError:
            self.label_5.setText(_translate("Dialog", "Connection Failed", None))

        except psycopg2.OperationalError:
            self.label_5.setText(_translate("Dialog", "Connection Failed", None))
        # conn = psycopg2._connect(self.data_connection_string)
        # connec_test = psycopg2.connect(database="%s"%(self.dbname),user="%s"%(self.uname),password="%s"%(self.pwd),host="%s"%(self.ip_add), port="5432")
        #self.label_5.setText(_translate("Dialog", "Connection Success", None))


class Ui_MainWindow(QtGui.QMainWindow, Ui_Dialog):
    x=0
    y=0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1047, 777)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.calendarWidget.clicked.connect(self.date_select)


        self.horizontalLayout.addWidget(self.calendarWidget)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem3 = QtGui.QSpacerItem(6, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Sewing.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.comboBox.addItem(icon, _fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Feedbin-Icon-home-edit.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Feedbin-Icon-home-edit.svg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setCheckable(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.edit_month)
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem5 = QtGui.QSpacerItem(16, 19, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.lineEdit_8 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_3.addWidget(self.lineEdit_5)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.edit_day)

        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(14)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)

        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        #
        rowcnt = self.tableWidget.rowCount()
        colcnt = self.tableWidget.columnCount()

        for row in range(0,rowcnt):
            for colomn in range(0,colcnt):
                item = QtGui.QTableWidgetItem()
                if colomn in [1,4,7,10]:
                    item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled |QtCore.Qt.ItemIsEditable)
                    item.setCheckState(QtCore.Qt.Unchecked)
                if colomn in range(0,3):
                    item.setBackground(QtGui.QColor(193,205,205,150))
                if colomn in range(3,6):
                    item.setBackground(QtGui.QColor(224,238,238))
                if colomn in range(6,9):
                    item.setBackground(QtGui.QColor(173,184,184,110))
                if colomn in range(9,12):
                    item.setBackground(QtGui.QColor(240,255,255,220))

                self.tableWidget.setItem(row, colomn, item)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.TimeNow)
        self.timer.start(1000)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(77)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(11)
        self.tableWidget.verticalHeader().setDefaultSectionSize(26)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/3d6cfa22471.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.savefunc)
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1033, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuConnect = QtGui.QMenu(self.menubar)
        self.menuConnect.setObjectName(_fromUtf8("menuConnect"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.actionServer_Login = QtGui.QAction(MainWindow)
        self.actionServer_Login.setObjectName(_fromUtf8("actionServer_Login"))

        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))

        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuConnect.addAction(self.actionServer_Login)
        self.actionServer_Login.triggered.connect(self.clicked_connection)

        self.menuConnect.addAction(self.actionQuit)

        self.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.menuHelp.addAction(self.actionAbout)

        self.actionAbout.triggered.connect(self.clicked_about)
        self.menubar.addAction(self.menuConnect.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_8.setReadOnly(True)

        # self.data_database= ('database = \"plottest\", user = \"postgres\", password = \"123456\", host = \"192.168.21.109\", port = \"5432\"')


        # self.lineEdit.setText("LINEEDIT1")
        # self.lineEdit_2.setText("LINEEDIT2")
        # self.lineEdit_3.setText("LINEEDIT3")
        # self.lineEdit_4.setText("LINEEDIT4")
        # self.lineEdit_5.setText("LINEEDIT5")
        # self.lineEdit_6.setText("LINEEDIT6")
        # self.lineEdit_7.setText("LINEEDIT7")
        # self.lineEdit_8.setText("LINEEDIT8")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DSISP-PMS", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">DSI-SP Production Monitoring System</span></p></body></html>", None))
        # self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; font-weight:600;\">TIMENOW</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Section Select :</span></p></body></html>", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sewing", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "IM", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Monthly Target :</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Daily Target : </span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "                                                               Section A                                          Section B                                           Section C                                          Section D                     ", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "07:00-08:00", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "08:00-09:00", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "09:00-10:00", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "10:00-11:00", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "11:00-12:00", None))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "12:00-13:00", None))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "13:00-14:00", None))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "14:00-15:00", None))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "16:00-17:00", None))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "17:00-18:00", None))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "18:00-19:00", None))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "19:00-20:00", None))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "20:00-21:00", None))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "21:00-22:00", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Plan", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Actual", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Item", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Plan", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Actual", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Item", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Plan", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Actual", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Item", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Plan", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Actual", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "Connection Status :", None))
        # self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Connected </span><span style=\" font-weight:600; color:#ff1a0a;\">Disconnected</span></p></body></html>", None))
        # self.label_6.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Connected to "+  "  " + str(Ui_Dialog.ip_add)+ "  " + str(Ui_Dialog.dbname)+ "  " + str(Ui_Dialog.uname) +"</span></body></html>", None))
        self.menuConnect.setTitle(_translate("MainWindow", "Connect", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionServer_Login.setText(_translate("MainWindow", "Server Login", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))


    def clicked_connection(self):
        dialog_win = QtGui.QDialog()
        connection_dialog = Ui_Dialog()
        connection_dialog.setupUi(dialog_win)
        dialog_win.exec_()

    def clicked_about(self):
        about_win = QtGui.QDialog()
        about_connection = Ui_Dialog2()
        about_connection.setupUi(about_win)
        about_win.exec_()

    def edit_day(self):
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Connected to " + "  " + str(
                                            Ui_Dialog.ip_add) + "  " + str(Ui_Dialog.dbname) + "  " + str(
                                            Ui_Dialog.uname) + "</span></body></html>", None))

        qdate = self.calendarWidget.selectedDate()
        date = qdate.toPyDate()
        date = str(date)
        print(self.x)
        self.x += 1
        if (self.x % 2) == 1:
            self.lineEdit_8.setReadOnly(False)
            self.lineEdit_7.setReadOnly(False)
            self.lineEdit_6.setReadOnly(False)
            self.lineEdit_5.setReadOnly(False)
        else:
            self.lineEdit_8.setReadOnly(True)
            self.lineEdit_7.setReadOnly(True)
            self.lineEdit_6.setReadOnly(True)
            self.lineEdit_5.setReadOnly(True)
            try:
                # conn = psycopg2.connect(database="plottest", user="postgres")
                # conn = psycopg2.connect(database = "dsisppms", user = "postgres", password = "123456", host = "192.168.21.109", port = "5432")
                conn = psycopg2.connect(database="%s" % (Ui_Dialog.dbname), user="%s" % (Ui_Dialog.uname),
                                             password="%s" % (Ui_Dialog.pwd), host="%s" % (Ui_Dialog.ip_add),
                                             port="5432")
                self.statusbar.showMessage("Database opened Sucessfully", 1000)
                cur = conn.cursor()
                cur.execute("INSERT INTO DAILY(date,a,b,c,d) VALUES (\'%s\',%d ,%d ,%d ,%d) " % (date, int(self.lineEdit_8.text()), int(self.lineEdit_7.text()), int(self.lineEdit_6.text()), int(self.lineEdit_5.text())))
                # print(self.lineEdit_2.text())
                conn.commit()
                conn.close()
            except psycopg2.IntegrityError:
                # conn = psycopg2.connect(database="plottest", user="postgres")
                # conn = psycopg2.connect(database="dsisppms", user="postgres", password="123456", host="192.168.21.109",
                #                         port="5432")
                conn = psycopg2.connect(database="%s" % (Ui_Dialog.dbname), user="%s" % (Ui_Dialog.uname),
                                             password="%s" % (Ui_Dialog.pwd), host="%s" % (Ui_Dialog.ip_add),
                                             port="5432")
                self.statusbar.showMessage("Database opened Sucessfully", 1000)
                cur = conn.cursor()
                cur.execute(("UPDATE daily set a =%d, b =%d, c=%d, d=%d where date=\'%s\'") % (
                int(self.lineEdit_8.text()), int(self.lineEdit_7.text()), int(self.lineEdit_6.text()),
                int(self.lineEdit_5.text()), date))
                # print(self.lineEdit_2.text())
                conn.commit()
                conn.close()

    def edit_month(self):
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Connected to " + "  " + str(
                                            Ui_Dialog.ip_add) + "  " + str(Ui_Dialog.dbname) + "  " + str(
                                            Ui_Dialog.uname) + "</span></body></html>", None))

        qdate = self.calendarWidget.selectedDate()
        date = qdate.toPyDate()
        date = str(date)
        # print("date=",date)
        month = date[0:7]
        # print(month)
        self.y += 1
        if (self.y % 2) == 1:
            self.lineEdit_4.setReadOnly(False)
            self.lineEdit_3.setReadOnly(False)
            self.lineEdit_2.setReadOnly(False)
            self.lineEdit.setReadOnly(False)
        else:
            self.lineEdit_4.setReadOnly(True)
            self.lineEdit_3.setReadOnly(True)
            self.lineEdit_2.setReadOnly(True)
            self.lineEdit.setReadOnly(True)
            try:
                # conn = psycopg2.connect(database="plottest", user="postgres")
                conn = psycopg2.connect(database="%s" % (Ui_Dialog.dbname), user="%s" % (Ui_Dialog.uname),
                                             password="%s" % (Ui_Dialog.pwd), host="%s" % (Ui_Dialog.ip_add),
                                             port="5432")
                self.statusbar.showMessage("Database opened Sucessfully", 1000)
                cur = conn.cursor()

                cur.execute("INSERT INTO MONTHLY(month,a,b,c,d) VALUES (\'%s\',%d ,%d ,%d ,%d) " % (
                month, int(self.lineEdit_4.text()), int(self.lineEdit_3.text()), int(self.lineEdit_2.text()),
                int(self.lineEdit.text())))

                conn.commit()
                conn.close()
            except psycopg2.IntegrityError:
                # conn = psycopg2.connect(database="plottest", user="postgres")
                conn = psycopg2.connect(database="%s" % (Ui_Dialog.dbname), user="%s" % (Ui_Dialog.uname),
                                        password="%s" % (Ui_Dialog.pwd), host="%s" % (Ui_Dialog.ip_add),
                                        port="5432")
                self.statusbar.showMessage("Database opened Sucessfully", 1000)
                cur = conn.cursor()
                cur.execute(("UPDATE MONTHLY set a =%d, b =%d, c=%d, d=%d where month=\'%s\'") % (
                int(self.lineEdit_4.text()), int(self.lineEdit_3.text()), int(self.lineEdit_2.text()),
                int(self.lineEdit.text()), month))
                conn.commit()
                conn.close()
            # print(self.lineEdit.text())

    def date_select(self):
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Connected to " + "  " + str(
                                            Ui_Dialog.ip_add) + "  " + str(Ui_Dialog.dbname) + "  " + str(
                                            Ui_Dialog.uname) + "</span></body></html>", None))

        qdate = self.calendarWidget.selectedDate()
        date = qdate.toPyDate()
        date = str(date)
        month = date[0:7]
        today = str(datetime.datetime.now().date())
        try:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.tableWidget.clearContents()
            if date != today:
                # self.tableWidget.setEnabled(False)
                self.lineEdit_8.setEnabled(False)
                self.lineEdit_7.setEnabled(False)
                self.lineEdit_6.setEnabled(False)
                self.lineEdit_5.setEnabled(False)
            else:
                # self.tableWidget.setEnabled(True)
                self.lineEdit_8.setEnabled(True)
                self.lineEdit_7.setEnabled(True)
                self.lineEdit_6.setEnabled(True)
                self.lineEdit_5.setEnabled(True)

            rowcnt = self.tableWidget.rowCount()
            colcnt = self.tableWidget.columnCount()

            for row in range(0, rowcnt):
                for colomn in range(0, colcnt):
                    item = QtGui.QTableWidgetItem()
                    if colomn in [1, 4, 7, 10]:
                        item.setFlags(
                            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                        item.setCheckState(QtCore.Qt.Unchecked)
                    if colomn in range(0, 3):
                        item.setBackground(QtGui.QColor(193, 205, 205, 150))
                    if colomn in range(3, 6):
                        item.setBackground(QtGui.QColor(224, 238, 238))
                    if colomn in range(6, 9):
                        item.setBackground(QtGui.QColor(173, 184, 184, 110))
                    if colomn in range(9, 12):
                        item.setBackground(QtGui.QColor(240, 255, 255, 220))

                    self.tableWidget.setItem(row, colomn, item)

            # conn = psycopg2.connect(database="plottest", user="postgres")
            conn = psycopg2.connect(database="%s" % (Ui_Dialog.dbname), user="%s" % (Ui_Dialog.uname),
                                    password="%s" % (Ui_Dialog.pwd), host="%s" % (Ui_Dialog.ip_add),
                                    port="5432")
            self.statusbar.showMessage("Database opened Sucessfully", 1000)
            cur = conn.cursor()
            cur.execute("SELECT TIM,ia,pa,aa,ua,ib,pb,ab,ua,ic,pc,ac,uc,id,pd,ad,ua from \"%s\" " % date)
            rows = cur.fetchall()
            print(rows)
            # ordereddic = collections.OrderedDict(sorted(dict_rows.items()))
            # print(ordereddic)
            # count = 0
            # for x in ordereddic.values():
            #     item = QtGui.QTableWidgetItem()
            #     item.setFlags(QtCore.Qt.ItemIsEditable)
            #     item.setText(" %s " % x)
            #     self.tableWidget.setItem(count, 0, item)
            #     #print(x,count)
            #     count += 1
            for x in rows:
                item1 = QtGui.QTableWidgetItem() ##IA
                item2 = QtGui.QTableWidgetItem() ##AA
                item3 = QtGui.QTableWidgetItem()
                item4 = QtGui.QTableWidgetItem()
                item5 = QtGui.QTableWidgetItem()
                item6 = QtGui.QTableWidgetItem()
                item7 = QtGui.QTableWidgetItem()
                item8 = QtGui.QTableWidgetItem()
                item8 = QtGui.QTableWidgetItem()
                item9 = QtGui.QTableWidgetItem()
                item10 = QtGui.QTableWidgetItem()
                item11 = QtGui.QTableWidgetItem()
                item12 = QtGui.QTableWidgetItem()

                item1.setText(" %s " % x[1])
                item1.setBackground(QtGui.QColor(193, 205, 205, 150))
                item2.setText(" %s " % x[2])
                item2.setBackground(QtGui.QColor(193, 205, 205, 150))
                item3.setText(" %s " % x[3])
                item3.setBackground(QtGui.QColor(193, 205, 205, 150))

                item4.setText(" %s " % x[5])
                item4.setBackground(QtGui.QColor(224, 238, 238))
                item5.setText(" %s " % x[6])
                item5.setBackground(QtGui.QColor(224, 238, 238))
                item6.setText(" %s " % x[7])
                item6.setBackground(QtGui.QColor(224, 238, 238))

                item7.setText(" %s " % x[9])
                item7.setBackground(QtGui.QColor(173, 184, 184, 110))
                item8.setText(" %s " % x[10])
                item8.setBackground(QtGui.QColor(173, 184, 184, 110))
                item9.setText(" %s " % x[11])
                item9.setBackground(QtGui.QColor(173, 184, 184, 110))

                item10.setText(" %s " % x[13])
                item10.setBackground(QtGui.QColor(240, 255, 255, 220))
                item11.setText(" %s " % x[14])
                item11.setBackground(QtGui.QColor(240, 255, 255, 220))
                item12.setText(" %s " % x[15])
                item12.setBackground(QtGui.QColor(240, 255, 255, 220))

                if x[4] is True:
                    item2.setCheckState(QtCore.Qt.Checked)
                else:
                    item2.setCheckState(QtCore.Qt.Unchecked)

                if x[8] is True:
                    item5.setCheckState(QtCore.Qt.Checked)
                else:
                    item5.setCheckState(QtCore.Qt.Unchecked)

                if x[12] is True:
                    item8.setCheckState(QtCore.Qt.Checked)
                else:
                    item8.setCheckState(QtCore.Qt.Unchecked)

                if x[16] == True:
                    item11.setCheckState(QtCore.Qt.Checked)
                else:
                    item11.setCheckState(QtCore.Qt.Unchecked)

                self.tableWidget.setItem(x[0], 0, item1)
                self.tableWidget.setItem(x[0], 1, item2)
                self.tableWidget.setItem(x[0], 2, item3)

                self.tableWidget.setItem(x[0], 3, item4)
                self.tableWidget.setItem(x[0], 4, item5)
                self.tableWidget.setItem(x[0], 5, item6)

                self.tableWidget.setItem(x[0], 6, item7)
                self.tableWidget.setItem(x[0], 7, item8)
                self.tableWidget.setItem(x[0], 8, item9)

                self.tableWidget.setItem(x[0], 9, item10)
                self.tableWidget.setItem(x[0], 10, item11)
                self.tableWidget.setItem(x[0], 11, item12)


            conn.commit()
            conn.close()

            # conn = psycopg2.connect(database="plottest", user="postgres")
            conn = psycopg2.connect(database="%s" % (Ui_Dialog.dbname), user="%s" % (Ui_Dialog.uname),
                                    password="%s" % (Ui_Dialog.pwd), host="%s" % (Ui_Dialog.ip_add),
                                    port="5432")
            self.statusbar.showMessage("Database opened Sucessfully", 1000)
            cur1 = conn.cursor()
            cur1.execute("SELECT a,b,c,d from DAILY where date = \'%s\'" % date)
            cur2 = conn.cursor()
            cur2.execute("SELECT a,b,c,d from MONTHLY where month = \'%s\'" % month)
            dailyqty = cur1.fetchall()
            monthqty = cur2.fetchall()
            for y in dailyqty:
                print(y[0], y[1], y[2], y[3])
                self.lineEdit_8.setText(str(y[0]))
                self.lineEdit_7.setText(str(y[1]))
                self.lineEdit_6.setText(str(y[2]))
                self.lineEdit_5.setText(str(y[3]))

            for z in monthqty:
                print(z[0], z[1], z[2], z[3])
                self.lineEdit_4.setText(str(z[0]))
                self.lineEdit_3.setText(str(z[1]))
                self.lineEdit_2.setText(str(z[2]))
                self.lineEdit.setText(str(z[3]))

            conn.commit()
            conn.close()

        except psycopg2.ProgrammingError:
            self.statusbar.showMessage("Table not Exist", 1000)
            self.tableWidget.clearContents()
            # conn = psycopg2.connect(database="plottest", user="postgres")
            conn = psycopg2.connect(database="%s" % (Ui_Dialog.dbname), user="%s" % (Ui_Dialog.uname),
                                    password="%s" % (Ui_Dialog.pwd), host="%s" % (Ui_Dialog.ip_add),
                                    port="5432")
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE \"%s\" (TIM INT PRIMARY KEY NOT NULL,IA TEXT NOT NULL,PA TEXT NOT NULL,AA TEXT NOT NULL,UA BOOLEAN NOT NULL,IB TEXT NOT NULL, PB TEXT NOT NULL,AB TEXT NOT NULL,UB BOOLEAN NOT NULL,IC TEXT NOT NULL, PC TEXT NOT NULL,AC TEXT NOT NULL,UC BOOLEAN NOT NULL,ID TEXT NOT NULL,PD TEXT NOT NULL,AD TEXT NOT NULL,UD BOOLEAN NOT NULL)" % date)
            self.statusbar.showMessage("Table created : %s" % (date), 1000)
            conn.commit()
            conn.close()

        except TypeError:
            self.statusbar.showMessage("Update daily qty", 1000)


    def savefunc(self):
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Connected to " + "  " + str(
                                            Ui_Dialog.ip_add) + "  " + str(Ui_Dialog.dbname) + "  " + str(
                                            Ui_Dialog.uname) + "</span></body></html>", None))

        qdate = self.calendarWidget.selectedDate()
        date = qdate.toPyDate()
        date = str(date)
        self.statusbar.showMessage("SAVED", 1000)
        allRows = self.tableWidget.rowCount()
        actualrc=0
        for row1 in range(0, allRows):
            actualrc+=1
            print(actualrc)
            if self.tableWidget.item(row1,0).text() =='':
                break

        for row in range(0, (actualrc-1)):
            # conn = psycopg2.connect(database="plottest", user="postgres")
            conn = psycopg2.connect(database="%s" % (Ui_Dialog.dbname), user="%s" % (Ui_Dialog.uname),
                                    password="%s" % (Ui_Dialog.pwd), host="%s" % (Ui_Dialog.ip_add),
                                    port="5432")
            self.statusbar.showMessage("Database opened Sucessfully", 1000)
            cur = conn.cursor()
            col1 = self.tableWidget.item(row, 0).text() ##item A
            col2 = self.tableWidget.item(row, 1).text() ##Plan A
            col3 = self.tableWidget.item(row, 2).text() ##Actual A
            col4 = str(bool(self.tableWidget.item(row, 1).checkState())) ##Status A
            # col4 = self.tableWidget.item(row, 1).checkState()

            col5 = self.tableWidget.item(row, 3).text() ##Item B
            col6 = self.tableWidget.item(row, 4).text() ##Plan B
            col7 = self.tableWidget.item(row, 5).text() ##Actual B
            col8 = str(bool(self.tableWidget.item(row, 4).checkState())) ##Status B
            # col8 = self.tableWidget.item(row, 4).checkState()

            col9  = self.tableWidget.item(row, 6).text() ##Item C
            col10 = self.tableWidget.item(row, 7).text() ##Plan C
            col11 = self.tableWidget.item(row, 8).text() ##Actual C
            col12 = str(bool(self.tableWidget.item(row, 7).checkState())) ##Status C
            # col12 = self.tableWidget.item(row, 7).checkState()

            col13 = self.tableWidget.item(row, 9).text() ##Item D
            col14 = self.tableWidget.item(row, 10).text() ##Plan D
            col15 = self.tableWidget.item(row, 11).text() ##Actual D
            col16 = str(bool(self.tableWidget.item(row, 10).checkState())) ##Status D
            # col16 = self.tableWidget.item(row, 10).checkState()

            rownum = row
            print("COLLL =", date, rownum, col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12,
                  col13, col14, col15, col16)
            print(rownum)
            try:
                cur.execute(
                    "INSERT INTO \"%s\" (TIM,IA,PA,AA,UA,IB,PB,AB,UB,IC,PC,AC,UC,ID,PD,AD,UD) VALUES (%d,\'%s\',%s,%s,%s,\'%s\',%s,%s,%s,\'%s\',%s,%s,%s,\'%s\',%s,%s,%s)" % (date, rownum, col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16))
                # self.statusbar.showMessage("Inserted = %s %s %s %s" % (col1, col2, col3, col4), 500)
                print("INSERTED")
                conn.commit()
                conn.close()
            except psycopg2.IntegrityError:
                # conn = psycopg2.connect(database="plottest", user="postgres")
                conn = psycopg2.connect(database="%s" % (Ui_Dialog.dbname), user="%s" % (Ui_Dialog.uname),
                                        password="%s" % (Ui_Dialog.pwd), host="%s" % (Ui_Dialog.ip_add),
                                        port="5432")
                self.statusbar.showMessage("Database opened Sucessfully", 1000)
                cur = conn.cursor()
                # cur.execute(
                #     "UPDATE \"%s\" SET PA=%s , AA=%s , PB=%s , AB=%s, PC=%s , AC=%s , PD=%s , AD=%s WHERE id= %d" % (date, col1, col2, col3, col4, col5, col6, col7, col8, rownum))
                cur.execute("UPDATE \"%s\" SET IA =\'%s\', PA =%s, AA=%s, UA=%s, IB =\'%s\',PB =%s,AB=%s,UB=%s, IC =\'%s\', PC =%s, AC=%s, UC=%s, ID =\'%s\', PD =%s, AD=%s, UD=%s WHERE TIM= %d" % (date, col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, rownum))
                # self.statusbar.showMessage("updated = %s %s %s %s" % (col1, col2, col3, col4), 500)
                print("UPDATED")
                conn.commit()
                conn.close()
            except AttributeError:
                print("SUCESS")


    def TimeNow(self):
        timenow = str(datetime.datetime.now().time())
        date = str(datetime.datetime.now().date())
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; font-weight:600;\">"+" | " + timenow[0:5]+ " | " +date+"</span></p></body></html>",
                                        None))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Connected to " + "  " + str(
                                            Ui_Dialog.ip_add) + "  " + str(Ui_Dialog.dbname) + "  " + str(
                                            Ui_Dialog.uname) + "</span></body></html>", None))


# class Ui_Dialog(object):
#     ip_add = 'localhost'
#     dbname = 'dsisppms'
#     uname = 'postgres'
#     pwd = '123456'
#
#     def setupUi(self, Dialog):
#         Dialog.setObjectName(_fromUtf8("Dialog"))
#         Dialog.resize(350, 272)
#         self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
#         self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
#         self.verticalLayout = QtGui.QVBoxLayout()
#         self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
#         self.label = QtGui.QLabel(Dialog)
#         self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"Cantarell\";"))
#         self.label.setObjectName(_fromUtf8("label"))
#         self.verticalLayout.addWidget(self.label)
#         self.formLayout = QtGui.QFormLayout()
#         self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
#         self.formLayout.setObjectName(_fromUtf8("formLayout"))
#         self.label_2 = QtGui.QLabel(Dialog)
#         self.label_2.setObjectName(_fromUtf8("label_2"))
#         self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
#         self.lineEdit = QtGui.QLineEdit(Dialog)
#         self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
#         self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
#         self.label_3 = QtGui.QLabel(Dialog)
#         self.label_3.setObjectName(_fromUtf8("label_3"))
#         self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
#         self.lineEdit_2 = QtGui.QLineEdit(Dialog)
#         self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
#         self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
#         self.label_4 = QtGui.QLabel(Dialog)
#         self.label_4.setObjectName(_fromUtf8("label_4"))
#         self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
#         self.lineEdit_3 = QtGui.QLineEdit(Dialog)
#         self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
#         self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Password)
#         self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
#
#         self.label_6 = QtGui.QLabel(Dialog)
#         self.label_6.setObjectName(_fromUtf8("label_6"))
#         self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
#         self.lineEdit_6 = QtGui.QLineEdit(Dialog)
#         self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
#         self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
#
#         self.verticalLayout.addLayout(self.formLayout)
#         self.verticalLayout_2.addLayout(self.verticalLayout)
#         self.horizontalLayout = QtGui.QHBoxLayout()
#         self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
#         spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
#         self.horizontalLayout.addItem(spacerItem)
#         self.pushButton = QtGui.QPushButton(Dialog)
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/connector.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
#         self.pushButton.setIcon(icon)
#         self.pushButton.setObjectName(_fromUtf8("pushButton"))
#         self.pushButton.clicked.connect(self.connection)
#         self.horizontalLayout.addWidget(self.pushButton)
#         self.verticalLayout_2.addLayout(self.horizontalLayout)
#         self.buttonBox = QtGui.QDialogButtonBox(Dialog)
#         self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#         self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
#         self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
#         self.verticalLayout_2.addWidget(self.buttonBox)
#         self.label_5 = QtGui.QLabel(Dialog)
#         self.label_5.setObjectName(_fromUtf8("label_5"))
#         self.verticalLayout_2.addWidget(self.label_5)
#         self.retranslateUi(Dialog)
#         QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
#         QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#         self.variable = "LOVE"
#
#     def retranslateUi(self, Dialog):
#         Dialog.setWindowTitle(_translate("Dialog", "Server Login", None))
#         self.label.setText(_translate("Dialog", "Database Connection Settings", None))
#         self.label_2.setText(_translate("Dialog", "IP Address", None))
#         self.label_3.setText(_translate("Dialog", "User Name", None))
#         self.label_4.setText(_translate("Dialog", "Password", None))
#         self.pushButton.setText(_translate("Dialog", "Connect", None))
#         self.label_6.setText(_translate("Dialog", "Database Name", None))
#
#     def connection(self):
#         Ui_Dialog.ip_add = self.lineEdit.text()
#         Ui_Dialog.dbname = self.lineEdit_6.text()
#         Ui_Dialog.uname = self.lineEdit_2.text()
#         Ui_Dialog.pwd = self.lineEdit_3.text()
#         # self.data_connection_string =("database=%s, user=%s, password=%s, host=%s, port=5432" % (self.dbname,self.uname,self.pwd, self.ip_add))
#         # print(type(database="plottest", user="postgres",password="*",host="localhost", port="5432"))
#         try:
#             conn_test = psycopg2.connect(database="%s" % (Ui_Dialog.dbname), user="%s" % (Ui_Dialog.uname),
#                                            password="%s" % (Ui_Dialog.pwd), host="%s" % (Ui_Dialog.ip_add), port="5432")
#             self.label_5.setText(_translate("Dialog", "Connection Success", None))
#
#         except psycopg2.ProgrammingError:
#             self.label_5.setText(_translate("Dialog", "Connection Failed", None))
#
#         except psycopg2.OperationalError:
#             self.label_5.setText(_translate("Dialog", "Connection Failed", None))
#         # conn = psycopg2._connect(self.data_connection_string)
#         # connec_test = psycopg2.connect(database="%s"%(self.dbname),user="%s"%(self.uname),password="%s"%(self.pwd),host="%s"%(self.ip_add), port="5432")
#         #self.label_5.setText(_translate("Dialog", "Connection Success", None))


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(526, 494)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 12pt \"Cantarell\";"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setStyleSheet(_fromUtf8("image: url(:/Images/dsicropped.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">DSI-SPORTSWEAR PRODUCTION MONITORING SYSTEM</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Version Beta 2.1</span></p><p><span style=\" font-size:12pt;\">Copyright(c) 2016 DSISP Engineering Division. All Rights reserved</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Project Team</span></p><p><span style=\" font-weight:600;\">Lakshan Walpita</span> : Advisor</p><p><span style=\" font-weight:600;\">Gihan Anurudda </span>: Engineer (Design and UI)</p><p><span style=\" font-weight:600;\">Vibhutha Kumarage </span>: Engineer (System and Database)</p><p><span style=\" font-size:9pt;\">Contact : vkartz@gmail.com +94712069424</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())