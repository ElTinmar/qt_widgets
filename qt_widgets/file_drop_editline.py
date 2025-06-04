from PyQt5.QtWidgets import QLineEdit as QLineEditBase
from PyQt5.QtWidgets import QApplication

class FileDropLineEdit(QLineEditBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            local_path = urls[0].toLocalFile()
            if local_path:
                self.setText(local_path)
                self.editingFinished.emit()

if __name__ == "__main__":

    app = QApplication([])
    widget = FileDropLineEdit()
    widget.show()
    app.exec_()