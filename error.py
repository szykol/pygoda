# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ErrorWidget(object):
    def __init__(self, message, button_text='Powrót'):
        self.message = message
        self.button_text = button_text

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(708, 568)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.description = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.description.setFont(font)
        self.description.setStyleSheet("color: red")
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setWordWrap(True)
        self.description.setObjectName("description")
        self.verticalLayout.addWidget(self.description)
        self.back_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMinimumSize(QtCore.QSize(85, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("margin-bottom: 50")
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.description.setText(_translate("Form", self.message))
        self.back_button.setText(_translate("Form", self.button_text))

