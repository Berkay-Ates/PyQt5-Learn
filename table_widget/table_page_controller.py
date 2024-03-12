from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from table_page_view import Ui_Form as TablePageView


class TablePageController(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.table_view = TablePageView()
        self.table_view.setupUi(self)
        self.listele()
        self.table_view.pushButton_add_row.clicked.connect(self.add_row)
        self.table_view.pushButton_add_column.clicked.connect(self.add_column)
        self.table_view.pushButton_delete_row.clicked.connect(self.remove_row)
        self.table_view.pushButton_delete_column.clicked.connect(self.remove_column)

        self.table_view.tableWidget.clicked.connect(self.clicked)
        self.table_view.tableWidget.cellChanged.connect(self.cell_value_changed)

    def cell_value_changed(self):
        updated_text = self.table_view.tableWidget.currentItem().text()
        selected_row = self.table_view.tableWidget.currentRow()
        selected_column = self.table_view.tableWidget.currentColumn()
        id = self.table_view.tableWidget.item(selected_row, 0).text()
        print("seleccted id: ", id)
        print("selected Column: ", selected_column, "selected row :", selected_row)
        print("new text: ", updated_text)

    def clicked(self):
        try:
            selected_row = self.table_view.tableWidget.currentRow()
            selected_id = self.table_view.tableWidget.item(selected_row, 0).text()
            print("user selected id is:", selected_id)
        except Exception as e:
            print(e)

    def listele(self):
        self.table_view.tableWidget.setColumnWidth(0, 75)
        self.table_view.tableWidget.setColumnWidth(1, 185)
        self.table_view.tableWidget.setColumnWidth(2, 185)
        self.table_view.tableWidget.setColumnWidth(3, 185)

        people = [
            {"id": 1, "name": "Berkay", "surname": "Ates", "phone": "+905366981732"},
            {"id": 2, "name": "Berkay", "surname": "Ates", "phone": "+905366981732"},
            {"id": 3, "name": "Berkay", "surname": "Ates", "phone": "+905366981732"},
            {"id": 4, "name": "Berkay", "surname": "Ates", "phone": "+905366981732"},
            {"id": 5, "name": "Berkay", "surname": "Ates", "phone": "+905366981732"},
            {"id": 6, "name": "Berkay", "surname": "Ates", "phone": "+905366981732"},
        ]

        self.table_view.tableWidget.setRowCount(len(people))

        for idx, person in enumerate(people):
            self.table_view.tableWidget.setItem(
                idx, 0, QTableWidgetItem(str(person["id"]))
            )

            self.table_view.tableWidget.setItem(
                idx, 1, QTableWidgetItem(str(person["name"]))
            )
            self.table_view.tableWidget.setItem(
                idx, 2, QTableWidgetItem(str(person["surname"]))
            )
            self.table_view.tableWidget.setItem(
                idx, 3, QTableWidgetItem(str(person["phone"]))
            )

    def add_row(self):
        selected_row = self.table_view.tableWidget.currentRow() + 1
        if selected_row != None:
            self.table_view.tableWidget.insertRow(selected_row)

    def add_column(self):
        selected_column = self.table_view.tableWidget.currentColumn() + 1
        if selected_column != None:
            self.table_view.tableWidget.insertColumn(selected_column)
            self.table_view.tableWidget.setItem(
                column=selected_column, item=QTableWidgetItem("hello world")
            )

    def remove_row(self):
        selected_row = self.table_view.tableWidget.currentRow()
        if selected_row != None:
            self.table_view.tableWidget.removeRow(selected_row)

    def remove_column(self):
        selected_column = self.table_view.tableWidget.currentColumn()
        if selected_column != None:
            result = self.table_view.tableWidget.insertColumn(selected_column)
