from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from radio_btn_kullanimi_ui import Ui_Form as RadioBtnView


class RadioBtnController(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.radio_btn_view = RadioBtnView()
        self.radio_btn_view.setupUi(self)

        # # Push button pay the menu cost
        # # menu size radio buttons
        # self.radio_btn_view.radioButton_small_meal.toggled.connect(self.menu_select)
        # self.radio_btn_view.radioButton_medium_meal.toggled.connect(self.menu_select)
        # self.radio_btn_view.radioButton_large_meal.toggled.connect(self.menu_select)
        # self.radio_btn_view.radioButton_double_meal.toggled.connect(self.menu_select)

        # # beverage type selection
        # self.radio_btn_view.radioButton_ayran.toggled.connect(self.beverage_select)
        # self.radio_btn_view.radioButton_cola.toggled.connect(self.beverage_select)
        # self.radio_btn_view.radioButton_ice_tea.toggled.connect(self.beverage_select)
        # self.radio_btn_view.radioButton_mineral_water.toggled.connect(
        #     self.beverage_select
        # )
        self.radio_btn_view.pushButton.clicked.connect(self.pay_button)

    def pay_button(self):
        if self.radio_btn_view.radioButton_small_meal.isChecked():
            print("small button was clicked")

    # def menu_select(self):
    #     selected = self.sender()
    #     if selected.isChecked():
    #         selected_menu_size = selected.text()
    #         print(selected_menu_size)

    # def beverage_select(self):
    #     selected = self.sender()
    #     if selected.isChecked():
    #         selected_beverage = selected.text()
    #         print(selected_beverage)
