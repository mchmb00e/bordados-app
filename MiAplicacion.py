from bordados_app import Ui_MainWindow  # Importa la clase generada por pyuic5
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QMessageBox
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

        self.input_buscar.textChanged.connect(self.function_input_buscar)

        self.id_bordado_actual = -1
        self.item_actual = -1

    def function_input_buscar(self):
        if len(self.input_buscar.text()) == 0:
            self.mostrar_nombres(all=True)

    def btn_buscar_on_click(self):
        print(self.input_buscar.text())
        if len(self.input_buscar.text()) > 0:
            self.mostrar_nombres(all=False, search=self.input_buscar.text())


    def btn_renombrar_on_click(self):
        # Mostrar cuadro de diálogo de entrada de texto
        text, ok = QInputDialog.getText(self, 'Renombrar bordado', 'Ingresa nuevo nombre:')
        if ok and text:  # Si el usuario presionó "OK" y no está vacío
            resultado = sqlite.cambiar_nombre(id=self.id_bordado_actual, nombre=text)
            if resultado:
                self.input_buscar.setText("")
                self.mostrar_nombres(all=True)
            else:
                self.btn_renombrar_on_click()

    def btn_categoria_on_click(self):
        print("Boton presionado")

    def btn_favorito_on_click(self):
        sqlite.actualizar_favorito(self.id_bordado_actual)
        self.btn_listWidget_on_click(self.item_actual)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)  # Icono de información
        msg.setText("Se actualizó el estado favorito.")  # Mensaje
        msg.setWindowTitle("Bordado favorito.")  # Título del cuadro de diálogo
        msg.setStandardButtons(QMessageBox.Ok)  # Botones disponibles (OK)
        
        # Mostrar el mensaje
        msg.exec_()

    def btn_listWidget_on_click(self, item):
        nombre = item.text()
        self.item_actual = item
        ubicacion = sqlite.ubicacion_por_nombre(nombre=nombre)
        id = sqlite.id_por_nombre(nombre=nombre)
        self.id_bordado_actual = id
        render = tools.render(ubicacion, id)
        self.image.setPixmap(QPixmap(render))
        self.image.setScaledContents(True)
        bordado = sqlite.obtener(id=id)
        self.label_nombre.setText(bordado.nombre)
        self.label_categoria.setText(str(bordado.categoria))
        self.label_favorito.setText("Favorito" if bordado.favorito else "No favorito")

    def mostrar_nombres(self, all: bool, search : str = str):
        nombres = sorted(sqlite.obtener_nombres())
        self.listWidget.clear()
        if all:
            for nombre in nombres:
                self.listWidget.addItem(nombre[0])
        else:
            for nombre in nombres:
                if search.lower() in nombre[0].lower():
                    self.listWidget.addItem(nombre[0])
