# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartScreen_v15.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 467)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.vlayout_primary = QtWidgets.QVBoxLayout()
        self.vlayout_primary.setContentsMargins(3, 15, 3, 0)
        self.vlayout_primary.setSpacing(10)
        self.vlayout_primary.setObjectName("vlayout_primary")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(19)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.vlayout_primary.addWidget(self.lbl_title)
        self.lbl_version = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_version.sizePolicy().hasHeightForWidth())
        self.lbl_version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_version.setFont(font)
        self.lbl_version.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_version.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.vlayout_primary.addWidget(self.lbl_version)
        self.line_horizontal = QtWidgets.QFrame(self.centralwidget)
        self.line_horizontal.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_horizontal.sizePolicy().hasHeightForWidth())
        self.line_horizontal.setSizePolicy(sizePolicy)
        self.line_horizontal.setMinimumSize(QtCore.QSize(60, 0))
        self.line_horizontal.setBaseSize(QtCore.QSize(0, 0))
        self.line_horizontal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horizontal.setObjectName("line_horizontal")
        self.vlayout_primary.addWidget(self.line_horizontal, 0, QtCore.Qt.AlignHCenter)
        self.lbl_open_desc = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_open_desc.setFont(font)
        self.lbl_open_desc.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_open_desc.setObjectName("lbl_open_desc")
        self.vlayout_primary.addWidget(self.lbl_open_desc)
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btn_open.setFont(font)
        self.btn_open.setIconSize(QtCore.QSize(16, 16))
        self.btn_open.setObjectName("btn_open")
        self.vlayout_primary.addWidget(self.btn_open, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_authors = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_authors.setFont(font)
        self.lbl_authors.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lbl_authors.setIndent(5)
        self.lbl_authors.setObjectName("lbl_authors")
        self.horizontalLayout_2.addWidget(self.lbl_authors)
        self.vlayout_primary.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.vlayout_primary)
        self.vlayout_options = QtWidgets.QVBoxLayout()
        self.vlayout_options.setSpacing(0)
        self.vlayout_options.setObjectName("vlayout_options")
        self.btn_tutorial = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tutorial.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tutorial.sizePolicy().hasHeightForWidth())
        self.btn_tutorial.setSizePolicy(sizePolicy)
        self.btn_tutorial.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_tutorial.setFont(font)
        self.btn_tutorial.setObjectName("btn_tutorial")
        self.vlayout_options.addWidget(self.btn_tutorial)
        self.btn_requirements = QtWidgets.QPushButton(self.centralwidget)
        self.btn_requirements.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_requirements.sizePolicy().hasHeightForWidth())
        self.btn_requirements.setSizePolicy(sizePolicy)
        self.btn_requirements.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_requirements.setFont(font)
        self.btn_requirements.setObjectName("btn_requirements")
        self.vlayout_options.addWidget(self.btn_requirements)
        self.btn_documentation = QtWidgets.QPushButton(self.centralwidget)
        self.btn_documentation.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_documentation.sizePolicy().hasHeightForWidth())
        self.btn_documentation.setSizePolicy(sizePolicy)
        self.btn_documentation.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_documentation.setFont(font)
        self.btn_documentation.setObjectName("btn_documentation")
        self.vlayout_options.addWidget(self.btn_documentation)
        self.btn_sourcecode = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sourcecode.sizePolicy().hasHeightForWidth())
        self.btn_sourcecode.setSizePolicy(sizePolicy)
        self.btn_sourcecode.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_sourcecode.setFont(font)
        self.btn_sourcecode.setObjectName("btn_sourcecode")
        self.vlayout_options.addWidget(self.btn_sourcecode)
        self.btn_about = QtWidgets.QPushButton(self.centralwidget)
        self.btn_about.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_about.sizePolicy().hasHeightForWidth())
        self.btn_about.setSizePolicy(sizePolicy)
        self.btn_about.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_about.setFont(font)
        self.btn_about.setObjectName("btn_about")
        self.vlayout_options.addWidget(self.btn_about)
        self.btn_contact = QtWidgets.QPushButton(self.centralwidget)
        self.btn_contact.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_contact.sizePolicy().hasHeightForWidth())
        self.btn_contact.setSizePolicy(sizePolicy)
        self.btn_contact.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_contact.setFont(font)
        self.btn_contact.setObjectName("btn_contact")
        self.vlayout_options.addWidget(self.btn_contact)
        self.horizontalLayout.addLayout(self.vlayout_options)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_title.setText(_translate("MainWindow", "Processing & Analysis for\n"
"Radio Science Experiments"))
        self.lbl_version.setText(_translate("MainWindow", "Version 2020.09.18"))
        self.lbl_open_desc.setText(_translate("MainWindow", "Choose a folder that contains PDS3 radio science data files:"))
        self.btn_open.setText(_translate("MainWindow", "Open"))
        self.lbl_authors.setText(_translate("MainWindow", "Paul Sirri\n"
"Occidental College\n"
"\n"
"Elizabeth M. Palmer\n"
"University of Southern California\n"
"\n"
"Essam Heggy\n"
"NASA JPL/Caltech\n"
"University of Southern California\n"
""))
        self.btn_tutorial.setText(_translate("MainWindow", "Tutorial"))
        self.btn_requirements.setText(_translate("MainWindow", "Requirements"))
        self.btn_documentation.setText(_translate("MainWindow", "Documentation"))
        self.btn_sourcecode.setText(_translate("MainWindow", "Source Code"))
        self.btn_about.setText(_translate("MainWindow", "About"))
        self.btn_contact.setText(_translate("MainWindow", "Contact Us"))

