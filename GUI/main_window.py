from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog
from GUI.style.style_Qt import CONST_MAIN_WINDOW
from Logics.query_logic import popup_window, get_request, post_request

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Работа с API")
        self.setFixedSize(350, 300)
        self.setWindowIcon(QIcon(r"image\icon.webp"))
        self.setStyleSheet(CONST_MAIN_WINDOW)

        central_widget = QWidget()
        control_UI = QVBoxLayout()
        
        application_title = QLabel(text="Введите ваш API")
        self.api = QLineEdit()
        
        start_get = QPushButton("Произвести GET запрос")
        start_get.clicked.connect(self.get_m)
        
        start_post = QPushButton(text="Произвести POST запрос")
        start_post.clicked.connect(self.post_m)
        
        control_UI.addWidget(application_title, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.api)
        control_UI.addWidget(start_get)
        control_UI.addWidget(start_post)
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def get_m(self):
        try:
            api_r = self.api.text()
            path = QFileDialog().getExistingDirectory(self, "Выберите папку сохранения")
        except:
            popup_window("Ошибка", "Не удалось считать данные которые вы предоставили")
        
        result = get_request(api_r, path)
        
        if result == True:
            popup_window("Успех", "Все получлось")
        else:
            popup_window("Ошибка", 
                         "Не вышло записать данные в json")
            
    def post_m(self):
        try:
            api_r = self.api.text()
            path = QFileDialog().getExistingDirectory(self, "Выберите папку сохранения")
        except:
            popup_window("Ошибка", "Не удалось считать данные которые вы предоставили")
        
        result = post_request(api_r, path)
        
        if result == True:
            popup_window("Успех", "Все получлось")
        else:
            popup_window("Ошибка", 
                         "Не вышло записать данные в json")
        
        
        
        
        

