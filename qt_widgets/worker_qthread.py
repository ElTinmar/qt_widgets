from typing import Callable
from PyQt5.QtCore import QThread

class WorkerThread(QThread):

    def __init__(self, target: Callable, *args, **kwargs):
        
        super().__init__()

        self.target = target
        self.args = args
        self.kwargs = kwargs 

    def run(self):
        self.target(*self.args, **self.kwargs)