from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QSpinBox, QHBoxLayout
from PyQt5.QtCore import Qt

class LabeledSliderSpinBox(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.label = QLabel()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(self.slider_change)
        self.spinbox = QSpinBox()
        self.spinbox.setKeyboardTracking(False)
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

    def setRange(self, lo: int, hi: int) -> None:
        self.spinbox.setRange(lo,hi)
        self.slider.setMinimum(lo)
        self.slider.setMaximum(hi)
    
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
                
    @property
    def valueChanged(self):
        return self.spinbox.valueChanged 

    def value(self) -> int:
        return self.spinbox.value()