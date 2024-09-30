# Form implementation generated from reading ui file 'movies.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.titleEdit = QtWidgets.QLineEdit(parent=Form)
        self.titleEdit.setObjectName("titleEdit")
        self.verticalLayout.addWidget(self.titleEdit)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.yearSpinBox = QtWidgets.QSpinBox(parent=Form)
        self.yearSpinBox.setMinimum(0)
        self.yearSpinBox.setMaximum(2025)
        self.yearSpinBox.setObjectName("yearSpinBox")
        self.verticalLayout.addWidget(self.yearSpinBox)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.durationSpinBox = QtWidgets.QSpinBox(parent=Form)
        self.durationSpinBox.setMaximum(999)
        self.durationSpinBox.setObjectName("durationSpinBox")
        self.verticalLayout.addWidget(self.durationSpinBox)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.directorComboBox = QtWidgets.QComboBox(parent=Form)
        self.directorComboBox.setObjectName("directorComboBox")
        self.verticalLayout.addWidget(self.directorComboBox)
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.addButton = QtWidgets.QPushButton(parent=Form)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(parent=Form)
        self.editButton.setObjectName("editButton")
        self.verticalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(parent=Form)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Фильмы"))
        self.label.setText(_translate("Form", "Название"))
        self.label_2.setText(_translate("Form", "Год"))
        self.label_3.setText(_translate("Form", "Длительность"))
        self.label_4.setText(_translate("Form", "Режиссер"))
        self.label_5.setText(_translate("Form", "Жанры"))
        self.addButton.setText(_translate("Form", "Добавить фильм"))
        self.editButton.setText(_translate("Form", "Изменить фильм"))
        self.deleteButton.setText(_translate("Form", "Удалить фильм"))