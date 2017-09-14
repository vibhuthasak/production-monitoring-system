from PyQt4 import QtCore, QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random
import matplotlib
import psycopg2
import sys
from DisplayModel2 import Ui_MainWindow
import datetime
import matplotlib.style as style
import DisplayModel2
import numpy as np
import rersource_rc

style.use('ggplot')

class MyMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.figure = plt.figure("SectionAFig")
        self.canvas = FigureCanvas(self.figure)
        self.figure.set_facecolor(color='1')
        self.gridLayout.addWidget(self.canvas)

        self.figure2 = plt.figure("SectionBFig")
        self.canvas2 = FigureCanvas(self.figure2)
        self.figure2.set_facecolor(color='1')
        self.gridLayout_4.addWidget(self.canvas2)
        #
        self.figure3 = plt.figure("SectionCFig")
        self.canvas3 = FigureCanvas(self.figure3)
        self.figure3.set_facecolor(color='1')
        self.gridLayout_6.addWidget(self.canvas3)
        #
        self.figure4 = plt.figure("SectionDFig")
        self.canvas4 = FigureCanvas(self.figure4)
        self.figure4.set_facecolor(color='1')
        self.gridLayout_8.addWidget(self.canvas4)

        self.stackcount = 1


    # def clicked_button(self):
    #     send = self.sender()
    #     # print(send.text())
    #     if send.text() == "Section A":
    #         self.stackedWidget.setCurrentIndex(0)
    #     if send.text() == "Section B":
    #         self.stackedWidget.setCurrentIndex(1)
    #     if send.text() == "Section C":
    #         self.stackedWidget.setCurrentIndex(2)
    #     if send.text() == "Section D":
    #         self.stackedWidget.setCurrentIndex(3)

    def stackchange(self):
        print("StackCount=", self.stackcount)
        print("CurrentIndex=", self.stackedWidget.currentIndex())
        if self.stackcount > 3:
            self.stackcount = 0
        self.stackedWidget.setCurrentIndex(self.stackcount)
        self.stackcount += 1

    def graph_draw(self):

        current_index = self.stackedWidget.currentIndex()

        # if current_index == 0:
        #     print("FigA")
        #     plt.figure("SectionAFig")
        #     self.canvas.draw()
        # if current_index == 1:
        #     print("FigB")
        #     plt.figure("SectionBFig")
        #     self.canvas2.draw()
        # if current_index == 2:
        #     print("FigC")
        #     plt.figure("SectionCFig")
        #     self.canvas3.draw()
        # if current_index == 3:
        #     print("FigD")
        #     plt.figure("SectionDFig")
        #     self.canvas4.draw()


        conn = psycopg2.connect(database="plottest", user="postgres")
        print("Opened database successfully")
        cur = conn.cursor()

        ####### Varialbles Declare #######
        month_target = 0

        uptoday_month_qty_a = 0
        uptoday_month_qty_b = 0
        uptoday_month_qty_c = 0
        uptoday_month_qty_d = 0

        today_actual_qty_a = 0
        today_actual_qty_b = 0
        today_actual_qty_c = 0
        today_actual_qty_d = 0

        today_target_a = 0
        today_target_b = 0
        today_target_c = 0
        today_target_d = 0

        #####################

        today = datetime.datetime.now().date()
        today_str = str((datetime.datetime.now().date()))
        this_month_str = str((str(today.year) + "-" + str(today.month)))
        today_date = str(today.day)
        # print(this_month_str)

        cur.execute(("SELECT a,b,c,d FROM monthly Where MONTH = \'%s\' ") % this_month_str)
        rows_month_target = cur.fetchall()
        # print(rows_month_target[0])
        month_target_a = rows_month_target[0][0]
        month_target_b = rows_month_target[0][1]
        month_target_c = rows_month_target[0][2]
        month_target_d = rows_month_target[0][3]
        print("Month Target =", month_target_a, month_target_b, month_target_c, month_target_d)

        ### Today target
        cur.execute((("SELECT a,b,c,d FROM daily Where DATE = \'%s\' ") % today_str))
        rows_daily_target = cur.fetchall()

        today_target_a = rows_daily_target[0][0]
        today_target_b = rows_daily_target[0][1]
        today_target_c = rows_daily_target[0][2]
        today_target_d = rows_daily_target[0][3]

        print("today target = ", today_target_a, today_target_b, today_target_c, today_target_d)

        ## Today Production total
        cur1 = conn.cursor()
        cur1.execute((
                     "Select SUM(cast (AA as INTEGER)),SUM(cast (AB as INTEGER)),SUM(cast (AC as INTEGER)),SUM(cast (AD as INTEGER)) from \"%s\"") % today_str)  ## replace Today
        row_month_daily_all = cur1.fetchall()

        today_actual_qty_a = row_month_daily_all[0][0]
        today_actual_qty_b = row_month_daily_all[0][1]
        today_actual_qty_c = row_month_daily_all[0][2]
        today_actual_qty_d = row_month_daily_all[0][3]

        ## Today production per hour

        # cur1.execute(("SELECT COUNT(*) FROM \"%s\"")% today_str)
        # daily_row_count = cur1.fetchone()
        # print(daily_row_count[0])

        a_list = []
        a_cum = []
        b_list = []
        b_cum = []
        c_list = []
        c_cum = []
        d_list = []
        d_cum = []
        a_tot = 0
        b_tot = 0
        c_tot = 0
        d_tot = 0

        a_cum.append(0)
        b_cum.append(0)
        c_cum.append(0)
        d_cum.append(0)


        cur1.execute("SELECT AA,AB,AC,AD from \"%s\"" % today_str)
        daily_count_hbh = cur1.fetchall()
        today_row_count = len(daily_count_hbh)
        for rows in daily_count_hbh:
            a_tot += int(rows[0])
            b_tot += int(rows[1])
            c_tot += int(rows[2])
            d_tot += int(rows[3])
            a_list.append(rows[0])
            b_list.append(rows[1])
            c_list.append(rows[2])
            d_list.append(rows[3])
            a_cum.append(a_tot)
            b_cum.append(b_tot)
            c_cum.append(c_tot)
            d_cum.append(d_tot)

        a_plan_cum =[]
        a_plan_tot=0
        b_plan_cum =[]
        b_plan_tot = 0
        c_plan_cum =[]
        c_plan_tot = 0
        d_plan_cum =[]
        d_plan_tot = 0
        a_ptot = 0
        b_ptot = 0
        c_ptot = 0
        d_ptot = 0

        a_plan_cum.append(0)
        b_plan_cum.append(0)
        c_plan_cum.append(0)
        d_plan_cum.append(0)

        cur1.execute("SELECT PA,PB,PC,PD from \"%s\"" % today_str)
        daily_plan_hbh = cur1.fetchall()
        for rows in daily_plan_hbh:
            a_ptot += int(rows[0])
            b_ptot += int(rows[1])
            c_ptot += int(rows[2])
            d_ptot += int(rows[3])
            # a_list.append(rows[0])
            # b_list.append(rows[1])
            # c_list.append(rows[2])
            # d_list.append(rows[3])
            a_plan_cum.append(a_ptot)
            b_plan_cum.append(b_ptot)
            c_plan_cum.append(c_ptot)
            d_plan_cum.append(d_ptot)

        print(a_cum)
        print(b_cum)
        print(c_cum)
        print(d_cum)

        print(a_plan_cum)
        print(b_plan_cum)
        print(c_plan_cum)
        print(d_plan_cum)


        print("today actual qty = ", today_actual_qty_a, today_actual_qty_b, today_actual_qty_c, today_actual_qty_d)

        ## Calculating uptodate actual production

        for i in range(1, int(today_date)):  ## 1 to (today-1)
            date = str(this_month_str + "-" + str('%02d' % i))
            # print(date)
            cur2 = conn.cursor()
            cur2.execute((
                         "Select SUM(cast (AA as INTEGER)),SUM(cast (AB as INTEGER)),SUM(cast (AC as INTEGER)),SUM(cast (AD as INTEGER)) from \"%s\"") % date)
            row_monthly_date_by_date = cur2.fetchall()
            uptoday_month_qty_a += row_monthly_date_by_date[0][0]
            uptoday_month_qty_b += row_monthly_date_by_date[0][1]
            uptoday_month_qty_c += row_monthly_date_by_date[0][2]
            uptoday_month_qty_d += row_monthly_date_by_date[0][3]
            # remaining_qty = month_target - (uptoday_month_qty_a+uptoday_month_qty_b+uptoday_month_qty_c+uptoday_month_qty_d)
            # print(row_monthly_date_by_date)

        print("Up today Monthly Production of", this_month_str, "=", uptoday_month_qty_a, uptoday_month_qty_b,
              uptoday_month_qty_c, uptoday_month_qty_d)

        # fig = plt.figure()

        # f =plt.gcf()
        # print("current figure=", f)
        # print(self.stackedWidget.currentIndex())
        #
        # Current_fig = plt.figure("SectionCFig")

        if current_index == 0:
            print("FigA")
            # self.toolButton_4.setChecked(True)
            # self.toolButton_3.setChecked(False)
            # self.toolButton_9.setChecked(False)
            # self.toolButton_2.setChecked(False)
            plt.figure("SectionAFig")
            today_actual_qty = today_actual_qty_a
            today_target = today_target_a
            uptoday_month_qty = uptoday_month_qty_a
            cumilative = a_cum
            plancumilative = a_plan_cum
            month_target = month_target_a
            self.canvas.draw()
        if current_index == 1:
            print("FigB")
            # self.toolButton_4.setChecked(False)
            # self.toolButton_3.setChecked(True)
            # self.toolButton_9.setChecked(False)
            # self.toolButton_2.setChecked(False)
            plt.figure("SectionBFig")
            today_actual_qty = today_actual_qty_b
            today_target = today_target_b
            uptoday_month_qty = uptoday_month_qty_b
            cumilative = b_cum
            plancumilative = b_plan_cum
            month_target = month_target_b
            self.canvas2.draw()
        if current_index == 2:
            print("FigC")
            # self.toolButton_4.setChecked(False)
            # self.toolButton_3.setChecked(False)
            # self.toolButton_9.setChecked(True)
            # self.toolButton_2.setChecked(False)
            plt.figure("SectionCFig")
            today_actual_qty = today_actual_qty_c
            today_target = today_target_c
            uptoday_month_qty = uptoday_month_qty_c
            cumilative = c_cum
            plancumilative = c_plan_cum
            month_target = month_target_c
            self.canvas3.draw()
        if current_index == 3:
            print("FigD")
            # self.toolButton_4.setChecked(False)
            # self.toolButton_3.setChecked(False)
            # self.toolButton_9.setChecked(False)
            # self.toolButton_2.setChecked(True)
            plt.figure("SectionDFig")
            today_actual_qty = today_actual_qty_d
            today_target = today_target_d
            uptoday_month_qty = uptoday_month_qty_d
            cumilative = d_cum
            plancumilative = d_plan_cum
            month_target = month_target_d
            self.canvas4.draw()

        print("Today Vlaues =", today_actual_qty,today_target,uptoday_month_qty,cumilative)

