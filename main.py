from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QMainWindow, QTextEdit
from PyQt6.QtGui import QFont
import sys
from backend import ChatBot
import threading

 
API_KEY = 'your_api_key'
PROJECT_ID = 'your_project_id'
 
# Front-End
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = ChatBot(api_key=API_KEY,
                               project_id=PROJECT_ID)  # need to instantiate only once
 
        self.setWindowTitle('Gemini Chatbot')
        self.setMinimumSize(850, 500)  # size of the window 700 px width 500 px height
 
        # Add text area(chat area) widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setFont(QFont("Arial",16))
        self.chat_area.setGeometry(30, 30, 650, 400)  # x,y co-ordinates width and height
        # Add input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setFont(QFont("Arial",16))
        self.input_field.setGeometry(30, 450, 650, 30)
        self.input_field.returnPressed.connect(self.send_message)
 
        # Add Send Button widget
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(700, 450, 100, 30)
        self.send_button.clicked.connect(self.send_message)
        self.show()
 
    def send_message(self):
        user_input = self.input_field.text().strip()
        # append() is a method of QTextEdit()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color:#E9E9E9'>Bot: {response}</p>")
 
 
app = QApplication(sys.argv)
main_window = MainWindow()
sys.exit(app.exec())
 