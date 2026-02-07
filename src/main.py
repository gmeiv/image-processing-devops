import cv2
import os
from PIL import Image
from src.filters import apply_color_grading
from src.filters import apply_chromatic_aberration
from src.filters import apply_image_blending_reflection

input_dir = "input"
output_dir = "output"

def process_image(filename):
    path = os.path.join(input_dir, filename)
    img = cv2.imread(path)
    if img is None:
        return
    
    img = apply_color_grading(img)
    img = apply_chromatic_aberration(img)
    img = apply_image_blending_reflection(img)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pil_img.save(os.path.join(output_dir, f"color_graded_{filename}"))
    print(f"Successfully processed: {filename}")

if __name__ == "__main__":
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)

    files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not files:
        print("No images found in the input directory.")
    else:
        print(f"Found {len(files)} image(s) to process.")
        for filename in files:
            process_image(filename)