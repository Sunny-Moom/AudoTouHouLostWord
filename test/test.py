# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer


class CounterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("计数器")
        self.setGeometry(100, 100, 300, 200)

        self.counter = 2
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_counter)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        start_button = QPushButton("开始", self)
        start_button.clicked.connect(self.start_counting)

        stop_button = QPushButton("停止", self)
        stop_button.clicked.connect(self.stop_counting)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(start_button)
        layout.addWidget(stop_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_counting(self):
        self.timer.start(1000)  # 1 second interval

    def stop_counting(self):
        self.timer.stop()

    def update_counter(self):
        self.text_edit.append(str(self.counter))
        self.counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CounterApp()
    window.show()
    sys.exit(app.exec_())
