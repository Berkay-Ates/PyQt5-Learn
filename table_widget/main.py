from PyQt5.QtWidgets import QApplication
from table_page_controller import TablePageController

app = QApplication([])
window = TablePageController()
window.show()
app.exec_()
