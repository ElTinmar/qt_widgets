from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QHBoxLayout

class LabeledComboBox(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.label = QLabel()
        self.combobox = QComboBox()
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.combobox)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def setText(self, text: str) -> None:
        self.label.setText(text)

    def addItem(self, item: str) -> None:
        self.combobox.addItem(item)
 
    @property
    def currentIndexChanged(self):
        return self.combobox.currentIndexChanged 
    
    def currentIndex(self) -> int:
        return self.combobox.currentIndex()
