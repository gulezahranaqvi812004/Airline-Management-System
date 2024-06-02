from PyQt5 import QtCore, QtWidgets
import csv
import functionCall as sf


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1042, 875)
        Form.setStyleSheet("background-color: rgb(104, 38, 38);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(104, 38, 38);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 2)
        self.columnBox = QtWidgets.QComboBox(Form)
        self.columnBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.columnBox.setObjectName("columnBox")
        self.columnBox.addItem("")
        self.columnBox.addItem("")
        self.columnBox.addItem("")
        self.columnBox.addItem("")
        self.columnBox.addItem("")
        self.columnBox.addItem("")
        self.columnBox.addItem("")
        self.columnBox.addItem("")
        self.gridLayout.addWidget(self.columnBox, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 2)
        self.sortingMenu = QtWidgets.QComboBox(Form)
        self.sortingMenu.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.sortingMenu.setObjectName("sortingMenu")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.sortingMenu.addItem("")
        self.gridLayout.addWidget(self.sortingMenu, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 2)
        self.sortingType = QtWidgets.QComboBox(Form)
        self.sortingType.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.sortingType.setObjectName("sortingType")
        self.sortingType.addItem("")
        self.sortingType.addItem("")
        self.gridLayout.addWidget(self.sortingType, 3, 2, 1, 1)
        self.sortButton = QtWidgets.QPushButton(Form)
        self.sortButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.sortButton.setObjectName("sortButton")
        self.gridLayout.addWidget(self.sortButton, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.timeLable = QtWidgets.QLabel(Form)
        self.timeLable.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"")
        self.timeLable.setText("")
        self.timeLable.setObjectName("timeLable")
        self.gridLayout.addWidget(self.timeLable, 5, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Email"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "PhoneNumber"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Time"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "SourceCountry"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Destination"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Price"))
        self.label_4.setText(_translate("Form", "Select Column:"))
        self.columnBox.setItemText(0, _translate("Form", "Name"))
        self.columnBox.setItemText(1, _translate("Form", "Email"))
        self.columnBox.setItemText(2, _translate("Form", "PhoneNumber"))
        self.columnBox.setItemText(3, _translate("Form", "Date"))
        self.columnBox.setItemText(4, _translate("Form", "Time"))
        self.columnBox.setItemText(5, _translate("Form", "SourceCountry"))
        self.columnBox.setItemText(6, _translate("Form", "Destination"))
        self.columnBox.setItemText(7, _translate("Form", "Price"))
        self.label_5.setText(_translate("Form", "Select Sorting Algorithm:"))
        self.sortingMenu.setItemText(0, _translate("Form", "InsertionSort"))
        self.sortingMenu.setItemText(1, _translate("Form", "IndexSort"))
        self.sortingMenu.setItemText(2, _translate("Form", "PancakeSort"))
        self.sortingMenu.setItemText(3, _translate("Form", "SelectionSort"))
        self.sortingMenu.setItemText(4, _translate("Form", "BubbleSort"))
        self.sortingMenu.setItemText(5, _translate("Form", "MergeSort"))
        self.sortingMenu.setItemText(6, _translate("Form", "QuickSort"))
        self.sortingMenu.setItemText(7, _translate("Form", "HeapSort"))
        self.sortingMenu.setItemText(8, _translate("Form", "CountingSort"))
        self.sortingMenu.setItemText(9, _translate("Form", "RadixSort"))
        self.sortingMenu.setItemText(10, _translate("Form", "BucketSort"))
        self.sortingMenu.setItemText(11, _translate("Form", "CombSort"))
        self.sortingMenu.setItemText(12, _translate("Form", "ShellSort"))
        self.sortingMenu.setItemText(13, _translate("Form", "CockailSort"))
        self.label_6.setText(_translate("Form", "Select Sorting Order:"))
        self.sortingType.setItemText(0, _translate("Form", "Ascending"))
        self.sortingType.setItemText(1, _translate("Form", "Descending"))
        self.sortButton.setText(_translate("Form", "Sort"))
        self.label_7.setText(_translate("Form", "Time Taken:"))


        self.sortButton.clicked.connect(self.sort_button_click)
        self.load_DataFromFile()

    def sort_button_click(self):

        selected_item = self.sortingMenu.currentText()
        selected_column = self.columnBox.currentText()
        selected_order = self.sortingType.currentText()
        n, p, d, r, re, dp, de, po = self.getDataFromTable()
        time = 0
        result = []

        if selected_column == "Name":
            result, time = sf.SortingAlgorithmFunction_Call(n, selected_order, selected_item)
            self.populate_table(result, p, d, r, re, dp, de, po)
        elif selected_column == "Email":
            result, time = sf.SortingAlgorithmFunction_Call(p, selected_order, selected_item)
            self.populate_table(n, result, d, r, re, dp, de, po)
        elif selected_column == "PhoneNumber":
            result, time = sf.SortingAlgorithmFunction_Call(d, selected_order, selected_item)
            self.populate_table(n, p, result, r, re, dp, de, po)
        elif selected_column == "Date":
            result, time = sf.SortingAlgorithmFunction_Call(r, selected_order, selected_item)
            self.populate_table(n, p, d, result, re, dp, de, po)
        elif selected_column == "Time":
            result, time = sf.SortingAlgorithmFunction_Call(re, selected_order, selected_item)
            self.populate_table(n, p, d, r, result, dp, de, po)
        elif selected_column == "SourceCountry":
            result, time = sf.SortingAlgorithmFunction_Call(dp, selected_order, selected_item)
            self.populate_table(n, p, d, r, re, result, de, po)
        elif selected_column == "Destination":
            result, time = sf.SortingAlgorithmFunction_Call(de, selected_order, selected_item)
            self.populate_table(n, p, d, r, re, dp, result, po)
        elif selected_column == "Price":
            result, time = sf.SortingAlgorithmFunction_Call(po, selected_order, selected_item)
            self.populate_table(n, p, d, r, re, dp, de, result)

        roundedtime=round(time,4)
        self.timeLable.setText(str(roundedtime)+"seconds")

    def load_DataFromFile(self):
        with open("Example.csv", 'r', encoding='iso-8859-1',
                  errors='replace') as fileInput:
            tableRows = 0
            self.data = list(csv.reader(fileInput))
            self.tableWidget.setRowCount(len(self.data))
            for row in self.data:
                self.tableWidget.setItem(
                    tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
                self.tableWidget.setItem(
                    tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
                self.tableWidget.setItem(
                    tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
                self.tableWidget.setItem(
                    tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
                self.tableWidget.setItem(
                    tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))

                self.tableWidget.setItem(
                    tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
                self.tableWidget.setItem(
                    tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
                self.tableWidget.setItem(
                    tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))

                tableRows += 1

    def populate_table(self, Name, Price, Description, Ratings, NoOfReviews, DiscountedPrice, Delivery, perOff):
        # Clear the existing items in the tableWidget (optional)
        self.tableWidget.clearContents()

        # Assuming len(Name) is the number of rows
        num_rows = len(Name)
        self.tableWidget.setRowCount(num_rows)

        for row in range(num_rows):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(Name[row])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(Price[row])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(Description[row])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(Ratings[row])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(NoOfReviews[row])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(DiscountedPrice[row])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(Delivery[row])))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(perOff[row])))

    def getDataFromTable(self):
        Names = []
        Price = []
        Description = []
        Rating = []
        NoOfReview = []
        DiscountedPrice = []
        Delivery = []
        perOff = []
        for row in self.data:
            Names.append(row[0])
            Price.append(row[1])
            Description.append(row[2])
            Rating.append(row[3])
            NoOfReview.append(row[4])
            DiscountedPrice.append(row[5])
            Delivery.append(row[6])
            perOff.append(row[7])
        return Names, Price, Description, Rating, NoOfReview, DiscountedPrice, Delivery, perOff


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
