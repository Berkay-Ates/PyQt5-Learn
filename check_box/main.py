from PyQt5.QtWidgets import QApplication
from check_box_controller import CheckboxController

app = QApplication([])
window = CheckboxController()
window.show()
app.exec_()
