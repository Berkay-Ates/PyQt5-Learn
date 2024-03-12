from PyQt5.QtWidgets import *
from checkbox_ui_python import Ui_Form as CheckboxView


class CheckboxController(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.checkbox_view = CheckboxView()
        self.checkbox_view.setupUi(self)
        self.selected_sources = list()
        self.checkbox_view.pushButton_show.clicked.connect(self.showPage)

    def showPage(self):
        self.selected_sources.clear()
        if self.checkbox_view.checkBox_barbeque_soure.isChecked():
            self.selected_sources.append("BarbeQue Source")
        if self.checkbox_view.checkBox_chilly_source.isChecked():
            self.selected_sources.append("Chilly Source")
        if self.checkbox_view.checkBox_ketchup.isChecked():
            self.selected_sources.append("Ketchup")
        if self.checkbox_view.checkBox_mayonnaise.isChecked():
            self.selected_sources.append("Mayonnaise Source")

        self.show_sources(self.selected_sources)

    def show_sources(self, sources: list):
        self.checkbox_view.label_selected_siources_text.setText(" ".join(sources))
