# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beczka.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from location import LocationWidget
from result import ResultWidget
from error import ErrorWidget
from req import WeatherApi

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        
        locationWidget = QtWidgets.QWidget()
        self.location_ui = ui = LocationWidget()
        ui.setupUi(locationWidget)

        ui.pushButton.clicked.connect(self.click)
        ui.city_edit.textEdited.connect(self.clear_lat_lng)
        ui.lng_edit.textEdited.connect(self.clear_city)
        ui.lat_edit.textEdited.connect(self.clear_city)

        self.stackedWidget.addWidget(locationWidget)
        
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.location_ui.pushButton.setDisabled(True)
        self.location_ui.lat_edit.setValidator(QtGui.QDoubleValidator(-90.0, 90.0, 6))
        self.location_ui.lng_edit.setValidator(QtGui.QDoubleValidator(-180.0, 180.0, 6))

        self.geo = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pygoda"))

    def click(self):
        api = WeatherApi()
        if self.geo:
            lon, lat = self.location_ui.lng_edit.text(), self.location_ui.lat_edit.text()
            data = api.coord_weather(lon, lat)
            data['city'] = f'{lon}, {lat}'.replace(',','.')
        else:
            data = api.city_weather(self.location_ui.city_edit.text())
            data['city'] = self.location_ui.city_edit.text()

        resultWidget = QtWidgets.QWidget()
        if(data['status'] == 'ok'):
            ui = ResultWidget(data)
        else:
            ui = ErrorWidget()

        ui.setupUi(resultWidget)
        ui.back_button.clicked.connect(self.spawn_main_window)
        self.stackedWidget.addWidget(resultWidget)
        self.stackedWidget.setCurrentWidget(resultWidget)

    def clear_city(self):
        self.location_ui.city_edit.clear()
        self.update_button()
    
    def clear_lat_lng(self):
        self.location_ui.lat_edit.clear()
        self.location_ui.lng_edit.clear()
        self.location_ui.city_edit.setText(self.location_ui.city_edit.text().capitalize())
        self.update_button()

    def update_button(self):
        if self.location_ui.city_edit.text():
            self.location_ui.pushButton.setDisabled(False)
            self.geo = False
        elif self.location_ui.lng_edit.text() and self.location_ui.lat_edit.text():
            self.location_ui.pushButton.setDisabled(False)
            self.geo = True
        else:
            self.location_ui.pushButton.setDisabled(True)
            self.geo = None

    def spawn_main_window(self):
        self.stackedWidget.removeWidget(self.stackedWidget.currentWidget())
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

