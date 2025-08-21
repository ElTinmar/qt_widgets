from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QSpinBox, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

class LabeledSliderSpinBox(QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.label = QLabel()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.sliderMoved.connect(self.slider_change)
        self.slider.sliderReleased.connect(self.slider_released)
        self.spinbox = QSpinBox()
        self.spinbox.setKeyboardTracking(False)
        self.spinbox.valueChanged.connect(self.spinbox_change)
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        layout.addWidget(self.spinbox)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def slider_released(self):
        print('slider released')
        self.spinbox.setValue(self.slider.value())

    def slider_change(self):
        self.spinbox.blockSignals(True)
        self.spinbox.setValue(self.slider.value())
        self.spinbox.blockSignals(False)

    def spinbox_change(self):
        self.slider.blockSignals(True)
        self.slider.setValue(self.spinbox.value())
        self.slider.blockSignals(False)
        
    def setText(self, text: str) -> None:
        self.label.setText(text)

    def setRange(self, lo: int, hi: int) -> None:
        self.spinbox.setRange(lo,hi)
        self.slider.setMinimum(lo)
        self.slider.setMaximum(hi)

    def setMinimum(self, val: int) -> None:
        self.spinbox.setMinimum(val)
        self.slider.setMinimum(val)

    def setMaximum(self, val: int) -> None:
        self.spinbox.setMaximum(val)
        self.slider.setMaximum(val)

    def setValue(self, val: int) -> None:
        self.spinbox.setValue(val)
        self.slider.setValue(val)

    def setSingleStep(self, val: int) -> None:
        self.spinbox.setSingleStep(val)
        self.slider.setSingleStep(val)

    def setEnabled(self, enabled:bool) -> None:
        self.slider.setEnabled(enabled)
        self.spinbox.setEnabled(enabled)

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

    def printslot():
        print('triggered')

    app = QApplication([])
    widget = LabeledSliderSpinBox()
    widget.valueChanged.connect(printslot)
    widget.show()
    app.exec_()