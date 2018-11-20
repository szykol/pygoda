# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from req import WeatherApi

class ResultWidget(object):
    def __init__(self, data):
        self.miasto = '\nmiasta o współrzędnych {} {}'.format(data["data"][0], data["data"][1]) if data["geo"] else data["data"] 
        self.data = data

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(724, 568)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.label.setText('Oto pogoda dla miasta {}'.format(self.miasto))
        self.get_weather()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Pogoda dla miasta Kraków"))
        self.label_2.setText(_translate("Form", "22℃"))
        self.label_3.setText(_translate("Form", "Słonecznie"))

    def get_weather(self):
        api = WeatherApi()
        #weather = None

        if self.data['geo']:
            lon = self.data['data'][0]
            lat = self.data['data'][1]
            data = api.coord_weather(lon, lat)
        else:
            data = api.city_weather(self.data['data'])

        if data['status'] == "ok":
            self.label_3.setText(data['main'])
            self.label_2.setText(data['temp'])
        else:
            self.label_3.setText('Wprowadzono nieprawidłowe dane')
