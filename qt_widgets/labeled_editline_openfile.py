from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog, QPushButton, QLabel, QHBoxLayout
from .file_drop_editline import FileDropLineEdit
from pathlib import Path
from PyQt5.QtWidgets import QApplication

class FileOpenLabeledEditButton(QWidget):

    BASE_DIR = Path(__file__).resolve().parent  # Get the directory of the current script
    LOAD_ICON = str(BASE_DIR / "resources" / "document-open.svg") 

    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.default_file = ''

        self.label = QLabel()
        self.label.setText('Open file:')
        
        self.line_edit = FileDropLineEdit()
        self.line_edit.setMinimumWidth(300)
        self.line_edit.editingFinished.connect(self.validate_input)

        self.button = QPushButton()
        folder_icon = QIcon(self.LOAD_ICON)
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
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select file')
        if file_path:
            self.line_edit.setText(file_path)
            self.validate_input()

    def setLabel(self, text: str) -> None:
        self.label.setText(text)

    def setText(self, text: str) -> None:
        self.line_edit.setText(text)
        self.validate_input()

    def text(self) -> str:
        return self.line_edit.text()

    def setEnabled(self, enabled:bool) -> None:
        self.line_edit.setEnabled(enabled)
        self.label.setEnabled(enabled)
        self.button.setEnabled(enabled)

    def validate_input(self):
        path = Path(self.line_edit.text())
        if path.is_file():
            self.line_edit.setToolTip("")
            self.line_edit.setStyleSheet("")
        else:
            self.line_edit.setToolTip("File does not exist.")
            self.line_edit.setStyleSheet("border: 1px solid red;")
                
    @property
    def textChanged(self):
        return self.line_edit.textChanged 

if __name__ == "__main__":

    app = QApplication([])
    widget = FileOpenLabeledEditButton()
    widget.show()
    app.exec_()