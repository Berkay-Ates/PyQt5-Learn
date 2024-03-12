from PyQt5.QtWidgets import *
from user_save_form import Ui_MainWindow


class main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtTasarim = Ui_MainWindow()
        self.qtTasarim.setupUi(self)
        self.qtTasarim.pushButton.clicked.connect(self.add_clicked)

    def add_clicked(self):
        name = self.qtTasarim.lineEdit.text()
        gsm = self.qtTasarim.lineEdit.text()
        print(name, gsm)


app = QApplication([])
pencere = main()
pencere.show()
app.exec_()
