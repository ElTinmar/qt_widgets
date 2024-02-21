from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QDoubleSpinBox, QHBoxLayout
from PyQt5.QtCore import Qt

class LabeledSliderSpinBox(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.label = QLabel()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(self.slider_change)
        self.spinbox = QDoubleSpinBox()
        self.spinbox.valueChanged.connect(self.spinbox_change)
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        layout.addWidget(self.spinbox)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def slider_change(self):
        self.spinbox.setValue(self.slider.value())

    def spinbox_change(self):
        self.slider.setValue(self.spinbox.value())

    def setText(self, text: str) -> None:
        self.label.setText(text)

    def setRange(self, lo: float, hi: float) -> None:
        self.spinbox.setRange(lo,hi)
        self.slider.setMinimum(lo)
        self.slider.setMaximum(hi)
    
    def setValue(self, val: float) -> None:
        self.spinbox.setValue(val)
        self.slider.setValue(val)

    def setSingleStep(self, val: float) -> None:
        self.spinbox.setSingleStep(val)
        self.slider.setSingleStep(val)

    @property
    def valueChanged(self):
        return self.spinbox.valueChanged 

    def value(self) -> float:
        return self.spinbox.value()