from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QHBoxLayout
from PyQt5.QtWidgets import QApplication

class LabeledSpinBox(QWidget):

    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.label = QLabel()

        self.spinbox = QSpinBox()
        self.spinbox.setKeyboardTracking(False)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.spinbox)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    def setText(self, text: str) -> None:
        self.label.setText(text)

    def setRange(self, lo: int, hi: int) -> None:
        self.spinbox.setRange(lo,hi)

    def setMinimum(self, val: int) -> None:
        self.spinbox.setMinimum(val)

    def setMaximum(self, val: int) -> None:
        self.spinbox.setMaximum(val)
    
    def setValue(self, val: int) -> None:
        self.spinbox.setValue(val)

    def setSingleStep(self, val: int) -> None:
        self.spinbox.setSingleStep(val)

    def setEnabled(self, enabled:bool) -> None:
        self.spinbox.setEnabled(enabled)
    
    def minimum(self):
        return self.spinbox.minimum()

    def maximum(self):
        return self.spinbox.maximum()

    def singleStep(self):
        return self.spinbox.singleStep()
    
    def isEnabled(self):
        return self.spinbox.isEnabled()

    def stepUp(self):
        return self.spinbox.stepUp()
    
    def stepDown(self):
        return self.spinbox.stepDown()

    def stepBy(self, steps: int):
        return self.spinbox.stepBy(steps)
        
    @property
    def valueChanged(self):
        return self.spinbox.valueChanged 

    def value(self) -> int:
        return self.spinbox.value()

if __name__ == "__main__":

    app = QApplication([])
    widget = LabeledSpinBox()
    widget.show()
    app.exec_()