import sys
import json
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QFont
import os

class GeneradorCodigos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Códigos")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #2d2d2d;")

        # Ruta a datos.json y puntos.json
        self.ruta_datos = os.path.join(os.getcwd(), "0", "datos.json")
        self.ruta_puntos = os.path.join(os.getcwd(), "0", "puntos.json")

        # Cargar los códigos y puntos al iniciar
        self.datos = self.cargar_json(self.ruta_datos)
        self.puntos = self.cargar_puntos()

        # Botón para generar código
        self.generar_boton = QPushButton("Reclamar Código (50 pts)", self)
        self.generar_boton.setGeometry(110, 50, 180, 40)
        self.generar_boton.setStyleSheet("""
            QPushButton {
                background-color: #5a9; 
                color: white; 
                font-size: 14px; 
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #47a;
            }
        """)
        self.generar_boton.clicked.connect(self.generar_codigo)

        # Botón para copiar código
        self.copiar_boton = QPushButton("Copiar Código", self)
        self.copiar_boton.setGeometry(110, 110, 180, 40)
        self.copiar_boton.setStyleSheet("""
            QPushButton {
                background-color: #5a9; 
                color: white; 
                font-size: 14px; 
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #47a;
            }
        """)
        self.copiar_boton.clicked.connect(self.copiar_codigo)
        self.copiar_boton.setEnabled(False)

        # Etiqueta para mostrar el código generado
        self.resultado_label = QLabel("Código generado aparecerá aquí.", self)
        self.resultado_label.setGeometry(50, 200, 300, 30)
        self.resultado_label.setStyleSheet("color: #fff; font-size: 14px;")
        self.resultado_label.setFont(QFont("Arial", 12))

        # Etiqueta para mostrar los puntos
        self.puntos_label = QLabel(f"Puntos disponibles: {self.puntos}", self)
        self.puntos_label.setGeometry(50, 250, 300, 30)
        self.puntos_label.setStyleSheet("color: #fff; font-size: 14px;")
        self.puntos_label.setFont(QFont("Arial", 12))

    def cargar_json(self, ruta):
        try:
            with open(ruta, "r") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"El archivo {ruta} no se encontró.")
            return []
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", f"El archivo {ruta} tiene un formato inválido.")
            return []

    def cargar_puntos(self):
        try:
            with open(self.ruta_puntos, "r") as archivo:
                return json.load(archivo)["puntos"]
        except FileNotFoundError:
            # Si el archivo no existe, inicializamos con 100 puntos y lo creamos
            puntos_iniciales = 100
            self.guardar_puntos(puntos_iniciales)
            return puntos_iniciales
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "El archivo puntos.json tiene un formato inválido.")
            return 0

    def guardar_puntos(self, puntos):
        with open(self.ruta_puntos, "w") as archivo:
            json.dump({"puntos": puntos}, archivo)

    def generar_codigo(self):
        if self.puntos >= 50:
            if self.datos:
                # Deducir puntos
                self.puntos -= 50
                self.guardar_puntos(self.puntos)
                self.puntos_label.setText(f"Puntos disponibles: {self.puntos}")

                # Seleccionar y eliminar un código
                seleccionado = self.datos.pop(0)
                self.resultado_label.setText(f"Código generado: {seleccionado}")

                # Actualizar el archivo datos.json
                with open(self.ruta_datos, "w") as archivo:
                    json.dump(self.datos, archivo)

                # Activar el botón de copiar
                self.codigo_actual = seleccionado
                self.copiar_boton.setEnabled(True)
            else:
                QMessageBox.warning(self, "Sin códigos", "Todos los códigos han sido utilizados.")
        else:
            QMessageBox.warning(self, "Sin puntos", "No tienes suficientes puntos para reclamar un código.")

    def copiar_codigo(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.codigo_actual)
        QMessageBox.information(self, "Copiar", "El código se ha copiado al portapapeles.")

# Configuración de la aplicación
app = QApplication(sys.argv)
ventana = GeneradorCodigos()
ventana.show()
sys.exit(app.exec_())
