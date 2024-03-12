from PyQt5.QtWidgets import QApplication
from notification_controller import NotificationWindow

app = QApplication([])
window = NotificationWindow()
window.show()
app.exec_()
