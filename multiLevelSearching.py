from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import csv
from BST import *
import AVLTree as avl
from RedBlack import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1042, 875)
        Form.setStyleSheet("background-color: rgb(98, 36, 36);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setStyleSheet("background-color: rgb(97, 36, 36);\n"
"color: rgb(0, 0, 0);")
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
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 2)
        self.algo = QtWidgets.QComboBox(Form)
        self.algo.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.algo.setObjectName("algo")
        self.algo.addItem("")
        self.gridLayout.addWidget(self.algo, 1, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 2)
        self.type = QtWidgets.QComboBox(Form)
        self.type.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.gridLayout.addWidget(self.type, 2, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)
        self.order = QtWidgets.QComboBox(Form)
        self.order.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.order.setObjectName("order")
        self.order.addItem("")
        self.order.addItem("")
        self.order.addItem("")
        self.gridLayout.addWidget(self.order, 3, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 2)
        self.query = QtWidgets.QLineEdit(Form)
        self.query.setStyleSheet("color: rgb(255, 255, 255);")
        self.query.setObjectName("query")
        self.gridLayout.addWidget(self.query, 4, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.fNumber = QtWidgets.QCheckBox(Form)
        self.fNumber.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.fNumber.setObjectName("fNumber")
        self.gridLayout.addWidget(self.fNumber, 5, 1, 1, 2)
        self.ftype = QtWidgets.QCheckBox(Form)
        self.ftype.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.ftype.setObjectName("ftype")
        self.gridLayout.addWidget(self.ftype, 5, 3, 1, 1)
        self.pName = QtWidgets.QCheckBox(Form)
        self.pName.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.pName.setObjectName("pName")
        self.gridLayout.addWidget(self.pName, 6, 1, 1, 2)
        self.capacity = QtWidgets.QCheckBox(Form)
        self.capacity.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.capacity.setObjectName("capacity")
        self.gridLayout.addWidget(self.capacity, 6, 3, 1, 1)
        self.sCountry = QtWidgets.QCheckBox(Form)
        self.sCountry.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.sCountry.setObjectName("sCountry")
        self.gridLayout.addWidget(self.sCountry, 7, 1, 1, 2)
        self.dCountry = QtWidgets.QCheckBox(Form)
        self.dCountry.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.dCountry.setObjectName("dCountry")
        self.gridLayout.addWidget(self.dCountry, 7, 3, 1, 1)
        self.date = QtWidgets.QCheckBox(Form)
        self.date.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 8, 1, 1, 2)
        self.duaration = QtWidgets.QCheckBox(Form)
        self.duaration.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.duaration.setObjectName("duaration")
        self.gridLayout.addWidget(self.duaration, 8, 3, 1, 1)
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"\n"
"")
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 8, 4, 1, 1)
        self.searchingType = QtWidgets.QComboBox(Form)
        self.searchingType.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.searchingType.setObjectName("searchingType")
        self.searchingType.addItem("")
        self.searchingType.addItem("")
        self.searchingType.addItem("")
        self.gridLayout.addWidget(self.searchingType, 9, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Description"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Rating"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "No. of Ratings and Reviews"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "DiscountedPrice"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Delivery"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "%off"))
        self.label_4.setText(_translate("Form", "Select Sorting Algorithm:"))
        self.algo.setItemText(0, _translate("Form", "LinearSearching"))
        self.label_7.setText(_translate("Form", "Select Type:"))
        self.type.setItemText(0, _translate("Form", "Contains"))
        self.type.setItemText(1, _translate("Form", "EndWith"))
        self.type.setItemText(2, _translate("Form", "StartsWith"))
        self.label_5.setText(_translate("Form", "Select Order:"))
        self.order.setItemText(0, _translate("Form", "AND"))
        self.order.setItemText(1, _translate("Form", "OR"))
        self.order.setItemText(2, _translate("Form", "NOT"))
        self.label_6.setText(_translate("Form", "Search Query:"))
        self.label_3.setText(_translate("Form", "Select Column:"))
        self.fNumber.setText(_translate("Form", "FlightNumber"))
        self.ftype.setText(_translate("Form", "FlightType"))
        self.pName.setText(_translate("Form", "PilotName"))
        self.capacity.setText(_translate("Form", "Capacity"))
        self.sCountry.setText(_translate("Form", "SourceCountry"))
        self.dCountry.setText(_translate("Form", "DestinationCountry"))
        self.date.setText(_translate("Form", "Date"))
        self.duaration.setText(_translate("Form", "Duaration"))
        self.searchButton.setText(_translate("Form", "Search"))
        self.searchingType.setItemText(0, _translate("Form", "BST"))
        self.searchingType.setItemText(1, _translate("Form", "RB"))
        self.searchingType.setItemText(2, _translate("Form", "AVL"))




        self.load_DataFromFile("Example.csv")
        self.searchButton.clicked.connect(self.search_button_click)

    def search_button_click(self):
        self.clearHighlightedRows()
        selected_algo = self.algo.currentText()
        print(f"Selected item: {selected_algo}")
        selectedType = self.type.currentText()
        print(selectedType)
        selectedOrder = self.order.currentText()
        print(selectedOrder)
        sType = self.searchingType.currentText()
        searchQuery = self.query.text()
        print(searchQuery)
        fNumber, ftype, pName, capacity, sCountry, dCountry, date, duaration = self.getDataFromTable()
        checkedBoxes = self.getCheckBoxes()
        lists = []
        for i in range(len(checkedBoxes)):
            if checkedBoxes[i] == "FlightNumber":
                lists.append(fNumber)
            elif checkedBoxes[i] == "FlightType":
                lists.append(ftype)
            elif checkedBoxes[i] == "PilotName":
                lists.append(pName)
            elif checkedBoxes[i] == "Capacity":
                lists.append(capacity)
            elif checkedBoxes[i] == "SourceCountry":
                lists.append(sCountry)
            elif checkedBoxes[i] == "DestinationCountry":
                lists.append(dCountry)
            elif checkedBoxes[i] == "Date":
                lists.append(date)
            elif checkedBoxes[i] == "Duaration":
                lists.append(duaration)

        searched = []
        bst_root = None
        avl_root = None

        rb_tree = RBTree()
        for singleList in lists:
            if sType == "BST":
                for value in singleList:
                    bst_root = insert_bst(bst_root, value)
                if selectedType == "Contains":
                    searched.append(contains_BST(bst_root, searchQuery))
                elif selectedType == "StartsWith":
                    searched.append(startsWith_BST(bst_root, searchQuery))
                elif selectedType == "EndWith":
                    searched.append(endWith_BST(bst_root, searchQuery))
            elif sType == "AVL":
                for value in singleList:
                    avl_root =  avl.insert_avl(avl_root, value)
                if selectedType == "Contains":
                    searched.append(avl.contains_AVL(avl_root, searchQuery))
                elif selectedType == "StartsWith":
                    searched.append(avl.startsWith_AVL(avl_root, searchQuery))
                elif selectedType == "EndWith":
                    searched.append(avl.endWith_AVL(avl_root, searchQuery))
            elif sType == "RB":
                for value in singleList:
                    rb_insert(rb_tree, value)
                if selectedType == "Contains":
                    searched.append(contains_RB(rb_tree, searchQuery))
                elif selectedType == "StartsWith":
                    searched.append(startsWith_RB(rb_tree, searchQuery))
                elif selectedType == "EndWith":
                    searched.append(endWith_RB(rb_tree, searchQuery))

        mainList = []

        for i in range(len(searched)):
            mainList.append(self.getMatchingRows(lists[i], searched[i]))
        min_length = float('inf')

        max_length = 0
        min_length_index = None
        max_length_index = None
        other_lengths = []
        other_lists = []
        other_indices = []

        for index, sublist in enumerate(mainList):
            sublist_length = len(sublist)
            if sublist_length < min_length:
                min_length = sublist_length
                min_length_index = index
            if sublist_length > max_length:
                max_length = sublist_length
                max_length_index = index
            if sublist_length != max_length or sublist_length != min_length:
                other_lengths.append(sublist_length)
                other_lists.append(sublist)
                other_indices.append(index)

        print("LENGTH OF MAIN LIST", len(mainList))
        if len(mainList) == 2:
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            set1 = set(col0)
            set2 = set(col1)
            if selectedOrder == "AND":
                intersection = set1.intersection(set2)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder == "OR":
                union = set1.union(set2)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set1 - set2
                negationList = list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 3:
            print(other_indices[0])
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder == "OR":
                union = set0.union(set2, set1)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0 - set1 - set2
                negationList = list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 4:
            print(other_indices[0])
            print(other_indices[1])
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            col3 = mainList[other_indices[1]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            set3 = set(col3)
            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1, set3)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder == "OR":
                union = set0.union(set2, set1, set3)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0 - set1 - set2 - set3
                negationList = list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 5:
            print(other_indices[0])
            print(other_indices[1])
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            col3 = mainList[other_indices[1]]
            col4 = mainList[other_indices[2]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            set3 = set(col3)
            set4 = set(col4)
            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1, set3, set4)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder == "OR":
                union = set0.union(set2, set1, set3, set4)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0 - set1 - set2 - set3 - set4
                negationList = list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 6:
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            col3 = mainList[other_indices[1]]
            col4 = mainList[other_indices[2]]
            col5 = mainList[other_indices[3]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            set3 = set(col3)
            set4 = set(col4)
            set5 = set(col5)
            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1, set3, set4)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder == "OR":
                union = set0.union(set2, set1, set3, set4, set5)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0 - set1 - set2 - set3 - set4 - set5
                negationList = list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 7:
            print(other_indices[0])
            print(other_indices[1])
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            col3 = mainList[other_indices[1]]
            col4 = mainList[other_indices[2]]
            col5 = mainList[other_indices[3]]
            col6 = mainList[other_indices[4]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            set3 = set(col3)
            set4 = set(col4)
            set5 = set(col5)
            set6 = set(col6)

            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1, set3, set4, set5, set6)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder == "OR":
                union = set0.union(set2, set1, set3, set4, set5, set6)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0 - set1 - set2 - set3 - set4 - set5 - set6
                negationList = list(negation_result)
                self.highlightRows(negationList)
        elif len(mainList) == 8:
            print(other_indices[0])
            print(other_indices[1])
            print(max_length_index)
            print(min_length_index)
            col0 = mainList[min_length_index]
            col1 = mainList[max_length_index]
            col2 = mainList[other_indices[0]]
            col3 = mainList[other_indices[1]]
            col4 = mainList[other_indices[2]]
            col5 = mainList[other_indices[3]]
            col6 = mainList[other_indices[4]]
            col7 = mainList[other_indices[5]]
            set0 = set(col0)
            set1 = set(col1)
            set2 = set(col2)
            set3 = set(col3)
            set4 = set(col4)
            set5 = set(col5)
            set6 = set(col6)
            set7 = set(col7)

            if selectedOrder == "AND":
                intersection = set0.intersection(set2, set1, set3, set4, set5, set6, set7)
                # Convert the result back to a list
                intersection_list = list(intersection)
                self.highlightRows(intersection_list)
            elif selectedOrder == "OR":
                union = set0.union(set2, set1, set3, set4, set5, set6, set7)
                unionList = list(union)
                self.highlightRows(unionList)
            else:
                negation_result = set0 - set1 - set2 - set3 - set4 - set5 - set6 - set7
                negationList = list(negation_result)
                self.highlightRows(negationList)





    def getMatchingRows(self, listToSearch, searched):
        selected = []
        for i in range(len(listToSearch)):
            # print(searched[i])
            for j in range(len(searched)):
                if searched[j] == listToSearch[i]:
                    selected.append(i)
        return selected

    def clearHighlightedRows(self):
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setBackground(QColor(23, 107, 135))

    def highlightRows(self, selected):
        for row in selected:
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                item.setBackground(QColor(255, 0, 0))  # Set the background color (here, it's red)

    def getCheckBoxes(self):
        checked_checkboxes = []

        if self.fNumber.isChecked():
            checked_checkboxes.append("FlightNumber")
        if self.ftype.isChecked():
            checked_checkboxes.append("FlightType")
        if self.pName.isChecked():
            checked_checkboxes.append("PilotName")
        if self.capacity.isChecked():
            checked_checkboxes.append("Capacity")
        if self.sCountry.isChecked():
            checked_checkboxes.append("SourceCountry")
        if self.dCountry.isChecked():
            checked_checkboxes.append("DestinationCountry")
        if self.date.isChecked():
            checked_checkboxes.append("Date")
        if self.duaration.isChecked():
            checked_checkboxes.append("Duaration")
        # print("Checked checkboxes:", checked_checkboxes)
        return checked_checkboxes

    def getDataFromTable(self):
        fNumber = []
        ftype = []
        pName = []
        capacity = []
        sCountry = []
        dCountry = []
        date = []
        duaration = []
        for row in self.data:
            fNumber.append(row[0])
            ftype.append(row[1])
            pName.append(row[2])
            capacity.append(row[3])
            sCountry.append(row[4])
            dCountry.append(row[5])
            date.append(row[6])
            duaration.append(row[7])
        return fNumber, ftype, pName, capacity, sCountry, dCountry, date, duaration

    def load_DataFromFile(self,path):
        with open(path, 'r', encoding='iso-8859-1',
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

    def load_Data(self):
        tableRows = 0
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
            # if int(row[5].split(":")[0]) >= int(24):
            #     row[5] = row[5][0:len(row[5])-1]
            self.tableWidget.setItem(
                tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
            self.tableWidget.setItem(
                tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
            self.tableWidget.setItem(
                tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))
            tableRows += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
