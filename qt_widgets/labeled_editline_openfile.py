from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog, QLineEdit, QPushButton, QLabel, QSpinBox, QHBoxLayout

class FileOpenLabeledEditButton(QWidget):
    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.default_file = ''

        self.label = QLabel()
        self.label.setText('Open file:')
        
        self.line_edit = QLineEdit()
        self.line_edit.setMinimumWidth(300)

        self.button = QPushButton()
        folder_icon = QIcon('resources/document-open.svg')
        self.button.setIcon(folder_icon)
        self.button.clicked.connect(self.open_dialog)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def setDefault(self, filename: str):
        self.default_file = filename
        self.line_edit.setText(filename)

    def open_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, 'Select file')
        self.line_edit.setText(file_name[0])

    def setLabel(self, text: str) -> None:
        self.label.setText(text)

    def setText(self, text: str) -> None:
        self.line_edit.setText(text)

    def text(self) -> str:
        return self.line_edit.text()

    def setEnabled(self, enabled:bool) -> None:
        return self.button.setEnabled(enabled)
    
    @property
    def textChanged(self):
        return self.line_edit.textChanged 

    def text(self) -> int:
        return self.line_edit.text()