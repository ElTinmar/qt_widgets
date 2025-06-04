from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QHBoxLayout
from PyQt5.QtWidgets import QApplication

class LabeledEditLine(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.label = QLabel()
        
        self.line_edit = QLineEdit()
        self.line_edit.setMinimumWidth(300)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def setLabel(self, text: str) -> None:
        self.label.setText(text)

    def setText(self, text: str) -> None:
        self.line_edit.setText(text)

    def text(self) -> str:
        return self.line_edit.text()

    @property
    def textChanged(self):
        return self.line_edit.textChanged 

    def text(self) -> str:
        return self.line_edit.text()

if __name__ == "__main__":

    app = QApplication([])
    widget = LabeledEditLine()
    widget.show()
    app.exec_()