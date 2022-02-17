import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from TelaPrincipal import *

class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.btnPesquisar.clicked.connect(self.pesquisa)
        self.ui.btnAdicionar.clicked.connect(self.adiciona)
        self.ui.btnAtualizar.clicked.connect(self.atualiza)
        self.ui.btnRemover  .clicked.connect(self.remove  )
    
    def pesquisa(self):
        print("Pesquisa clicado!")
    
    def adiciona(self):
        print("Adiciona clicado!")

    def atualiza(self):
        print("Atualiza clicado!")

    def remove(self):
        print("Remove clicado!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TelaPrincipal()
    w.show()
    sys.exit(app.exec_())