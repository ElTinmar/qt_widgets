from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QGraphicsPixmapItem

class ZoomableGraphicsView(QGraphicsView):

    zoom_in_factor: float = 1.25
    zoom_in_limit: float = 12
    zoom_out_limit: float = -10 

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


if __name__ == "__main__":

    import numpy as np
    from ndarray_to_qpixmap import NDarray_to_QPixmap

    app = QApplication([])
    
    scene = QGraphicsScene()
    image_item = QGraphicsPixmapItem()
    image_item.setPixmap(NDarray_to_QPixmap(255*np.random.rand(512,512,3)))
    scene.addItem(image_item)

    widget = ZoomableGraphicsView(scene)
    widget.show()
    app.exec_()