import cv2
import numpy as np
from PIL import Image, ImageEnhance

def apply_color_grading(image):
    img_f = image.astype(np.float32)
    img_f[:,:,0] *= 1.4   # Boost Blue channel
    img_f[:,:,1] *= 0.85  # Dim Green channel
    img_f[:,:,2] *= 1.3   # Boost Red channel
    return np.clip(img_f, 0, 255).astype(np.uint8)
    