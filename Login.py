from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Login import *
from Stocker import *
import sys
import sqlite3 as sql
import datetime as date
import Icon_rc


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QFrame(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Background.sizePolicy().hasHeightForWidth())
        self.Background.setSizePolicy(sizePolicy)
        self.Background.setMinimumSize(QtCore.QSize(1200, 800))
        self.Background.setStyleSheet("*{\n"
"background-color: rgb(27, 62, 90);\n"
"border:none;\n"
"}")
        self.Background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Background.setObjectName("Background")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Background)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QFrame(self.Background)
        self.Header.setStyleSheet("*{\n"
"background-color: rgb(14, 32, 47);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_Title = QtWidgets.QFrame(self.Header)
        self.frame_Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Title.setObjectName("frame_Title")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_Title)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Logo = QtWidgets.QLabel(self.frame_Title)
        self.label_Logo.setMaximumSize(QtCore.QSize(20, 20))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap(":/Windows/Icon/Logo.png"))
        self.label_Logo.setScaledContents(True)
        self.label_Logo.setObjectName("label_Logo")
        self.horizontalLayout_3.addWidget(self.label_Logo)
        self.label_ProgramTitle = QtWidgets.QLabel(self.frame_Title)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ProgramTitle.setFont(font)
        self.label_ProgramTitle.setStyleSheet("*{\n"
"color: rgb(210,210,210)\n"
"}")
        self.label_ProgramTitle.setScaledContents(False)
        self.label_ProgramTitle.setWordWrap(False)
        self.label_ProgramTitle.setObjectName("label_ProgramTitle")
        self.horizontalLayout_3.addWidget(self.label_ProgramTitle)
        self.horizontalLayout.addWidget(self.frame_Title, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_WindowsButton = QtWidgets.QFrame(self.Header)
        self.frame_WindowsButton.setStyleSheet("QPushButton:Hover{\n"
"icon: \n"
"}")
        self.frame_WindowsButton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_WindowsButton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_WindowsButton.setObjectName("frame_WindowsButton")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_WindowsButton)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Btn_Minimize = QtWidgets.QPushButton(self.frame_WindowsButton)
        self.Btn_Minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Windows/Icon/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Minimize.setIcon(icon)
        self.Btn_Minimize.setIconSize(QtCore.QSize(20, 20))
        self.Btn_Minimize.setObjectName("Btn_Minimize")
        self.horizontalLayout_2.addWidget(self.Btn_Minimize)
        self.Btn_Close = QtWidgets.QPushButton(self.frame_WindowsButton)
        self.Btn_Close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Windows/Icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Close.setIcon(icon1)
        self.Btn_Close.setIconSize(QtCore.QSize(20, 20))
        self.Btn_Close.setObjectName("Btn_Close")
        self.horizontalLayout_2.addWidget(self.Btn_Close)
        self.horizontalLayout.addWidget(self.frame_WindowsButton, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.Header)
        self.Main = QtWidgets.QFrame(self.Background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main.sizePolicy().hasHeightForWidth())
        self.Main.setSizePolicy(sizePolicy)
        self.Main.setStyleSheet("")
        self.Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main.setObjectName("Main")
        self.label_Background = QtWidgets.QLabel(self.Main)
        self.label_Background.setGeometry(QtCore.QRect(0, 0, 1200, 760))
        self.label_Background.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Background.setText("")
        self.label_Background.setPixmap(QtGui.QPixmap(":/Background/Icon/Login_Bg.png"))
        self.label_Background.setScaledContents(True)
        self.label_Background.setObjectName("label_Background")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Main)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 50, 800, 650))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(800, 650))
        self.stackedWidget.setStyleSheet("border-radius:30px;\n"
"background-color:rgba(0, 0, 0, 0); ")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_Login = QtWidgets.QWidget()
        self.page_Login.setStyleSheet("")
        self.page_Login.setObjectName("page_Login")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_Login)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_Uretim = QtWidgets.QFrame(self.page_Login)
        self.frame_Uretim.setStyleSheet("border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"background-color:rgba(2, 128, 144, 220); ")
        self.frame_Uretim.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Uretim.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Uretim.setObjectName("frame_Uretim")
        self.label_photoUretim = QtWidgets.QLabel(self.frame_Uretim)
        self.label_photoUretim.setGeometry(QtCore.QRect(125, 150, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_photoUretim.sizePolicy().hasHeightForWidth())
        self.label_photoUretim.setSizePolicy(sizePolicy)
        self.label_photoUretim.setMinimumSize(QtCore.QSize(150, 150))
        self.label_photoUretim.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius: 75px;\n"
"")
        self.label_photoUretim.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_photoUretim.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_photoUretim.setLineWidth(1)
        self.label_photoUretim.setMidLineWidth(0)
        self.label_photoUretim.setText("")
        self.label_photoUretim.setPixmap(QtGui.QPixmap(":/Menu/Icon/Elektrik.png"))
        self.label_photoUretim.setMargin(20)
        self.label_photoUretim.setScaledContents(True)
        self.label_photoUretim.setObjectName("label_photoUretim")
        self.label_NameUretim = QtWidgets.QLabel(self.frame_Uretim)
        self.label_NameUretim.setGeometry(QtCore.QRect(125, 325, 150, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_NameUretim.sizePolicy().hasHeightForWidth())
        self.label_NameUretim.setSizePolicy(sizePolicy)
        self.label_NameUretim.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(28)
        font.setUnderline(True)
        self.label_NameUretim.setFont(font)
        self.label_NameUretim.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255)")
        self.label_NameUretim.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_NameUretim.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NameUretim.setObjectName("label_NameUretim")
        self.horizontalLayout_4.addWidget(self.frame_Uretim)
        self.frame_Depo = QtWidgets.QFrame(self.page_Login)
        self.frame_Depo.setStyleSheet("border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color:rgba(255, 255, 255, 180); ")
        self.frame_Depo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Depo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Depo.setObjectName("frame_Depo")
        self.label_NameDepo = QtWidgets.QLabel(self.frame_Depo)
        self.label_NameDepo.setGeometry(QtCore.QRect(125, 325, 150, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_NameDepo.sizePolicy().hasHeightForWidth())
        self.label_NameDepo.setSizePolicy(sizePolicy)
        self.label_NameDepo.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(28)
        font.setUnderline(True)
        self.label_NameDepo.setFont(font)
        self.label_NameDepo.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"")
        self.label_NameDepo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NameDepo.setObjectName("label_NameDepo")
        self.label_PhotoDepo = QtWidgets.QLabel(self.frame_Depo)
        self.label_PhotoDepo.setGeometry(QtCore.QRect(125, 150, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_PhotoDepo.sizePolicy().hasHeightForWidth())
        self.label_PhotoDepo.setSizePolicy(sizePolicy)
        self.label_PhotoDepo.setMinimumSize(QtCore.QSize(150, 150))
        self.label_PhotoDepo.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius: 75px;\n"
"")
        self.label_PhotoDepo.setText("")
        self.label_PhotoDepo.setPixmap(QtGui.QPixmap(":/Menu/Icon/Depo.png"))
        self.label_PhotoDepo.setMargin(30)
        self.label_PhotoDepo.setScaledContents(True)
        self.label_PhotoDepo.setObjectName("label_PhotoDepo")
        self.horizontalLayout_4.addWidget(self.frame_Depo)
        self.stackedWidget.addWidget(self.page_Login)
        self.page_Uretim = QtWidgets.QWidget()
        self.page_Uretim.setObjectName("page_Uretim")
        self.frame_UretimGiris = QtWidgets.QFrame(self.page_Uretim)
        self.frame_UretimGiris.setGeometry(QtCore.QRect(400, 0, 400, 650))
        self.frame_UretimGiris.setStyleSheet("border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color:rgba(255, 255, 255, 180); ")
        self.frame_UretimGiris.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_UretimGiris.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_UretimGiris.setObjectName("frame_UretimGiris")
        self.verticalFrame = QtWidgets.QFrame(self.frame_UretimGiris)
        self.verticalFrame.setGeometry(QtCore.QRect(50, 250, 300, 150))
        self.verticalFrame.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_UsernameUretim = QtWidgets.QLineEdit(self.verticalFrame)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        self.lineEdit_UsernameUretim.setFont(font)
        self.lineEdit_UsernameUretim.setStyleSheet("border-radius: 10px;\n"
"font: 16pt \"Tahoma\";\n"
"background-color: rgba(14, 32, 47, 255);\n"
"color:rgb(252, 252, 252);\n"
"padding: 5px, 5px 10px, 10px;")
        self.lineEdit_UsernameUretim.setMaxLength(20)
        self.lineEdit_UsernameUretim.setCursorPosition(7)
        self.lineEdit_UsernameUretim.setReadOnly(False)
        self.lineEdit_UsernameUretim.setPlaceholderText("")
        self.lineEdit_UsernameUretim.setObjectName("lineEdit_UsernameUretim")
        self.verticalLayout_2.addWidget(self.lineEdit_UsernameUretim)
        self.lineEdit_PasswordUretim = QtWidgets.QLineEdit(self.verticalFrame)
        self.lineEdit_PasswordUretim.setStyleSheet("border-radius: 10px;\n"
"font: 16pt \"Tahoma\";\n"
"background-color: rgba(14, 32, 47, 255);\n"
"color:rgb(252, 252, 252);\n"
"padding: 5px, 5px 10px, 10px;")
        self.lineEdit_PasswordUretim.setMaxLength(20)
        self.lineEdit_PasswordUretim.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_PasswordUretim.setObjectName("lineEdit_PasswordUretim")
        self.verticalLayout_2.addWidget(self.lineEdit_PasswordUretim)
        self.pushButton_LoginUretim = QtWidgets.QPushButton(self.frame_UretimGiris)
        self.pushButton_LoginUretim.setGeometry(QtCore.QRect(75, 470, 250, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_LoginUretim.sizePolicy().hasHeightForWidth())
        self.pushButton_LoginUretim.setSizePolicy(sizePolicy)
        self.pushButton_LoginUretim.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_LoginUretim.setFont(font)
        self.pushButton_LoginUretim.setStyleSheet("border-radius: 20px;\n"
"background-color:rgba(2, 128, 144, 255); \n"
"color: white;")
        self.pushButton_LoginUretim.setObjectName("pushButton_LoginUretim")
        self.label_ForgotPassword = QtWidgets.QLabel(self.frame_UretimGiris)
        self.label_ForgotPassword.setGeometry(QtCore.QRect(80, 425, 151, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ForgotPassword.sizePolicy().hasHeightForWidth())
        self.label_ForgotPassword.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_ForgotPassword.setFont(font)
        self.label_ForgotPassword.setStyleSheet("background-color:rgba(2, 128, 144, 0); \n"
"color: rgba(14, 32, 47, 255)")
        self.label_ForgotPassword.setObjectName("label_ForgotPassword")
        self.pushButton_BackUretim = QtWidgets.QPushButton(self.frame_UretimGiris)
        self.pushButton_BackUretim.setGeometry(QtCore.QRect(320, 30, 50, 50))
        self.pushButton_BackUretim.setWhatsThis("")
        self.pushButton_BackUretim.setStyleSheet("background-color: rgba(252,252,252,255);\n"
"border-radius: 15px;")
        self.pushButton_BackUretim.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Menu/Icon/Arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BackUretim.setIcon(icon2)
        self.pushButton_BackUretim.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BackUretim.setObjectName("pushButton_BackUretim")
        self.frame_UretimGiris_2 = QtWidgets.QFrame(self.page_Uretim)
        self.frame_UretimGiris_2.setGeometry(QtCore.QRect(0, 0, 400, 650))
        self.frame_UretimGiris_2.setStyleSheet("border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"background-color:rgba(2, 128, 144, 220); ")
        self.frame_UretimGiris_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_UretimGiris_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_UretimGiris_2.setObjectName("frame_UretimGiris_2")
        self.label_PhotoUretim_2 = QtWidgets.QLabel(self.frame_UretimGiris_2)
        self.label_PhotoUretim_2.setGeometry(QtCore.QRect(125, 150, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_PhotoUretim_2.sizePolicy().hasHeightForWidth())
        self.label_PhotoUretim_2.setSizePolicy(sizePolicy)
        self.label_PhotoUretim_2.setMinimumSize(QtCore.QSize(150, 150))
        self.label_PhotoUretim_2.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius: 75px;\n"
"")
        self.label_PhotoUretim_2.setText("")
        self.label_PhotoUretim_2.setPixmap(QtGui.QPixmap(":/Menu/Icon/Elektrik.png"))
        self.label_PhotoUretim_2.setMargin(20)
        self.label_PhotoUretim_2.setScaledContents(True)
        self.label_PhotoUretim_2.setObjectName("label_PhotoUretim_2")
        self.label_NameUretim_2 = QtWidgets.QLabel(self.frame_UretimGiris_2)
        self.label_NameUretim_2.setGeometry(QtCore.QRect(125, 325, 150, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_NameUretim_2.sizePolicy().hasHeightForWidth())
        self.label_NameUretim_2.setSizePolicy(sizePolicy)
        self.label_NameUretim_2.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(28)
        font.setUnderline(True)
        self.label_NameUretim_2.setFont(font)
        self.label_NameUretim_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255)")
        self.label_NameUretim_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NameUretim_2.setObjectName("label_NameUretim_2")
        self.stackedWidget.addWidget(self.page_Uretim)
        self.page_Depo = QtWidgets.QWidget()
        self.page_Depo.setObjectName("page_Depo")
        self.frame_DepoGiris_2 = QtWidgets.QFrame(self.page_Depo)
        self.frame_DepoGiris_2.setGeometry(QtCore.QRect(0, 0, 400, 650))
        self.frame_DepoGiris_2.setStyleSheet("border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"background-color:rgba(2, 128, 144, 220); ")
        self.frame_DepoGiris_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_DepoGiris_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_DepoGiris_2.setObjectName("frame_DepoGiris_2")
        self.verticalFrame_2 = QtWidgets.QFrame(self.frame_DepoGiris_2)
        self.verticalFrame_2.setGeometry(QtCore.QRect(50, 250, 300, 150))
        self.verticalFrame_2.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_UsernameDepo = QtWidgets.QLineEdit(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        self.lineEdit_UsernameDepo.setFont(font)
        self.lineEdit_UsernameDepo.setStyleSheet("border-radius: 10px;\n"
"font: 16pt \"Tahoma\";\n"
"background-color: rgba(252,252,252, 255);\n"
"color:rgb(14, 32, 47);\n"
"padding: 5px, 5px 10px, 10px;")
        self.lineEdit_UsernameDepo.setMaxLength(20)
        self.lineEdit_UsernameDepo.setCursorPosition(7)
        self.lineEdit_UsernameDepo.setReadOnly(False)
        self.lineEdit_UsernameDepo.setPlaceholderText("")
        self.lineEdit_UsernameDepo.setObjectName("lineEdit_UsernameDepo")
        self.verticalLayout_3.addWidget(self.lineEdit_UsernameDepo)
        self.lineEdit_PasswordDepo = QtWidgets.QLineEdit(self.verticalFrame_2)
        self.lineEdit_PasswordDepo.setStyleSheet("border-radius: 10px;\n"
"font: 16pt \"Tahoma\";\n"
"background-color: rgba(252,252,252, 255);\n"
"color:rgb(14, 32, 47);\n"
"padding: 5px, 5px 10px, 10px;")
        self.lineEdit_PasswordDepo.setMaxLength(20)
        self.lineEdit_PasswordDepo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_PasswordDepo.setObjectName("lineEdit_PasswordDepo")
        self.verticalLayout_3.addWidget(self.lineEdit_PasswordDepo)
        self.pushButton_LoginDepo = QtWidgets.QPushButton(self.frame_DepoGiris_2)
        self.pushButton_LoginDepo.setGeometry(QtCore.QRect(75, 470, 250, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_LoginDepo.sizePolicy().hasHeightForWidth())
        self.pushButton_LoginDepo.setSizePolicy(sizePolicy)
        self.pushButton_LoginDepo.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_LoginDepo.setFont(font)
        self.pushButton_LoginDepo.setStyleSheet("border-radius: 20px;\n"
"background-color:rgba(252, 252, 252, 255); \n"
"color: rgba(2, 128, 144, 255); ")
        self.pushButton_LoginDepo.setObjectName("pushButton_LoginDepo")
        self.label_ForgotPassword_2 = QtWidgets.QLabel(self.frame_DepoGiris_2)
        self.label_ForgotPassword_2.setGeometry(QtCore.QRect(80, 425, 151, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ForgotPassword_2.sizePolicy().hasHeightForWidth())
        self.label_ForgotPassword_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_ForgotPassword_2.setFont(font)
        self.label_ForgotPassword_2.setStyleSheet("background-color:rgba(2, 128, 144, 0); \n"
"color: rgba(14, 32, 47, 255)")
        self.label_ForgotPassword_2.setObjectName("label_ForgotPassword_2")
        self.pushButton_BackDepo = QtWidgets.QPushButton(self.frame_DepoGiris_2)
        self.pushButton_BackDepo.setGeometry(QtCore.QRect(30, 30, 50, 50))
        self.pushButton_BackDepo.setStyleSheet("background-color: rgba(252,252,252,255);\n"
"border-radius: 15px;")
        self.pushButton_BackDepo.setText("")
        self.pushButton_BackDepo.setIcon(icon2)
        self.pushButton_BackDepo.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BackDepo.setObjectName("pushButton_BackDepo")
        self.frame_DepoGiris = QtWidgets.QFrame(self.page_Depo)
        self.frame_DepoGiris.setGeometry(QtCore.QRect(400, 0, 400, 650))
        self.frame_DepoGiris.setStyleSheet("border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color:rgba(255, 255, 255, 180); ")
        self.frame_DepoGiris.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_DepoGiris.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_DepoGiris.setObjectName("frame_DepoGiris")
        self.label_NameDepo_2 = QtWidgets.QLabel(self.frame_DepoGiris)
        self.label_NameDepo_2.setGeometry(QtCore.QRect(125, 325, 150, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_NameDepo_2.sizePolicy().hasHeightForWidth())
        self.label_NameDepo_2.setSizePolicy(sizePolicy)
        self.label_NameDepo_2.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(28)
        font.setUnderline(True)
        self.label_NameDepo_2.setFont(font)
        self.label_NameDepo_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"")
        self.label_NameDepo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NameDepo_2.setObjectName("label_NameDepo_2")
        self.label_PhotoDepo_2 = QtWidgets.QLabel(self.frame_DepoGiris)
        self.label_PhotoDepo_2.setGeometry(QtCore.QRect(125, 150, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_PhotoDepo_2.sizePolicy().hasHeightForWidth())
        self.label_PhotoDepo_2.setSizePolicy(sizePolicy)
        self.label_PhotoDepo_2.setMinimumSize(QtCore.QSize(150, 150))
        self.label_PhotoDepo_2.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius: 75px;\n"
"")
        self.label_PhotoDepo_2.setText("")
        self.label_PhotoDepo_2.setPixmap(QtGui.QPixmap(":/Menu/Icon/Depo.png"))
        self.label_PhotoDepo_2.setMargin(30)
        self.label_PhotoDepo_2.setScaledContents(True)
        self.label_PhotoDepo_2.setObjectName("label_PhotoDepo_2")
        self.stackedWidget.addWidget(self.page_Depo)
        self.verticalLayout.addWidget(self.Main)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        self.stackedWidget.setCurrentIndex(0)
        self.Btn_Close.clicked.connect(Login.close) # type: ignore
        self.Btn_Minimize.clicked.connect(Login.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Login)


#------------------------------------------MAIN--------------------------------------------
        
#---------------------------------------Back Button----------------------------------------

        self.pushButton_BackUretim.clicked.connect(lambda back: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_BackDepo.clicked.connect(lambda back: self.stackedWidget.setCurrentIndex(0))

#--------------------------------------Cursor Change---------------------------------------

        self.frame_Uretim.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_Depo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_BackUretim.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_BackDepo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_LoginUretim.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_LoginDepo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_ForgotPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_ForgotPassword_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

#-------------------------------------------Hover-------------------------------------------
        
        self.frame_Uretim.enterEvent = lambda event: self.EnterHoverUretim()
        self.frame_Uretim.leaveEvent = lambda event: self.LeaveHoverUretim()
        self.frame_Depo.enterEvent = lambda event: self.EnterHoverDepo()
        self.frame_Depo.leaveEvent = lambda event: self.LeaveHoverDepo()
        self.pushButton_LoginUretim.enterEvent = lambda event: self.EnterHoverUretimLogin()
        self.pushButton_LoginUretim.leaveEvent = lambda event: self.LeaveHoverUretimLogin()
        self.pushButton_LoginDepo.enterEvent = lambda event: self.EnterHoverDepoLogin()
        self.pushButton_LoginDepo.leaveEvent = lambda event: self.LeaveHoverDepoLogin()
        self.pushButton_BackDepo.enterEvent = lambda event: self.EnterHoverBack()
        self.pushButton_BackDepo.leaveEvent = lambda event: self.LeaveHoverBack()
        self.pushButton_BackUretim.enterEvent = lambda event: self.EnterHoverBack()
        self.pushButton_BackUretim.leaveEvent = lambda event: self.LeaveHoverBack()
        self.Btn_Close.enterEvent = lambda event: self.EnterHoverClose()
        self.Btn_Close.leaveEvent = lambda event: self.LeaveHoverClose()
        self.Btn_Minimize.enterEvent = lambda event: self.EnterHoverMinimize()
        self.Btn_Minimize.leaveEvent = lambda event: self.LeaveHoverMinimize()
        self.label_ForgotPassword.enterEvent = lambda event: self.EnterHoverPassword()
        self.label_ForgotPassword.leaveEvent = lambda event: self.LeaveHoverPassword()
        self.label_ForgotPassword_2.enterEvent = lambda event: self.EnterHoverPassword_2()
        self.label_ForgotPassword_2.leaveEvent = lambda event: self.LeaveHoverPassword_2()

#------------------------------------------Click-------------------------------------------
        
        self.pushButton_LoginUretim.pressed.connect(lambda: self.PressedButtonFont())
        self.pushButton_LoginUretim.released.connect(lambda: self.ReleasedButtonFont())
        self.pushButton_LoginUretim.clicked.connect(lambda: self.GirisIslemi())
        self.pushButton_LoginDepo.pressed.connect(lambda: self.PressedButtonFont())
        self.pushButton_LoginDepo.released.connect(lambda: self.ReleasedButtonFont())
        self.pushButton_LoginDepo.clicked.connect(lambda: self.GirisIslemi())
        self.pushButton_BackDepo.pressed.connect(lambda: self.PressedBack())
        self.pushButton_BackDepo.released.connect(lambda: self.ReleasedBack())
        self.pushButton_BackUretim.pressed.connect(lambda: self.PressedBack())
        self.pushButton_BackUretim.released.connect(lambda: self.ReleasedBack())       
        self.label_ForgotPassword.mousePressEvent = lambda event: self.MessageBox()
        self.label_ForgotPassword_2.mousePressEvent = lambda event: self.MessageBox()

#-----------------------------------Choose Uretim or Depo----------------------------------
        
        self.frame_Uretim.mousePressEvent = lambda clickedMouse: self.ClickedUretim()
        self.frame_Depo.mousePressEvent = lambda clickedMouse: self.ClickedDepo()
        self.ChooseDb=0

    def ClickedUretim(self):
        self.lineEdit_UsernameUretim.setText("")
        self.lineEdit_PasswordUretim.setText("")
        self.stackedWidget.setCurrentIndex(1)
        self.ChooseDb = 1

    def ClickedDepo(self):
        self.lineEdit_UsernameDepo.setText("")
        self.lineEdit_PasswordDepo.setText("")
        self.stackedWidget.setCurrentIndex(2)
        self.ChooseDb = 2

    def PressedButtonFont(self):
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_LoginUretim.setFont(font)
        self.pushButton_LoginDepo.setFont(font)
    
    def ReleasedButtonFont(self):
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton_LoginUretim.setFont(font)
        self.pushButton_LoginDepo.setFont(font)

#-------------------------------------Hover Function---------------------------------------

    def EnterHoverUretim(self):
                self.frame_Uretim.setStyleSheet("border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"background-color:rgba(2, 128, 144, 255); ")
                
                self.label_photoUretim.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius: 75px;\n"
"")

    def LeaveHoverUretim(self):
                self.frame_Uretim.setStyleSheet("border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"background-color:rgba(2, 128, 144, 220); ")
                
                self.label_photoUretim.setStyleSheet("background-color:rgba(2, 89, 100, 255);\n"
"border-radius: 75px;\n"
"")

    def EnterHoverDepo(self):
                self.frame_Depo.setStyleSheet("border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color:rgba(255, 255, 255, 255); ")
                
                self.label_PhotoDepo.setStyleSheet("background-color:rgba(2, 128, 144, 255);\n"
"border-radius: 75px;\n"
"")
                
    def LeaveHoverDepo(self):
                self.frame_Depo.setStyleSheet("border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color:rgba(255, 255, 255, 180); ")
                
                self.label_PhotoDepo.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius: 75px;\n"
"")

    def EnterHoverUretimLogin(self):
                self.pushButton_LoginUretim.setStyleSheet("border-radius: 20px;\n"
"background-color:rgba(2, 89, 100, 255); \n"
"color: rgb(214, 214, 214);")

    def LeaveHoverUretimLogin(self):
                self.pushButton_LoginUretim.setStyleSheet("border-radius: 20px;\n"
"background-color:rgba(2, 128, 144, 255); \n"
"color: white;")

    def EnterHoverDepoLogin(self):
                self.pushButton_LoginDepo.setStyleSheet("border-radius: 20px;\n"
"background-color:rgba(214, 214, 214, 255); \n"
"color: rgba(2, 89, 100, 255); ")

    def LeaveHoverDepoLogin(self):
                self.pushButton_LoginDepo.setStyleSheet("border-radius: 20px;\n"
"background-color:rgba(252, 252, 252, 255); \n"
"color: rgba(2, 128, 144, 255); ")

    def PressedBack(self):
                self.pushButton_BackDepo.setStyleSheet("background-color: rgba(214, 214, 214, 255);\n"
"border-radius: 15px;")
                self.pushButton_BackUretim.setStyleSheet("background-color: rgba(214, 214, 214, 255);\n"
"border-radius: 15px;")

    def ReleasedBack(self):
                self.pushButton_BackDepo.setStyleSheet("background-color: rgba(252,252,252,255);\n"
"border-radius: 15px;")
                self.pushButton_BackUretim.setStyleSheet("background-color: rgba(252,252,252,255);\n"
"border-radius: 15px;")
                
    def EnterHoverBack(self):
                self.pushButton_BackDepo.setStyleSheet("background-color: rgba(235, 235, 235, 255);\n"
"border-radius: 15px;")
                self.pushButton_BackUretim.setStyleSheet("background-color: rgba(235, 235, 235, 255);\n"
"border-radius: 15px;")

    def LeaveHoverBack(self):
                self.pushButton_BackDepo.setStyleSheet("background-color: rgba(252,252,252,255);\n"
"border-radius: 15px;")
                self.pushButton_BackUretim.setStyleSheet("background-color: rgba(252,252,252,255);\n"
"border-radius: 15px;")
                
    def EnterHoverClose(self):
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/Windows/Icon/close_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Btn_Close.setIcon(icon1)
                self.Btn_Close.setIconSize(QtCore.QSize(20, 20))

    def LeaveHoverClose(self):
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/Windows/Icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Btn_Close.setIcon(icon1)
                self.Btn_Close.setIconSize(QtCore.QSize(20, 20))

    def EnterHoverMinimize(self):
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/Windows/Icon/minimize_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Btn_Minimize.setIcon(icon1)
                self.Btn_Minimize.setIconSize(QtCore.QSize(20, 20))
    def LeaveHoverMinimize(self):
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/Windows/Icon/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Btn_Minimize.setIcon(icon1)
                self.Btn_Minimize.setIconSize(QtCore.QSize(20, 20))

    def EnterHoverPassword(self):
                self.label_ForgotPassword.setStyleSheet("background-color:rgba(2, 128, 144, 0); \n"
"color: rgba(56, 129, 188, 255)")
                
    def LeaveHoverPassword(self):
                self.label_ForgotPassword.setStyleSheet("background-color:rgba(2, 128, 144, 0); \n"
"color: rgba(14, 32, 47, 255)")   
                         
    def EnterHoverPassword_2(self):
                self.label_ForgotPassword_2.setStyleSheet("background-color:rgba(2, 128, 144, 0); \n"
"color: rgba(255, 224, 153, 255)")
                
    def LeaveHoverPassword_2(self):
                self.label_ForgotPassword_2.setStyleSheet("background-color:rgba(2, 128, 144, 0); \n"
"color: rgba(14, 32, 47, 255)")  


#------------------------------------------------------------------------------------------

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label_ProgramTitle.setText(_translate("Login", "Stocker"))
        self.label_NameUretim.setText(_translate("Login", "Üretim"))
        self.label_NameDepo.setText(_translate("Login", "Depo"))
        self.lineEdit_UsernameUretim.setPlaceholderText(_translate("Login", "EM Pano"))
        self.lineEdit_PasswordUretim.setPlaceholderText(_translate("Login", "Password"))
        self.pushButton_LoginUretim.setText(_translate("Login", "Login"))
        self.label_ForgotPassword.setText(_translate("Login", "Forgot Password ?"))
        self.label_NameUretim_2.setText(_translate("Login", "Üretim"))
        self.lineEdit_UsernameDepo.setPlaceholderText(_translate("Login", "EM Depo"))
        self.lineEdit_PasswordDepo.setPlaceholderText(_translate("Login", "Password"))
        self.pushButton_LoginDepo.setText(_translate("Login", "Login"))
        self.label_ForgotPassword_2.setText(_translate("Login", "Forgot Password ?"))
        self.label_NameDepo_2.setText(_translate("Login", "Depo"))

#---------------------------------------Message Box----------------------------------------
        
    def MessageBox(self):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Forgot Password")
        msg.setWindowIcon(QIcon(":/Windows/Icon/Logo.png"))
        msg.setText("""Lütfen Yetkili kişi ile görüşün...
                    
İletişim : mesut.selcuk45@gmail.com""")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()     

#------------------------------------GİRİŞ İŞLEMLERİ---------------------------------------

    def GirisIslemi(self):
        Login_db = sql.connect(r".\Login\Login.sqlite")
        im = Login_db.cursor()
        im.execute("CREATE TABLE IF NOT EXISTS Login(No INTEGER NOT NULL UNIQUE, Username UNIQUE NOT NULL, Password NOT NULL, PRIMARY KEY(No AUTOINCREMENT))")

        GirisUsername = self.lineEdit_UsernameDepo.text() or self.lineEdit_UsernameUretim.text()
        GirisPassword = self.lineEdit_PasswordDepo.text() or self.lineEdit_PasswordUretim.text()
        
        try:
                db_Password = im.execute("SELECT Password FROM Login WHERE Username='%s'"%(GirisUsername)).fetchone()
                if db_Password[0] == GirisPassword:
                        msg=QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Login Success")
                        msg.setWindowIcon(QIcon(":/Windows/Icon/Logo.png"))
                        msg.setText("Giris Yapıldı")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()
                        if self.ChooseDb == 1:
                                PanoDB()
                        else:
                                DepoDB()
                else:
                        msg=QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Hatali Giris")
                        msg.setWindowIcon(QIcon(":/Windows/Icon/Logo.png"))
                        msg.setText("Şifre Hatalı")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()  

        except Exception:
                        msg=QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Hatali Giris")
                        msg.setWindowIcon(QIcon(":/Windows/Icon/Logo.png"))
                        msg.setText("Kullanıcı Adı Hatalı")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()


#--------------------------------------START APP-------------------------------------------

class FramelessWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)

app=QApplication(sys.argv)
window=FramelessWindow()
ui=Ui_Login()
ui.setupUi(window)
window.show()

def PanoDB():
        window.close()
        ui=Ui_Stocker()
        ui.setupUi(window)
        window.show()
def DepoDB():
        window.close()
        ui=Ui_Stocker()
        ui.setupUi(window)
        window.show()

#--------------------------------------CLOSE APP-------------------------------------------

sys.exit(app.exec_())