
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from Main import mainclass

class Welcone_menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Click to Dust-Welcome")
        self.setWindowIcon(QIcon('MPF/PJ_CTD_Files/PJ_Logo/Logo.ico'))
       
        self.setMinimumSize(500,400)
        self.setMaximumSize(700,600)
        self.initUi()
        self.Layout()

    def initUi(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.title = QLabel("Welcome to Click to Dust 1\nTo play click on Start", self.central_widget)
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.btn_lvl_start = QPushButton("Start", self.central_widget)
        self.btn_lvl_start.setObjectName("startButton")  
        self.btn_lvl_start.clicked.connect(self.Start_btn)



        self.setStyleSheet("""
        #title {
            color: #ffffff;
            font-size: 20pt;
            padding: 20px;
            border:none;
            font-weight:Bold;
        }
        #startButton {
            font-size: 14pt;
            padding: 10px 20px;
            background-color:#ffffff;
            color: #000000;
            border-radius: 8px;
            font-weight:Bold;
        }
        #startButton:hover {
            background-color: #666666;
        }
        """)

    def Layout(self):
        gridlayout = QGridLayout()
        gridlayout.setContentsMargins(20, 20, 20, 20)  # حاشیه داخلی لایه
   
        self.central_widget.setLayout(gridlayout)

        gridlayout.addWidget(self.title, 0, 0)
        gridlayout.addWidget(self.btn_lvl_start, 1, 0)
    def Start_btn(self):
        try:
            self.start = mainclass()
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

    

def main_window():
    app = QApplication(sys.argv)
    window = Welcone_menu()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main_window()





















'''





from calendar import WEDNESDAY
import sys
import winreg
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from Main import mainclass

class Welcone_menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Click to Dust-Welcome")
        self.setWindowIcon(QIcon('MPF/PJ_CTD_Files/PJ_Logo/Logo.png'))
        self.resize(800, 500)
        
        # تشخیص تم ویندوز
        self.is_dark_theme = self.detect_windows_theme()
        
        self.initUi()
        self.Layout()
        self.apply_theme()

    def detect_windows_theme(self):
        """تشخیص تم ویندوز از رجیستری"""
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                               r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            winreg.CloseKey(key)
            return value == 0  # 0 = Dark Theme, 1 = Light Theme
        except:
            return False  # اگر خطا داد، Light Theme فرض کن

    def get_theme_colors(self):
        """رنگ‌های تم"""
        if self.is_dark_theme:
            return {
                'bg': '#2b2b2b',
                'text': '#ffffff',
                'button_bg': '#404040',
                'button_hover': '#505050',
                'button_text': '#ffffff'
            }
        else:
            return {
                'bg': '#ffffff',
                'text': '#000000',
                'button_bg': '#e1e1e1',
                'button_hover': '#d1d1d1',
                'button_text': '#000000'
            }

    def apply_theme(self):
        """اعمال تم"""
        colors = self.get_theme_colors()
        
        self.setStyleSheet(f"""
        QMainWindow {{
            background-color: {colors['bg']};
        }}
        QWidget {{
            background-color: {colors['bg']};
        }}
        #title {{
            color: {colors['text']};
            font-size: 20pt;
            padding: 20px;
            border: none;
            font-weight: Bold;
        }}
        #startButton {{
            font-size: 14pt;
            padding: 10px 20px;
            background-color: {colors['button_bg']};
            color: {colors['button_text']};
            border-radius: 8px;
            font-weight: Bold;
        }}
        #startButton:hover {{
            background-color: {colors['button_hover']};
        }}
        """)

    def initUi(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.title = QLabel("Welcome to Click to Dust 1\nTo play click on Play Button", self.central_widget)
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.btn_lvl_start = QPushButton("Start", self.central_widget)
        self.btn_lvl_start.setObjectName("startButton")  
        self.btn_lvl_start.clicked.connect(self.Start_btn)

    def Layout(self):
        gridlayout = QGridLayout()
        gridlayout.setContentsMargins(20, 20, 20, 20)
        gridlayout.setVerticalSpacing(15)
        self.central_widget.setLayout(gridlayout)

        gridlayout.addWidget(self.title, 0, 0)
        gridlayout.addWidget(self.btn_lvl_start, 1, 0)

    def Start_btn(self):
        try:
            self.start = mainclass()
            self.start.show()
            self.close()
            
        except Exception as e:
            error_msg = QMessageBox()
            error_msg.setWindowIcon(QIcon('MPF/PJ_CTD_Files/PJ_Logo/Logo.png'))
            error_msg.setWindowTitle("Fatal Error : Code 403")
            error_msg.setText("Problem opening a new window")
            error_msg.setDetailedText(f"Error Detail\n{str(e)}")
            error_msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            
            # اعمال تم به MessageBox
            colors = self.get_theme_colors()
            error_msg.setStyleSheet(f"""
                QMessageBox {{
                    background-color: {colors['bg']};
                    color: {colors['text']};
                }}
                QMessageBox QPushButton {{
                    background-color: {colors['button_bg']};
                    color: {colors['button_text']};
                    border: 1px solid #666666;
                    border-radius: 4px;
                    padding: 5px 15px;
                    min-width: 60px;
                }}
                QMessageBox QPushButton:hover {{
                    background-color: {colors['button_hover']};
                }}
            """)
            
            error_msg.exec()

def main_window():
    app = QApplication(sys.argv)
    window = Welcone_menu()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main_window()




'''
