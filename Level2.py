
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import Main
from Main import *


class p2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Click to Dust 1-Level2")
        self.setWindowIcon(QIcon('MPF/PJ_CTD_Files/PJ_Logo/Logo.ico'))

        self.setFixedSize(600, 300)
        self.score = 0
        self.initUI()   
        self.Layout()
        
    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.TextBox = QLineEdit(self.central_widget)
        self.TextBox.setStyleSheet("""
            QLineEdit {
                height: 60px; 
                font-weight: bold;
                font-size: 18pt;
                border-radius: 20px;
                
                color: white;
            }
        """)
        self.TextBox.setText("2XP active")
        self.TextBox.setReadOnly(True)
        self.TextBox.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        self.btn_plus = QPushButton(text="+")
        self.btn_plus.setStyleSheet("""
            QPushButton {
                height: 60px; 
                font-size: 20pt;
                font-weight: bold;
                background: red;
                border-radius: 30px;
                color: white;
                border: none;
            }
            QPushButton:hover {
                background: darkred;
            }
          
        """)
        self.btn_plus.clicked.connect(self.ScoreBtn)


        self.mission_One = QLabel("Mission 1: 200 clicks to pass")
        self.mission_One.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.mission_One.setStyleSheet("""
            QLabel {
                font-size: 16pt;
                font-weight: bold;
                color: #333;
                padding: 10px;
                margin: 10px;
            }
        """)


        self.mission_Two = QLabel("Mission 2: 300 clicks to pass")
        self.mission_Two.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.mission_Two.setStyleSheet("""
            QLabel {
                font-size: 16pt;
                font-weight: bold;
                color: #333;
                padding: 10px;
                margin: 10px;
            }
        """)

        self.btn_next = QPushButton("next level")
        self.btn_next.setStyleSheet("""
            QPushButton {
                padding: 15px;
                font-size: 14pt;
                font-weight: bold;
               background: green;
                border-radius: 15px;
                color: white;
                border: none;
            }
            QPushButton:hover {
                background: darkgreen;
            }
        """)
        self.btn_next.hide()
        self.btn_back = QPushButton("Back to Main Menu")
        self.btn_back.setStyleSheet("""
            QPushButton {
                padding: 15px;
                font-size: 14pt;
                font-weight: bold;
               background: #B5B5B5;
                border-radius: 15px;
                color: white;
                border: none;
            }
            QPushButton:hover {
                background: #9E9E9E;
                
            }
        """)
        self.btn_back.clicked.connect(self.back_to_main)
        self.timer = QTimer()

        self.timer.timeout.connect(self.decrease_score)
        self.timer.start(3000)
    def Layout(self):
        
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        
     
 
        

        self.grid_layout.addWidget(self.TextBox, 0, 0, 1, 2)
        self.grid_layout.addWidget(self.btn_plus, 1, 1)
        

        self.grid_layout.addWidget(self.mission_One, 1, 0, 1, 1)
        

        self.grid_layout.addWidget(self.mission_Two, 2, 0, 1, 1)
        

        self.grid_layout.setRowStretch(3, 1)

        self.grid_layout.addWidget(self.btn_back, 2, 1)
        self.grid_layout.addWidget(self.btn_next, 3, 1)




    def ScoreBtn(self):
     self.score += 2

     self.record=self.score
     self.TextBox.setText(str(self.score))


     if 200 <= self.score < 300:
        self.mission_One.setStyleSheet("""
            QLabel {
                color: green;
                font-size: 16pt;
                font-weight: bold;
                padding: 10px;
                margin: 10px;
            }
        """)
        self.mission_One.setText("✓ Mission 1: Completed!")

     elif self.score >= 300:
        self.mission_Two.setStyleSheet("""
            QLabel {
                color: green;
                font-size: 16pt;
                font-weight: bold;
                padding: 10px;
                margin: 10px;
            }
        """)
        self.btn_plus.hide()
        self.mission_One.setText("✓ All missions Completed!\nYou can go to next level!")
        self.mission_Two.setText("")
        self.grid_layout.addWidget(self.btn_back, 2, 1)


    def back_to_main(self):
            self.start = Main.mainclass()
            self.start.show()
            self.start.btn_lvl2.setText("practice 2")
            self.start.btn_lvl2.show()

            self.close()




    def decrease_score(self):

        if self.score >= 300:
            self.timer.stop()
        elif self.score > 0:
            self.score -= 5
            self.TextBox.setText(str(self.score))


def main_window():
    app = QApplication(sys.argv)
    

    font = QFont()
    font.setFamily("Arial,bold")
    font.setPointSize(10)
    app.setFont(font)
    
    window = p2()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main_window()
