from TelaCadastro import Ui_Dialog
from PyQt5.QtWidgets import QDialog

class DialogCadastro(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)