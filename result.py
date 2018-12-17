# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from req import WeatherApi
from images import images_dir
import urllib 
from webcams import WebcamsApi
from webcams_window import WebcamsWindow

class ResultWidget(object):
    def __init__(self, data):
        self.miasto = data['city']
        self.data = data
        

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(724, 568)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.city_name = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.city_name.setFont(font)
        self.city_name.setAlignment(QtCore.Qt.AlignCenter)
        self.city_name.setObjectName("city_name")
        self.verticalLayout.addWidget(self.city_name)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.temperature = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperature.sizePolicy().hasHeightForWidth())
        self.temperature.setSizePolicy(sizePolicy)
        self.temperature.setMinimumSize(QtCore.QSize(702, 75))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.temperature.setFont(font)
        self.temperature.setStyleSheet("padding: 0")
        self.temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature.setObjectName("temperature")
        self.verticalLayout_2.addWidget(self.temperature)
        self.img = QtWidgets.QLabel(Form)
        self.img.setMinimumSize(QtCore.QSize(0, 0))
        self.img.setText("")
        self.img.setObjectName("img")
        self.verticalLayout_2.addWidget(self.img, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.description = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.description.setFont(font)
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setObjectName("description")
        self.verticalLayout.addWidget(self.description)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(85, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("margin-bottom: 20")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.back_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMinimumSize(QtCore.QSize(85, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("margin-bottom: 20")
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.city_name.setText(self.miasto)
        self.get_weather()
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.city_name.setText(_translate("Form", "Miasto"))
        self.temperature.setText(_translate("Form", "22℃"))
        self.description.setText(_translate("Form", "Słonecznie"))
        self.pushButton.setText(_translate("Form", "Kamerki"))
        self.back_button.setText(_translate("Form", "Gotowe"))

    def get_weather(self):
        data = self.data
        if data['status']:
            self.description.setText(data['main'])
            self.temperature.setText(data['temp'])
            icon_name = images_dir[data["icon"]]
            pix = QtGui.QPixmap()
            pix.load(f'img/{icon_name}.png')
            self.img.setPixmap(pix)
            self.img.show()
