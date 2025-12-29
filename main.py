from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QComboBox, QLabel, QFrame
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from deep_translator import GoogleTranslator

class GMTranslator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GM-TRANSLATION")
        self.setGeometry(300, 200, 500, 400)
        self.setStyleSheet("background-color: #121212; color: white;")

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # Input Text
        layout.addWidget(QLabel("Input Text:"))
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Type your text here...")
        self.input_text.setFont(QFont("Arial", 12))
        self.input_text.setStyleSheet("background-color: #1e1e1e; color: white;")
        layout.addWidget(self.input_text)

        # Languages Selection
        lang_layout = QHBoxLayout()
        self.source_lang = QComboBox()
        self.dest_lang = QComboBox()
        languages = {
            "English": "en",
            "Persian": "fa",
            "French": "fr",
            "German": "de",
            "Spanish": "es"
        }
        for lang in languages:
            self.source_lang.addItem(lang)
            self.dest_lang.addItem(lang)

        lang_layout.addWidget(QLabel("Source:"))
        lang_layout.addWidget(self.source_lang)
        lang_layout.addWidget(QLabel("Target:"))
        lang_layout.addWidget(self.dest_lang)
        layout.addLayout(lang_layout)

        # Translate Button
        self.translate_button = QPushButton("Translate")
        self.translate_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                padding: 6px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.translate_button.clicked.connect(self.translate_text)
        layout.addWidget(self.translate_button)

        # Output Text
        layout.addWidget(QLabel("Translation:"))
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setFont(QFont("Arial", 12))
        self.output_text.setStyleSheet("background-color: #1e1e1e; color: white;")
        layout.addWidget(self.output_text)

        # Add a line separator
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("color: #444444;")
        layout.addWidget(line)

        # Footer
        footer = QLabel("GM-TRANSLATION © 2025")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: #888888; font-size: 10px;")
        layout.addWidget(footer)

        self.setLayout(layout)

        # Mapping for translator
        self.lang_map = languages

    def translate_text(self):
        text = self.input_text.toPlainText().strip()
        if not text:
            self.output_text.setPlainText("Please enter some text to translate.")
            return

        src = self.lang_map[self.source_lang.currentText()]
        dest = self.lang_map[self.dest_lang.currentText()]

        if src == dest:
            self.output_text.setPlainText("Source and target languages are the same!")
            return

        try:
            translated = GoogleTranslator(source=src, target=dest).translate(text)
            self.output_text.setPlainText(translated)
        except Exception as e:
            self.output_text.setPlainText(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication([])
    window = GMTranslator()
    window.show()
    app.exec()
