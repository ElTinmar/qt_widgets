from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QDoubleSpinBox, QHBoxLayout
from PyQt5.QtCore import Qt

class LabeledSliderDoubleSpinBox(QWidget):

    slider_precision: int = 100

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.label = QLabel()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(self.slider_change)
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
        value = self.spinbox.value() * self.slider_precision
        self.slider.setValue(value)

    def setText(self, text: str) -> None:
        self.label.setText(text)

    def setRange(self, lo: float, hi: float) -> None:
        self.spinbox.setRange(lo,hi)
        self.slider.setMinimum(int(lo*self.slider_precision))
        self.slider.setMaximum(int(hi*self.slider_precision))
    
    def setValue(self, val: float) -> None:
        self.spinbox.setValue(val)
        self.slider.setValue(int(val*self.slider_precision))

    def setSingleStep(self, val: float) -> None:
        self.spinbox.setSingleStep(val)
        self.slider.setSingleStep(int(val*self.slider_precision))
    
    @property
    def valueChanged(self):
        return self.spinbox.valueChanged 

    def value(self) -> float:
        return self.spinbox.value()