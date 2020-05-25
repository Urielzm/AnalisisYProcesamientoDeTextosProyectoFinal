# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaPrincipal_url.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")
from Dialogos.DialogoAviso.DialogoAvisos import Ui_DialogAviso
from Backend.Resumen import Resumen
from Backend.Html2Text import Html2Text


class Ui_MainWindow_URL(object):
    def setupUi(self, MainWindow_URL):
        MainWindow_URL.setObjectName("MainWindow_URL")
        MainWindow_URL.resize(801, 600)
        MainWindow_URL.setMinimumSize(QtCore.QSize(801, 600))
        MainWindow_URL.setMaximumSize(QtCore.QSize(801, 600))
        MainWindow_URL.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(145, 214, 243, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0.824, y1:0.198864, x2:1, y2:0, stop:0 rgba(145, 214, 243, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow_URL)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Salir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Salir.setGeometry(QtCore.QRect(710, 530, 75, 23))
        self.pushButton_Salir.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.pushButton_Salir.setObjectName("pushButton_Salir")
        self.pushButton_Obtemer_Resumen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Obtemer_Resumen.setGeometry(QtCore.QRect(700, 490, 81, 23))
        self.pushButton_Obtemer_Resumen.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.pushButton_Obtemer_Resumen.setObjectName("pushButton_Obtemer_Resumen")
        self.label_TextoIntroduce_Texto = QtWidgets.QLabel(self.centralwidget)
        self.label_TextoIntroduce_Texto.setGeometry(QtCore.QRect(170, 60, 351, 31))
        self.label_TextoIntroduce_Texto.setObjectName("label_TextoIntroduce_Texto")
        self.label_Resumen_Obtenido = QtWidgets.QLabel(self.centralwidget)
        self.label_Resumen_Obtenido.setGeometry(QtCore.QRect(180, 360, 241, 31))
        self.label_Resumen_Obtenido.setObjectName("label_Resumen_Obtenido")
        self.textEdit_Entrada_de_texto = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Entrada_de_texto.setGeometry(QtCore.QRect(170, 90, 441, 21))
        self.textEdit_Entrada_de_texto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Entrada_de_texto.setObjectName("textEdit_Entrada_de_texto")
        self.textEdit_Salida_Resumen_Obtenido = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Salida_Resumen_Obtenido.setGeometry(QtCore.QRect(180, 400, 441, 151))
        self.textEdit_Salida_Resumen_Obtenido.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Salida_Resumen_Obtenido.setReadOnly(False)
        self.textEdit_Salida_Resumen_Obtenido.setObjectName("textEdit_Salida_Resumen_Obtenido")
        self.textEdit_Salida_Tabla_Frecuencias = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Salida_Tabla_Frecuencias.setGeometry(QtCore.QRect(70, 230, 311, 131))
        self.textEdit_Salida_Tabla_Frecuencias.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Salida_Tabla_Frecuencias.setReadOnly(False)
        self.textEdit_Salida_Tabla_Frecuencias.setObjectName("textEdit_Salida_Tabla_Frecuencias")
        self.label_Texto_Tabla_fr = QtWidgets.QLabel(self.centralwidget)
        self.label_Texto_Tabla_fr.setGeometry(QtCore.QRect(70, 190, 241, 31))
        self.label_Texto_Tabla_fr.setObjectName("label_Texto_Tabla_fr")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(290, 0, 201, 51))
        self.label_titulo.setObjectName("label_titulo")
        self.label_escudo_unam = QtWidgets.QLabel(self.centralwidget)
        self.label_escudo_unam.setGeometry(QtCore.QRect(10, 10, 131, 171))
        self.label_escudo_unam.setStyleSheet("border-image: url(:/escudoUnam/Imagenes/ImagenesSesion/unam.png);")
        self.label_escudo_unam.setText("")
        self.label_escudo_unam.setObjectName("label_escudo_unam")
        self.label_escudo_fi = QtWidgets.QLabel(self.centralwidget)
        self.label_escudo_fi.setGeometry(QtCore.QRect(660, 0, 131, 171))
        self.label_escudo_fi.setStyleSheet("border-image: url(:/escudofi/Imagenes/InterfazPrincipal/escudo_fi_color.png);")
        self.label_escudo_fi.setText("")
        self.label_escudo_fi.setObjectName("label_escudo_fi")
        self.textEdit_Salida_Organizacion_Valorizacion = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Salida_Organizacion_Valorizacion.setGeometry(QtCore.QRect(420, 230, 311, 131))
        self.textEdit_Salida_Organizacion_Valorizacion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Salida_Organizacion_Valorizacion.setReadOnly(False)
        self.textEdit_Salida_Organizacion_Valorizacion.setObjectName("textEdit_Salida_Organizacion_Valorizacion")
        self.label_Texto_Org_Y_Valorizacion = QtWidgets.QLabel(self.centralwidget)
        self.label_Texto_Org_Y_Valorizacion.setGeometry(QtCore.QRect(420, 190, 301, 31))
        self.label_Texto_Org_Y_Valorizacion.setObjectName("label_Texto_Org_Y_Valorizacion")
        self.pushButton_Limpiar_cuadros = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Limpiar_cuadros.setGeometry(QtCore.QRect(650, 460, 91, 23))
        self.pushButton_Limpiar_cuadros.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_Limpiar_cuadros.setObjectName("pushButton_Limpiar_cuadros")
        MainWindow_URL.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_URL)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow_URL.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_URL)
        self.statusbar.setObjectName("statusbar")
        MainWindow_URL.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.pushButton_Obtemer_Resumen.clicked.connect(self.imprime)
        self.r1=Resumen()
        self.url1 = Html2Text() 
        self.retranslateUi(MainWindow_URL)
        self.pushButton_Salir.clicked.connect(self.salirVolverAlMenuAnterior)
        self.pushButton_Salir.clicked.connect(MainWindow_URL.close)
        self.pushButton_Limpiar_cuadros.clicked.connect(self.limpiarCuadros)
        #self.fecha=datetime.now()
        QtCore.QMetaObject.connectSlotsByName(MainWindow_URL)

    def retranslateUi(self, MainWindow_URL):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_URL.setWindowTitle(_translate("MainWindow_URL", "Resumen por URL"))
        self.pushButton_Salir.setText(_translate("MainWindow_URL", "Salir"))
        self.pushButton_Obtemer_Resumen.setText(_translate("MainWindow_URL", "Resumir texto"))
        self.label_TextoIntroduce_Texto.setText(_translate("MainWindow_URL", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">Introduce un URL con texto:</span></p></body></html>"))
        self.label_Resumen_Obtenido.setText(_translate("MainWindow_URL", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">Resumen obtenido:</span></p></body></html>"))
        self.label_Texto_Tabla_fr.setText(_translate("MainWindow_URL", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">Tabla de frecuencias</span></p></body></html>"))
        self.label_titulo.setText(_translate("MainWindow_URL", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#c8371a;\">Resumen</span></p></body></html>"))
        self.label_Texto_Org_Y_Valorizacion.setText(_translate("MainWindow_URL", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">Oraciones y Valorización</span></p></body></html>"))
        self.menuArchivo.setTitle(_translate("MainWindow_URL", "Archivo"))

    def guardarResumenEnArchivo(self):
        tiempo_segundos = time.time()
        nombre="Resumen_"+str(tiempo_segundos)+".txt"
        #print(nombre)
        f = open (nombre,"w",encoding="utf-8")
        f.write(self.textEdit_Salida_Resumen_Obtenido.toPlainText())
        f.close()
        self.abrirDialogoAviso("Resumen Guardado")

    def limpiarCuadros(self):
        self.textEdit_Entrada_de_texto.setText("")
        self.textEdit_Salida_Organizacion_Valorizacion.setText("")
        self.textEdit_Salida_Tabla_Frecuencias.setText("")
        self.textEdit_Salida_Resumen_Obtenido.setText("")

    def imprime(self):
        text = self.textEdit_Entrada_de_texto.toPlainText()
        text = self.url1.get_full_text(text)
        if text:
            tabla_frecuencias=self.r1.tablaFrecuencias(text)
            oracionesYValorizacion=self.r1.oracionesYvalorizacion(tabla_frecuencias, text)
            tabla_frec_string=self.convertirAString(tabla_frecuencias)
            oracionesYvalorizacion_string=self.convertirAString(oracionesYValorizacion)
            #print(string)
            res =self.r1.resumir(text, oracionesYValorizacion)
        else:
            res = "Error. Direccion URL no valida"


        self.textEdit_Salida_Resumen_Obtenido.setText(str(res))
        self.textEdit_Salida_Tabla_Frecuencias.setText(str(tabla_frec_string))
        self.textEdit_Salida_Organizacion_Valorizacion.setText(str(oracionesYvalorizacion_string))        
        self.abrirDialogoAviso("Resumen listo")

    def convertirAString(self, diccionario):
        string=""
        for key in diccionario:
            string+=str(key)+":"+"\t"+str(diccionario[key])+"\n"
        return string


    def abrirDialogoAviso(self, texto):
        self.ventanaCam=QtWidgets.QDialog()
        self.uiCam=Ui_DialogAviso()
        self.uiCam.setupUi(self.ventanaCam,texto)
        self.ventanaCam.show()

    def salirVolverAlMenuAnterior(self):
        from VentanaMenu import Ui_Form_Menu_Principal
        self.ventanaMenu=QtWidgets.QMainWindow()
        #self.ui0=Ui_FormVentanaPrincipal()
        self.ui0=Ui_Form_Menu_Principal()
        self.ui0.setupUi(self.ventanaMenu)
        self.ventanaMenu.show()

import Logos.LogoVentanaInicio.LogoEscudoFi_rc
import Logos.LogoVentanaInicio.LogoEscudoUNAM_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_URL = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_URL()
    ui.setupUi(MainWindow_URL)
    MainWindow_URL.show()
    sys.exit(app.exec_())
