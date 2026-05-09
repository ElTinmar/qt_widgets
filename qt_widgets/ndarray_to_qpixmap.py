from qtpy.QtGui import QPixmap, QImage
from numpy.typing import NDArray
import numpy as np

def float_to_uint8(img: np.ndarray) -> np.ndarray:
    """Standardizes float images to uint8 range [0, 255]."""
    if img.dtype == np.float32 or img.dtype == np.float64:
        img = img * 255.0
        img = img.clip(0, 255).astype(np.uint8)
    return img

def NDarray_to_QPixmap(img: NDArray, format=QImage.Format_BGR888) -> QPixmap:
    """
    Converts a NumPy array to a QPixmap. 
    Note: OpenCV uses BGR format by default.
    """
    img = float_to_uint8(img)
    
    # Handle singleton dimension (H, W, 1) -> (H, W, 3)
    if (len(img.shape) == 3) and img.shape[2] == 1:
        img = np.dstack((img[:, :, 0], img[:, :, 0], img[:, :, 0]))

    # Handle grayscale (H, W) -> (H, W, 3)
    if len(img.shape) == 2:
        img = np.dstack((img, img, img))
    
    h, w, ch = img.shape
    bytes_per_line = ch * w
    
    # Convert to QImage
    #qimg = QImage(img.data, w, h, bytes_per_line, format).copy() # This might be safer
    qimg = QImage(img.data, w, h, bytes_per_line, format)

    return QPixmap.fromImage(qimg)