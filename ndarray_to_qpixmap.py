from PyQt5.QtGui import QPixmap, QImage
from numpy.typing import NDArray
import numpy as np

def NDarray_to_QPixmap(img: NDArray) -> QPixmap:
    if len(img.shape) == 2:
        img = np.dstack((img,img,img))
    
    h,w,ch = img.shape
    # note opencv uses BGR format by default
    qimg = QImage(img.data, w, h, 3*w, QImage.Format_BGR888) 
    return QPixmap(qimg)