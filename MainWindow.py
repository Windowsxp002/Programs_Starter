# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(882, 634)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(882, 634))
        Dialog.setMaximumSize(QtCore.QSize(882, 634))
        self.Button_start = QtWidgets.QPushButton(Dialog)
        self.Button_start.setGeometry(QtCore.QRect(740, 550, 101, 51))
        self.Button_start.setObjectName("Button_start")
        self.Button_add = QtWidgets.QPushButton(Dialog)
        self.Button_add.setGeometry(QtCore.QRect(630, 550, 101, 51))
        self.Button_add.setObjectName("Button_add")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 20, 801, 501))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.Button_save = QtWidgets.QPushButton(Dialog)
        self.Button_save.setGeometry(QtCore.QRect(440, 550, 91, 51))
        self.Button_save.setObjectName("Button_save")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(50, 550, 261, 51))
        self.comboBox.setObjectName("comboBox")
        self.Button_read = QtWidgets.QPushButton(Dialog)
        self.Button_read.setGeometry(QtCore.QRect(330, 550, 91, 51))
        self.Button_read.setObjectName("Button_read")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Button_start.setText(_translate("Dialog", "启动"))
        self.Button_add.setText(_translate("Dialog", "添加"))
        self.Button_save.setText(_translate("Dialog", "保存配置"))
        self.Button_read.setText(_translate("Dialog", "读取配置"))
