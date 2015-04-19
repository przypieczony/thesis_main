# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Sun Apr 19 22:22:47 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket
import random
import sys
import os
import string
import cStringIO
import time
import threading
from sniff import *
import pickle



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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        self.template_vars = {}
        self.templates = {}
        self.message_counter = -1
        self.thread = None
        self.thread_popup = None
        self.scenario = []
        self.ip_addresses = []
        self.ports = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(850, 635)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Inputdata = QtGui.QWidget()
        self.Inputdata.setObjectName(_fromUtf8("Inputdata"))
        self.simulateRadioButton = QtGui.QRadioButton(self.Inputdata)
        self.simulateRadioButton.setEnabled(True)
        self.simulateRadioButton.setGeometry(QtCore.QRect(690, 10, 116, 22))
        self.simulateRadioButton.setStatusTip(_fromUtf8(""))
        self.simulateRadioButton.setCheckable(True)
        self.simulateRadioButton.setChecked(False)
        self.simulateRadioButton.setObjectName(_fromUtf8("simulateRadioButton"))
        self.layoutWidget = QtGui.QWidget(self.Inputdata)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 181, 444))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.sourceAddressField = QtGui.QLineEdit(self.layoutWidget)
        self.sourceAddressField.setEnabled(True)
        self.sourceAddressField.setStatusTip(_fromUtf8(""))
        self.sourceAddressField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.sourceAddressField.setFrame(True)
        self.sourceAddressField.setObjectName(_fromUtf8("sourceAddressField"))
        self.verticalLayout.addWidget(self.sourceAddressField)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.sourcePortField = QtGui.QLineEdit(self.layoutWidget)
        self.sourcePortField.setStatusTip(_fromUtf8(""))
        self.sourcePortField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.sourcePortField.setInputMask(_fromUtf8(""))
        self.sourcePortField.setObjectName(_fromUtf8("sourcePortField"))
        self.verticalLayout.addWidget(self.sourcePortField)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.destAddresField = QtGui.QLineEdit(self.layoutWidget)
        self.destAddresField.setStatusTip(_fromUtf8(""))
        self.destAddresField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.destAddresField.setInputMask(_fromUtf8(""))
        self.destAddresField.setObjectName(_fromUtf8("destAddresField"))
        self.verticalLayout.addWidget(self.destAddresField)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.destPortField = QtGui.QLineEdit(self.layoutWidget)
        self.destPortField.setStatusTip(_fromUtf8(""))
        self.destPortField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.destPortField.setInputMask(_fromUtf8(""))
        self.destPortField.setObjectName(_fromUtf8("destPortField"))
        self.verticalLayout.addWidget(self.destPortField)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.proxyOneAddresField = QtGui.QLineEdit(self.layoutWidget)
        self.proxyOneAddresField.setStatusTip(_fromUtf8(""))
        self.proxyOneAddresField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.proxyOneAddresField.setInputMask(_fromUtf8(""))
        self.proxyOneAddresField.setObjectName(_fromUtf8("proxyOneAddresField"))
        self.verticalLayout.addWidget(self.proxyOneAddresField)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.proxyOnePortField = QtGui.QLineEdit(self.layoutWidget)
        self.proxyOnePortField.setStatusTip(_fromUtf8(""))
        self.proxyOnePortField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.proxyOnePortField.setInputMask(_fromUtf8(""))
        self.proxyOnePortField.setObjectName(_fromUtf8("proxyOnePortField"))
        self.verticalLayout.addWidget(self.proxyOnePortField)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.proxyTwoAddresField = QtGui.QLineEdit(self.layoutWidget)
        self.proxyTwoAddresField.setStatusTip(_fromUtf8(""))
        self.proxyTwoAddresField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.proxyTwoAddresField.setInputMask(_fromUtf8(""))
        self.proxyTwoAddresField.setObjectName(_fromUtf8("proxyTwoAddresField"))
        self.verticalLayout.addWidget(self.proxyTwoAddresField)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.proxyTwoPortField = QtGui.QLineEdit(self.layoutWidget)
        self.proxyTwoPortField.setStatusTip(_fromUtf8(""))
        self.proxyTwoPortField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.proxyTwoPortField.setInputMask(_fromUtf8(""))
        self.proxyTwoPortField.setObjectName(_fromUtf8("proxyTwoPortField"))
        self.verticalLayout.addWidget(self.proxyTwoPortField)
        self.layoutWidget1 = QtGui.QWidget(self.Inputdata)
        self.layoutWidget1.setGeometry(QtCore.QRect(590, 470, 211, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clearButton = QtGui.QPushButton(self.layoutWidget1)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.acceptButton = QtGui.QPushButton(self.layoutWidget1)
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.horizontalLayout.addWidget(self.acceptButton)
        self.splitter = QtGui.QSplitter(self.Inputdata)
        self.splitter.setGeometry(QtCore.QRect(320, 50, 441, 291))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_5 = QtGui.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.sipTemplate = QtGui.QTextEdit(self.splitter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        self.sipTemplate.setFont(font)
        self.sipTemplate.setReadOnly(True)
        self.sipTemplate.setObjectName(_fromUtf8("sipTemplate"))
        self.layoutWidget2 = QtGui.QWidget(self.Inputdata)
        self.layoutWidget2.setGeometry(QtCore.QRect(260, 360, 221, 108))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_16 = QtGui.QLabel(self.layoutWidget2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 0, 0, 1, 1)
        self.senderField = QtGui.QLineEdit(self.layoutWidget2)
        self.senderField.setStatusTip(_fromUtf8(""))
        self.senderField.setInputMask(_fromUtf8(""))
        self.senderField.setObjectName(_fromUtf8("senderField"))
        self.gridLayout_2.addWidget(self.senderField, 1, 0, 1, 1)
        self.receiverField = QtGui.QLineEdit(self.layoutWidget2)
        self.receiverField.setStatusTip(_fromUtf8(""))
        self.receiverField.setInputMask(_fromUtf8(""))
        self.receiverField.setObjectName(_fromUtf8("receiverField"))
        self.gridLayout_2.addWidget(self.receiverField, 3, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.layoutWidget2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.Inputdata)
        self.label_18.setGeometry(QtCore.QRect(10, 500, 240, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.tabWidget.addTab(self.Inputdata, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(30, 310, 401, 221))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.layoutWidget3 = QtGui.QWidget(self.frame)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 10, 381, 171))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.sourceAddresBox = QtGui.QComboBox(self.layoutWidget3)
        self.sourceAddresBox.setObjectName(_fromUtf8("sourceAddresBox"))
        self.gridLayout_3.addWidget(self.sourceAddresBox, 1, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.layoutWidget3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 2, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.chooseTemplateButton = QtGui.QPushButton(self.layoutWidget3)
        self.chooseTemplateButton.setObjectName(_fromUtf8("chooseTemplateButton"))
        self.gridLayout_3.addWidget(self.chooseTemplateButton, 5, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.templatePathField = QtGui.QLineEdit(self.layoutWidget3)
        self.templatePathField.setEnabled(True)
        self.templatePathField.setStatusTip(_fromUtf8(""))
        self.templatePathField.setInputMethodHints(QtCore.Qt.ImhNone)
        self.templatePathField.setInputMask(_fromUtf8(""))
        self.templatePathField.setText(_fromUtf8(""))
        self.templatePathField.setFrame(True)
        self.templatePathField.setReadOnly(False)
        self.templatePathField.setPlaceholderText(_fromUtf8(""))
        self.templatePathField.setObjectName(_fromUtf8("templatePathField"))
        self.gridLayout_3.addWidget(self.templatePathField, 5, 0, 1, 1)
        self.sourcePortBox = QtGui.QComboBox(self.layoutWidget3)
        self.sourcePortBox.setObjectName(_fromUtf8("sourcePortBox"))
        self.gridLayout_3.addWidget(self.sourcePortBox, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.layoutWidget3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)
        self.destPortBox = QtGui.QComboBox(self.layoutWidget3)
        self.destPortBox.setObjectName(_fromUtf8("destPortBox"))
        self.gridLayout_3.addWidget(self.destPortBox, 3, 1, 1, 1)
        self.destAddressBox = QtGui.QComboBox(self.layoutWidget3)
        self.destAddressBox.setObjectName(_fromUtf8("destAddressBox"))
        self.gridLayout_3.addWidget(self.destAddressBox, 3, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.layoutWidget3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(10, 190, 240, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.scenarioField = QtGui.QTextEdit(self.tab)
        self.scenarioField.setGeometry(QtCore.QRect(30, 30, 771, 251))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        self.scenarioField.setFont(font)
        self.scenarioField.setReadOnly(True)
        self.scenarioField.setObjectName(_fromUtf8("scenarioField"))
        self.layoutWidget4 = QtGui.QWidget(self.tab)
        self.layoutWidget4.setGeometry(QtCore.QRect(690, 410, 124, 121))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.layoutWidget4)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.loadScenarioButton = QtGui.QPushButton(self.layoutWidget4)
        self.loadScenarioButton.setObjectName(_fromUtf8("loadScenarioButton"))
        self.gridLayout_4.addWidget(self.loadScenarioButton, 0, 0, 1, 1)
        self.CreateScenarioButton = QtGui.QPushButton(self.layoutWidget4)
        self.CreateScenarioButton.setObjectName(_fromUtf8("CreateScenarioButton"))
        self.gridLayout_4.addWidget(self.CreateScenarioButton, 1, 0, 1, 1)
        self.clearCreateScenarioButton = QtGui.QPushButton(self.layoutWidget4)
        self.clearCreateScenarioButton.setObjectName(_fromUtf8("clearCreateScenarioButton"))
        self.gridLayout_4.addWidget(self.clearCreateScenarioButton, 2, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(340, 280, 240, 19))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(450, 390, 189, 62))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_7 = QtGui.QGridLayout(self.widget)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.addCaseButton = QtGui.QPushButton(self.widget)
        self.addCaseButton.setEnabled(False)
        self.addCaseButton.setObjectName(_fromUtf8("addCaseButton"))
        self.gridLayout_7.addWidget(self.addCaseButton, 0, 0, 1, 1)
        self.removeCaseButton = QtGui.QPushButton(self.widget)
        self.removeCaseButton.setObjectName(_fromUtf8("removeCaseButton"))
        self.gridLayout_7.addWidget(self.removeCaseButton, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.Simulation = QtGui.QWidget()
        self.Simulation.setObjectName(_fromUtf8("Simulation"))
        self.flowField = QtGui.QTextEdit(self.Simulation)
        self.flowField.setGeometry(QtCore.QRect(10, 120, 811, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.flowField.setFont(font)
        self.flowField.setReadOnly(True)
        self.flowField.setObjectName(_fromUtf8("flowField"))
        self.splitter_2 = QtGui.QSplitter(self.Simulation)
        self.splitter_2.setGeometry(QtCore.QRect(20, 280, 381, 241))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.labelCurrentMessage = QtGui.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setItalic(True)
        self.labelCurrentMessage.setFont(font)
        self.labelCurrentMessage.setObjectName(_fromUtf8("labelCurrentMessage"))
        self.currentMessageField = QtGui.QTextEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(9)
        self.currentMessageField.setFont(font)
        self.currentMessageField.setReadOnly(True)
        self.currentMessageField.setObjectName(_fromUtf8("currentMessageField"))
        self.layoutWidget5 = QtGui.QWidget(self.Simulation)
        self.layoutWidget5.setGeometry(QtCore.QRect(680, 380, 131, 151))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.gridLayout_5 = QtGui.QGridLayout(self.layoutWidget5)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.previousButton = QtGui.QPushButton(self.layoutWidget5)
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.gridLayout_5.addWidget(self.previousButton, 0, 0, 1, 1)
        self.nextButton = QtGui.QPushButton(self.layoutWidget5)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.gridLayout_5.addWidget(self.nextButton, 1, 0, 1, 1)
        self.simulateButton = QtGui.QPushButton(self.layoutWidget5)
        self.simulateButton.setObjectName(_fromUtf8("simulateButton"))
        self.gridLayout_5.addWidget(self.simulateButton, 2, 0, 1, 1)
        self.clearSimulationButton = QtGui.QPushButton(self.layoutWidget5)
        self.clearSimulationButton.setObjectName(_fromUtf8("clearSimulationButton"))
        self.gridLayout_5.addWidget(self.clearSimulationButton, 3, 0, 1, 1)
        self.layoutWidget6 = QtGui.QWidget(self.Simulation)
        self.layoutWidget6.setGeometry(QtCore.QRect(0, 10, 821, 105))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.gridLayout_6 = QtGui.QGridLayout(self.layoutWidget6)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 3, 1, 1)
        self.destHW = QtGui.QLineEdit(self.layoutWidget6)
        self.destHW.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.destHW.setFont(font)
        self.destHW.setStatusTip(_fromUtf8(""))
        self.destHW.setInputMethodHints(QtCore.Qt.ImhNone)
        self.destHW.setInputMask(_fromUtf8(""))
        self.destHW.setText(_fromUtf8(""))
        self.destHW.setFrame(True)
        self.destHW.setReadOnly(False)
        self.destHW.setPlaceholderText(_fromUtf8(""))
        self.destHW.setObjectName(_fromUtf8("destHW"))
        self.gridLayout_6.addWidget(self.destHW, 0, 6, 1, 1)
        self.sourceHW = QtGui.QLineEdit(self.layoutWidget6)
        self.sourceHW.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sourceHW.setFont(font)
        self.sourceHW.setStatusTip(_fromUtf8(""))
        self.sourceHW.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sourceHW.setInputMask(_fromUtf8(""))
        self.sourceHW.setText(_fromUtf8(""))
        self.sourceHW.setFrame(True)
        self.sourceHW.setReadOnly(False)
        self.sourceHW.setPlaceholderText(_fromUtf8(""))
        self.sourceHW.setObjectName(_fromUtf8("sourceHW"))
        self.gridLayout_6.addWidget(self.sourceHW, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 1, 1, 1)
        self.proxyOneHW = QtGui.QLineEdit(self.layoutWidget6)
        self.proxyOneHW.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.proxyOneHW.setFont(font)
        self.proxyOneHW.setStatusTip(_fromUtf8(""))
        self.proxyOneHW.setInputMethodHints(QtCore.Qt.ImhNone)
        self.proxyOneHW.setInputMask(_fromUtf8(""))
        self.proxyOneHW.setText(_fromUtf8(""))
        self.proxyOneHW.setFrame(True)
        self.proxyOneHW.setReadOnly(False)
        self.proxyOneHW.setPlaceholderText(_fromUtf8(""))
        self.proxyOneHW.setObjectName(_fromUtf8("proxyOneHW"))
        self.gridLayout_6.addWidget(self.proxyOneHW, 0, 2, 1, 1)
        self.proxyTwoHW = QtGui.QLineEdit(self.layoutWidget6)
        self.proxyTwoHW.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.proxyTwoHW.setFont(font)
        self.proxyTwoHW.setStatusTip(_fromUtf8(""))
        self.proxyTwoHW.setInputMethodHints(QtCore.Qt.ImhNone)
        self.proxyTwoHW.setInputMask(_fromUtf8(""))
        self.proxyTwoHW.setText(_fromUtf8(""))
        self.proxyTwoHW.setFrame(True)
        self.proxyTwoHW.setReadOnly(False)
        self.proxyTwoHW.setPlaceholderText(_fromUtf8(""))
        self.proxyTwoHW.setObjectName(_fromUtf8("proxyTwoHW"))
        self.gridLayout_6.addWidget(self.proxyTwoHW, 0, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 5, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.phone = QtGui.QLabel(self.layoutWidget6)
        self.phone.setText(_fromUtf8(""))
        self.phone.setPixmap(QtGui.QPixmap(_fromUtf8("img/phone.jpg")))
        self.phone.setScaledContents(True)
        self.phone.setObjectName(_fromUtf8("phone"))
        self.horizontalLayout_3.addWidget(self.phone)
        self.line_2 = QtGui.QFrame(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_3.addWidget(self.line_2)
        self.server = QtGui.QLabel(self.layoutWidget6)
        self.server.setText(_fromUtf8(""))
        self.server.setPixmap(QtGui.QPixmap(_fromUtf8("img/sip proxy server.jpg")))
        self.server.setScaledContents(True)
        self.server.setObjectName(_fromUtf8("server"))
        self.horizontalLayout_3.addWidget(self.server)
        self.line = QtGui.QFrame(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_3.addWidget(self.line)
        self.server_2 = QtGui.QLabel(self.layoutWidget6)
        self.server_2.setText(_fromUtf8(""))
        self.server_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/sip proxy server.jpg")))
        self.server_2.setScaledContents(True)
        self.server_2.setObjectName(_fromUtf8("server_2"))
        self.horizontalLayout_3.addWidget(self.server_2)
        self.line_3 = QtGui.QFrame(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_3.addWidget(self.line_3)
        self.phone_2 = QtGui.QLabel(self.layoutWidget6)
        self.phone_2.setText(_fromUtf8(""))
        self.phone_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/phone.jpg")))
        self.phone_2.setScaledContents(True)
        self.phone_2.setObjectName(_fromUtf8("phone_2"))
        self.horizontalLayout_3.addWidget(self.phone_2)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 1, 0, 1, 7)
        self.flowLabel = QtGui.QLabel(self.Simulation)
        self.flowLabel.setGeometry(QtCore.QRect(348, 280, 112, 17))
        font = QtGui.QFont()
        font.setItalic(True)
        self.flowLabel.setFont(font)
        self.flowLabel.setObjectName(_fromUtf8("flowLabel"))
        self.tabWidget.addTab(self.Simulation, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuExit = QtGui.QMenu(self.menubar)
        self.menuExit.setObjectName(_fromUtf8("menuExit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_template = QtGui.QAction(MainWindow)
        self.actionAdd_template.setObjectName(_fromUtf8("actionAdd_template"))
        self.actionAdd_scenario = QtGui.QAction(MainWindow)
        self.actionAdd_scenario.setObjectName(_fromUtf8("actionAdd_scenario"))
        self.menuFile.addAction(self.actionAdd_scenario)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.fileDialog = QtGui.QFileDialog(MainWindow)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sourceAddressField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sourcePortField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.destAddresField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.destPortField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sipTemplate.clear)
        QtCore.QObject.connect(self.clearSimulationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.currentMessageField.clear)
        QtCore.QObject.connect(self.clearSimulationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.flowField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.proxyOneAddresField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.proxyOnePortField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.proxyTwoAddresField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.proxyTwoPortField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.senderField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.receiverField.clear)
        QtCore.QObject.connect(self.clearSimulationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sourceHW.clear)
        QtCore.QObject.connect(self.clearSimulationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.proxyOneHW.clear)
        QtCore.QObject.connect(self.clearSimulationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.proxyTwoHW.clear)
        QtCore.QObject.connect(self.clearSimulationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.destHW.clear)
        QtCore.QObject.connect(self.clearCreateScenarioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.templatePathField.clear)
        QtCore.QObject.connect(self.clearCreateScenarioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.scenarioField.clear)
        self.simulateRadioButton.toggled.connect(self.simulateRadioClicked)
        self.templatePathField.textChanged.connect(self.enableAddCaseButton)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def enableAddCaseButton(self):
        if os.path.exists(self.templatePathField.text()):
            self.addCaseButton.setEnabled(True)
        else:
            self.addCaseButton.setEnabled(False)

    def simulateRadioClicked(self, enabled):
        if enabled:
            self.sourceAddressField.setEnabled(False)
            self.sourcePortField.setEnabled(False)
            self.destAddresField.setEnabled(False)
            self.destPortField.setEnabled(False)
            self.proxyOneAddresField.setEnabled(False)
            self.proxyOnePortField.setEnabled(False)
            self.proxyTwoAddresField.setEnabled(False)
            self.proxyTwoPortField.setEnabled(False)
            self.senderField.setEnabled(False)
            self.receiverField.setEnabled(False)
        else:
            self.sourceAddressField.setEnabled(True)
            self.sourcePortField.setEnabled(True)
            self.destAddresField.setEnabled(True)
            self.destPortField.setEnabled(True)
            self.proxyOneAddresField.setEnabled(True)
            self.proxyOnePortField.setEnabled(True)
            self.proxyTwoAddresField.setEnabled(True)
            self.proxyTwoPortField.setEnabled(True)
            self.senderField.setEnabled(True)
            self.receiverField.setEnabled(True)



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        MainWindow.setStatusTip(_translate("MainWindow", "Ready", None))
        self.simulateRadioButton.setText(_translate("MainWindow", "Simulation", None))
        self.label.setText(_translate("MainWindow", "Enter source address:", None))
        self.sourceAddressField.setText(_translate("MainWindow", "192.168.100.1", None))
        self.sourceAddressField.setPlaceholderText(_translate("MainWindow", "e. g.192.168.100.1", None))
        self.label_2.setText(_translate("MainWindow", "Enter source port:", None))
        self.sourcePortField.setText(_translate("MainWindow", "5060", None))
        self.sourcePortField.setPlaceholderText(_translate("MainWindow", "e.g. 5060", None))
        self.label_3.setText(_translate("MainWindow", "Enter destiantion address:", None))
        self.destAddresField.setText(_translate("MainWindow", "192.168.100.2", None))
        self.destAddresField.setPlaceholderText(_translate("MainWindow", "e. g.192.168.100.2", None))
        self.label_4.setText(_translate("MainWindow", "Enter destination port:", None))
        self.destPortField.setText(_translate("MainWindow", "5060", None))
        self.destPortField.setPlaceholderText(_translate("MainWindow", "e.g. 5060", None))
        self.label_6.setText(_translate("MainWindow", "Proxy 1 address:", None))
        self.proxyOneAddresField.setText(_translate("MainWindow", "192.168.100.3", None))
        self.proxyOneAddresField.setPlaceholderText(_translate("MainWindow", "e. g.192.168.100.3", None))
        self.label_7.setText(_translate("MainWindow", "Proxy 1 port:", None))
        self.proxyOnePortField.setText(_translate("MainWindow", "5060", None))
        self.proxyOnePortField.setPlaceholderText(_translate("MainWindow", "e.g. 5060", None))
        self.label_8.setText(_translate("MainWindow", "Proxy 2 address:", None))
        self.proxyTwoAddresField.setText(_translate("MainWindow", "192.168.100.4", None))
        self.proxyTwoAddresField.setPlaceholderText(_translate("MainWindow", "e. g.192.168.100.4", None))
        self.label_9.setText(_translate("MainWindow", "Proxy 2 port:", None))
        self.proxyTwoPortField.setText(_translate("MainWindow", "5060", None))
        self.proxyTwoPortField.setPlaceholderText(_translate("MainWindow", "e.g. 5060", None))
        self.clearButton.setText(_translate("MainWindow", "Clear", None))
        self.acceptButton.setText(_translate("MainWindow", "Accept", None))
        self.label_5.setText(_translate("MainWindow", "Saved parameters", None))
        self.label_16.setText(_translate("MainWindow", "Sender:", None))
        self.senderField.setText(_translate("MainWindow", "kamszy", None))
        self.senderField.setPlaceholderText(_translate("MainWindow", "Enter sender name", None))
        self.receiverField.setText(_translate("MainWindow", "revszy", None))
        self.receiverField.setPlaceholderText(_translate("MainWindow", "Enter receiver name", None))
        self.label_17.setText(_translate("MainWindow", "Receiver:", None))
        self.label_18.setText(_translate("MainWindow", "All fields should be filled!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inputdata), _translate("MainWindow", "Input data", None))
        self.label_13.setText(_translate("MainWindow", "Destination port:", None))
        self.label_10.setText(_translate("MainWindow", "From:", None))
        self.chooseTemplateButton.setText(_translate("MainWindow", "Choose template", None))
        self.label_11.setText(_translate("MainWindow", "To:", None))
        self.label_12.setText(_translate("MainWindow", "Source port:", None))
        self.label_14.setText(_translate("MainWindow", "Template path:", None))
        self.label_15.setText(_translate("MainWindow", "All fields should be filled!", None))
        self.loadScenarioButton.setText(_translate("MainWindow", "Load scenario", None))
        self.CreateScenarioButton.setText(_translate("MainWindow", "Save scenario", None))
        self.clearCreateScenarioButton.setText(_translate("MainWindow", "Clear", None))
        self.label_19.setText(_translate("MainWindow", "Scenario stack", None))
        self.addCaseButton.setText(_translate("MainWindow", "Add template to scenario", None))
        self.removeCaseButton.setText(_translate("MainWindow", "Remove last template", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Create Scenario", None))
        self.labelCurrentMessage.setText(_translate("MainWindow", "Current message", None))
        self.previousButton.setText(_translate("MainWindow", "Previous", None))
        self.nextButton.setText(_translate("MainWindow", "Next", None))
        self.simulateButton.setText(_translate("MainWindow", "Simulate", None))
        self.clearSimulationButton.setText(_translate("MainWindow", "Clear", None))
        self.flowLabel.setText(_translate("MainWindow", "Connection flow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Simulation), _translate("MainWindow", "Simulation", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuExit.setTitle(_translate("MainWindow", "Exit", None))
        self.actionAdd_template.setText(_translate("MainWindow", "Add template", None))
        self.actionAdd_scenario.setText(_translate("MainWindow", "Add scenario", None))

        self.acceptButton.clicked.connect(self.getParameters)
        self.simulateButton.clicked.connect(self.loadTemplate)
        self.simulateButton.clicked.connect(self.startSniff)
        self.nextButton.clicked.connect(self.next)
        self.previousButton.clicked.connect(self.previous)
        self.clearSimulationButton.clicked.connect(self.reset)
        self.chooseTemplateButton.clicked.connect(self.getTemplate)
        self.addCaseButton.clicked.connect(self.addTemplateToScenario)
        self.removeCaseButton.clicked.connect(self.removeTemplateFromScenario)
        self.CreateScenarioButton.clicked.connect(self.createScenario)
        self.loadScenarioButton.clicked.connect(self.loadScenario)
 

    def getParameters(self):
        """This function captures input parameters and shows message template"""
 
        self.sourceAddress = str(self.sourceAddressField.text())
        self.destAddress = str(self.destAddresField.text())
        self.proxyOneAddress = str(self.proxyOneAddresField.text())
        self.proxyTwoAddress = str(self.proxyTwoAddresField.text())
        self.proxyOnePort = str(self.proxyOnePortField.text())
        self.proxyTwoPort = str(self.proxyTwoPortField.text())
        self.senderName = str(self.senderField.text())
        self.receiverName = str(self.receiverField.text())

        if self.sourceAddress != self.destAddress:
            try:
                socket.inet_aton(self.sourceAddress)
                socket.inet_aton(self.destAddress)
            except socket.error:
                self.statusbar.showMessage('Error! Wrong ip address')
        else:
            self.statusbar.showMessage('Error! ip addresses are the same')
        try:
            self.sourcePort = int(self.sourcePortField.text())
            self.destPort = int(self.destPortField.text())
        except ValueError:
            self.statusbar.showMessage('Error! Empty port number, choose between 1024-65535')
        if (self.sourcePort < 1024 or self.sourcePort > 65535) or \
            (self.destPort < 1024 or self.destPort > 65535):
            self.statusbar.showMessage('Error! Wrong port number, choose between 1024-65535')
 
        if self.simulateRadioButton.isChecked():
            self.sourceAddress = self.randomLoopback()
            self.proxyOneAddress = self.randomLoopback()
            self.proxyTwoAddress = self.randomLoopback()
            self.destAddress = "127.0.0.1"
            self.sourcePort = random.randint(1024, 65535)
            self.destPort = random.randint(1024, 65535)
            self.proxyOnePort = random.randint(1024, 65535)
            self.proxyTwoPort = random.randint(1024, 65535)

        self.template_vars = {
        "source_ip": self.sourceAddress,
        "source_port": self.sourcePort,
        "dest_ip": self.destAddress,
        "dest_port": self.destPort,
        "proxy_one_address": self.proxyOneAddress,
        "proxy_one_port": self.proxyOnePort,
        "proxy_two_address": self.proxyTwoAddress,
        "proxy_two_port": self.proxyTwoPort,
        "user": "kamszy", #To replace by value inputed by user
        "callid": ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6)),
        "seq": 0,
        "cseq":0, #temp var
        "from": self.senderName,
        "to": self.receiverName,
        "body": "to jest tresc" #temp var
        }

        self.loadParameters()

    def randomLoopback(self):
        """Return ip address 127.{}.{}.{} """
        return "127.{}.{}.{}".format(random.randint(1,255), \
                random.randint(1,255), random.randint(1,255))

    def loadParameters(self):
        """ """
        try:
            self.ip_addresses = (self.template_vars["source_ip"], self.template_vars["proxy_one_address"], \
                self.template_vars["proxy_two_address"], self.template_vars["dest_ip"])
            self.ports = (str(self.template_vars["source_port"]), str(self.template_vars["proxy_one_port"]), \
                str(self.template_vars["proxy_two_port"]), str(self.template_vars["dest_port"]))
        except Exception, e:
            PopupDialog("Some of the paramters are missing in template: {}".format(e), "Whopsie..")
            raise Exception, e

        self.sourceAddresBox.addItems(self.ip_addresses)
        self.destAddressBox.addItems(self.ip_addresses)
        self.sourcePortBox.addItems(self.ports)
        self.destPortBox.addItems(self.ports)
        self.sipTemplate.insertPlainText(self.printSample())
        self.sourceHW.setText(self.ip_addresses[0])
        self.proxyOneHW.setText(self.ip_addresses[1])
        self.proxyTwoHW.setText(self.ip_addresses[2])
        self.destHW.setText(self.ip_addresses[3])

    def printSample(self):
        """Method to print text into text box"""

        sample = """Source Address %(source_ip)s:%(source_port)s
        Proxy one Address: %(proxy_one_address)s:%(proxy_one_port)s
        Proxy two address: %(proxy_two_address)s:%(proxy_two_port)s
        Destiantion address: %(dest_ip)s:%(dest_port)s
        Sender: %(from)s
        Receiver: %(to)s
        """
        try:
            ret = sample % self.template_vars #replaces %(<variable>)s by template_vars
        except Exception, e:
            PopupDialog("Some paramters are missing in template: {}".format(e), "Whopsie..")
            raise Exception, e
        PopupDialog("Parameters Saved", "All good")
        return ret


    def loadTemplate(self):
        """Gets file path to template file, renders it and returns string"""
        i=0
        for template in self.scenario:
            try:
                with open(template["path"], 'r') as template_file:
                    clean_template = template_file.read()
            except Exception, e:
                self.statusbar.showMessage('Error! RROR: cannot open file {}, {}'.format(template_path, e))

            template["message"] = clean_template % self.template_vars #replaces %(<variable>)s by template_vars

            self.scenario.pop(i)
            i+=1
            self.scenario.insert(0, template)
        self.scenario.reverse()

    def startScenario(self):
        """Start scenario according to messages in current scenario"""
        for req, request in self.generateRequest():
            self.send(req, request)

    def previous(self):
        """ """
        if self.message_counter > 0:
            self.currentMessageField.clear()
            self.message_counter -= 1
            print "message counter: {}\nlength: {}".format(self.message_counter, len(self.scenario))
            req, request = self.generateRequest(self.scenario[self.message_counter])
            self.send(req, request)
        else:
            self.statusbar.showMessage('It is first message to display')

    def next(self):
        """ """
        if self.message_counter < len(self.scenario)-1:
            self.currentMessageField.clear()
            self.message_counter += 1
            print "message counter: {}\nlength: {}".format(self.message_counter, len(self.scenario))
            req, request = self.generateRequest(self.scenario[self.message_counter])
            self.send(req, request)
        else:
            self.statusbar.showMessage('There is no more messages to send')

    def generateRequest(self, request):
        """Generates request message"""

        self.template_vars["seq"] = self.message_counter
        try:
            req = Request(request["message"])
        except SipUnpackError, e:
            self.statusbar.showMessage("ERROR: malformed SIP Request. {}".format(e))
        
        req.headers["content-length"] = len(req.body)
        req.headers["cseq"] = "%d %s" % (self.message_counter, req.method)
    
        return req, request

    def send(self, sip_req, request):
        """ """
        try:
            self.sending_sock = self.open_sock(request["source_ip"], int(request["source_port"]))
            self.sending_sock.sendto(str(sip_req),(request["dest_ip"], int(request["dest_port"])))
        except Exception, e:
            self.statusbar.showMessage('Error! cannot send packet to {}:{}. {}'.format(request["dest_ip"], request["dest_port"], e))
        self.currentMessageField.insertPlainText("sent Request %s from: \"%s\" to: \"%s:%s\" cseq=%s len=%s\n" % (sip_req.method, request["source_ip"], request['dest_ip'], request["dest_port"], sip_req.headers['cseq'].split()[0], len(str(sip_req))))

        self.currentMessageField.insertPlainText("\n=== Full Request sent ===\n")
        self.currentMessageField.insertPlainText("%s\n" % sip_req)

    def open_sock(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            sock.setblocking(0)
        except Exception, e:
            sys.stderr.write("ERROR: cannot create socket. %s\n" % e)
            sys.exit(-1)
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except AttributeError, e:
            pass

        sock.bind((ip, port))
        sock.settimeout(10)
        return sock

    def reset(self):
        print "CLEARED"
        self.scenario = []
        self.message_counter = -1
        try:
            closeConnection()
        except Exception as e:
            print "Exception", e
        self.thread.stop()
        self.thread.join()

        print "Closed all threads"

    def startSniff(self):
        self.thread = Sniff(self.ip_addresses, self.flowField)
        self.thread.start()

    def addTemplateToScenario(self):
        """ """
        template_path = str(self.templatePathField.text())
        self.scenario.append(
            {"source_ip": str(self.sourceAddresBox.currentText()), \
            "source_port": str(self.sourcePortBox.currentText()), \
            "dest_ip": str(self.destAddressBox.currentText()), \
            "dest_port": str(self.destPortBox.currentText()), \
            "path": template_path}
            )
        self.scenarioField.clear()
        self.scenarioField.insertPlainText(self.formatedScenario())

    def removeTemplateFromScenario(self):
        """ """
        self.scenario.pop(-1)
        self.scenarioField.clear()
        self.scenarioField.insertPlainText(self.formatedScenario())

    def getTemplate(self):
        """ """
        template = IO(show_path=self.templatePathField)
        template_data, filename = template.loadFile()

    def createScenario(self):
        """ """
        self.scenario.insert(0, self.template_vars)
        scenario = Scenario(self.scenario)
        filename = scenario.create()
        self.statusbar.showMessage("Saved scenario to: {}".format(str(filename)))

    def loadScenario(self):
        """ """
        scenario = Scenario()
        try:
            self.scenario, filename = scenario.load()
            self.template_vars = self.scenario.pop(0)
        except Exception, e:
            PopupDialog("Something went wrong during scenario importing, propably file is corrupted.", "Whopsie.." )
            return
        self.loadParameters()
        self.scenarioField.clear()
        self.scenarioField.insertPlainText(str(self.scenario))
        PopupDialog("Scenario \"{0}\" loaded properly. Go to the {0} tab now.".format(os.path.basename(filename)), "Success :)" )
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Simulation), _translate("MainWindow", os.path.basename(filename), None))

    def formatedScenario(self):
        formated = ""
        for template in self.scenario:
            formated += "{source_ip:s} : {source_port:s}  ------->  {dest_ip:s} : {dest_port:s}\nContent: {path:s}\n".format(**template)
            formated += "{:-^80}\n".format("")
        return formated


class IO(QtGui.QFileDialog):
    """ """
    def __init__(self, show_path=None):
        QtGui.QFileDialog.__init__(self)
        self.show_path = show_path

    def loadFile(self):
        """ """
        filename = self.getOpenFileName(self, 'Open File', '.')
        if self.show_path:
            self.show_path.setText(filename)
        with open(str(filename)) as fname:
            content = fname.read()
        return content, str(filename)

    def saveFile(self, content):
        """ """
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.')
        if self.show_path:
            self.show_path.setText(filename)
        with open(str(filename), 'w') as fname:
            fname.wirte(content)
        return filename

    def saveToPickle(self, content):
        """ """
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.')
        if self.show_path:
            self.show_path.setText(filename)
        with open(str(filename), 'w') as fname:
            pickle.dump(content, fname)
        return filename

    def loadFromPickle(self):
        """ """
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        if self.show_path:
            self.show_path.setText(filename)
        with open(str(filename)) as fname:
            content = pickle.load(fname)
        return content, str(filename)


class Scenario(IO):
    """ """
    def __init__(self, scenario=None):
        IO.__init__(self)
        self.scenario = scenario

    def create(self):
        """ """
        return super(Scenario, self).saveToPickle(self.scenario)

    def load(self):
        """ """
        return super(Scenario, self).loadFromPickle()


class PopupDialog(QtGui.QMessageBox):

    def __init__(self, message, title=""):
        QtGui.QMessageBox.__init__(self)
        self.title = title
        self.message = message
        self.show()

    def show(self):
        dialog = QtGui.QMessageBox.information(self, self.title, self.message, buttons = QtGui.QMessageBox.Ok)


class Sniff(threading.Thread):

    def __init__(self, ip_addresses, flowField):
        threading.Thread.__init__(self)
        self.ip_addresses = ip_addresses
        self.flowField = flowField
        self.doSniff = True

    def run(self):
        print "Starting..."
        while self.doSniff:
            sniff_results=sniff('UDP', self.ip_addresses)
            if sniff_results:
                self.flowField.insertPlainText(sniff_results['graph'])

    def stop(self):
        self.doSniff = False


def canon_header(s):
    exception    = {'call-id':'Call-ID','cseq':'CSeq','www-authenticate':'WWW-Authenticate'}
    short        = ['allow-events', 'u', 'call-id', 'i', 'contact', 'm', 'content-encoding', 'e', 'content-length', 'l', 'content-type', 'c', 'event', 'o', 'from', 'f', 'subject', 's', 'supported', 'k', 'to', 't', 'via', 'v']
    s = s.lower()
    return ((len(s)==1) and s in short and canon_header(short[short.index(s)-1])) \
        or (s in exception and exception[s]) or '-'.join([x.capitalize() for x in s.split('-')])

def parse_headers(f):
    """Return dict of HTTP headers parsed from a file object."""
    d = {}
    while 1:
        line = f.readline()
        line = line.strip()
        if not line:
            break
        l = line.split(None, 1)
        if not l[0].endswith(':'):
            raise SipUnpackError('invalid header: %r' % line)
        k = l[0][:-1].lower()
        d[k] = len(l) != 1 and l[1] or ''
    return d

def parse_body(f, headers):
    """Return SIP body parsed from a file object, given HTTP header dict."""
    if 'content-length' in headers:
        n = int(headers['content-length'])
        body = f.read(n)
        if len(body) != n:
            raise SipNeedData('short body (missing %d bytes)' % (n - len(body)))
    elif 'content-type' in headers:
        body = f.read()
    else:
        body = ''
    return body


class Message:
    """SIP Protocol headers + body."""
    __metaclass__ = type
    __hdr_defaults__ = {}
    headers = None
    body = None
    
    def __init__(self, *args, **kwargs):
        if args:
            self.unpack(args[0])
        else:
            self.headers = {}
            self.body = ''
            for k, v in self.__hdr_defaults__.iteritems():
                setattr(self, k, v)
            for k, v in kwargs.iteritems():
                setattr(self, k, v)

    
    def unpack(self, buf):
        f = cStringIO.StringIO(buf)
        # Parse headers
        self.headers = parse_headers(f)
        # Parse body
        self.body = parse_body(f, self.headers)
        # Save the rest
        self.data = f.read()

    def pack_hdr(self):
        return ''.join([ '%s: %s\r\n' % (canon_header(k),v) for k,v in self.headers.iteritems() ])
    
    def __len__(self):
        return len(str(self))
    
    def __str__(self):
        return '%s\r\n%s' % (self.pack_hdr(), self.body)

class SipError(Exception): pass
class SipUnpackError(SipError): pass
class SipNeedData(SipUnpackError): pass
class SipPackError(SipError): pass

class Request(Message):
    """SIP request."""
    __hdr_defaults__ = {
        'method':'INVITE',
        'uri':'sip:user@example.com',
        'version':'2.0',
        'headers':{ 'to':'', 'from':'', 'call-id':'', 'cseq':'', 'contact':'' }
        }
    __methods = dict.fromkeys((
        'ACK', 'BYE', 'CANCEL', 'INFO', 'INVITE', 'MESSAGE', 'NOTIFY',
        'OPTIONS', 'PRACK', 'PUBLISH', 'REFER', 'REGISTER', 'SUBSCRIBE',
        'UPDATE'
        ))
    __proto = 'SIP'

    def unpack(self, buf):
        f = cStringIO.StringIO(buf)
        line = f.readline()
        l = line.strip().split()
        if len(l) != 3 or l[0] not in self.__methods or \
            not l[2].startswith(self.__proto):
            raise SipUnpackError('invalid request: %r' % line)
        self.method = l[0]
        self.uri = l[1]
        self.version = l[2][len(self.__proto)+1:]
        Message.unpack(self, f.read())
    
    def __str__(self):
        return '%s %s %s/%s\r\n' % (self.method, self.uri, self.__proto,
                                    self.version) + Message.__str__(self)

if __name__ == "__main__":
#try:
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
#except BaseException:
    #raw_input("Ups.. Something unexpected happened, press any key to shutdown...")
    sys.exit(app.exec_())

