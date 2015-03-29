# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'un.ui'
#
# Created: Sun Mar 29 21:09:10 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys
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
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(284, 163)
        self.dial = QtGui.QDial(Dialog)
        self.dial.setGeometry(QtCore.QRect(20, 10, 50, 64))
        self.dial.setObjectName(_fromUtf8("dial"))
        self.lcdNumber = QtGui.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(210, 10, 64, 23))
        self.lcdNumber.setStyleSheet(_fromUtf8("color: rgb(177, 2, 34);\n"
"background-color: rgb(185, 69, 15);"))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        
        
app = QtGui.QApplication(sys.argv)
window = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())

