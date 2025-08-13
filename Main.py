import sys
import level1
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import level2
from level2 import *
class mainclass(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Click to Dust 1-Home")
        self.setWindowIcon(QIcon('MPF/PJ_CTD_Files/PJ_Logo/Logo.ico'))
        self.setMinimumSize(600,800)
        self.initUI()
        self.Layout()
        self.score()
    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.title=QLabel(self.central_widget,text="\nChoose a level to play.")
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignCenter)
        self.btn_lvl1=QPushButton(self.central_widget,text="practice 1")
        self.btn_lvl1.clicked.connect(self.Start_lvl1)
        self.btn_lvl1.setObjectName("button1")
        self.btn_lvl2=QPushButton(self.central_widget,text="Locked")
        self.btn_lvl2.setObjectName("button2")
        self.btn_lvl2.hide()
        self.btn_lvl2.clicked.connect(self.Start_lvl2)
        self.btn_lvl3=QPushButton(self.central_widget,text="Soon")
        self.btn_lvl3.setObjectName("button3")
        self.btn_lvl3.hide()
        self.setStyleSheet("""
            #title{
            font-weight:bold;
            font-size:30pt; 
            }
            #button1{
            color:lightgreen;
            background:darkgreen;
            padding:30px;
            margin:70px;
            border-radius:20px;
            font-weight:bold;
            font-size:13pt; 
           
            }
            #button1::hover{
            background:green;
            color:darkgreen;
            }
            #button2{
            color:yellow;
            background:darkorange;
            padding:30px;
            margin:70px;
            border-radius:20px;
            font-weight:bold;
            font-size:13pt; 
            }
            #button2::hover{
            background:yellow;
            color:darkorange;
            }            
            #button3{
            color:red;
            background:darkred;
            padding:30px;
            margin:70px;
             border-radius:20px;
             font-weight:bold;
             font-size:13pt; 
            }
            #button3::hover{
            background:red;
            color:darkred;
            }
        """)
    def Layout(self):
        gridlayout = QGridLayout()

        self.central_widget.setLayout(gridlayout)

        gridlayout.addWidget(self.title, 0, 1,1,2)
        gridlayout.addWidget(self.btn_lvl1,1,1,2,2)
        gridlayout.addWidget(self.btn_lvl2,2,1,2,2)
        gridlayout.addWidget(self.btn_lvl3,3,1,2,2)


    def score(self):
        self.record=level1.p1()
        print(self.score)

    def Start_lvl1(self):
        try:
            self.start = level1.p1()
            self.start.show()
            self.close()

        except Exception as e:

            error_msg = QMessageBox()
            error_msg.setWindowIcon(QIcon('MPF/PJ_CTD_Files/PJ_Logo/Logo.png'))
            error_msg.setWindowTitle("Fatal Error : Code 403")
            error_msg.setText("Problem opening a new window")
            error_msg.setDetailedText(f"Error Detail\n{str(e)}")
            error_msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            error_msg.exec()


    def Start_lvl2(self):
        self.start=level2.p2()
        self.start.show()
        self.close()





def main_window():
    app = QApplication(sys.argv)
    window = mainclass()
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main_window()
