# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 457)
        MainWindow.setStyleSheet("")
        self.informationTabWidget = QtWidgets.QTabWidget(MainWindow)
        self.informationTabWidget.setGeometry(QtCore.QRect(310, 70, 311, 331))
        self.informationTabWidget.setMouseTracking(False)
        self.informationTabWidget.setAutoFillBackground(True)
        self.informationTabWidget.setStyleSheet("")
        self.informationTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.informationTabWidget.setObjectName("informationTabWidget")
        self.mode_tab = QtWidgets.QWidget()
        self.mode_tab.setObjectName("mode_tab")
        self.label_8 = QtWidgets.QLabel(self.mode_tab)
        self.label_8.setGeometry(QtCore.QRect(120, 10, 81, 41))
        self.label_8.setStyleSheet("background-color: red;")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.mode_tab)
        self.label_9.setGeometry(QtCore.QRect(120, 60, 81, 41))
        self.label_9.setStyleSheet("background-color:  green;")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.mode_tab)
        self.label_10.setGeometry(QtCore.QRect(120, 110, 81, 41))
        self.label_10.setStyleSheet("background-color: orange;")
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.mode_tab)
        self.label_11.setGeometry(QtCore.QRect(120, 160, 81, 41))
        self.label_11.setStyleSheet("background-color: yellow;")
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.mode_tab)
        self.label_12.setGeometry(QtCore.QRect(120, 210, 81, 41))
        self.label_12.setStyleSheet("background-color: beige;")
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.mode_tab)
        self.label_13.setGeometry(QtCore.QRect(120, 260, 81, 41))
        self.label_13.setStyleSheet("background-color: white;")
        self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.informationTabWidget.addTab(self.mode_tab, "")
        self.battery_tab = QtWidgets.QWidget()
        self.battery_tab.setObjectName("battery_tab")
        self.label_4 = QtWidgets.QLabel(self.battery_tab)
        self.label_4.setGeometry(QtCore.QRect(130, 10, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.battery_tab)
        self.label_7.setGeometry(QtCore.QRect(130, 150, 61, 16))
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.battery_tab)
        self.tableWidget.setGeometry(QtCore.QRect(70, 30, 181, 91))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(2, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.battery_tab)
        self.tableWidget_2.setGeometry(QtCore.QRect(70, 170, 181, 91))
        self.tableWidget_2.setAutoScroll(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(2, 0, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.informationTabWidget.addTab(self.battery_tab, "")
        self.misc_tab = QtWidgets.QWidget()
        self.misc_tab.setObjectName("misc_tab")
        self.batteryBar = QtWidgets.QProgressBar(self.misc_tab)
        self.batteryBar.setGeometry(QtCore.QRect(140, 50, 95, 20))
        self.batteryBar.setProperty("value", 75)
        self.batteryBar.setOrientation(QtCore.Qt.Horizontal)
        self.batteryBar.setInvertedAppearance(False)
        self.batteryBar.setObjectName("batteryBar")
        self.batteryLabel = QtWidgets.QLabel(self.misc_tab)
        self.batteryLabel.setGeometry(QtCore.QRect(83, 51, 49, 16))
        self.batteryLabel.setObjectName("batteryLabel")
        self.batteryLabel_2 = QtWidgets.QLabel(self.misc_tab)
        self.batteryLabel_2.setGeometry(QtCore.QRect(83, 81, 49, 16))
        self.batteryLabel_2.setObjectName("batteryLabel_2")
        self.batteryBar_2 = QtWidgets.QProgressBar(self.misc_tab)
        self.batteryBar_2.setGeometry(QtCore.QRect(140, 80, 95, 20))
        self.batteryBar_2.setProperty("value", 53)
        self.batteryBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.batteryBar_2.setInvertedAppearance(False)
        self.batteryBar_2.setObjectName("batteryBar_2")
        self.batteryLabel_3 = QtWidgets.QLabel(self.misc_tab)
        self.batteryLabel_3.setGeometry(QtCore.QRect(83, 111, 49, 16))
        self.batteryLabel_3.setObjectName("batteryLabel_3")
        self.batteryBar_3 = QtWidgets.QProgressBar(self.misc_tab)
        self.batteryBar_3.setGeometry(QtCore.QRect(140, 110, 95, 20))
        self.batteryBar_3.setProperty("value", 34)
        self.batteryBar_3.setOrientation(QtCore.Qt.Horizontal)
        self.batteryBar_3.setInvertedAppearance(False)
        self.batteryBar_3.setObjectName("batteryBar_3")
        self.batteryLabel_4 = QtWidgets.QLabel(self.misc_tab)
        self.batteryLabel_4.setGeometry(QtCore.QRect(83, 141, 49, 16))
        self.batteryLabel_4.setObjectName("batteryLabel_4")
        self.batteryLabel_5 = QtWidgets.QLabel(self.misc_tab)
        self.batteryLabel_5.setGeometry(QtCore.QRect(83, 201, 49, 16))
        self.batteryLabel_5.setObjectName("batteryLabel_5")
        self.batteryBar_4 = QtWidgets.QProgressBar(self.misc_tab)
        self.batteryBar_4.setGeometry(QtCore.QRect(140, 140, 95, 20))
        self.batteryBar_4.setProperty("value", 92)
        self.batteryBar_4.setOrientation(QtCore.Qt.Horizontal)
        self.batteryBar_4.setInvertedAppearance(False)
        self.batteryBar_4.setObjectName("batteryBar_4")
        self.batteryLabel_6 = QtWidgets.QLabel(self.misc_tab)
        self.batteryLabel_6.setGeometry(QtCore.QRect(83, 171, 49, 16))
        self.batteryLabel_6.setObjectName("batteryLabel_6")
        self.batteryBar_5 = QtWidgets.QProgressBar(self.misc_tab)
        self.batteryBar_5.setGeometry(QtCore.QRect(140, 170, 95, 20))
        self.batteryBar_5.setProperty("value", 0)
        self.batteryBar_5.setOrientation(QtCore.Qt.Horizontal)
        self.batteryBar_5.setInvertedAppearance(False)
        self.batteryBar_5.setObjectName("batteryBar_5")
        self.batteryBar_6 = QtWidgets.QProgressBar(self.misc_tab)
        self.batteryBar_6.setGeometry(QtCore.QRect(140, 200, 95, 20))
        self.batteryBar_6.setProperty("value", 22)
        self.batteryBar_6.setOrientation(QtCore.Qt.Horizontal)
        self.batteryBar_6.setInvertedAppearance(False)
        self.batteryBar_6.setObjectName("batteryBar_6")
        self.informationTabWidget.addTab(self.misc_tab, "")
        self.health_test = QtWidgets.QWidget()
        self.health_test.setObjectName("health_test")
        self.healthTestButton = QtWidgets.QPushButton(self.health_test)
        self.healthTestButton.setGeometry(QtCore.QRect(90, 0, 131, 32))
        self.healthTestButton.setObjectName("healthTestButton")
        self.current_status_label_4 = QtWidgets.QLabel(self.health_test)
        self.current_status_label_4.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.current_status_label_4.setObjectName("current_status_label_4")
        self.status_label_4 = QtWidgets.QLabel(self.health_test)
        self.status_label_4.setGeometry(QtCore.QRect(100, 30, 89, 16))
        self.status_label_4.setObjectName("status_label_4")
        self.label_14 = QtWidgets.QLabel(self.health_test)
        self.label_14.setGeometry(QtCore.QRect(130, 50, 61, 16))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.health_test)
        self.tableWidget_3.setGeometry(QtCore.QRect(30, 60, 251, 211))
        self.tableWidget_3.setAutoFillBackground(False)
        self.tableWidget_3.setAutoScroll(True)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.tableWidget_3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget_3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget_3.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget_3.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(253, 128, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.tableWidget_3.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.tableWidget_3.setItem(6, 0, item)
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.informationTabWidget.addTab(self.health_test, "")
        self.navTab = QtWidgets.QWidget()
        self.navTab.setObjectName("navTab")
        self.batteryLabel_7 = QtWidgets.QLabel(self.navTab)
        self.batteryLabel_7.setGeometry(QtCore.QRect(51, 11, 101, 16))
        self.batteryLabel_7.setObjectName("batteryLabel_7")
        self.batteryBar_7 = QtWidgets.QProgressBar(self.navTab)
        self.batteryBar_7.setGeometry(QtCore.QRect(160, 10, 95, 20))
        self.batteryBar_7.setProperty("value", 53)
        self.batteryBar_7.setOrientation(QtCore.Qt.Horizontal)
        self.batteryBar_7.setInvertedAppearance(False)
        self.batteryBar_7.setObjectName("batteryBar_7")
        self.current_status_label_5 = QtWidgets.QLabel(self.navTab)
        self.current_status_label_5.setGeometry(QtCore.QRect(32, 70, 121, 16))
        self.current_status_label_5.setObjectName("current_status_label_5")
        self.status_label_5 = QtWidgets.QLabel(self.navTab)
        self.status_label_5.setGeometry(QtCore.QRect(160, 70, 121, 16))
        self.status_label_5.setStyleSheet("background-color: rgb(0,200,9)")
        self.status_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label_5.setObjectName("status_label_5")
        self.current_status_label_6 = QtWidgets.QLabel(self.navTab)
        self.current_status_label_6.setGeometry(QtCore.QRect(32, 100, 121, 16))
        self.current_status_label_6.setObjectName("current_status_label_6")
        self.status_label_6 = QtWidgets.QLabel(self.navTab)
        self.status_label_6.setGeometry(QtCore.QRect(160, 100, 121, 16))
        self.status_label_6.setStyleSheet("background-color: rgb(0,200,9)")
        self.status_label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label_6.setObjectName("status_label_6")
        self.current_status_label_7 = QtWidgets.QLabel(self.navTab)
        self.current_status_label_7.setGeometry(QtCore.QRect(32, 40, 121, 16))
        self.current_status_label_7.setObjectName("current_status_label_7")
        self.status_label_7 = QtWidgets.QLabel(self.navTab)
        self.status_label_7.setGeometry(QtCore.QRect(160, 40, 121, 16))
        self.status_label_7.setStyleSheet("background-color: rgb(0,200,9)")
        self.status_label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label_7.setObjectName("status_label_7")
        self.informationTabWidget.addTab(self.navTab, "")
        self.line = QtWidgets.QFrame(MainWindow)
        self.line.setGeometry(QtCore.QRect(30, 50, 591, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.commandLineEdit = QtWidgets.QLineEdit(MainWindow)
        self.commandLineEdit.setGeometry(QtCore.QRect(370, 420, 125, 21))
        self.commandLineEdit.setText("")
        self.commandLineEdit.setObjectName("commandLineEdit")
        self.sendCommandButton = QtWidgets.QPushButton(MainWindow)
        self.sendCommandButton.setGeometry(QtCore.QRect(497, 416, 139, 32))
        self.sendCommandButton.setObjectName("sendCommandButton")
        self.current_status_label = QtWidgets.QLabel(MainWindow)
        self.current_status_label.setGeometry(QtCore.QRect(30, 40, 92, 16))
        self.current_status_label.setObjectName("current_status_label")
        self.status_label = QtWidgets.QLabel(MainWindow)
        self.status_label.setGeometry(QtCore.QRect(130, 40, 89, 16))
        self.status_label.setObjectName("status_label")
        self.eStopButton = QtWidgets.QPushButton(MainWindow)
        self.eStopButton.setGeometry(QtCore.QRect(20, 10, 142, 32))
        self.eStopButton.setStyleSheet("eStopButton{\n"
"background-color: rgb(252, 1, 7);\n"
"}")
        self.eStopButton.setObjectName("eStopButton")
        self.logo = QtWidgets.QLabel(MainWindow)
        self.logo.setGeometry(QtCore.QRect(330, 10, 291, 41))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setObjectName("logo")
        self.cameraWidget = QtWidgets.QTabWidget(MainWindow)
        self.cameraWidget.setGeometry(QtCore.QRect(30, 70, 271, 231))
        self.cameraWidget.setObjectName("cameraWidget")
        self.frontcam_tab = QtWidgets.QWidget()
        self.frontcam_tab.setObjectName("frontcam_tab")
        self.label_5 = QtWidgets.QLabel(self.frontcam_tab)
        self.label_5.setGeometry(QtCore.QRect(70, 70, 131, 16))
        self.label_5.setObjectName("label_5")
        self.cameraWidget.addTab(self.frontcam_tab, "")
        self.rearcam_tab = QtWidgets.QWidget()
        self.rearcam_tab.setObjectName("rearcam_tab")
        self.label_6 = QtWidgets.QLabel(self.rearcam_tab)
        self.label_6.setGeometry(QtCore.QRect(70, 70, 131, 16))
        self.label_6.setObjectName("label_6")
        self.cameraWidget.addTab(self.rearcam_tab, "")
        self.current_status_label_2 = QtWidgets.QLabel(MainWindow)
        self.current_status_label_2.setGeometry(QtCore.QRect(20, 350, 161, 16))
        self.current_status_label_2.setObjectName("current_status_label_2")
        self.status_label_2 = QtWidgets.QLabel(MainWindow)
        self.status_label_2.setGeometry(QtCore.QRect(180, 350, 89, 16))
        self.status_label_2.setStyleSheet("background-color: rgb(0,200,9)")
        self.status_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label_2.setObjectName("status_label_2")
        self.current_status_label_3 = QtWidgets.QLabel(MainWindow)
        self.current_status_label_3.setGeometry(QtCore.QRect(20, 380, 161, 16))
        self.current_status_label_3.setObjectName("current_status_label_3")
        self.status_label_3 = QtWidgets.QLabel(MainWindow)
        self.status_label_3.setGeometry(QtCore.QRect(180, 380, 89, 16))
        self.status_label_3.setStyleSheet("background-color: rgb(0,191,255)")
        self.status_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label_3.setObjectName("status_label_3")

        self.retranslateUi(MainWindow)
        self.informationTabWidget.setCurrentIndex(3)
        self.cameraWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AlbertaLoop Command Centre"))
        self.label_8.setText(_translate("MainWindow", "Shutdown"))
        self.label_9.setText(_translate("MainWindow", "Launch"))
        self.label_10.setText(_translate("MainWindow", "Accelerating"))
        self.label_11.setText(_translate("MainWindow", "Slewing"))
        self.label_12.setText(_translate("MainWindow", "Soft Stop"))
        self.label_13.setText(_translate("MainWindow", "Idle"))
        self.informationTabWidget.setTabText(self.informationTabWidget.indexOf(self.mode_tab), _translate("MainWindow", "Mode"))
        self.label_4.setText(_translate("MainWindow", "Battery 1"))
        self.label_7.setText(_translate("MainWindow", "Battery 2"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Voltage"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Current"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Temperature"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "25.23 V"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "5.37 A"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "15.84 ºC"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Voltage"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Current"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Temperature"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainWindow", "18.02 V"))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("MainWindow", "1.56 A"))
        item = self.tableWidget_2.item(2, 0)
        item.setText(_translate("MainWindow", "21.78 ºC"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.informationTabWidget.setTabText(self.informationTabWidget.indexOf(self.battery_tab), _translate("MainWindow", "Battery"))
        self.batteryLabel.setText(_translate("MainWindow", "Battery:"))
        self.batteryLabel_2.setText(_translate("MainWindow", "Thing 1:"))
        self.batteryLabel_3.setText(_translate("MainWindow", "Thing 2:"))
        self.batteryLabel_4.setText(_translate("MainWindow", "Thing 3:"))
        self.batteryLabel_5.setText(_translate("MainWindow", "Thing 5:"))
        self.batteryLabel_6.setText(_translate("MainWindow", "Thing 4:"))
        self.informationTabWidget.setTabText(self.informationTabWidget.indexOf(self.misc_tab), _translate("MainWindow", "Misc."))
        self.healthTestButton.setText(_translate("MainWindow", "Start Health Test"))
        self.current_status_label_4.setText(_translate("MainWindow", "Time Elapsed:"))
        self.status_label_4.setText(_translate("MainWindow", "0 s"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Battery Voltage 1"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Battery Voltage 2"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Battery Temperature 1"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Battery Temperature 2"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Battery Capacity 1"))
        item = self.tableWidget_3.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Battery Capacity 2"))
        item = self.tableWidget_3.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Vessel Pressure"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(0, 0)
        item.setText(_translate("MainWindow", "25.23 V"))
        item = self.tableWidget_3.item(1, 0)
        item.setText(_translate("MainWindow", "18.34 V"))
        item = self.tableWidget_3.item(2, 0)
        item.setText(_translate("MainWindow", "15.84 ºC"))
        item = self.tableWidget_3.item(3, 0)
        item.setText(_translate("MainWindow", "26.75 ºC"))
        item = self.tableWidget_3.item(4, 0)
        item.setText(_translate("MainWindow", "75%"))
        item = self.tableWidget_3.item(5, 0)
        item.setText(_translate("MainWindow", "42%"))
        item = self.tableWidget_3.item(6, 0)
        item.setText(_translate("MainWindow", "117.3 kPa"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.informationTabWidget.setTabText(self.informationTabWidget.indexOf(self.health_test), _translate("MainWindow", "Health Test"))
        self.batteryLabel_7.setText(_translate("MainWindow", "Path Estimation:"))
        self.current_status_label_5.setText(_translate("MainWindow", "Telemetry Position:"))
        self.status_label_5.setText(_translate("MainWindow", "127m"))
        self.current_status_label_6.setText(_translate("MainWindow", "Telemetry Velocity:"))
        self.status_label_6.setText(_translate("MainWindow", "7.9 m/s"))
        self.current_status_label_7.setText(_translate("MainWindow", "Time Elapsed:"))
        self.status_label_7.setText(_translate("MainWindow", "23 s"))
        self.informationTabWidget.setTabText(self.informationTabWidget.indexOf(self.navTab), _translate("MainWindow", "Nav"))
        self.sendCommandButton.setText(_translate("MainWindow", "Send Command"))
        self.current_status_label.setText(_translate("MainWindow", "Current Status:"))
        self.status_label.setText(_translate("MainWindow", "No Connection"))
        self.eStopButton.setText(_translate("MainWindow", "Emergency Stop"))
        self.label_5.setText(_translate("MainWindow", "Camera footage here"))
        self.cameraWidget.setTabText(self.cameraWidget.indexOf(self.frontcam_tab), _translate("MainWindow", "Front Camera"))
        self.label_6.setText(_translate("MainWindow", "Camera footage here"))
        self.cameraWidget.setTabText(self.cameraWidget.indexOf(self.rearcam_tab), _translate("MainWindow", "Rear Camera"))
        self.current_status_label_2.setText(_translate("MainWindow", "SpaceX Telemetry Status:"))
        self.status_label_2.setText(_translate("MainWindow", "Ready"))
        self.current_status_label_3.setText(_translate("MainWindow", "FSM state:"))
        self.status_label_3.setText(_translate("MainWindow", "Launch"))

app = QApplication(sys.argv)
window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
