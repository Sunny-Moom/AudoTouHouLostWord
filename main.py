import time
from contextlib import redirect_stdout

from PyQt5.QtGui import QTextCursor

import utils.adb_lw as adb
import utils.ocr_lw as ocr
import utils.cv_lw as cv
import utils.other_lw as ot
import scripts.startini as starting

path = './config/settings.ini'  # 配置文件路径

import sys
import os
import asyncio
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal


class Worker(QThread):
    output = pyqtSignal(str)

    def run(self):
        # 由于main_run是一个同步函数，我们在这里模拟异步行为
        # 实际上，你需要将main_run内部的逻辑调整为异步模式
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.async_main_run())

    async def async_main_run(self):
        # 你的main_run逻辑，改为异步版本
        # 使用await asyncio.sleep()替代time.sleep()
        for i in range(7):
            self.output.emit(f"这是第{i}次输出")
            # 更多逻辑...
            await asyncio.sleep(1)  # 举例替换time.sleep(1)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Demo')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()
        self.textEdit = QTextEdit()
        self.startButton = QPushButton('开始')
        self.stopButton = QPushButton('停止')

        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.startButton)
        self.layout.addWidget(self.stopButton)
        self.setLayout(self.layout)

        self.startButton.clicked.connect(self.startScript)
        self.stopButton.clicked.connect(self.stopScript)

        self.worker = Worker()
        self.worker.output.connect(self.updateText)

    def startScript(self):
        if not self.worker.isRunning():
            self.worker.start()

    def stopScript(self):
        # 停止线程的逻辑需要根据你的需求来实现，这里只是个示例
        self.worker.terminate()  # 注意：terminate()是比较粗暴的停止线程方法，可能会有副作用
        self.textEdit.append("脚本已停止")

    def updateText(self, text):
        self.textEdit.append(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
