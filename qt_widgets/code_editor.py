import keyword
import builtins

from PyQt5.QtWidgets import QWidget, QPlainTextEdit, QVBoxLayout, QFileDialog, QMessageBox, QPushButton, QHBoxLayout
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont, QPalette
from PyQt5.QtCore import QRegExp, Qt


class PythonHighlighter(QSyntaxHighlighter):

    def __init__(self, parent=None):

        super().__init__(parent)

        # Formats
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))  # blue
        keyword_format.setFontWeight(QFont.Bold)

        builtin_format = QTextCharFormat()
        builtin_format.setForeground(QColor("#DCDCAA"))  # yellow

        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178"))  # orange

        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))  # green
        comment_format.setFontItalic(True)

        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#B5CEA8"))  # light green

        operator_format = QTextCharFormat()
        operator_format.setForeground(QColor("#C586C0"))  # purple

        # Rules
        self.rules = []
        self.rules += [(QRegExp(r"\b" + kw + r"\b"), keyword_format) for kw in keyword.kwlist]

        builtins_list = [name for name in dir(builtins) if callable(getattr(builtins, name))]
        self.rules += [(QRegExp(r"\b" + bi + r"\b"), builtin_format) for bi in builtins_list]

        self.rules.append((QRegExp(r"#[^\n]*"), comment_format))
        self.rules.append((QRegExp(r'"[^"\\]*(\\.[^"\\]*)*"'), string_format))
        self.rules.append((QRegExp(r"'[^'\\]*(\\.[^'\\]*)*'"), string_format))
        self.rules.append((QRegExp(r"\b[0-9]+\b"), number_format))

        operators = [
            r"=", r"\+", r"-", r"\*", r"/", r"//", r"%", r"\*\*", 
            r"<", r">", r"==", r"!=", r"<=", r">=", 
            r"&", r"\|", r"\^", r"~", r"<<", r">>", r":="
        ]
        self.rules += [(QRegExp(op), operator_format) for op in operators]

    def highlightBlock(self, text):

        for pattern, fmt in self.rules:
            index = pattern.indexIn(text)
            while index >= 0:
                length = pattern.matchedLength()
                self.setFormat(index, length, fmt)
                index = pattern.indexIn(text, index + length)


class CodeEdit(QPlainTextEdit):

    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.setFont(QFont("Consolas", 11))
        self.setTabChangesFocus(False)

        # Dark theme palette
        palette = self.palette()
        palette.setColor(QPalette.Base, QColor("#1E1E1E"))       # background
        palette.setColor(QPalette.Text, QColor("#D4D4D4"))       # default text
        palette.setColor(QPalette.Highlight, QColor("#264F78"))  # selection
        palette.setColor(QPalette.HighlightedText, QColor("#FFFFFF"))
        self.setPalette(palette)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Tab:
            self.insertPlainText(" " * 4)
        else:
            super().keyPressEvent(event)


class CodeEditor(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.editor = CodeEdit()
        self.highlighter = PythonHighlighter(self.editor.document())

        self.load_button = QPushButton('Load')
        self.load_button.clicked.connect(self.load_file)
        
        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.save_file)

        control_layout = QHBoxLayout()
        control_layout.addWidget(self.load_button)
        control_layout.addWidget(self.save_button)

        layout = QVBoxLayout(self)
        layout.addLayout(control_layout)
        layout.addWidget(self.editor)

    def setPlainText(self, text: str):
        self.editor.setPlainText(text)

    def toPlainText(self) -> str:
        return self.editor.toPlainText()

    def load_file(self):

        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Python Files (*.py);;All Files (*)")
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.setPlainText(f.read())
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file:\n{e}")

    def save_file(self):

        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Python Files (*.py);;All Files (*)")
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.toPlainText())
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file:\n{e}")


if __name__ == "__main__":

    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    w = CodeEditor()
    w.setPlainText("# Dark themed code editor\nfor i in range(3):\n    print(i)")
    w.resize(600, 400)
    w.show()
    app.exec_()
    print(w.toPlainText())
