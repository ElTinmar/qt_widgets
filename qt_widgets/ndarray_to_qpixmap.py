from PyQt5.QtGui import QPixmap, QImage
from numpy.typing import NDArray
import numpy as np

def NDarray_to_QPixmap(img: NDArray) -> QPixmap:
    
    # in case we have a singleton dimension
    if (len(img.shape) == 3) and img.shape[2] == 1:
        img = np.dstack((img[:,:,0],img[:,:,0],img[:,:,0]))

    # in case we have grayscale
    if len(img.shape) == 2:
        img = np.dstack((img,img,img))
    
    h,w,ch = img.shape
    # note opencv uses BGR format by default
    qimg = QImage(img.data, w, h, 3*w, QImage.Format_BGR888) 
    return QPixmap(qimg)