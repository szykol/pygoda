# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'location.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class LocationWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(823, 625)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.city_edit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_edit.sizePolicy().hasHeightForWidth())
        self.city_edit.setSizePolicy(sizePolicy)
        self.city_edit.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.city_edit.setFont(font)
        self.city_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.city_edit.setObjectName("city_edit")
        self.gridLayout.addWidget(self.city_edit, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 125))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, 15)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lat_edit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lat_edit.sizePolicy().hasHeightForWidth())
        self.lat_edit.setSizePolicy(sizePolicy)
        self.lat_edit.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lat_edit.setFont(font)
        self.lat_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.lat_edit.setObjectName("lat_edit")
        self.horizontalLayout_2.addWidget(self.lat_edit)
        self.lng_edit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lng_edit.sizePolicy().hasHeightForWidth())
        self.lng_edit.setSizePolicy(sizePolicy)
        self.lng_edit.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lng_edit.setFont(font)
        self.lng_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.lng_edit.setObjectName("lng_edit")
        self.horizontalLayout_2.addWidget(self.lng_edit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Lub współrzędne geograficzne"))
        self.city_edit.setPlaceholderText(_translate("Form", "Miasto"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.label.setText(_translate("Form", "Wprowadź nazwę miasta"))
        self.lat_edit.setPlaceholderText(_translate("Form", "Szerokość"))
        self.lng_edit.setPlaceholderText(_translate("Form", "Długość"))
