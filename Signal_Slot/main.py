from PyQt5.QtWidgets import QApplication
from signal_slot_controller import PageViewController

app = QApplication([])
window = PageViewController()
window.show()
app.exec_()
