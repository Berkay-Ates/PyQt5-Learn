from PyQt5.QtWidgets import QApplication
from radio_btn_controller import RadioBtnController

app = QApplication([])
window = RadioBtnController()
window.show()
app.exec_()
