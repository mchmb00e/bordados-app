import sys
from PyQt5.QtWidgets import QApplication
from MiAplicacion import MiAplicacion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiAplicacion()
    ventana.mostrar_nombres(all=True)
    ventana.show()
    sys.exit(app.exec_())
