# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webcam.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class WebcamsWindow(object):
    def __init__(self, data):
        self.data = data

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(674, 528)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        

        for webcam in self.data:
            label = QtWidgets.QLabel()
            label.setText(f"<a href=\"{webcam['link']}\">{webcam['title']}</a>")
            label.setTextFormat(QtCore.Qt.RichText)
            label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
            label.setOpenExternalLinks(True)
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, label)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Gotowe"))

