from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QGraphicsPixmapItem

class ZoomableGraphicsView(QGraphicsView):

    def __init__(self, *args, **kwargs):
    
        super().__init__(*args, **kwargs)
        self._zoom = 0
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def wheelEvent(self, event):
    
        zoom_in_factor = 1.25
        zoom_out_factor = 1 / zoom_in_factor

        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
            self._zoom += 1
        else:
            zoom_factor = zoom_out_factor
            self._zoom -= 1

        if self._zoom < -10:  # optional zoom out limit
            self._zoom = -10
            return

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