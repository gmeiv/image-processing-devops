import cv2
import numpy as np
from PIL import Image, ImageEnhance

def apply_color_grading(image):
    img_f = image.astype(np.float32)
    img_f[:,:,0] *= 1.4   # Boost Blue channel
    img_f[:,:,1] *= 0.85  # Dim Green channel
    img_f[:,:,2] *= 1.3   # Boost Red channel
    return np.clip(img_f, 0, 255).astype(np.uint8)
    
def apply_chromatic_aberration(image, shift=5):
    b, g, r = cv2.split(image)
    b = np.roll(b, -shift, axis=1)
    r = np.roll(r, shift, axis=1)
    return cv2.merge([b, g, r])

def apply_image_blending_reflection(image):
    h, w = image.shape[:2]
    ref_line = int(h * 0.6)
    
    # Flipping to create reflection
    top_h = h - ref_line
    top_section = image[ref_line - top_h : ref_line, :]
    reflection = cv2.flip(top_section, 0)

    # Gaussian blur for smooth reflection
    reflection = cv2.GaussianBlur(reflection, (45, 45), 15)

    # Image Blending
    image[ref_line:h, :] = cv2.addWeighted(image[ref_line:h, :], 0.4, reflection, 0.6, 0)
    return image