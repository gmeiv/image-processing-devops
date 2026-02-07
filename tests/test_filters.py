import pytest
import cv2
import numpy as np
import os
import sys

# This allows the test to find the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.filters import apply_color_grading

def test_apply_color_grading():
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    processed_img = apply_color_grading(dummy_img)
    assert processed_img is not None

def test_create_output_folder():
   
    output_path = "output"
    if not os.path.exists(output_path):
        os.makedirs(output_path) 
    
    assert os.path.exists(output_path)
    
    with open(os.path.join(output_path, ".gitkeep"), "w") as f:
        f.write("")