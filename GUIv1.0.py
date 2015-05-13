# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Tue May  5 23:21:01 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import socket
import random
import sys
import os
import string
import time
import threading
import pickle
import cStringIO

from PyQt4 import QtCore, QtGui

from sniff import *

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
    def __init__(self, *args, **kwargs):
        super(Ui_MainWindow, self).__init__(*args, **kwargs)
        self.template_vars = {}
        self.message_counter = -1
        self.sniff_thread = None
        self.scenario = []
        self.ip_addresses = []
        self.ports = []
        self.setupUi()
        self.last_cseq = None
        self.cseq_nr = 0
        self.description_pattern = re.compile("<description>(.*)</description>", re.DOTALL | re.IGNORECASE)
        self.template_content = ""
        self.template_path = ""

    def setupUi(self):
        self.setObjectName(_fromUtf8("MainWindow"))
        self.setWindowModality(QtCore.Qt.NonModal)
        self.resize(950, 680)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(950, 680))
        self.setMaximumSize(QtCore.QSize(950, 680))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget()
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
        self.simulateRadioButton.setGeometry(QtCore.QRect(800, 20, 116, 22))
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
        self.layoutWidget1.setGeometry(QtCore.QRect(700, 520, 211, 31))
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
        self.splitter.setGeometry(QtCore.QRect(280, 40, 411, 251))
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
        self.layoutWidget2.setGeometry(QtCore.QRect(250, 400, 221, 108))
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
        self.label_45 = QtGui.QLabel(self.Inputdata)
        self.label_45.setGeometry(QtCore.QRect(580, 220, 321, 291))
        self.label_45.setText(_fromUtf8(""))
        self.label_45.setPixmap(QtGui.QPixmap(_fromUtf8("img/icon.png")))
        self.label_45.setScaledContents(True)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.tabWidget.addTab(self.Inputdata, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(30, 310, 471, 241))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.layoutWidget3 = QtGui.QWidget(self.frame)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 10, 421, 181))
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
        self.label_15.setGeometry(QtCore.QRect(20, 200, 240, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.layoutWidget4 = QtGui.QWidget(self.tab)
        self.layoutWidget4.setGeometry(QtCore.QRect(780, 440, 131, 121))
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
        self.layoutWidget5 = QtGui.QWidget(self.tab)
        self.layoutWidget5.setGeometry(QtCore.QRect(530, 400, 189, 62))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.gridLayout_7 = QtGui.QGridLayout(self.layoutWidget5)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.addCaseButton = QtGui.QPushButton(self.layoutWidget5)
        self.addCaseButton.setEnabled(False)
        self.addCaseButton.setObjectName(_fromUtf8("addCaseButton"))
        self.gridLayout_7.addWidget(self.addCaseButton, 0, 0, 1, 1)
        self.removeCaseButton = QtGui.QPushButton(self.layoutWidget5)
        self.removeCaseButton.setObjectName(_fromUtf8("removeCaseButton"))
        self.gridLayout_7.addWidget(self.removeCaseButton, 1, 0, 1, 1)
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(30, 10, 873, 276))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_17 = QtGui.QGridLayout(self.widget)
        self.gridLayout_17.setMargin(0)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.label_19 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_17.addWidget(self.label_19, 0, 0, 1, 1)
        self.scenarioField = QtGui.QTextEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scenarioField.sizePolicy().hasHeightForWidth())
        self.scenarioField.setSizePolicy(sizePolicy)
        self.scenarioField.setMinimumSize(QtCore.QSize(871, 251))
        self.scenarioField.setMaximumSize(QtCore.QSize(871, 251))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        self.scenarioField.setFont(font)
        self.scenarioField.setReadOnly(True)
        self.scenarioField.setObjectName(_fromUtf8("scenarioField"))
        self.gridLayout_17.addWidget(self.scenarioField, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.Simulation = QtGui.QWidget()
        self.Simulation.setObjectName(_fromUtf8("Simulation"))
        self.splitter_2 = QtGui.QSplitter(self.Simulation)
        self.splitter_2.setGeometry(QtCore.QRect(10, 330, 411, 231))
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
        font.setPointSize(10)
        self.currentMessageField.setFont(font)
        self.currentMessageField.setReadOnly(True)
        self.currentMessageField.setObjectName(_fromUtf8("currentMessageField"))
        self.layoutWidget6 = QtGui.QWidget(self.Simulation)
        self.layoutWidget6.setGeometry(QtCore.QRect(780, 440, 131, 121))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.gridLayout_5 = QtGui.QGridLayout(self.layoutWidget6)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.nextButton = QtGui.QPushButton(self.layoutWidget6)
        self.nextButton.setEnabled(False)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.gridLayout_5.addWidget(self.nextButton, 0, 0, 1, 1)
        self.simulateButton = QtGui.QPushButton(self.layoutWidget6)
        self.simulateButton.setObjectName(_fromUtf8("simulateButton"))
        self.gridLayout_5.addWidget(self.simulateButton, 1, 0, 1, 1)
        self.clearSimulationButton = QtGui.QPushButton(self.layoutWidget6)
        self.clearSimulationButton.setObjectName(_fromUtf8("clearSimulationButton"))
        self.gridLayout_5.addWidget(self.clearSimulationButton, 2, 0, 1, 1)
        self.layoutWidget7 = QtGui.QWidget(self.Simulation)
        self.layoutWidget7.setGeometry(QtCore.QRect(0, 10, 931, 53))
        self.layoutWidget7.setObjectName(_fromUtf8("layoutWidget7"))
        self.gridLayout_6 = QtGui.QGridLayout(self.layoutWidget7)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.proxyTwoHW = QtGui.QLineEdit(self.layoutWidget7)
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
        self.proxyTwoHW.setReadOnly(True)
        self.proxyTwoHW.setPlaceholderText(_fromUtf8(""))
        self.proxyTwoHW.setObjectName(_fromUtf8("proxyTwoHW"))
        self.gridLayout_6.addWidget(self.proxyTwoHW, 1, 5, 1, 1)
        self.sourceHW = QtGui.QLineEdit(self.layoutWidget7)
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
        self.sourceHW.setReadOnly(True)
        self.sourceHW.setPlaceholderText(_fromUtf8(""))
        self.sourceHW.setObjectName(_fromUtf8("sourceHW"))
        self.gridLayout_6.addWidget(self.sourceHW, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 4, 1, 1)
        self.destHW = QtGui.QLineEdit(self.layoutWidget7)
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
        self.destHW.setReadOnly(True)
        self.destHW.setPlaceholderText(_fromUtf8(""))
        self.destHW.setObjectName(_fromUtf8("destHW"))
        self.gridLayout_6.addWidget(self.destHW, 1, 7, 1, 1)
        self.proxyOneHW = QtGui.QLineEdit(self.layoutWidget7)
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
        self.proxyOneHW.setReadOnly(True)
        self.proxyOneHW.setPlaceholderText(_fromUtf8(""))
        self.proxyOneHW.setObjectName(_fromUtf8("proxyOneHW"))
        self.gridLayout_6.addWidget(self.proxyOneHW, 1, 3, 1, 1)
        self.label_21 = QtGui.QLabel(self.layoutWidget7)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_6.addWidget(self.label_21, 0, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.layoutWidget7)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_6.addWidget(self.label_20, 0, 3, 1, 1)
        self.label_23 = QtGui.QLabel(self.layoutWidget7)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_6.addWidget(self.label_23, 0, 5, 1, 1)
        self.label_22 = QtGui.QLabel(self.layoutWidget7)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_6.addWidget(self.label_22, 0, 7, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 1, 6, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 0, 8, 1, 1)
        self.layoutWidget8 = QtGui.QWidget(self.Simulation)
        self.layoutWidget8.setGeometry(QtCore.QRect(0, 70, 931, 50))
        self.layoutWidget8.setObjectName(_fromUtf8("layoutWidget8"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.phone = QtGui.QLabel(self.layoutWidget8)
        self.phone.setText(_fromUtf8(""))
        self.phone.setPixmap(QtGui.QPixmap(_fromUtf8("img/Phone.png")))
        self.phone.setScaledContents(True)
        self.phone.setObjectName(_fromUtf8("phone"))
        self.horizontalLayout_3.addWidget(self.phone)
        self.line_2 = QtGui.QFrame(self.layoutWidget8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_3.addWidget(self.line_2)
        self.server = QtGui.QLabel(self.layoutWidget8)
        self.server.setText(_fromUtf8(""))
        self.server.setPixmap(QtGui.QPixmap(_fromUtf8("img/Computer.png")))
        self.server.setScaledContents(True)
        self.server.setObjectName(_fromUtf8("server"))
        self.horizontalLayout_3.addWidget(self.server)
        self.line = QtGui.QFrame(self.layoutWidget8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_3.addWidget(self.line)
        self.server_2 = QtGui.QLabel(self.layoutWidget8)
        self.server_2.setText(_fromUtf8(""))
        self.server_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/Computer.png")))
        self.server_2.setScaledContents(True)
        self.server_2.setObjectName(_fromUtf8("server_2"))
        self.horizontalLayout_3.addWidget(self.server_2)
        self.line_3 = QtGui.QFrame(self.layoutWidget8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_3.addWidget(self.line_3)
        self.phone_2 = QtGui.QLabel(self.layoutWidget8)
        self.phone_2.setText(_fromUtf8(""))
        self.phone_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/Phone.png")))
        self.phone_2.setScaledContents(True)
        self.phone_2.setObjectName(_fromUtf8("phone_2"))
        self.horizontalLayout_3.addWidget(self.phone_2)
        spacerItem6 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.layoutWidget9 = QtGui.QWidget(self.Simulation)
        self.layoutWidget9.setGeometry(QtCore.QRect(780, 380, 137, 21))
        self.layoutWidget9.setObjectName(_fromUtf8("layoutWidget9"))
        self.gridLayout_8 = QtGui.QGridLayout(self.layoutWidget9)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.flowLabel_2 = QtGui.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.flowLabel_2.setFont(font)
        self.flowLabel_2.setObjectName(_fromUtf8("flowLabel_2"))
        self.gridLayout_8.addWidget(self.flowLabel_2, 0, 0, 1, 1)
        self.label_59 = QtGui.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setAutoFillBackground(False)
        self.label_59.setFrameShape(QtGui.QFrame.Panel)
        self.label_59.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.gridLayout_8.addWidget(self.label_59, 0, 1, 1, 1)
        self.splitter_5 = QtGui.QSplitter(self.Simulation)
        self.splitter_5.setGeometry(QtCore.QRect(440, 330, 321, 231))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.labelCurrentMessage_3 = QtGui.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setItalic(True)
        self.labelCurrentMessage_3.setFont(font)
        self.labelCurrentMessage_3.setObjectName(_fromUtf8("labelCurrentMessage_3"))
        self.descriptionField = QtGui.QTextEdit(self.splitter_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.descriptionField.setFont(font)
        self.descriptionField.setReadOnly(True)
        self.descriptionField.setObjectName(_fromUtf8("descriptionField"))
        self.widget1 = QtGui.QWidget(self.Simulation)
        self.widget1.setGeometry(QtCore.QRect(80, 120, 773, 196))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.gridLayout_16 = QtGui.QGridLayout(self.widget1)
        self.gridLayout_16.setMargin(0)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.flowLabel = QtGui.QLabel(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flowLabel.sizePolicy().hasHeightForWidth())
        self.flowLabel.setSizePolicy(sizePolicy)
        self.flowLabel.setMinimumSize(QtCore.QSize(112, 17))
        self.flowLabel.setMaximumSize(QtCore.QSize(112, 17))
        font = QtGui.QFont()
        font.setItalic(True)
        self.flowLabel.setFont(font)
        self.flowLabel.setObjectName(_fromUtf8("flowLabel"))
        self.gridLayout_16.addWidget(self.flowLabel, 0, 0, 1, 1)
        self.flowField = QtGui.QTextEdit(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flowField.sizePolicy().hasHeightForWidth())
        self.flowField.setSizePolicy(sizePolicy)
        self.flowField.setMinimumSize(QtCore.QSize(771, 171))
        self.flowField.setMaximumSize(QtCore.QSize(771, 171))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.flowField.setFont(font)
        self.flowField.setReadOnly(True)
        self.flowField.setObjectName(_fromUtf8("flowField"))
        self.gridLayout_16.addWidget(self.flowField, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Simulation, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuExit = QtGui.QMenu(self.menubar)
        self.menuExit.setObjectName(_fromUtf8("menuExit"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar()
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.actionAdd_template = QtGui.QAction(self)
        self.actionAdd_template.setObjectName(_fromUtf8("actionAdd_template"))
        self.actionAdd_scenario = QtGui.QAction(self)
        self.actionAdd_scenario.setObjectName(_fromUtf8("actionAdd_scenario"))
        self.menuFile.addAction(self.actionAdd_scenario)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.fileDialog = QtGui.QFileDialog()

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.destAddresField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sourceAddressField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sourcePortField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.destAddresField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.destPortField.clear)
        QtCore.QObject.connect(self.clearSimulationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.currentMessageField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sipTemplate.clear)
        QtCore.QObject.connect(self.clearSimulationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.currentMessageField.clear)
        QtCore.QObject.connect(self.clearSimulationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.flowField.clear)
        QtCore.QObject.connect(self.loadScenarioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.currentMessageField.clear)
        QtCore.QObject.connect(self.loadScenarioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.flowField.clear)
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
        QtCore.QObject.connect(self.clearCreateScenarioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sipTemplate.clear)
        QtCore.QObject.connect(self.clearCreateScenarioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.scenarioField.clear)
        QtCore.QObject.connect(self.loadScenarioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.descriptionField.clear)
        QtCore.QObject.connect(self.clearSimulationButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.descriptionField.clear)
        self.simulateRadioButton.toggled.connect(self.simulateRadioClicked)
        self.templatePathField.textChanged.connect(self.enableAddCaseButton)
        QtCore.QMetaObject.connectSlotsByName(self)

    def closeEvent(self, event):
        
        result = QtGui.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
            self.reset()
            event.accept()
       
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


    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.setStatusTip(_translate("MainWindow", "Ready", None))
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
        self.addCaseButton.setText(_translate("MainWindow", "Add template to scenario", None))
        self.removeCaseButton.setText(_translate("MainWindow", "Remove last template", None))
        self.label_19.setText(_translate("MainWindow", "Scenario stack", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Create/Load Scenario", None))
        self.labelCurrentMessage.setText(_translate("MainWindow", "Current message", None))
        self.nextButton.setText(_translate("MainWindow", "Next", None))
        self.simulateButton.setText(_translate("MainWindow", "Simulate", None))
        self.clearSimulationButton.setText(_translate("MainWindow", "Stop", None))
        self.label_21.setText(_translate("MainWindow", "Source address", None))
        self.label_20.setText(_translate("MainWindow", "Proxy 1 address", None))
        self.label_23.setText(_translate("MainWindow", "Proxy 2 address", None))
        self.label_22.setText(_translate("MainWindow", "Destination address", None))
        self.flowLabel_2.setText(_translate("MainWindow", "Simulation is:", None))
        self.label_59.setText(_translate("MainWindow", "OFF", None))
        self.labelCurrentMessage_3.setText(_translate("MainWindow", "Description", None))
        self.flowLabel.setText(_translate("MainWindow", "Connection flow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Simulation), _translate("MainWindow", "Simulation", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuExit.setTitle(_translate("MainWindow", "Exit", None))
        self.actionAdd_template.setText(_translate("MainWindow", "Add template", None))
        self.actionAdd_scenario.setText(_translate("MainWindow", "Load scenario", None))

        self.acceptButton.clicked.connect(self.getParameters)
        self.simulateButton.clicked.connect(self.loadTemplate)
        self.simulateButton.clicked.connect(self.loadParameters)
        self.simulateButton.clicked.connect(self.startSniff)
        self.nextButton.clicked.connect(self.next)
        self.clearSimulationButton.clicked.connect(self.reset)
        self.chooseTemplateButton.clicked.connect(self.getTemplate)
        self.addCaseButton.clicked.connect(self.addTemplateToScenario)
        self.removeCaseButton.clicked.connect(self.removeTemplateFromScenario)
        self.CreateScenarioButton.clicked.connect(self.createScenario)
        self.loadScenarioButton.clicked.connect(self.loadScenario)
        self.loadScenarioButton.clicked.connect(self.reset)


    def getParameters(self):
        """This function captures input parameters and shows message template"""
        try:
            self.sourceAddress = str(self.sourceAddressField.text())
            self.destAddress = str(self.destAddresField.text())
            self.proxyOneAddress = str(self.proxyOneAddresField.text())
            self.proxyTwoAddress = str(self.proxyTwoAddresField.text())
            self.proxyOnePort = str(self.proxyOnePortField.text())
            self.proxyTwoPort = str(self.proxyTwoPortField.text())
            self.senderName = str(self.senderField.text())
            self.receiverName = str(self.receiverField.text())
            self.sourcePort = str(self.sourcePortField.text())
            self.destPort = str(self.destPortField.text())
        except ValueError:
            pass

        if self.simulateRadioButton.isChecked():
            self.sourceAddress = self.randomLoopback()
            self.proxyOneAddress = self.randomLoopback()
            self.proxyTwoAddress = self.randomLoopback()
            self.destAddress = "127.0.0.1"
            self.sourcePort = random.randint(1024, 65535)
            self.destPort = random.randint(1024, 65535)
            self.proxyOnePort = random.randint(1024, 65535)
            self.proxyTwoPort = random.randint(1024, 65535)
            self.senderName = "Alice"
            self.receiverName = "Bob"

 
        self.template_vars = {
        "source_ip": self.sourceAddress,
        "source_port": self.sourcePort,
        "dest_ip": self.destAddress,
        "dest_port": self.destPort,
        "proxy_one_ip": self.proxyOneAddress,
        "proxy_one_port": self.proxyOnePort,
        "proxy_two_ip": self.proxyTwoAddress,
        "proxy_two_port": self.proxyTwoPort,
        "callid": ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6)),
        "sender": self.senderName,
        "receiver": self.receiverName,
        }

        self.loadParameters()

    def randomLoopback(self):
        """Return ip address 127.{}.{}.{} """
        return "127.{}.{}.{}".format(random.randint(1,255), \
                random.randint(1,255), random.randint(1,255))

    def loadParameters(self):
        """Separates ip addresses and ports onto two lists (source it from template_vars)."""
        try:
            self.ip_addresses = (self.template_vars["source_ip"], self.template_vars["proxy_one_ip"], \
                self.template_vars["proxy_two_ip"], self.template_vars["dest_ip"])

            self.ports = (str(self.template_vars["source_port"]), str(self.template_vars["proxy_one_port"]), \
                str(self.template_vars["proxy_two_port"]), str(self.template_vars["dest_port"]))

        except Exception, e:
            PopupDialog("Some of the paramters are missing in template: {}".format(e), "Whopsie..", "warning")
            raise Exception, e



        try:
            self.checkIps()
        except WrongIp, e:
            return
        try:
            self.checkPorts()
        except WrongPort, e:
            return
        try:
            self.checkSenderReceiver()
        except WrongSenderReceiver, e:
            return

        self.prepareFieldsToSimulation()

    def checkIps(self):
        """ """
        ips = self.ip_addresses
        ips = list(ips)
        pattern = re.compile("[0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?")
        for ip in ips[:]:
            ip = ips.pop(0)
            if ip: #if ip exists
                if pattern.match(ip): #if ip is an ip number
                    for ip_ in ips:
                        try:
                            assert (ip != ip_) #check if any pair of them are the same
                        except AssertionError:
                            PopupDialog("Some IPs are the same, please correct that", "Whopsie..", "warning")
                            raise WrongIp
                else:
                    PopupDialog('WARNING: Wrong IP address', "Whopsie..", 'warning')
                    raise WrongIp
            else: #if ip does not exists
                try:
                    assert (self.ports[self.ip_addresses.index(ip)] == ip) #Check if port for that ip also does not exist
                except AssertionError:
                    PopupDialog("""WARNING: Some pair: "port and IP", are incomplete.
If you want exclude some hardware, be sure that both, port and IP, are empty""", "Whopsie..", 'warning')
                    raise WrongIp

    def checkPorts(self):
        """ """
        for port in self.ports[:]:
            try:
                if not (1024 <= int(port) <= 65535):
                    PopupDialog('WARNING: Wrong source port number, choose between 1024-65535', "Whopsie..", 'warning')
                    raise WrongPort
            except ValueError: #port does not exists
                try:
                    assert (self.ip_addresses[self.ports.index(port)] == port) #Check if ip for that port also does not exist
                except AssertionError:
                    PopupDialog("""WARNING: Some pair: "port and IP" are incomplete.
If you want exclude some hardware, be sure that both, port and IP, are empty""", "Whopsie..", 'warning')
                    raise WrongPort

    def checkSenderReceiver(self):
        """ """
        legendary_phrases = ["huj", "dupa", "kurwa", "cycki"]
        if not self.template_vars['sender']:
            PopupDialog('WARNING: Sender field is empty', "Whopsie..", 'warning')
            raise WrongSenderReceiver
        if not  self.template_vars['receiver']:
            PopupDialog('WARNING: Receiver field is empty', "Whopsie..", 'warning')
            raise WrongSenderReceiver
        elif self.template_vars['sender'] in legendary_phrases:
            PopupDialog('Sam jestes {}, popraw to chociaz na cos bardziej kreatywnego ;)'.format(self.template_vars['sender']))
            raise WrongSenderReceiver
        elif self.template_vars['receiver'] in legendary_phrases:
            PopupDialog('Sam jestes {}, popraw to chociaz na cos bardziej kreatywnego ;)'.format(self.template_vars['receiver']))
            raise WrongSenderReceiver

    def prepareFieldsToSimulation(self):
        """Clears and adds ips and ports in proper fields"""
        self.sourceAddresBox.clear()
        self.destAddressBox.clear()
        self.sourcePortBox.clear()
        self.destPortBox.clear()
        self.sipTemplate.clear()
        self.sourceAddresBox.addItems(self.ip_addresses)
        self.destAddressBox.addItems(self.ip_addresses)
        self.sourcePortBox.addItems(self.ports)
        self.destPortBox.addItems(self.ports)
        self.sipTemplate.insertPlainText(self.printSample())
        self.sourceHW.setText(self.ip_addresses[0])
        self.proxyOneHW.setText(self.ip_addresses[1])
        self.proxyTwoHW.setText(self.ip_addresses[2])
        self.destHW.setText(self.ip_addresses[3])

    def checkTemplates(self):
        """ """
        for case in self.scenario:
            #Check mandatory fields
            try:
                match = re.search('(^Via: ).*', case["template"], re.MULTILINE).group(1)
            except AttributeError, e:
                PopupDialog("Some of the mandatory parameters are missing \
                    in template file: {}".format(os.path.basename(case["path"])), "Whopsie..", "warning")
                raise AttributeError, e

    def printSample(self):
        """Method to print text into text box"""

        parameters_info = """Parameters seems to be valid!

Source Address %(source_ip)s:%(source_port)s
Proxy one Address: %(proxy_one_ip)s:%(proxy_one_port)s
Proxy two address: %(proxy_two_ip)s:%(proxy_two_port)s
Destiantion address: %(dest_ip)s:%(dest_port)s
Sender: %(sender)s
Receiver: %(receiver)s
        """
        try:
            parameters_info = parameters_info % self.template_vars #replaces %(<variable>)s by template_vars
        except Exception, e:
            PopupDialog("Some paramters are missing in template: {}".format(e), "Whopsie..", "warning")
            raise Exception, e
        self.statusbar.showMessage("OK: All good, parameters Saved")
        return parameters_info


    def loadTemplate(self):
        """Renders given template file, add it to case under "message" key as string
        and insert it to scenario"""
        i=0
        for case in self.scenario:
            try:
                case["description"] = case["description"] % self.template_vars
                case["message"] = case["template"] % self.template_vars #replaces %(<variable>)s by template_vars
            except KeyError, e:
                PopupDialog("Some of the paramters are missing in template: {}".format(e), "Whopsie..", "warning")

            self.scenario.pop(i)
            i+=1
            self.scenario.insert(0, case)
        self.scenario.reverse()

    def next(self):
        """ """
        if self.message_counter < len(self.scenario)-1:
            self.currentMessageField.clear()
            self.descriptionField.clear()
            self.message_counter += 1
            case = self.generateRequest(self.scenario[self.message_counter])
            self.send(case)
            self.descriptionField.insertPlainText(case["description"])
        else:
            self.statusbar.showMessage('WARNING: There is no more messages to send')

    def generateRequest(self, case):
        """Generates request message"""
        try:
            req = Request(case["message"]) #This is just to check if template is fine
        except SipUnpackError, req_error:
            #Maybe it's a response
            try:
                req = Response(case["message"]) #This is just to check if template is fine
            except SipUnpackError, resp_error:
                PopupDialog("ERROR: malformed SIP Request. Caused, most likely by:\n{} \
                    or:\n{}".format(req_error, resp_error), "Whopsie..", "warning")
        
        req.headers["content-length"] = len(req.body)
        return case

    def send(self, case):
        """ """
        try:
            self.sending_sock = self.open_sock(case["source_ip"], int(case["source_port"]))
            self.sending_sock.sendto(case["message"],(case["dest_ip"], int(case["dest_port"])))
        except Exception, e:
            PopupDialog('Cannot send packet to {}:{}. {}'.format(case["dest_ip"], case["dest_port"], e), 'Whopsie..', 'warning')
        self.currentMessageField.insertPlainText("%s\n" % case["message"])

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
        self.nextButton.setEnabled(False)
        self.message_counter = -1
        try:
            killTransmission()
        except NameError:
            return
        self.sniff_thread.stop()
        self.sniff_thread = None
        self.send({'message':'END TRANSMISSION', 'source_ip': '127.0.0.1', 'source_port': '6666', \
        'dest_port': '6666', 'dest_ip': '127.0.0.1'})

        self.turnOnOff(self.label_59, off=True)
        self.statusbar.showMessage("OK: Cleared")

    def startSniff(self):
        """ """
        if self.scenario:
            if not self.sniff_thread:
                self.turnOnOff(self.label_59, off=False)
                self.nextButton.setEnabled(True)
                try:
                    self.sniff_thread = Sniff(self.ip_addresses, self.flowField)
                    self.sniff_thread.start()
                except Exception, e:
                     PopupDialog(str(e), "Whopsie..", "warning")
            else:
                PopupDialog("Simulation is already ongoing, STOP it first", "Whopsie..")
        else:
            PopupDialog("There are no messages to send, please load a scenario first", "Whopsie..", "warning")

    def addTemplateToScenario(self):
        """ """
        description, template = self.popDescriptionFromTemplate()
        self.scenario.append(
            {"source_ip": str(self.sourceAddresBox.currentText()), \
            "source_port": str(self.sourcePortBox.currentText()), \
            "dest_ip": str(self.destAddressBox.currentText()), \
            "dest_port": str(self.destPortBox.currentText()), \
            "path": self.template_path, \
            "template": template, \
            "description": description}
            )
        self.scenarioField.clear()
        self.scenarioField.insertPlainText(self.formatedScenario())

    def popDescriptionFromTemplate(self):
        """Pulls out description from template file and removes it
        return: str description, str template"""
        description = self.description_pattern.search(self.template_content)
        if not description:
            error = "Cannot find description, in: {} \nCheck if it's properly formated:\n " \
             "\"<description>Here should be a description</description>\"".format(self.template_path)
            PopupDialog(error, "Whopsie..", "warning")
            raise Exception, error
        description = description.group(1).strip()
        #description = re.sub('\s+', ' ', description)
        description = unicode(description, "utf-8")
        template = re.sub(self.description_pattern, '', self.template_content).strip()
        return description, template

    def removeTemplateFromScenario(self):
        """ """
        self.scenario.pop(-1)
        self.scenarioField.clear()
        self.scenarioField.insertPlainText(self.formatedScenario())

    def getTemplate(self, show_path=None):
        """ """
        template = IO(show_path=self.templatePathField)
        self.template_content, self.template_path = template.loadFile()

    def createScenario(self):
        """ """
        self.scenario.insert(0, self.template_vars)
        scenario = Scenario(self.scenario)
        filename = scenario.create()
        self.statusbar.showMessage("OK: Saved scenario to: {}".format(str(filename)))

    def loadScenario(self):
        """ """
        scenario = Scenario()
        try:
            self.scenario, filename = scenario.load()
            self.template_vars = self.scenario.pop(0) #removes first dict in list with startup parameters
        except Exception, e:
            PopupDialog("Something went wrong during scenario importing, propably file is " \
                "corrupted or you didn't choose any file.", "Whopsie..", "warning" )
            return
        self.checkTemplates()
        self.loadParameters()
        self.scenarioField.clear()
        self.scenarioField.insertPlainText(self.formatedScenario())
        PopupDialog("Scenario \"{0}\" loaded properly. Go to the \"{0}\" tab now.".format(os.path.basename(filename)), "Success :)" )
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Simulation), _translate("MainWindow", os.path.basename(filename), None))

    def formatedScenario(self):
        formated = ""
        for template in self.scenario:
            formated += "{source_ip:s} : {source_port:s}  ------->  {dest_ip:s} : {dest_port:s}\nContent: {path:s}\n".format(**template)
            formated += "{:-^80}\n".format("")
        return formated

    def turnOnOff(self, label, off):
        """ """
        label.setAutoFillBackground(True)
        if off:
            label.setText("OFF")
            color = QtGui.QColor(204, 0, 0)
        else:
            label.setText("ON")
            color  = QtGui.QColor(0, 204, 0)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                             g = color.green(),
                                             b = color.blue(),
                                             a = alpha
                                             )
        label.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        label.show()

class IO(QtGui.QFileDialog):
    """ """
    def __init__(self, show_path=None):
        QtGui.QFileDialog.__init__(self)
        self.show_path = show_path

    def loadFile(self):
        """ """
        filename = self.getOpenFileName(self, 'Open File', './templates')
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

    def __init__(self, message, title="", event="info"):
        QtGui.QMessageBox.__init__(self)
        self.title = title
        self.message = message
        self.event = event
        self.show()

    def show(self):
        if self.event == "info":
            dialog = QtGui.QMessageBox.information(self, self.title, self.message, buttons = QtGui.QMessageBox.Ok)
        else:
            dialog = QtGui.QMessageBox.warning(self, self.title, self.message, buttons = QtGui.QMessageBox.Ok)


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
    short        = ['allow-events', 'u', 'call-id', 'i', 'contact', 'm', 'content-encoding', 'e', \
    'content-length', 'l', 'content-type', 'c', 'event', 'o', 'from', 'f', 'subject', 's', 'supported', 'k', 'to', 't', 'via', 'v']
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
            headers['content-length'] = len(body)
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
        # Parse header
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

class WrongIp(Exception): pass
class WrongPort(Exception): pass
class WrongSenderReceiver(Exception): pass
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
        'headers':{ 'to':'', 'from':'', 'call-id':'', 'cseq':'', 'contact':'', 'Via':'' }
        }
    __methods = dict.fromkeys((
        'ACK', 'BYE', 'CANCEL', 'INFO', 'INVITE', 'MESSAGE', 'NOTIFY',
        'OPTIONS', 'PRACK', 'PUBLISH', 'REFER', 'REGISTER', 'SUBSCRIBE',
        'UPDATE'
        ))
    __proto = 'SIP'

    def unpack(self, buf):
        f = cStringIO.StringIO(buf)
        line = f.readline() #read first line of template
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


class Response(Message):
    """SIP response."""
    __hdr_defaults__ = {
        'version':'2.0',
        'status':'200',
        'reason':'OK',
        'headers':{ 'to':'', 'from':'', 'call-id':'', 'cseq':'', 'contact':'' }
        }
    __proto = 'SIP'

    def unpack(self, buf):
        f = cStringIO.StringIO(buf)
        line = f.readline()
        l = line.strip().split(None, 2)
        if len(l) < 2 or not l[0].startswith(self.__proto) or not l[1].isdigit():
            raise SipUnpackError('invalid response: %r' % line)
        self.version = l[0][len(self.__proto)+1:]
        self.status = l[1]
        self.reason = l[2]
        Message.unpack(self, f.read())

    def __str__(self):
        return '%s/%s %s %s\r\n' % (self.__proto, self.version, self.status,
                                    self.reason) + Message.__str__(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

