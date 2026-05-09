from typing import Callable
from qtpy.QtCore import QThread, Signal as pyqtSignal

class WorkerThread(QThread):
    """
    A generic worker thread to execute a function in the background.
    Compatible with PyQt5, PyQt6, and PySide via qtpy.
    """
    result = pyqtSignal(object)
    exception = pyqtSignal(Exception)  

    def __init__(self, target: Callable, *args, **kwargs):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs 

    def run(self):
        try:
            res = self.target(*self.args, **self.kwargs)
            self.result.emit(res)
        except Exception as e:
            self.exception.emit(e)