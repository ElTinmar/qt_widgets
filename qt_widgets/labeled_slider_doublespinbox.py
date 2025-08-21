from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QDoubleSpinBox, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

class LabeledSliderDoubleSpinBox(QWidget):

    slider_precision: int = 100

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.label = QLabel()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.sliderReleased.connect(self.slider_change)
        self.spinbox = QDoubleSpinBox()
        self.spinbox.setKeyboardTracking(False)
        self.spinbox.valueChanged.connect(self.spinbox_change)
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        layout.addWidget(self.spinbox)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def slider_change(self):
        value = self.slider.value() / self.slider_precision
        self.spinbox.setValue(value)

    def spinbox_change(self):
        value = int(self.spinbox.value() * self.slider_precision)
        self.slider.blockSignals(True)
        self.slider.setValue(value)
        self.slider.blockSignals(False)

    def setText(self, text: str) -> None:
        self.label.setText(text)

    def setRange(self, lo: float, hi: float) -> None:
        self.spinbox.setRange(lo,hi)
        self.slider.setMinimum(int(lo*self.slider_precision))
        self.slider.setMaximum(int(hi*self.slider_precision))

    def setMinimum(self, val: float) -> None:
        self.spinbox.setMinimum(val)
        self.slider.setMinimum(int(val*self.slider_precision))

    def setMaximum(self, val: float) -> None:
        self.spinbox.setMaximum(val)
        self.slider.setMaximum(int(val*self.slider_precision))

    def setValue(self, val: float) -> None:
        self.spinbox.setValue(val)
        self.slider.setValue(int(val*self.slider_precision))

    def setSingleStep(self, val: float) -> None:
        self.spinbox.setSingleStep(val)
        self.slider.setSingleStep(int(val*self.slider_precision))

    def setEnabled(self, enabled:bool) -> None:
        self.slider.setEnabled(enabled)
        self.spinbox.setEnabled(enabled)

    def stepUp(self):
        return self.spinbox.stepUp()
    
    def stepDown(self):
        return self.spinbox.stepDown()

    def stepBy(self, steps: int):
        return self.spinbox.stepBy(steps)
    
    def blockSignals(self, block: bool) -> None:
        self.slider.blockSignals(block)
        self.spinbox.blockSignals(block)

    @property
    def valueChanged(self):
        return self.spinbox.valueChanged 

    def value(self) -> float:
        return self.spinbox.value()

if __name__ == "__main__":

    app = QApplication([])
    widget = LabeledSliderDoubleSpinBox()
    widget.show()
    app.exec_()