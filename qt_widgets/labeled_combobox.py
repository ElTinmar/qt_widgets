from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
from typing import Iterable, Any

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

    def addItem(self, item: str, userData: Any = None) -> None:
        self.combobox.addItem(item, userData=userData)

    def addItems(self, items: Iterable) -> None:
        for item in items:
            self.combobox.addItem(item)

    def setEnabled(self, enabled:bool) -> None:
        self.combobox.setEnabled(enabled)
    
    def setCurrentIndex(self, index: int):
        self.combobox.setCurrentIndex(index)
 
    def setCurrentText(self, text: str):
        self.combobox.setCurrentText(text)

    def clear(self):
        self.combobox.clear()

    @property
    def currentIndexChanged(self):
        return self.combobox.currentIndexChanged 

    @property
    def currentTextChanged(self):
        return self.combobox.currentTextChanged 
    
    def currentData(self, role = Qt.UserRole) -> Any:
        return self.combobox.currentData(role)

    def currentIndex(self) -> int:
        return self.combobox.currentIndex()
    
    def currentText(self) -> str:
        return self.combobox.currentText()

if __name__ == "__main__":

    app = QApplication([])
    widget = LabeledComboBox()
    widget.show()
    app.exec_()