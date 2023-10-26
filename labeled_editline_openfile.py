from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog, QLineEdit, QPushButton, QLabel, QSpinBox, QHBoxLayout

class FileOpenLabeledEditButton(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.label = QLabel()
        self.label.setText('Open file:')
        
        self.line_edit = QLineEdit()
        self.line_edit.setMinimumWidth(300)

        self.button = QPushButton()
        folder_icon = QIcon.fromTheme('document-open')
        self.button.setIcon(folder_icon)
        self.button.clicked.connect(self.open_file)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Select file')
        self.line_edit.setText(file_name[0])

    def setText(self, text: str) -> None:
        self.label.setText(text)

    @property
    def textChanged(self):
        return self.line_edit.textChanged 

    def text(self) -> int:
        return self.line_edit.text()