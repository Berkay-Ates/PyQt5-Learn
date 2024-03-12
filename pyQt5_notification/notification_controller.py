from PyQt5.QtWidgets import *
from notification_page import Ui_MainWindow as NotificationUI


class NotificationWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.notification_window = NotificationUI()
        self.notification_window.setupUi(self)
        self.notification_window.pushButton_message.clicked.connect(
            self.notification_received
        )

    def notification_received(self):
        message_object = QMessageBox()
        message_object.setIcon(QMessageBox.Information)
        message_object.setText("Are you older than 18")
        message_object.setWindowTitle("Age restriction!")
        message_object.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_object.setEscapeButton(QMessageBox.No)

        message_object.button(QMessageBox.Yes).setText("Yes Sir!")
        message_object.button(QMessageBox.No).setText("No, unfortunately.")

        answer = message_object.exec_()
        if answer == QMessageBox.Yes:
            print("Yes i am older than 18")
        elif answer == QMessageBox.No:
            print("No i am younger than 18")

    # def notification_received(self):
    #     answer = QMessageBox.critical(
    #         self, "Info", "Are you older than 18", QMessageBox.Yes, QMessageBox.No
    #     )
    #     if answer == QMessageBox.Yes:
    #         print("Yes, user is older than 18")
    #     elif answer == QMessageBox.No:
    #         print("No, user younger than 18!")
