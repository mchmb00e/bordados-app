from bordados_app import Ui_MainWindow  # Importa la clase generada por pyuic5
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
import sqlite
from os import walk
import tools

class MiAplicacion(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz

        # Evento on click en Botones
        self.btn_buscar.clicked.connect(self.btn_buscar_on_click)
        self.btn_renombrar.clicked.connect(self.btn_renombrar_on_click)
        self.btn_categoria.clicked.connect(self.btn_categoria_on_click)
        self.btn_favorito.clicked.connect(self.btn_favorito_on_click)

        # Evento on click en elementos de QListWidget
        self.listWidget.itemClicked.connect(self.btn_listWidget_on_click)

        

    def btn_buscar_on_click(self):
        print("Boton presionado")

    def btn_renombrar_on_click(self):
        print("Boton presionado")
    def btn_categoria_on_click(self):
        print("Boton presionado")
    def btn_favorito_on_click(self):
        print("Boton presionado")

    def btn_listWidget_on_click(self, item):
        nombre = item.text()
        ubicacion = sqlite.ubicacion_por_nombre(nombre=nombre)
        id = sqlite.id_por_nombre(nombre=nombre)
        render = tools.render(ubicacion, id)
        self.image.setPixmap(QPixmap(render))
        self.image.setScaledContents(True)

    def mostrar_nombres(self):
        nombres = sqlite.obtener_nombres()
        for nombre in nombres:
            self.listWidget.addItem(nombre[0])