##Subplot2Grid
        ax1 = plt.subplot2grid((12, 16), (0, 0), rowspan=12, colspan=12)
        ax1.set_title('Daily Production', color='k', style='normal', weight='medium')

        ax2 = plt.subplot2grid((12, 16), (0, 12), rowspan=4, colspan=4)
        ax2.set_title('Monthly Production', color='k', style='normal', weight='medium')

        ax3 = plt.subplot2grid((12, 16), (5, 12), rowspan=7, colspan=4)
        ax3.set_title('Daily Summary', color='k', style='normal', weight='medium')


        plt.subplots_adjust(right=0.18)

        plt.tight_layout()

        ###1 to 24
        y = []
        y_label = []
        target = []
        for j in range(7, 23):
            y.append(j)
            date_time = datetime.datetime.strptime((("%02d" + ":00") % j), "%H:%M")
            y_label.append(date_time)

        y_for_target =[]
        for ij in range(0,16):
            y_for_target.append(ij)

        # print(y_label)
        target = [int((elem * (today_target * (1 / 15))) + today_target / 15) for elem in y_for_target]
        print("target_plot=", target)
        #Current_fig.tight_layout()

##Plot functions
        ax1.plot(y_label, target, '--', lw=0.1, color='k')
        ax1.plot(y_label[:(today_row_count+1)], cumilative, '-', lw=4, color='#ff0000')
        ax1.plot(y_label[:(today_row_count+1)], plancumilative, '-', lw=4, color='#00ced1')

