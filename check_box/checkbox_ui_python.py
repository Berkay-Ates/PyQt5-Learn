# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\checkbox_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(987, 616)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(320, 70, 391, 221))
        self.groupBox.setObjectName("groupBox")
        self.checkBox_mayonnaise = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_mayonnaise.setGeometry(QtCore.QRect(40, 60, 101, 20))
        self.checkBox_mayonnaise.setObjectName("checkBox_mayonnaise")
        self.checkBox_ketchup = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_ketchup.setGeometry(QtCore.QRect(40, 90, 81, 20))
        self.checkBox_ketchup.setObjectName("checkBox_ketchup")
        self.checkBox_chilly_source = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_chilly_source.setGeometry(QtCore.QRect(40, 120, 101, 20))
        self.checkBox_chilly_source.setObjectName("checkBox_chilly_source")
        self.checkBox_barbeque_soure = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_barbeque_soure.setGeometry(QtCore.QRect(40, 150, 121, 20))
        self.checkBox_barbeque_soure.setObjectName("checkBox_barbeque_soure")
        self.label_selected_tag = QtWidgets.QLabel(self.groupBox)
        self.label_selected_tag.setGeometry(QtCore.QRect(10, 190, 51, 20))
        self.label_selected_tag.setObjectName("label_selected_tag")
        self.label_selected_siources_text = QtWidgets.QLabel(self.groupBox)
        self.label_selected_siources_text.setGeometry(QtCore.QRect(90, 190, 271, 16))
        self.label_selected_siources_text.setText("")
        self.label_selected_siources_text.setObjectName("label_selected_siources_text")
        self.pushButton_show = QtWidgets.QPushButton(Form)
        self.pushButton_show.setGeometry(QtCore.QRect(470, 340, 93, 28))
        self.pushButton_show.setObjectName("pushButton_show")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Sources"))
        self.checkBox_mayonnaise.setText(_translate("Form", "Mayonnaise"))
        self.checkBox_ketchup.setText(_translate("Form", "Ketchup"))
        self.checkBox_chilly_source.setText(_translate("Form", "Chilly Source"))
        self.checkBox_barbeque_soure.setText(_translate("Form", "Barbeque Source"))
        self.label_selected_tag.setText(_translate("Form", "selected:"))
        self.pushButton_show.setText(_translate("Form", "Show"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
