from PyQt5.QtWidgets import *
from add_icon import Ui_MainWindow as IconView


class IconViewController(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.icon_view = IconView()
        self.icon_view.setupUi(self)
        self.icon_view.pushButton_add.clicked.connect(self.add_ice_cream)
        self.icon_view.pushButton_remove.clicked.connect(self.remove_ice_cream)
        self.count = 0

    def add_ice_cream(self):
        self.count += 1
        self.icon_view.label_ice_cream_count.setText(str(self.count))

    def remove_ice_cream(self):
        self.count -= 1
        self.icon_view.label_ice_cream_count.setText(str(self.count))
