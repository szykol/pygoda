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
from coordinates import Geolocation
from translation import translate_text
from webcams import WebcamsApi
from webcams_window import WebcamsWindow

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

        self.location_ui.lat_edit.setValidator(QtGui.QDoubleValidator(-90.0, 90.0, 6))
        self.location_ui.lng_edit.setValidator(QtGui.QDoubleValidator(-180.0, 180.0, 6))

        self.geo = None

        self.geo_api = None
        if Geolocation.api_key_specified():
            self.geo_api = Geolocation()
            data = self.geo_api.get_city_name()
            if data["status"]:
                self.location_ui.city_edit.setText(data["data"])
        else:
            self.location_ui.pushButton.setDisabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pygoda"))
    def exit(self):
        QtCore.QCoreApplication.quit()

    def click(self):
        resultWidget = QtWidgets.QWidget()

        if not WeatherApi.api_key_specified():
            ui = ErrorWidget("Aplikacja nie posiada klucza do api pogody", 'Wyjscie')
            ui.setupUi(resultWidget)
            ui.back_button.clicked.connect(lambda:  QtCore.QCoreApplication.quit())

        else:
            api = WeatherApi()
            if self.geo:
                lon, lat = self.location_ui.lng_edit.text(), self.location_ui.lat_edit.text()
                data = api.coord_weather(lon, lat)
                if self.geo_api is not None:
                    data['city'] = self.geo_api.get_city_name(lat, lon)["data"]
                else:
                    data['city'] = f'{lat} {lon}'.replace(',','.')
                data['coords'] = (lat, lon)
            else:
                translated_city_name = translate_text(self.location_ui.city_edit.text())
                data = api.city_weather(translated_city_name)
                data['city'] = self.location_ui.city_edit.text()
                coords = self.geo_api.get_coords_from_name(translated_city_name)
                data['coords'] = (coords['lat'], coords['lng']) 

            temp = False
            if(data['status']):
                ui = ResultWidget(data)
                w_api = WebcamsApi()
                self.webcams = w_api.get_webcams_by_coord(data['coords'][0], data['coords'][1])
                temp = True                
            else:
                ui = ErrorWidget("Nie udało się pobrać pogody.\n"
" Sprawdź poprawność wprowadzonych danych")

            ui.setupUi(resultWidget)
            ui.back_button.clicked.connect(self.spawn_main_window)
            if temp and len(self.webcams) > 0:
                ui.pushButton.clicked.connect(self.spawn_webcam_window)
                ui.pushButton.setDisabled(False)


        self.stackedWidget.addWidget(resultWidget)
        self.stackedWidget.setCurrentWidget(resultWidget)

    def clear_city(self):
        self.location_ui.city_edit.clear()
        self.update_button()
    
    def clear_lat_lng(self):
        self.location_ui.lat_edit.clear()
        self.location_ui.lng_edit.clear()
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

    def spawn_webcam_window(self):
        self.webcam_window = QtWidgets.QMainWindow()
        self.webcam_ui = WebcamsWindow(self.webcams)
        self.webcam_ui.setupUi(self.webcam_window)
        self.webcam_ui.pushButton.clicked.connect(lambda: self.webcam_window.close())
        self.webcam_window.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

