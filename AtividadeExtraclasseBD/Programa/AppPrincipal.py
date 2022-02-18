import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from TelaPrincipal import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TelaPrincipal()
    w.show()
    sys.exit(app.exec_())
