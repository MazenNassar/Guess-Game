import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QPalette, QColor
from PyQt6.QtCore import Qt
from random import randint

class Root(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Guessing Game")
        self.rd()
        self.initUI()

    def initUI(self):
        self.title_label = QLabel("Enter A Number From 1 to 10")
        self.level_label = QLabel(f"Level: {self.level}")
        self.chances_label = QLabel(f"Chances: {self.ch}")
        self.totals_label = QLabel(f"Total Score: {self.ts}")
        self.entry = QLineEdit()
        self.button = QPushButton('Guess')
        self.label = QLabel("")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        layout.addWidget(self.title_label)
        layout.addWidget(self.level_label)
        layout.addWidget(self.chances_label)
        layout.addWidget(self.totals_label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.apply_stylesheet()

        self.button.clicked.connect(self.guess)

        self.adjustWindowSize()
    def apply_stylesheet(self):
        style_sheet = """
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit {
                font-size: 14px;
                padding: 6px;
                border: 1px solid #ccc;
            }
            QPushButton {
                font-size: 14px;
                padding: 8px;
                border: none;
                background-color: #4caf50;
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3c893d;
            }
        """
        self.setStyleSheet(style_sheet)
    def adjustWindowSize(self):
        self.adjustSize()
    def rd(self):
        try:
            with open("gm.tmp", "r") as fg:
                lst = fg.readlines()
                self.ch = int(lst[0])
                if self.ch == "":
                    self.ch = 10
                elif self.ch < 1:
                    self.ch = 10
                self.ts = round(float(lst[1]))
                if self.ts == "":
                    self.ts = 0
                self.tn = int(lst[2])
                if self.tn == "":
                    tn = randint(1, 10)
                self.score = round(float(lst[3]))
                if self.score == "":
                    self.score = 100
                self.level = int(lst[4])
                if self.level == "":
                    self.level = 1
                self.lvl1 = int(lst[5])
                if self.lvl1 == "":
                    self.lvl1 = 1
        except FileNotFoundError:
            self.ch = 10
            self.ts = 0
            tn = randint(1, 10)
            self.score = 100
            self.level = 1
            self.lvl1 = 1

    def updasy(self):
        lst = [str(self.ch), str(self.ts), str(self.tn), str(self.score), str(self.level), str(self.lvl1)]
        with open("gm.tmp", "w") as fg:
            fg.write("\n".join(lst))
            fg.close()
        self.level_label.setText(f"Level: {self.level}")
        self.chances_label.setText(f"Chances: {self.ch}")
        self.totals_label.setText(f"Total Score: {round(self.ts)}")

    def updlvl1(self):
        if self.lvl1 == 1:
            self.ch = 10
        elif self.lvl1 == 2:
            self.ch = 9
        elif self.lvl1 == 3:
            self.ch = 8
        elif self.lvl1 == 4:
            self.ch = 7
        elif self.lvl1 == 5:
            self.ch = 6
        elif self.lvl1 == 6:
            self.ch = 5
        elif self.lvl1 == 7:
            self.ch = 4
        elif self.lvl1 == 8:
            self.ch = 3
        elif self.lvl1 == 9:
            self.ch = 2
        elif self.lvl1 == 10:
            self.ch = 1

    def guess(self):
        if self.lvl1 > 10:
            self.lvl1 = 1
        if self.lvl1 == 1:
            self.punish = 10
        elif self.lvl1 == 2:
            self.punish = 11.11111111111111
        elif self.lvl1 == 3:
            self.punish = 12.5
        elif self.lvl1 == 4:
            self.punish = 14.285714285714286
        elif self.lvl1 == 5:
            self.punish = 16.666666666666668
        elif self.lvl1 == 6:
            self.punish = 20.0
        elif self.lvl1 == 7:
            self.punish = 25.0
        elif self.lvl1 == 8:
            self.punish = 33.333333333333336
        elif self.lvl1 == 9:
            self.punish = 50.0
        elif self.lvl1 == 10:
            self.punish = 100.0
        self.tn = randint(1, 10)
        try:
            with open("gm.tmp", "r") as tnr:
                self.tn = int(tnr.readlines()[2])
                if self.tn == "":
                    self.tn = randint(1, 10)
                tnr.close()

        except FileNotFoundError:
            pass
        gn = int(self.entry.text())
        if self.tn == gn:
            self.ts = self.ts + self.score
            self.lvl1 += 1
            self.level += 1
            self.updlvl1()
            self.entry.clear()
            self.label.setText("True Guess")
            self.tn = randint(1, 10)
            self.updasy()
            self.score = 100
            return
        elif gn < self.tn:
            self.label.setText("Go Up")
        elif gn > self.tn:
            self.label.setText("Go Down")
        self.entry.clear()
        self.score = self.score - self.punish
        self.ch = self.ch - 1
        if self.ch < 1:
            self.updlvl1()
            self.label.setText("You Lost This Round")
            self.score = 100
        self.updasy()


    def onclick(self):
        self.guess()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = Root()
    root.show()
    sys.exit(app.exec())
