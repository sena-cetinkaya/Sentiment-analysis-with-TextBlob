# Sentiment Analysis Libraries
from textblob import TextBlob

# PyQT5 GUI Libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QFont
from PyQt5.QtCore import Qt
import sys


# PyQT5 Interface Func.
def new_window():
    mbox = QMessageBox(window)
    mbox.setWindowTitle("Result")
    mbox.setStyleSheet("background-color: lightgray; color: darkred; ")
    mbox.setFont(QFont("Comic Sans MS", 15, QFont.Bold))
    mbox.setText(analyze_sentiment(sentence.text()))
    mbox.setStandardButtons(QMessageBox.Ok)
    sentence.clear()
    mbox.show()
    mbox.exec_()

def close_buton():
    sys.exit()

# Sentiment Analysis Func.
def analyze_sentiment(text):
    analysis = TextBlob(text)

    if analysis.sentiment.polarity > 0:
        return "Positive :)"
    elif analysis.sentiment.polarity == 0:
        return "Neutral :|"
    else:
        return "Negative :("

if __name__ == '__main__':
    # PyQT5 Interface
    app = QApplication(sys.argv)
    qp = QPalette()
    qp.setColor(QPalette.Window, Qt.gray)
    app.setPalette(qp)

    window = QWidget()
    window.setWindowTitle("Sentiment Analysis")
    window.setFixedSize(800, 500)

    label_1 = QLabel(window)
    label_1.setText("Sentiment Analysis")
    label_1.setFixedSize(400, 50)
    label_1.setStyleSheet("color: darkred;")
    label_1.setFont(QFont("Comic Sans MS", 20, QFont.Bold))
    label_1.move(200, 40)
    label_1.show()

    label_2 = QLabel(window)
    label_2.setText("Enter the sentence:")
    label_2.setFixedSize(450, 100)
    label_2.setFont(QFont("Comic Sans MS", 15, QFont.Bold))
    label_2.setStyleSheet("color: white;")
    label_2.move(100, 100)
    label_2.show()

    sentence = QLineEdit(window)
    sentence.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
    sentence.setStyleSheet("border: 1px solid white; background-color: lightgray; color: darkred;")
    sentence.move(400, 125)
    sentence.resize(250, 50)

    btn = QPushButton(window)
    btn.setText("Show Result")
    btn.setFixedSize(300, 50)
    btn.setFont(QFont("Comic Sans MS", 15, QFont.Bold))
    btn.setStyleSheet("background-color: gray; color: white;")
    btn.move(250, 250)
    btn.show()
    btn.clicked.connect(new_window)

    close_btn = QPushButton(window)
    close_btn.setText("Close")
    close_btn.setFixedSize(150, 50)
    close_btn.move(330, 400)
    close_btn.setFont(QFont("Comic Sans MS", 15, QFont.Bold))
    close_btn.setStyleSheet("background-color: gray; color: white;")
    close_btn.show()
    close_btn.clicked.connect(close_buton)

    window.show()
    app.exec_()
