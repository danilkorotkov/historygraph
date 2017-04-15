# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Documents/Monkey Studio/My Progect/mainwindow.ui'
#
# Created: Tue Apr 11 17:27:49 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(639, 409)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ExitButton = QtGui.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(480, 350, 85, 30))
        self.ExitButton.setObjectName(_fromUtf8("ExitButton"))
        self.ExitButton2 = QtGui.QPushButton(self.centralwidget)
        self.ExitButton2.setGeometry(QtCore.QRect(480, 310, 85, 30))
        self.ExitButton2.setObjectName(_fromUtf8("ExitButton2"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 50, 271, 321))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setGeometry(QtCore.QRect(340, 50, 256, 192))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.ExitButton3 = QtGui.QPushButton(self.centralwidget)
        self.ExitButton3.setGeometry(QtCore.QRect(480, 270, 85, 30))
        self.ExitButton3.setObjectName(_fromUtf8("ExitButton3"))
        self.ExitButton4 = QtGui.QPushButton(self.centralwidget)
        self.ExitButton4.setGeometry(QtCore.QRect(390, 270, 85, 30))
        self.ExitButton4.setObjectName(_fromUtf8("ExitButton4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Form1", None))
        self.ExitButton.setText(_translate("MainWindow", "Exit", None))
        self.ExitButton2.setText(_translate("MainWindow", "PushButton2", None))
        self.ExitButton3.setText(_translate("MainWindow", "PushButton3", None))
        self.ExitButton4.setText(_translate("MainWindow", "PushButton4", None))

