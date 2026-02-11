# image-processing-devops
# Image Processing DevOps Project - Group 5
## Elective 4 - Midterm Project

### Project Overview
This project demonstrates a complete DevOps workflow applied to image processing. We utilize Python and OpenCV to automate digital image filters, integrated with a Continuous Integration (CI) pipeline using GitHub Actions to ensure code stability and automated validation.

### Group Roles
1. **Image Processing Lead (Trisha Mae S. Villareal)**: Handles algorithms and filters.
2. **DevOps Engineer (Glorie May G. Verayo)**: Configures the GitHub Actions pipeline.
3. **Tester (Leimrei P. Sta. Rosa)**: Writes and validates automated tests.
4. **Documenter/Presenter (Yanna Adelene E. Santos)**: Prepares the README and final presentation.

### Tools and Technologies
* **Language**: Python 3
* **Library**: OpenCV (opencv-python) for image manipulation
* **Automation**: GitHub Actions for CI pipeline
* **Testing**: PyTest for automated validation

### System Requirements
- [x] **Automatic Detection**: The system automatically detects image files in the `input/` directory.
- [x] **Processing Techniques**: Applies multiple techniques including Chromatic Aberration and Vignette.
- [x] **Output Management**: All processed images are saved directly to the `output/` directory.
- [x] **CI/CD Pipeline**: The pipeline runs automatically and is validated by Github Actions on every push.
- [x] **Safe Directory Handling**: Automatically creates the input/ and output/ directories if they don't exist, preventing crashes.

### Image Processing Techniques
Technical Note: All filter algorithms in filters.py were developed from scratch by our Image Processing Lead to demonstrate custom pixel manipulation in OpenCV.
We implemented the following filters using OpenCV:
* **Chromatic Aberration**: Simulates lens color bleeding by shifting the Red and Blue channels.
* **Vignette Effect**: Darkens the corners of the image to create a cinematic look.
* **Color Grading**: Adjusts the brightness and contrast to match a specific aesthetic.
* **Image Blending & Reflection**: Applies a layering effect to the input image.
* **Contrast Enhancement**: Uses ImageEnhance.Contrast (Pillow) to boost the final image contrast by 1.4x for a punchier look.

### Project Structure
* `src/`: Core logic and filter algorithms (`main.py`, `filters.py`).
* `tests/`: Automated test scripts.
* `input/`: Source directory for raw images.
* `output/`: Destination for processed images.
* `.github/workflows/`: Configuration for the CI/CD pipeline.

### Required Deliverables
As per the project guidelines:
- [x] GitHub repository with complete source code.
- [x] Working CI pipeline with successful execution.
- [x] Processed image outputs generated in the output/ folder.
- [x] Presentation explaining the DevOps workflow.

### DevOps Workflow (CI/CD)
This project implements a professional DevOps lifecycle:
1. **Plan & Code**: Local development and version control using Git.
2. **Continuous Integration**: On every `git push`, GitHub Actions triggers a workflow that:
   - Sets up a virtual environment.
   - Installs dependencies from `requirements.txt`.
   - Executes `pytest` to ensure all 6 tests pass before deployment.

### Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/gmeiv/image-processing-devops.git
   ```
2. **Setup Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Project**
   ```bash
   python -m src.main
   ```

### Submission & Verification
This section provides direct links to the evidence for submission and verification.
* **Version Control Monitor**: [Click here to view Commit History and Timestamps](https://github.com/gmeiv/image-processing-devops/commits/main/)
* **CI Pipeline Status**: [Click here to view GitHub Actions Successful Executions](https://github.com/gmeiv/image-processing-devops/actions)
* **Functionality Verification**: Automated tests pass locally and in the cloud via `pytest`.