# -*- coding: utf-8 -*-

import rersource_rc
from PyQt4 import QtCore, QtGui
from datetime import *
import psycopg2
import Connection2

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

class Ui_Dialog3(QtGui.QDialog,Connection2.Ui_Dialog2):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(568, 598)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.dateEdit = QtGui.QDateEdit(Dialog)
        self.dateEdit.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.dateEdit.setAutoFillBackground(False)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumDate(QtCore.QDate(2021, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate(2016, 1, 1))
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        # self.dateEdit.text()

        self.horizontalLayout.addWidget(self.dateEdit)
        self.pushButton = QtGui.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/red-sign-black-green-icon-right-blue-mark.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.apply_press)


        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setRowCount(32)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
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
        self.verticalLayout.addWidget(self.tableWidget)

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)

        self.buttonBox.button(QtGui.QDialogButtonBox.Apply).clicked.connect(self.database_save)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Monthly Plan", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Monthly Plan</span></p></body></html>", None))
        self.dateEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM", None))
        self.pushButton.setText(_translate("Dialog", "LOAD", None))
        #self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">2016-12-25</span></p></body></html>", None))
        # self.label_3.setText(_translate("Dialog", "to", None))
        #self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">2017-01-25</span></p></body></html>", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Date", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "A", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "B", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "C", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "D", None))

    def apply_press(self):
        '''
        1.Create a table #of rows = No of dates 25previous month-25current Month == done
        2.Fill Date Row in the table == done
        3.25previous month to 25 currentMonth == done
        :return:
        '''

        ### Startdate and Enddate Variables and Change Display Date in UI
        year_month = self.dateEdit.date()
        year_month = year_month.toPyDate()
        start_date = year_month - timedelta(days=13)
        start_date = start_date.replace(day=25)
        end_date   = year_month.replace(day=25)
        self.label_2.setText(_translate("Dialog","<html><head/><body><p><span style=\" font-weight:600;\">"+str(end_date)+"</span></p></body></html>",None))
        self.label_3.setText(_translate("Dialog", "to", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">" + str(start_date) + "</span></p></body></html>", None))
        ###

        ##Create a table using #of dates
        date_delta = (end_date-start_date)
        self.numberofrows = int(date_delta.days) ## Used in def database_save(self):
        ## POSTPONED OPERATION. REPALCED BY FIXED 32 ROWS

        self.this_month = end_date.strftime("%Y-%m")
        import pandas as pd

        daterange = pd.date_range(start_date, end_date)
        self.tableWidget.clearContents()

        enumerated_dates = enumerate(daterange, 0)
        # enumerated_dates2 = enumerate(daterange, 0)

        for self.count, self.single_date in enumerated_dates:
            item1 = QtGui.QTableWidgetItem()
            item1.setText(self.single_date.strftime("%Y-%m-%d"))
            self.tableWidget.setItem(self.count, 0, item1)
            item1.setFlags(QtCore.Qt.ItemIsEditable)
            item1.setBackground(QtGui.QColor(193, 205, 205, 150))
            item1.setTextColor(QtGui.QColor(0, 0, 0))

        # conn = psycopg2.connect(database="dsisppms", user="postgres", host="127.0.0.1", port="5432") ## psycopg2.ProgrammingError was risen :("

        try: ##Read the table
            # conn = psycopg2.connect(database="dsisppms", user="postgres", host="127.0.0.1", port="5432")
            conn = psycopg2.connect(database="%s" % (Connection2.Ui_Dialog2.dbname), user="%s" % (Connection2.Ui_Dialog2.uname),
                                           password="%s" % (Connection2.Ui_Dialog2.pwd), host="%s" % (Connection2.Ui_Dialog2.ip_add), port="5432")

            cur = conn.cursor()
            cur.execute("SELECT * FROM \"{0}\"".format(self.this_month))
            data_for_table = cur.fetchall()
            # print(data_for_table)
            for row in data_for_table:
                index = -1
                print(row)
                item2 = QtGui.QTableWidgetItem()
                item3 = QtGui.QTableWidgetItem()
                item4 = QtGui.QTableWidgetItem()
                item5 = QtGui.QTableWidgetItem()

                ## Match Date with Index and set value to table

                for c, v in enumerate(daterange, 0):
                    if v == datetime.strptime(row[0], "%Y-%m-%d"):
                        index = c

                item2.setText(str(row[1]))
                item3.setText(str(row[2]))
                item4.setText(str(row[3]))
                item5.setText(str(row[4]))

                self.tableWidget.setItem(index, 1, item2)
                self.tableWidget.setItem(index, 2, item3)
                self.tableWidget.setItem(index, 3, item4)
                self.tableWidget.setItem(index, 4, item5)

        except psycopg2.ProgrammingError: ##Create new table
            # conn = psycopg2.connect(database="dsisppms", user="postgres", host="127.0.0.1", port="5432")
            conn = psycopg2.connect(database="%s" % (Connection2.Ui_Dialog2.dbname),
                                    user="%s" % (Connection2.Ui_Dialog2.uname),
                                    password="%s" % (Connection2.Ui_Dialog2.pwd),
                                    host="%s" % (Connection2.Ui_Dialog2.ip_add), port="5432")
            cur = conn.cursor()
            cur.execute("CREATE TABLE  \"{0}\" (DATE TEXT PRIMARY KEY,SECA INT,SECB INT,SECC INT,SECD INT);".format(self.this_month))

        conn.commit()
        conn.close()

    def database_save(self):
        '''
        Save data row in table to the database
        if data row not exist save
        Trigged when click APPLY
        exist update
        self.numberofrows
        self.this_month  from previous function
        :return:
        '''
        print("This Month = {0} , Number of Row Count = {1}".format(self.this_month,self.numberofrows))

        for row in range(0, (self.numberofrows+1)):
            col1 = 0
            col2 = 0
            col3 = 0
            col4 = 0
            col5 = 0

            try:
            ##Colomn Data
                col1 = self.tableWidget.item(row, 0).text()
                col2 = self.tableWidget.item(row, 1).text()
                col3 = self.tableWidget.item(row, 2).text()
                col4 = self.tableWidget.item(row, 3).text()
                col5 = self.tableWidget.item(row, 4).text()
            ##
            except AttributeError: ## 1st run eke values aawe nathnam case hinda
                pass

            print("Colomns", col1, col2, col3, col4, col5)

            try:
                # conn = psycopg2.connect(database="dsisppms", user="postgres", host="127.0.0.1", port="5432")
                conn = psycopg2.connect(database="%s" % (Connection2.Ui_Dialog2.dbname),
                                        user="%s" % (Connection2.Ui_Dialog2.uname),
                                        password="%s" % (Connection2.Ui_Dialog2.pwd),
                                        host="%s" % (Connection2.Ui_Dialog2.ip_add), port="5432")
                cur = conn.cursor()
                cur.execute("INSERT INTO \"{0}\" (DATE,SECA,SECB,SECC,SECD) VALUES(\'{1}\',{2},{3},{4},{5})".format(self.this_month, col1, col2, col3, col4, col5))
                print("SAVED", row)
                conn.commit()
                conn.close()


            except psycopg2.IntegrityError:
                # conn = psycopg2.connect(database="dsisppms", user="postgres", host="127.0.0.1", port="5432")
                conn = psycopg2.connect(database="%s" % (Connection2.Ui_Dialog2.dbname),
                                        user="%s" % (Connection2.Ui_Dialog2.uname),
                                        password="%s" % (Connection2.Ui_Dialog2.pwd),
                                        host="%s" % (Connection2.Ui_Dialog2.ip_add), port="5432")
                cur = conn.cursor()
                cur.execute("UPDATE \"{0}\" SET SECA = {2},SECB = {3},SECC = {4},SECD = {5} WHERE DATE =\'{1}\'".format(self.this_month,col1,col2,col3,col4,col5))
                ##Key error will be rised if "Where DATE = {self.this_month} is not used
                print("UPDATED", row)
                conn.commit()
                conn.close()