##Annotation
        # ax1.annotate("Test 1", (target[2], y_label[5]), xycoords="data",
        #                   va="center", ha="center",
        #                   bbox=dict(boxstyle="round", fc="w"))

        ax1.set_xticks(y_label)
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(30)

        xfmt = matplotlib.dates.DateFormatter('%H:%M')
        ax1.xaxis.set_major_formatter(xfmt)
        ax1.grid(True)

        # month_remain = month_target - (uptoday_month_qty_a + today_actual_qty_a)
        month_remain = month_target - (uptoday_month_qty + today_actual_qty)
        month_remain_percentage = (month_remain / month_target) * 100

        labels = 'Remaining', 'Completed'
        sizes = [(month_remain_percentage), (100 - month_remain_percentage)]
        colors = ['r', '#008000']
        explode = (0, 0)

        patches, texts, autotexts = ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                                            shadow=False, startangle=90)

        pr_ratio = int((today_actual_qty/today_target)*100)
        if pr_ratio < 25:
            bar_colors = ['#666666', 'r']
        if (pr_ratio >= 25) and (pr_ratio < 50):
            bar_colors = ['#666666', '#ff7f50']
        if (pr_ratio >= 50) and (pr_ratio < 60):
            bar_colors = ['#666666', '#ffd700']
        if (pr_ratio >= 60) and (pr_ratio < 80):
            bar_colors = ['#666666', '#00ced1']
        if (pr_ratio >= 80) and (pr_ratio < 100):
            bar_colors = ['#666666', '#008000']

        # bar_colors = ['#666666', '#008000']

        xlabels4bar =('Target', 'Completed')
        x_pos = np.arange(len(xlabels4bar))

        ax3.bar(x_pos, [today_target, today_actual_qty], color=bar_colors)
        plt.xticks(x_pos, xlabels4bar, ha='left')
        ax3.grid(True)

        today_row_count = (today_row_count+1)


        hourlyloss = (plancumilative[today_row_count - 1] - plancumilative[today_row_count - 2]) - (
        cumilative[today_row_count - 1] - cumilative[today_row_count - 2])
        print("hourlyloss=",hourlyloss)

        #

        # ##SectionA Labels
        # self.label_8.setText(FinalModel2._translate("MainWindow", str(today_target_a), None))  ##Today Target
        # self.label_9.setText(FinalModel2._translate("MainWindow", str(today_actual_qty_a) + " (" + str(
        #     int((today_actual_qty_a / today_target_a) * 100)) + "% )", None))
        # self.label_11.setText(FinalModel2._translate("MainWindow", str(month_target), None))
        # self.label_12.setText(FinalModel2._translate("MainWindow", str(uptoday_month_qty_a + today_actual_qty_a) +" (" +
        #     str(int(100 - month_remain_percentage))+"% )", None))
        # self.label_52.setText(FinalModel2._translate("MainWindow", str(month_remain), None))
        # self.label_50.setText(FinalModel2._translate("MainWindow", str(int(today_target_a-today_actual_qty_a)), None))
        # self.label_48.setText(FinalModel2._translate("MainWindow", str(cumilative[today_row_count-1]-cumilative[today_row_count -2]), None))
        # self.label_53.setText(FinalModel2._translate("MainWindow", str(cumilative[today_row_count - 1] - target[today_row_count - 1]), None))
        self.label_2.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">"+str(plancumilative[today_row_count-1]-plancumilative[today_row_count -2])+"</span></p></body></html>", None))
        self.label_4.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">"+str(cumilative[today_row_count-1]-cumilative[today_row_count -2])+"</span></p></body></html>", None))
        self.label_23.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">"+str(cumilative[today_row_count - 1] - plancumilative[today_row_count - 1])+"</span></p></body></html>", None))
        self.label_24.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">"+str(today_target)+"</span></p></body></html>", None))
        self.label_25.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">"+str(today_actual_qty)+"</span></p></body></html>", None))
        self.label_26.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">"+str(int(today_target-today_actual_qty))+"</span></p></body></html>", None))
        self.label_27.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">"+str(month_target)+"</span></p></body></html>", None))
        self.label_28.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">"+str(int(uptoday_month_qty+today_actual_qty))+"</span></p></body></html>", None))
        self.label_29.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">"+str(month_remain)+"</span></p></body></html>", None))
        self.label_31.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">"+str(hourlyloss)+"</span></p></body></html>",None))



        #
        #
        # ##SectionB Labels
        #
        # self.label_20.setText(FinalModel2._translate("MainWindow", str(today_target_b), None))  ##Today Target
        # self.label_21.setText(FinalModel2._translate("MainWindow", str(today_actual_qty_b) + " (" + str(
        #     int((today_actual_qty_b / today_target_b) * 100)) + "% )", None))
        # self.label_22.setText(FinalModel2._translate("MainWindow", str(month_target), None))
        # self.label_23.setText(
        #     FinalModel2._translate("MainWindow", str(uptoday_month_qty_b + today_actual_qty_b) + " (" +
        #                            str(int(100 - month_remain_percentage)) + "% )", None))
        # self.label_59.setText(FinalModel2._translate("MainWindow", str(month_remain), None))
        # self.label_57.setText(FinalModel2._translate("MainWindow", str(int(today_target_b - today_actual_qty_b)), None))
        # self.label_63.setText(FinalModel2._translate("MainWindow", str(cumilative[today_row_count-1]- cumilative[today_row_count -2]), None))
        # self.label_64.setText(FinalModel2._translate("MainWindow", str(cumilative[today_row_count - 1] - target[today_row_count - 1]),None))
        self.label_52.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">" + str(plancumilative[today_row_count - 1] - plancumilative[today_row_count - 2]) + "</span></p></body></html>",None))
        self.label_54.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">" + str(cumilative[today_row_count - 1] - cumilative[today_row_count - 2]) + "</span></p></body></html>",None))
        self.label_40.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(cumilative[today_row_count - 1] - plancumilative[today_row_count - 1]) + "</span></p></body></html>",None))
        self.label_41.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(today_target) + "</span></p></body></html>", None))
        self.label_42.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(today_actual_qty) + "</span></p></body></html>", None))
        self.label_43.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(int(today_target - today_actual_qty)) + "</span></p></body></html>",None))
        self.label_44.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(month_target) + "</span></p></body></html>", None))
        self.label_45.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(int(uptoday_month_qty + today_actual_qty)) + "</span></p></body></html>",None))
        self.label_46.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(month_remain) + "</span></p></body></html>", None))
        self.label_48.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" +str(hourlyloss) + "</span></p></body></html>",None))

        #
        # ##SectionC Labels
        #
        # self.label_32.setText(FinalModel2._translate("MainWindow", str(today_target_c), None))  ##Today Target
        # self.label_33.setText(FinalModel2._translate("MainWindow", str(today_actual_qty_c) + " (" + str(
        #     int((today_actual_qty_c / today_target_c) * 100)) + "% )", None))
        # self.label_34.setText(FinalModel2._translate("MainWindow", str(month_target), None))
        # self.label_35.setText(
        #     FinalModel2._translate("MainWindow", str(uptoday_month_qty_c + today_actual_qty_c) + " (" +
        #                            str(int(100 - month_remain_percentage)) + "% )", None))
        # self.label_73.setText(FinalModel2._translate("MainWindow", str(month_remain), None))
        # self.label_71.setText(FinalModel2._translate("MainWindow", str(int(today_target_c - today_actual_qty_c)), None))
        # self.label_68.setText(FinalModel2._translate("MainWindow", str(cumilative[today_row_count-1]-cumilative[today_row_count -2]), None))
        # self.label_69.setText(FinalModel2._translate("MainWindow", str(cumilative[today_row_count - 1] - target[today_row_count - 1]), None))

        self.label_62.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">" + str(plancumilative[today_row_count - 1] - plancumilative[today_row_count - 2]) + "</span></p></body></html>",None))
        self.label_64.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">" + str(cumilative[today_row_count - 1] - cumilative[today_row_count - 2]) + "</span></p></body></html>",None))
        self.label_89.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(cumilative[today_row_count - 1] - plancumilative[today_row_count - 1]) + "</span></p></body></html>",None))
        self.label_90.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(today_target) + "</span></p></body></html>", None))
        self.label_91.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(today_actual_qty) + "</span></p></body></html>", None))
        self.label_92.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(int(today_target - today_actual_qty)) + "</span></p></body></html>",None))
        self.label_93.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(month_target) + "</span></p></body></html>", None))
        self.label_94.setText(DisplayModel2._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(int(uptoday_month_qty + today_actual_qty)) + "</span></p></body></html>",None))
        self.label_95.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(month_remain) + "</span></p></body></html>", None))

        self.label_97.setText(DisplayModel2._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(hourlyloss) + "</span></p></body></html>",None))

        #
        # ##SectionD Labels
        #
        # self.label_40.setText(FinalModel2._translate("MainWindow", str(today_target_d), None))  ##Today Target
        # self.label_41.setText(FinalModel2._translate("MainWindow", str(today_actual_qty_d) + " (" + str(
        #     int((today_actual_qty_d / today_target_d) * 100)) + "% )", None))
        # self.label_45.setText(FinalModel2._translate("MainWindow", str(month_target), None))
        # self.label_46.setText(FinalModel2._translate("MainWindow", str(uptoday_month_qty_d + today_actual_qty_d) + " (" +
        #                            str(int(100 - month_remain_percentage)) + "% )", None))
        # self.label_77.setText(FinalModel2._translate("MainWindow", str(month_remain), None))
        # self.label_75.setText(FinalModel2._translate("MainWindow", str(int(today_target_d - today_actual_qty_d)), None))
        # self.label_81.setText(FinalModel2._translate("MainWindow", str(cumilative[today_row_count-1]-cumilative[today_row_count -2]), None))
        # self.label_82.setText(FinalModel2._translate("MainWindow", str(cumilative[today_row_count - 1] - target[today_row_count - 1]), None))

        self.label_72.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">" + str(plancumilative[today_row_count - 1] - plancumilative[today_row_count - 2]) + "</span></p></body></html>",None))
        self.label_74.setText(DisplayModel2._translate("MainWindow","<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">" + str(cumilative[today_row_count - 1] - cumilative[today_row_count - 2]) + "</span></p></body></html>",None))
        self.label_108.setText(DisplayModel2._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(cumilative[today_row_count - 1] - plancumilative[today_row_count - 1]) + "</span></p></body></html>",None))
        self.label_109.setText(DisplayModel2._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(today_target) + "</span></p></body></html>", None))
        self.label_110.setText(DisplayModel2._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(today_actual_qty) + "</span></p></body></html>", None))
        self.label_111.setText(DisplayModel2._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(int(today_target - today_actual_qty)) + "</span></p></body></html>",None))
        self.label_112.setText(DisplayModel2._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(month_target) + "</span></p></body></html>", None))
        self.label_113.setText(DisplayModel2._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(int(uptoday_month_qty + today_actual_qty)) + "</span></p></body></html>",None))
        self.label_114.setText(DisplayModel2._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(month_remain) + "</span></p></body></html>", None))
        self.label_116.setText(DisplayModel2._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + str(hourlyloss) + "</span></p></body></html>", None))

        # for t in texts:
        #     t.set_size('small')
        #     # print("tex=", t)
        # for t in autotexts:
        #     t.set_size('small')
        #     # print("auto =",t)
        # autotexts[0].set_color('y')

        # plt.axis('equal')
        #self.canvas.draw()

        conn.commit()
        conn.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Plastique'))
    myGUI = MyMainWindow()
    myGUI.show()
    sys.exit(app.exec_())

