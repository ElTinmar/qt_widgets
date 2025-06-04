from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog, QPushButton, QLabel, QHBoxLayout
from pathlib import Path
from PyQt5.QtWidgets import QApplication
from .file_drop_editline import FileDropLineEdit

class FileSaveLabeledEditButton(QWidget):

    BASE_DIR = Path(__file__).resolve().parent  # Get the directory of the current script
    SAVE_ICON = str(BASE_DIR / "resources" / "document-save.svg")
    
    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.default_file = ''

        self.label = QLabel()
        self.label.setText('Save file:')
        
        self.line_edit = FileDropLineEdit()
        self.line_edit.setMinimumWidth(300)

        self.button = QPushButton()
        folder_icon = QIcon(self.SAVE_ICON)
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
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save file', self.default_file)
        if file_path:
            self.line_edit.setText(file_path)

    def setLabel(self, text: str) -> None:
        self.label.setText(text)

    def setEnabled(self, enabled:bool) -> None:
        self.line_edit.setEnabled(enabled)
        self.label.setEnabled(enabled)
        self.button.setEnabled(enabled)

    @property
    def textChanged(self):
        return self.line_edit.textChanged 

    def text(self) -> str:
        return self.line_edit.text()
    
    def setText(self, text: str) -> None:
        self.line_edit.setText(text)

if __name__ == "__main__":

    app = QApplication([])
    widget = FileSaveLabeledEditButton()
    widget.show()
    app.exec_()