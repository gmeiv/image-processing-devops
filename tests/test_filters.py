import pytest
import cv2
import numpy as np
import os
import sys

# Ensure the 'src' directory is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.filters import apply_color_grading, apply_chromatic_aberration, apply_image_blending_reflection

# 1. Test Color Grading
def test_apply_color_grading():
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    processed_img = apply_color_grading(dummy_img)
    assert processed_img is not None
    assert processed_img.shape == (100, 100, 3)

# 2. Test Chromatic Aberration
def test_apply_chromatic_aberration():
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    processed_img = apply_chromatic_aberration(dummy_img, shift=5)
    assert processed_img is not None
    assert processed_img.shape == (100, 100, 3)

# 3. Test Image Blending Reflection (NEW)
def test_apply_reflection():
    # Use a larger dummy image (e.g., 200x200) because the reflection logic uses 60% height
    dummy_img = np.ones((200, 200, 3), dtype=np.uint8) * 255
    processed_img = apply_image_blending_reflection(dummy_img)
    assert processed_img is not None
    assert processed_img.shape == (200, 200, 3)
    
def test_input_directory_exists():
    assert os.path.exists("input"), "Input directory is missing!"