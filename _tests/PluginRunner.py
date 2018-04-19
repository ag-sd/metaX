import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QVBoxLayout,
                             QProgressBar, QPushButton, QStyleFactory, QGroupBox, QTextEdit)
from PyQt5.QtCore import Qt


class PluginRunner(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label = QLabel('script...')
        label.setStyleSheet("background-color: white;")

        progress = QProgressBar()
        progress.setAlignment(Qt.AlignCenter)

        text = QTextEdit()
        text.setStyleSheet("background-color: white; color: green")

        groupBox = QGroupBox(" Plugin Messages ")
        groupLayout = QVBoxLayout()
        groupLayout.addWidget(text)
        groupBox.setLayout(groupLayout)

        btn = QPushButton('Download', self)
        btn.clicked.connect(self.download)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(progress)

        layout.addWidget(groupBox)
        layout.addWidget(btn)

        self.setLayout(layout)

        self.setWindowTitle('Review')
        self.show()

    def download(self, progress):
        completed = 0
        while completed < 100:
            completed += 0.00001
            progress.setValue(completed)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("GTK+"))
    ex = PluginRunner()
    sys.exit(app.exec_())
