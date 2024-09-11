from PyQt5.QtWidgets import QWidget, QLabel, QDoubleSpinBox, QHBoxLayout

class LabeledDoubleSpinBox(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QLabel()
        self.spinbox = QDoubleSpinBox()
        self.spinbox.setKeyboardTracking(False)
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.spinbox)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def setText(self, text: str) -> None:
        self.label.setText(text)

    def setRange(self, lo: float, hi: float) -> None:
        self.spinbox.setRange(lo,hi)
    
    def setValue(self, val: float) -> None:
        self.spinbox.setValue(val)
    
    def setSingleStep(self, val: float) -> None:
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
        
    @property
    def editingFinished(self):
        return self.spinbox.editingFinished
    
    @property
    def valueChanged(self):
        return self.spinbox.valueChanged 

    def value(self) -> float:
        return self.spinbox.value()