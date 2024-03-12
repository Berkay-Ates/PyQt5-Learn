from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from signal_slot_view import Ui_MainWindow as PageView


class PageViewController(QMainWindow):
    signal1 = pyqtSignal(int)
    signal2 = pyqtSignal(int)

    def __init__(self) -> None:
        super().__init__()
        self.page_view = PageView()
        self.page_view.setupUi(self)
        # self.page_view.verticalScrollBar.valueChanged["int"].connect(self.set_progress)  # type: ignore

        # self.page_view.verticalScrollBar.valueChanged[int].connect(self.signal1[int])
        # self.signal1[int].connect(self.signal2[int])
        # self.signal2[int].connect(self.slot_func)

        self.page_view.verticalScrollBar.valueChanged[int].connect(self.slot1)
        self.signal1[int].connect(self.slot2)

    def slot1(self, value):
        self.signal1.emit(value)

    def slot2(self, value):
        self.page_view.progressBar.setValue(value)

    # def slot_func(self, value):
    #     self.page_view.progressBar.setValue(value)

    # # def set_progress(self, val_progress):
    # #     self.page_view.progressBar.setValue(val_progress)

    # @pyqtSlot(int)
    # def on_verticalScrollBar_valueChanged(self, value):
    #     self.page_view.progressBar.setValue(value)
    #     print(value)

    # def slot0(self):
    #     print("slot1 has clicked" * 3)
