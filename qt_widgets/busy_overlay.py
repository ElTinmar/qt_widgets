from qtpy.QtCore import Qt, QTimer
from qtpy.QtGui import QPainter, QColor, QPen
from qtpy.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

class Spinner(QWidget):

    def __init__(self, parent=None, radius=20, line_width=4, speed=50, color='white'):

        super().__init__(parent)
        self.angle = 0
        self.radius = radius
        self.line_width = line_width
        self.color = color

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.rotate)
        self.timer.start(speed)
        
        self.setFixedSize(radius * 2 + line_width * 2 + 2, radius * 2 + line_width * 2 + 2)

    def rotate(self):
        self.angle = (self.angle + 12) % 360 
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Center the coordinate system in the widget
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.angle)
        
        pen = QPen(QColor(self.color), self.line_width)
        painter.setPen(pen)
        
        # Qt's drawArc spans 1/16th of a degree per unit
        painter.drawArc(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius, 0, 270 * 16)

class BusyOverlay(QWidget):

    def __init__(self, parent):
        
        super().__init__(parent)
        # Block user interactions with background widgets
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        
        self.spinner = Spinner(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.spinner, alignment=Qt.AlignCenter)
        
        # Install an event filter on the parent to auto-resize when the window sizes change
        if parent:
            parent.installEventFilter(self)
            
        self.hide()

    def eventFilter(self, obj, event):
        # Dynamically follow parent size changes
        if obj == self.parent() and event.type() == event.Resize:
            self.resize(obj.size())
        return super().eventFilter(obj, event)

    def paintEvent(self, event):
        painter = QPainter(self)
        # Semi-transparent black backdrop
        painter.fillRect(self.rect(), QColor(0, 0, 0, 128))

    def show_overlay(self):
        if self.parent():
            self.resize(self.parent().size())
        self.raise_()
        self.show()

    def hide_overlay(self):
        self.hide()

if __name__ == "__main__":
    app = QApplication([])

    window = QMainWindow()
    window.setWindowTitle("Busy Overlay Test")
    #window.setFixedSize(400, 300)
    
    # Instantiate overlay with window as parent
    overlay = BusyOverlay(window)
    window.show()

    # Fixed timeline intervals
    QTimer.singleShot(1000, overlay.show_overlay)  # Appears at 1s
    QTimer.singleShot(4000, overlay.hide_overlay)  # Disappears at 4s
    QTimer.singleShot(5000, overlay.show_overlay)  # Re-appears at 5s

    app.exec()