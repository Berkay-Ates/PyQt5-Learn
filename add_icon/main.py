from PyQt5.QtWidgets import QApplication
from icon_controller import IconViewController

app = QApplication([])
window = IconViewController()
window.show()
app.exec_()
