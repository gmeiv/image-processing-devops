import pytest
import cv2
import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.filters import (
    apply_color_grading, 
    apply_chromatic_aberration, 
    apply_image_blending_reflection,
    apply_vignette
)

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

# 3. Test Reflection Blending
def test_apply_reflection():
    dummy_img = np.ones((200, 200, 3), dtype=np.uint8) * 255
    processed_img = apply_image_blending_reflection(dummy_img)
    assert processed_img is not None
    assert processed_img.shape == (200, 200, 3)

# 4. Test Vignette (New)
def test_apply_vignette():
    dummy_img = np.ones((100, 100, 3), dtype=np.uint8) * 255
    processed_img = apply_vignette(dummy_img)
    assert processed_img is not None
    # Verify corners are darker than the center
    assert processed_img[0, 0, 0] < processed_img[50, 50, 0]

# --- COMBINED / INTEGRATION TEST ---

def test_integration_full_pipeline():
    img = (np.random.rand(300, 300, 3) * 255).astype(np.uint8)
    
    try:
        # Step 1: Individual Unit Logic
        img1 = apply_color_grading(img)
        # Step 2: Individual Unit Logic
        img2 = apply_chromatic_aberration(img1)
        # Step 3: Individual Unit Logic
        img3 = apply_image_blending_reflection(img2)
        # Step 4: Final Pipeline Logic
        final_img = apply_vignette(img3)
        
        # Final Pass/Fail Checks
        assert final_img is not None
        assert final_img.shape == (300, 300, 3)
        assert final_img.dtype == np.uint8
        
    except Exception as e:
        pytest.fail(f"The combined filter pipeline failed! Error: {e}")

def test_input_directory_exists():
    assert os.path.exists("input"), "Input directory is missing!"