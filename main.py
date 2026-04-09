import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QWidget, QMenu, QWidgetAction
from PyQt6.QtGui import QAction, QFont
from PyQt6.QtCore import Qt
import os

def load_text():
    with open("content.txt") as f: 
        return f.read()


class LongTextWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Long Paragraph Example")
        self.setMinimumSize(50, 50)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # 1. Create a central widget and a layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 2. Create the label for the text
        text_label = QLabel()
        
        # Example of a long paragraph
        long_paragraph = load_text()
        font = QFont("arial", 30)
        text_label.setText(long_paragraph)
        text_label.setFont(font)
        # 3. Enable Word Wrap
        text_label.setWordWrap(True)
        
        # Optional: Align text to the top
        text_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        # 4. Add a Scroll Area (incase the text is longer than the window height)
        self.scrol = QScrollArea()
        self.scrol.setWidgetResizable(True)
        self.scrol.setWidget(text_label)
        self.scrol.setStyleSheet("background: transparent; border: none;")
        self.scrol.viewport().setStyleSheet("background: transparent;")
        

        layout.addWidget(self.scrol)

        central_widget.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 0.5); /* Dark grey, 70% opacity */
                border-radius: 10px;
            }
            QLabel {
                color: white; /* Text stays 100% solid white */
                background-color: transparent; /* Ensure label doesn't have its own box */
            }""")
            
        def hide_log():
            geo = self.geometry()
            is_frameless = self.windowFlags() & Qt.WindowType.FramelessWindowHint
            print(is_frameless)
            if is_frameless == 0:
                self.setWindowFlags(
        Qt.WindowType.FramelessWindowHint |
        Qt.WindowType.WindowStaysOnTopHint
)
                self.setGeometry(geo)
                self.show()
            else:
                 self.setWindowFlags(Qt.WindowType.Window)
                 self.show()
                 self.setGeometry(geo)
                 
        self.hide_log = hide_log

    def contextMenuEvent(self, event):
            menu = QMenu(self)
            ionknowwhattocallthis = QAction("hide")
            quitm = QAction("quit")
            ionknowwhattocallthis.triggered.connect(self.hide_log)
            quitm.triggered.connect(lambda: QApplication.instance().quit())
            menu.addActions([ionknowwhattocallthis, quitm])
            menu.exec(event.globalPos())

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LongTextWindow()
    window.show()
    sys.exit(app.exec())