import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(903, 582)
        loadUi("User.ui", self)

        # Connect each button to its corresponding function
        self.pushButton.clicked.connect(self.run_script)
        self.pushButton_3.clicked.connect(self.run_script)
        self.pushButton_5.clicked.connect(self.run_script)
        self.pushButton_4.clicked.connect(self.run_script)
    def run_script(self):
        sender_button = self.sender()
        try:
            if sender_button == self.pushButton_3:
                script_path = "graph.py"

            elif sender_button == self.pushButton_5:
                script_path = "multiLevelSearching.py"
                
            elif sender_button == self.pushButton:
                script_path = "crudofUser.py"

            elif sender_button == self.pushButton_4:
                script_path = "all_graph_types.py"
            else:
                return

            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:

            print(f"Error running script: {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
