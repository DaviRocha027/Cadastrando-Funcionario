# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(473, 309)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(60, 50, 49, 16))
        self.label_cargo = QLabel(self.centralwidget)
        self.label_cargo.setObjectName(u"label_cargo")
        self.label_cargo.setGeometry(QRect(60, 70, 49, 16))
        self.label_dtadmissao = QLabel(self.centralwidget)
        self.label_dtadmissao.setObjectName(u"label_dtadmissao")
        self.label_dtadmissao.setGeometry(QRect(240, 50, 101, 16))
        self.label_salario = QLabel(self.centralwidget)
        self.label_salario.setObjectName(u"label_salario")
        self.label_salario.setGeometry(QRect(240, 70, 49, 16))
        self.label_genero = QLabel(self.centralwidget)
        self.label_genero.setObjectName(u"label_genero")
        self.label_genero.setGeometry(QRect(60, 100, 49, 16))
        self.escolha_homem = QRadioButton(self.centralwidget)
        self.escolha_homem.setObjectName(u"escolha_homem")
        self.escolha_homem.setGeometry(QRect(110, 100, 92, 20))
        self.escolha_mulher = QRadioButton(self.centralwidget)
        self.escolha_mulher.setObjectName(u"escolha_mulher")
        self.escolha_mulher.setGeometry(QRect(110, 120, 92, 20))
        self.btn_salvar = QPushButton(self.centralwidget)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setGeometry(QRect(160, 160, 91, 31))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 50, 111, 20))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 70, 113, 21))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(340, 50, 113, 21))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(280, 70, 113, 21))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 473, 33))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.label_name.setText(QCoreApplication.translate("mainWindow", u"Nome:", None))
        self.label_cargo.setText(QCoreApplication.translate("mainWindow", u"Cargo:", None))
        self.label_dtadmissao.setText(QCoreApplication.translate("mainWindow", u"Data de Admiss\u00e3o:", None))
        self.label_salario.setText(QCoreApplication.translate("mainWindow", u"Salario:", None))
        self.label_genero.setText(QCoreApplication.translate("mainWindow", u"Genero:", None))
        self.escolha_homem.setText(QCoreApplication.translate("mainWindow", u"Masculino", None))
        self.escolha_mulher.setText(QCoreApplication.translate("mainWindow", u"Feminino", None))
        self.btn_salvar.setText(QCoreApplication.translate("mainWindow", u"Salvar", None))
    # retranslateUi

