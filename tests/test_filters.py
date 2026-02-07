import pytest
import cv2
import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.filters import apply_color_grading, apply_chromatic_aberration

def test_apply_color_grading():
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    processed_img = apply_color_grading(dummy_img)
    assert processed_img is not None
    assert processed_img.shape == (100, 100, 3)

def test_apply_chromatic_aberration():
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    processed_img = apply_chromatic_aberration(dummy_img)
    assert processed_img is not None
    assert processed_img.shape == (100, 100, 3)

def test_input_directory_exists():
    assert os.path.exists("input"), "Input directory is missing!"