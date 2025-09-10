from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt, pyqtSignal
from typing import Iterable, Any

class LabeledComboBox(QWidget):

    currentDataChanged = pyqtSignal(object)
    currentIndexChanged = pyqtSignal(int)
    currentTextChanged = pyqtSignal(str)

    def __init__(self, *args, **kwargs) -> None:
    
        super().__init__(*args, **kwargs)
    
        self.label = QLabel()
        self.combobox = QComboBox()
        self.combobox.currentIndexChanged.connect(self.on_change)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.combobox)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def setText(self, text: str) -> None:
        self.label.setText(text)

    def addItem(self, item: str, userData: Any = None) -> None:
        if userData is None:
            self.combobox.addItem(item)
        else:
            self.combobox.addItem(item, userData)
            
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

    def on_change(self):
        index = self.combobox.currentIndex()
        text = self.combobox.currentText()
        data = self.combobox.currentData()
        self.currentDataChanged.emit(data)
        self.currentIndexChanged.emit(index)
        self.currentTextChanged.emit(text)
    
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