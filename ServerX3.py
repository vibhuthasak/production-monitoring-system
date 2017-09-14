from PyQt4 import QtCore, QtGui
from Connection2 import *
from MonthlyPlan import *
from about2 import *
import psycopg2
import datetime as dt

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

class Ui_MainWindow(QtGui.QMainWindow,Connection2.Ui_Dialog2):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1049, 777)
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
        self.timenow = QtGui.QLabel(self.centralwidget)
        self.timenow.setObjectName(_fromUtf8("timenow"))
        self.horizontalLayout_4.addWidget(self.timenow)
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
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.sectionC = QtGui.QLabel(self.centralwidget)
        self.sectionC.setObjectName(_fromUtf8("sectionC"))
        self.gridLayout.addWidget(self.sectionC, 1, 3, 1, 1)
        self.dailyplan = QtGui.QLabel(self.centralwidget)
        self.dailyplan.setObjectName(_fromUtf8("dailyplan"))
        self.gridLayout.addWidget(self.dailyplan, 5, 0, 1, 1)
        self.sectionD = QtGui.QLabel(self.centralwidget)
        self.sectionD.setObjectName(_fromUtf8("sectionD"))
        self.gridLayout.addWidget(self.sectionD, 1, 4, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.secCmonth = QtGui.QLabel(self.centralwidget)
        self.secCmonth.setObjectName(_fromUtf8("secCmonth"))
        self.gridLayout.addWidget(self.secCmonth, 3, 3, 1, 1)
        self.sectionA = QtGui.QLabel(self.centralwidget)
        self.sectionA.setObjectName(_fromUtf8("sectionA"))
        self.gridLayout.addWidget(self.sectionA, 1, 1, 1, 1)
        self.secDmonthly = QtGui.QLabel(self.centralwidget)
        self.secDmonthly.setObjectName(_fromUtf8("secDmonthly"))
        self.gridLayout.addWidget(self.secDmonthly, 3, 4, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 1)
        self.secDdaily = QtGui.QLabel(self.centralwidget)
        self.secDdaily.setObjectName(_fromUtf8("secDdaily"))
        self.gridLayout.addWidget(self.secDdaily, 5, 4, 1, 1)
        self.secBmonthly = QtGui.QLabel(self.centralwidget)
        self.secBmonthly.setObjectName(_fromUtf8("secBmonthly"))
        self.gridLayout.addWidget(self.secBmonthly, 3, 2, 1, 1)
        self.secBdaily = QtGui.QLabel(self.centralwidget)
        self.secBdaily.setObjectName(_fromUtf8("secBdaily"))
        self.gridLayout.addWidget(self.secBdaily, 5, 2, 1, 1)
        self.secCdaily = QtGui.QLabel(self.centralwidget)
        self.secCdaily.setObjectName(_fromUtf8("secCdaily"))
        self.gridLayout.addWidget(self.secCdaily, 5, 3, 1, 1)
        self.monthlyplan = QtGui.QLabel(self.centralwidget)
        self.monthlyplan.setObjectName(_fromUtf8("monthlyplan"))
        self.gridLayout.addWidget(self.monthlyplan, 3, 0, 1, 1)
        self.secAmonth = QtGui.QLabel(self.centralwidget)
        self.secAmonth.setObjectName(_fromUtf8("secAmonth"))
        self.gridLayout.addWidget(self.secAmonth, 3, 1, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShadow(QtGui.QFrame.Plain)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 6, 0, 1, 1)
        self.secAdaily = QtGui.QLabel(self.centralwidget)
        self.secAdaily.setObjectName(_fromUtf8("secAdaily"))
        self.gridLayout.addWidget(self.secAdaily, 5, 1, 1, 1)
        self.sectionB = QtGui.QLabel(self.centralwidget)
        self.sectionB.setObjectName(_fromUtf8("sectionB"))
        self.gridLayout.addWidget(self.sectionB, 1, 2, 1, 1)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShadow(QtGui.QFrame.Plain)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 0, 1, 1, 1)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShadow(QtGui.QFrame.Plain)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 0, 2, 1, 1)
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setFrameShadow(QtGui.QFrame.Plain)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout.addWidget(self.line_6, 0, 3, 1, 1)
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setFrameShadow(QtGui.QFrame.Plain)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout.addWidget(self.line_7, 0, 4, 1, 1)
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setFrameShadow(QtGui.QFrame.Plain)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout.addWidget(self.line_8, 2, 1, 1, 1)
        self.line_9 = QtGui.QFrame(self.centralwidget)
        self.line_9.setFrameShadow(QtGui.QFrame.Plain)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.gridLayout.addWidget(self.line_9, 2, 2, 1, 1)
        self.line_10 = QtGui.QFrame(self.centralwidget)
        self.line_10.setFrameShadow(QtGui.QFrame.Plain)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.gridLayout.addWidget(self.line_10, 2, 3, 1, 1)
        self.line_11 = QtGui.QFrame(self.centralwidget)
        self.line_11.setFrameShadow(QtGui.QFrame.Plain)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.gridLayout.addWidget(self.line_11, 2, 4, 1, 1)
        self.line_12 = QtGui.QFrame(self.centralwidget)
        self.line_12.setFrameShadow(QtGui.QFrame.Plain)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.gridLayout.addWidget(self.line_12, 4, 1, 1, 1)
        self.line_13 = QtGui.QFrame(self.centralwidget)
        self.line_13.setFrameShadow(QtGui.QFrame.Plain)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.gridLayout.addWidget(self.line_13, 4, 2, 1, 1)
        self.line_14 = QtGui.QFrame(self.centralwidget)
        self.line_14.setFrameShadow(QtGui.QFrame.Plain)
        self.line_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.gridLayout.addWidget(self.line_14, 4, 3, 1, 1)
        self.line_15 = QtGui.QFrame(self.centralwidget)
        self.line_15.setFrameShadow(QtGui.QFrame.Plain)
        self.line_15.setFrameShape(QtGui.QFrame.HLine)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.gridLayout.addWidget(self.line_15, 4, 4, 1, 1)
        self.line_16 = QtGui.QFrame(self.centralwidget)
        self.line_16.setFrameShadow(QtGui.QFrame.Plain)
        self.line_16.setFrameShape(QtGui.QFrame.HLine)
        self.line_16.setObjectName(_fromUtf8("line_16"))
        self.gridLayout.addWidget(self.line_16, 6, 1, 1, 1)
        self.line_17 = QtGui.QFrame(self.centralwidget)
        self.line_17.setFrameShadow(QtGui.QFrame.Plain)
        self.line_17.setFrameShape(QtGui.QFrame.HLine)
        self.line_17.setObjectName(_fromUtf8("line_17"))
        self.gridLayout.addWidget(self.line_17, 6, 2, 1, 1)
        self.line_18 = QtGui.QFrame(self.centralwidget)
        self.line_18.setFrameShadow(QtGui.QFrame.Plain)
        self.line_18.setFrameShape(QtGui.QFrame.HLine)
        self.line_18.setObjectName(_fromUtf8("line_18"))
        self.gridLayout.addWidget(self.line_18, 6, 3, 1, 1)
        self.line_19 = QtGui.QFrame(self.centralwidget)
        self.line_19.setFrameShadow(QtGui.QFrame.Plain)
        self.line_19.setFrameShape(QtGui.QFrame.HLine)
        self.line_19.setObjectName(_fromUtf8("line_19"))
        self.gridLayout.addWidget(self.line_19, 6, 4, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(15)
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
        self.tableWidget.setVerticalHeaderItem(14, item)
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
        # item = QtGui.QTableWidgetItem()
        # item.setCheckState(QtCore.Qt.Unchecked)
        # self.tableWidget.setItem(0, 1, item)

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

        self.tableWidget.horizontalHeader().setDefaultSectionSize(77)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(11)
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
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/3d6cfa22471.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.save_function)
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuConnect = QtGui.QMenu(self.menubar)
        self.menuConnect.setObjectName(_fromUtf8("menuConnect"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuPlan = QtGui.QMenu(self.menubar)
        self.menuPlan.setObjectName(_fromUtf8("menuPlan"))
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

        self.actionMonthly_Plan = QtGui.QAction(MainWindow)
        self.actionMonthly_Plan.setObjectName(_fromUtf8("actionMonthly_Plan"))

        self.menuConnect.addAction(self.actionServer_Login)
        self.actionServer_Login.triggered.connect(self.clicked_connection)

        self.menuConnect.addAction(self.actionQuit)
        self.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)

        self.menuHelp.addAction(self.actionAbout)
        self.actionAbout.triggered.connect(self.clicked_about)

        self.menuPlan.addAction(self.actionMonthly_Plan)
        self.actionMonthly_Plan.triggered.connect(self.clicked_month_plan)

        self.menubar.addAction(self.menuConnect.menuAction())
        self.menubar.addAction(self.menuPlan.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.time_now)
        self.timer.start(1000)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DSISPPMS", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">DSI-SP Production Monitoring System</span></p></body></html>", None))
        # self.timenow.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; font-weight:600;\">TIMENOW</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Section Select    :</span></p></body></html>", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sewing", None))
        self.sectionC.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Section C</span></p></body></html>", None))
        self.dailyplan.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Daily Plan</span></p></body></html>", None))
        self.sectionD.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Section D</span></p></body></html>", None))
        # self.secCmonth.setText(_translate("MainWindow", "12547", None))
        self.sectionA.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Section A</span></p></body></html>", None))
        # self.secDmonthly.setText(_translate("MainWindow", "15478", None))
        # self.secDdaily.setText(_translate("MainWindow", "12547", None))
        # self.secBmonthly.setText(_translate("MainWindow", "14455", None))
        # self.secBdaily.setText(_translate("MainWindow", "45785", None))
        # self.secCdaily.setText(_translate("MainWindow", "98745", None))
        self.monthlyplan.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Monthly Plan</span></p></body></html>", None))
        # self.secAmonth.setText(_translate("MainWindow", "12354", None))
        # self.secAdaily.setText(_translate("MainWindow", "78984", None))
        self.sectionB.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Section B</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "                     |                   Section A                      |                   Section B                      |                    Section C                     |                    Section D                 |", None))
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
        item.setText(_translate("MainWindow", "15:00-16:00", None))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "16:00-17:00", None))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "17:00-18:00", None))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "18:00-19:00", None))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "19:00-20:00", None))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "20:00-21:00", None))
        item = self.tableWidget.verticalHeaderItem(14)
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
        # self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Connected </span>", None))
        self.menuConnect.setTitle(_translate("MainWindow", "Settings", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuPlan.setTitle(_translate("MainWindow", "Plan", None))
        self.actionServer_Login.setText(_translate("MainWindow", "Server Login", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionMonthly_Plan.setText(_translate("MainWindow", "Monthly Plan", None))

    def clicked_connection(self):
        '''
        Execute Log-in dialog Connection2.py
        Set psycopg2 connection parameters
        :return:
        '''
        connection_window = QtGui.QDialog()
        connection_dialog = Ui_Dialog2()
        connection_dialog.setupUi(connection_window)
        connection_window.exec_()
        # print("Connection")

    def clicked_about(self):
        '''
        Launch about2.py
        :return: Nothin Return
        '''
        about_window = QtGui.QDialog()
        about_dialog = Ui_Dialog()
        about_dialog.setupUi(about_window)
        about_window.exec_()
        # print("About")

    def clicked_month_plan(self):
        '''
        Launch MonthlyPlan.py
        :return:
        '''
        monthly_window = QtGui.QDialog()
        monthly_dialog = Ui_Dialog3()
        monthly_dialog.setupUi(monthly_window)
        monthly_window.exec_()
        # print("MonthlyPlan")

    def time_now(self):
        '''
        Display Time on the MainWindow
        :return:
        '''
        dtime = str(dt.datetime.now().time())
        ddate = str(dt.datetime.now().date())
        # print("TIME =",dtime, "DATE =", ddate)
        self.timenow.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; font-weight:200;\">"+dtime[0:8]+" "+ddate+"</span></p></body></html>",
                                        None))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Connected to " + "  " + str(
                                            Connection2.Ui_Dialog2.ip_add) + "  " + str(Connection2.Ui_Dialog2.dbname) + "  " + str(
                                            Connection2.Ui_Dialog2.uname) + "</span></body></html>", None))

    def date_select(self):
        '''
        1.Create Table for each date if the date is not exist
        2.Load Table cell from Database Values
        3.Set Daily Target,Monthly Target on the MainWindow
        :return:
        '''

        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Connected to " + "  " + str(
                                            Connection2.Ui_Dialog2.ip_add) + "  " + str(
                                            Connection2.Ui_Dialog2.dbname) + "  " + str(
                                            Connection2.Ui_Dialog2.uname) + "</span></body></html>", None))

        ## Get the selected date on Calender Widget
        selected_date = self.calendarWidget.selectedDate()
        date = str(selected_date.toPyDate())
        month = date[0:7]
        print(month)

        try:
            # conn = psycopg2.connect(database="dsisppms", user="postgres", host="127.0.0.1", port="5432")
            conn = psycopg2.connect(database="%s" % (Connection2.Ui_Dialog2.dbname),
                                    user="%s" % (Connection2.Ui_Dialog2.uname),
                                    password="%s" % (Connection2.Ui_Dialog2.pwd),
                                    host="%s" % (Connection2.Ui_Dialog2.ip_add), port="5432")

            self.statusbar.showMessage("Database opened Sucessfully", 1000)
            cur1 = conn.cursor()
            cur1.execute(
                "SELECT SUM(seca),sum(secb),sum(secc),sum(secd) from \"{0}\"".format(month))  ##SELECTING MONTHLY TARGET
            cur2 = conn.cursor()
            cur2.execute("SELECT seca,secb,secc,secd from \"{0}\" where date = \'{1}\'".format(month,
                                                                                               date))  ##SELECTING DAILY TARGET
            monthqty = cur1.fetchall()
            dailyqty = cur2.fetchall()

            ## Assigning Monthly and Daily Target Values to lables
            for y in dailyqty:
                print("dailyqty", y[0], y[1], y[2], y[3])
                self.secAdaily.setText(_translate("MainWindow", str(y[0]), None))
                self.secBdaily.setText(_translate("MainWindow", str(y[1]), None))
                self.secCdaily.setText(_translate("MainWindow", str(y[2]), None))
                self.secDdaily.setText(_translate("MainWindow", str(y[3]), None))
            #
            for z in monthqty:
                print("monthqty", z[0], z[1], z[2], z[3])
                self.secAmonth.setText(_translate("MainWindow", str(z[0]), None))
                self.secBmonthly.setText(_translate("MainWindow", str(z[1]), None))
                self.secCmonth.setText(_translate("MainWindow", str(z[2]), None))
                self.secDmonthly.setText(_translate("MainWindow", str(z[3]), None))

            conn.commit()
            conn.close()
        except psycopg2.ProgrammingError:
            self.statusbar.showMessage("Month Data for {0} not exists".format(month), 1000)
            self.secAdaily.setText(_translate("MainWindow", "N/A", None))
            self.secBdaily.setText(_translate("MainWindow", "N/A", None))
            self.secCdaily.setText(_translate("MainWindow", "N/A", None))
            self.secDdaily.setText(_translate("MainWindow", "N/A", None))
            self.secAmonth.setText(_translate("MainWindow", "N/A", None))
            self.secBmonthly.setText(_translate("MainWindow", "N/A", None))
            self.secCmonth.setText(_translate("MainWindow", "N/A", None))
            self.secDmonthly.setText(_translate("MainWindow", "N/A", None))


        try:
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

            # conn = psycopg2.connect(database="dsisppms", user="postgres", host="127.0.0.1", port="5432")
            conn = psycopg2.connect(database="%s" % (Connection2.Ui_Dialog2.dbname),
                                    user="%s" % (Connection2.Ui_Dialog2.uname),
                                    password="%s" % (Connection2.Ui_Dialog2.pwd),
                                    host="%s" % (Connection2.Ui_Dialog2.ip_add), port="5432")

            self.statusbar.showMessage("Database opened Sucessfully", 1000)
            cur = conn.cursor()
            cur.execute("SELECT TIM,ia,pa,aa,ua,ib,pb,ab,ub,ic,pc,ac,uc,id,pd,ad,ud from \"{0}\" ".format(date))
            rows = cur.fetchall()
            print(rows)
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

                item1.setText("{0}".format(x[1]))
                item1.setBackground(QtGui.QColor(193, 205, 205, 150))
                item2.setText("{0}".format(x[2]))
                item2.setBackground(QtGui.QColor(193, 205, 205, 150))
                item3.setText("{0}".format(x[3]))
                item3.setBackground(QtGui.QColor(193, 205, 205, 150))

                item4.setText("{0}".format(x[5]))
                item4.setBackground(QtGui.QColor(224, 238, 238))
                item5.setText("{0}".format(x[6]))
                item5.setBackground(QtGui.QColor(224, 238, 238))
                item6.setText("{0}".format(x[7]))
                item6.setBackground(QtGui.QColor(224, 238, 238))

                item7.setText("{0}".format(x[9]))
                item7.setBackground(QtGui.QColor(173, 184, 184, 110))
                item8.setText("{0}".format(x[10]))
                item8.setBackground(QtGui.QColor(173, 184, 184, 110))
                item9.setText("{0}".format(x[11]))
                item9.setBackground(QtGui.QColor(173, 184, 184, 110))

                item10.setText("{0}".format(x[13]))
                item10.setBackground(QtGui.QColor(240, 255, 255, 220))
                item11.setText("{0}".format(x[14]))
                item11.setBackground(QtGui.QColor(240, 255, 255, 220))
                item12.setText("{0}".format(x[14]))
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

                if x[16] is True:
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

        except psycopg2.ProgrammingError:
            self.statusbar.showMessage("Table not Exist", 1000)
            self.tableWidget.clearContents()
            # conn = psycopg2.connect(database="dsisppms", user="postgres", host="127.0.0.1", port="5432")
            conn = psycopg2.connect(database="%s" % (Connection2.Ui_Dialog2.dbname),
                                    user="%s" % (Connection2.Ui_Dialog2.uname),
                                    password="%s" % (Connection2.Ui_Dialog2.pwd),
                                    host="%s" % (Connection2.Ui_Dialog2.ip_add), port="5432")

            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE \"{0}\" (TIM INT PRIMARY KEY NOT NULL,IA TEXT NOT NULL,PA INT NOT NULL,AA INT NOT NULL,UA BOOLEAN NOT NULL,IB TEXT NOT NULL, PB INT NOT NULL,AB INT NOT NULL,UB BOOLEAN NOT NULL,IC TEXT NOT NULL, PC INT NOT NULL,AC INT NOT NULL,UC BOOLEAN NOT NULL,ID TEXT NOT NULL,PD INT NOT NULL,AD INT NOT NULL,UD BOOLEAN NOT NULL)".format(date))
            self.statusbar.showMessage("Table created : %s" % (date), 1000)
            conn.commit()
            conn.close()

        except TypeError:
            self.statusbar.showMessage("Update daily qty", 1000)

    def save_function(self):
        '''
        save data on table cells to the database table(eg:2017-01-23)
        update database table data if exist
        :return:
        '''

        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Connected to " + "  " + str(
                                            Connection2.Ui_Dialog2.ip_add) + "  " + str(
                                            Connection2.Ui_Dialog2.dbname) + "  " + str(
                                            Connection2.Ui_Dialog2.uname) + "</span></body></html>", None))

        qdate = self.calendarWidget.selectedDate()
        date = qdate.toPyDate()
        date = str(date)
        self.statusbar.showMessage("SAVED", 1000)
        allRows = self.tableWidget.rowCount()
        actualrc = 0
        ## Get the row count which data is available
        for row1 in range(0, allRows):
            actualrc += 1
            print(actualrc)
            if self.tableWidget.item(row1, 0).text() == '':
                break

        for row in range(0, (actualrc - 1)): ##Loop until actual data table row-1
            # conn = psycopg2.connect(database="dsisppms", user="postgres", host="127.0.0.1", port="5432")
            conn = psycopg2.connect(database="%s" % (Connection2.Ui_Dialog2.dbname),
                                    user="%s" % (Connection2.Ui_Dialog2.uname),
                                    password="%s" % (Connection2.Ui_Dialog2.pwd),
                                    host="%s" % (Connection2.Ui_Dialog2.ip_add), port="5432")

            self.statusbar.showMessage("Database opened Sucessfully", 1000)
            cur = conn.cursor()
            col1 = self.tableWidget.item(row, 0).text()  ##item A
            col2 = self.tableWidget.item(row, 1).text()  ##Plan A
            col3 = self.tableWidget.item(row, 2).text()  ##Actual A
            col4 = str(bool(self.tableWidget.item(row, 1).checkState()))  ##Status A

            col5 = self.tableWidget.item(row, 3).text()  ##Item B
            col6 = self.tableWidget.item(row, 4).text()  ##Plan B
            col7 = self.tableWidget.item(row, 5).text()  ##Actual B
            col8 = str(bool(self.tableWidget.item(row, 4).checkState()))  ##Status B

            col9 = self.tableWidget.item(row, 6).text()  ##Item C
            col10 = self.tableWidget.item(row, 7).text()  ##Plan C
            col11 = self.tableWidget.item(row, 8).text()  ##Actual C
            col12 = str(bool(self.tableWidget.item(row, 7).checkState()))  ##Status C

            col13 = self.tableWidget.item(row, 9).text()  ##Item D
            col14 = self.tableWidget.item(row, 10).text()  ##Plan D
            col15 = self.tableWidget.item(row, 11).text()  ##Actual D
            col16 = str(bool(self.tableWidget.item(row, 10).checkState()))  ##Status D

            rownum = row
            print("COL =", date, rownum,col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12,
                  col13, col14, col15, col16)
            print(rownum)
            try:
                cur.execute(
                    "INSERT INTO \"{0}\" (TIM,IA,PA,AA,UA,IB,PB,AB,UB,IC,PC,AC,UC,ID,PD,AD,UD) VALUES ({1},\'{2}',{3},{4},{5},\'{6}\',{7},{8},{9},\'{10}\',{11},{12},{13},\'{14}\',{15},{16},{17})".format(
                    date, rownum, col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13,
                    col14, col15, col16))

                # self.statusbar.showMessage("Inserted = %s %s %s %s" % (col1, col2, col3, col4), 500)
                print("INSERTED")
                conn.commit()
                conn.close()
            except psycopg2.IntegrityError:
                # conn = psycopg2.connect(database="dsisppms", user="postgres", host="127.0.0.1", port="5432")
                conn = psycopg2.connect(database="%s" % (Connection2.Ui_Dialog2.dbname),
                                        user="%s" % (Connection2.Ui_Dialog2.uname),
                                        password="%s" % (Connection2.Ui_Dialog2.pwd),
                                        host="%s" % (Connection2.Ui_Dialog2.ip_add), port="5432")
                self.statusbar.showMessage("Database opened Sucessfully", 1000)
                cur = conn.cursor()
                cur.execute(
                    "UPDATE \"{0}\" SET IA =\'{1}\', PA ={2}, AA={3}, UA={4}, IB =\'{5}\',PB ={6},AB={7},UB={8}, IC =\'{9}\', PC ={10}, AC={11}, UC={12}, ID =\'{13}\', PD ={14}, AD={15}, UD={16} WHERE TIM= {17}".format(
                    date, col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14,
                    col15, col16, rownum))
                print("UPDATED")
                conn.commit()
                conn.close()
            except AttributeError:
                print("SUCESS")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())