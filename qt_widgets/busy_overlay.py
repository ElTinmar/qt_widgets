from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

class Spinner(QWidget):

    def __init__(self, parent=None, radius=20, line_width=4, speed=50):
        super().__init__(parent)
        self.angle = 0
        self.radius = radius
        self.line_width = line_width
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.rotate)
        self.timer.start(speed)
        self.setFixedSize(radius * 2 + line_width * 2, radius * 2 + line_width * 2)

    def rotate(self):
        self.angle = (self.angle + 30) % 360
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor("white"), self.line_width)
        painter.setPen(pen)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.angle)
        painter.drawArc(-self.radius, -self.radius, 2*self.radius, 2*self.radius, 0, 270*16)

class BusyOverlay(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("background: rgba(0, 0, 0, 128);")
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        self.spinner = Spinner(self)
        layout.addWidget(self.spinner, alignment=Qt.AlignCenter)
        self.hide()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 128))
        super().paintEvent(event)

    def show_overlay(self):
        self.resize(self.parent().size())
        self.raise_()
        self.show()

    def hide_overlay(self):
        self.hide()

if __name__ == "__main__":

    app = QApplication([])

    window = QMainWindow()
    window.setFixedSize(400, 300)
    overlay = BusyOverlay(window)
    window.show()

    QTimer.singleShot(1000, overlay.show_overlay)
    QTimer.singleShot(4000, overlay.hide_overlay)
    QTimer.singleShot(1000, overlay.show_overlay)

    app.exec_()
