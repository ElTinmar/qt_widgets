from typing import Callable
from PyQt5.QtCore import QThread, pyqtSignal

class WorkerThread(QThread):

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