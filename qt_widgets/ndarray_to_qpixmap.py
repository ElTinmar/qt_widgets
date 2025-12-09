from PyQt5.QtGui import QPixmap, QImage
from numpy.typing import NDArray
import numpy as np

def float_to_uint8(img: np.ndarray) -> np.ndarray:
    if img.dtype == np.float32 or img.dtype == np.float64:
        img = img * 255.0
        img = img.clip(0, 255).astype(np.uint8)
    return img

def NDarray_to_QPixmap(img: NDArray, format = QImage.Format_BGR888) -> QPixmap:
    # note opencv uses BGR format by default
    img = float_to_uint8(img)
    
    # in case we have a singleton dimension
    if (len(img.shape) == 3) and img.shape[2] == 1:
        img = np.dstack((img[:,:,0],img[:,:,0],img[:,:,0]))

    # in case we have grayscale
    if len(img.shape) == 2:
        img = np.dstack((img,img,img))
    
    h,w,ch = img.shape
    qimg = QImage(img.data, w, h, 3*w, format)  
    return QPixmap(qimg)

