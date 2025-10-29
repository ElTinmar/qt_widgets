from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QGraphicsPixmapItem
from PyQt5.QtCore import QTimer, Qt
import numpy as np
import sys
import numpy as np
import sys
from .ndarray_to_qpixmap import NDarray_to_QPixmap

class ZoomableGraphicsView(QGraphicsView):

    zoom_in_factor: float = 1.25
    zoom_in_limit: float = 12
    zoom_out_limit: float = 0 

    def __init__(
            self,
            *args, 
            **kwargs
        ):
    
        super().__init__(*args, **kwargs)
        self._zoom: int = 0
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def wheelEvent(self, event):

        zoom_out_factor = 1 / self.zoom_in_factor

        if event.angleDelta().y() > 0:
            zoom_factor = self.zoom_in_factor
            if self._zoom >= self.zoom_in_limit:
                return
            self._zoom += 1

        else:
            zoom_factor = zoom_out_factor
            if self._zoom <= self.zoom_out_limit:
                return
            self._zoom -= 1

        self.scale(zoom_factor, zoom_factor)

class QtImageWindows:
    windows = {}
    app = None

def imshow(win_name: str, frame: np.ndarray):

    if QtImageWindows.app is None:
        QtImageWindows.app = QApplication.instance() or QApplication(sys.argv)

    if win_name not in QtImageWindows.windows:
        scene = QGraphicsScene()
        image_item = QGraphicsPixmapItem()
        scene.addItem(image_item)

        view = ZoomableGraphicsView(scene)
        view.setWindowTitle(win_name)
        view.resize(frame.shape[1], frame.shape[0])
        view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        view.show()

        QtImageWindows.windows[win_name] = {
            "view": view,
            "scene": scene,
            "image_item": image_item
        }

    win = QtImageWindows.windows[win_name]
    win["image_item"].setPixmap(NDarray_to_QPixmap(frame))
    QtImageWindows.app.processEvents()

def waitKey(ms: int = 0) -> int:

    if QtImageWindows.app is None:
        QtImageWindows.app = QApplication.instance() or QApplication(sys.argv)

    key = []

    def on_key(ev):
        key.append(ev.key())
        QtImageWindows.app.quit()

    for win in QtImageWindows.windows.values():
        win["view"].keyPressEvent = on_key

    if ms == 0:
        while not key:
            QtImageWindows.app.processEvents()
    else:
        timer = QTimer()
        timer.timeout.connect(QtImageWindows.app.quit)
        timer.start(ms)
        QtImageWindows.app.exec_()
        timer.stop()

    return key[0] if key else -1
            
def destroyAllWindows():
    for win in list(QtImageWindows.windows.values()):
        win["view"].close()
    QtImageWindows.windows.clear()

def destroyWindow(win_name: str):
    win = QtImageWindows.windows.get(win_name)
    if win:
        win["view"].close()  
        del QtImageWindows.windows[win_name]

if __name__ == "__main__":

    for i in range(100):
        frame = (255 * np.random.rand(512, 512, 3)).astype(np.uint8)
        imshow("Random Feed", frame)
        k = waitKey(30)
        if k != -1:
            print(f"Key pressed: {k}")

        imshow("Random Feed2", frame//2)
        k = waitKey(30)
        if k != -1:
            print(f"Key pressed: {k}")


