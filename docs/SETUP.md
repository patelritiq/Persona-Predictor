# Setup Guide - Persona Predictor

Complete setup and installation instructions for Persona Predictor.

---

## Prerequisites

### System Requirements
- Windows, macOS, or Linux
- Python 3.8 or higher
- 2GB RAM minimum
- Webcam (optional, for real-time detection)

### Software Requirements
- Python 3.8+
- pip (Python package manager)
- Git (for cloning repository)

---

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/pateltitiq/Persona-Predictor.git
cd Persona-Predictor
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- OpenCV 4.8.1.78
- NumPy 1.24.3

### 4. Verify Model Files

Ensure all model files are present in the `models/` directory:

```
models/
├── opencv_face_detector.pbtxt
├── opencv_face_detector_uint8.pb
├── age_deploy.prototxt
├── age_net.caffemodel
├── gender_deploy.prototxt
└── gender_net.caffemodel
```

If any files are missing, download them from the repository or the original sources.

### 5. Test Installation

Run a quick test with your webcam:

```bash
python src/predictor.py
```

You should see a window with real-time face detection and age/gender predictions.

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'cv2'"

**Solution:**
```bash
pip install --upgrade opencv-python
```

### Issue: "FileNotFoundError: Model file not found"

**Causes:**
- Model files are not in the `models/` directory
- Running the script from wrong directory

**Solutions:**
1. Verify all model files exist in `models/` folder
2. Run the script from the project root directory:
   ```bash
   python src/predictor.py
   ```

### Issue: "Cannot open camera" or "VideoCapture failed"

**Causes:**
- Webcam is already in use by another application
- Webcam driver issues
- No webcam connected

**Solutions:**
1. Close other applications using the webcam
2. Try specifying a different camera index (advanced)
3. Use an image file instead:
   ```bash
   python src/predictor.py --image path/to/image.jpg
   ```

### Issue: "No face detected" message

**Causes:**
- Poor lighting conditions
- Face not clearly visible
- Confidence threshold too high
- Face angle not frontal

**Solutions:**
1. Improve lighting
2. Position face directly toward camera
3. Lower confidence threshold:
   ```bash
   python src/predictor.py --confidence 0.5
   ```

### Issue: Slow performance or lag

**Causes:**
- Low-end hardware
- High resolution input
- Other CPU-intensive applications running

**Solutions:**
1. Close unnecessary applications
2. Reduce input resolution
3. Increase confidence threshold (fewer detections = faster)

### Issue: ImportError on macOS

**Solution:**
```bash
pip install opencv-python-headless
```

---

## Virtual Environment Setup

### Why Use Virtual Environment?

Virtual environments isolate project dependencies, preventing conflicts with system Python packages.

### Setup Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Deactivate Virtual Environment

```bash
deactivate
```

---

## Updating Dependencies

To update packages to latest versions:

```bash
pip install --upgrade -r requirements.txt
```

---

## Uninstallation

To remove the project and dependencies:

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment folder
# Windows: rmdir /s venv
# macOS/Linux: rm -rf venv

# Remove project folder
# Windows: rmdir /s Persona-Predictor
# macOS/Linux: rm -rf Persona-Predictor
```

---

## System-Specific Notes

### Windows

- Use `python` instead of `python3`
- Use `venv\Scripts\activate` to activate virtual environment
- Some antivirus software may interfere with OpenCV

### macOS

- Use `python3` instead of `python`
- May need to install Xcode Command Line Tools:
  ```bash
  xcode-select --install
  ```
- Use `source venv/bin/activate` to activate virtual environment

### Linux

- Use `python3` instead of `python`
- May need to install additional packages:
  ```bash
  sudo apt-get install python3-dev
  sudo apt-get install libatlas-base-dev
  ```
- Use `source venv/bin/activate` to activate virtual environment

---

## GPU Acceleration (Advanced)

For faster processing with NVIDIA GPU:

1. Install CUDA Toolkit
2. Install cuDNN
3. Install GPU-enabled OpenCV:
   ```bash
   pip install opencv-contrib-python
   ```

Note: GPU setup is complex and optional for basic usage.

---

## Next Steps

After successful installation:
1. Read [USAGE.md](USAGE.md) for usage examples
2. Read [MODELS.md](MODELS.md) for model information
3. Run the program with different inputs
4. Explore the code in `src/predictor.py`

---

## Getting Help

If you encounter issues not covered here:
1. Check the [USAGE.md](USAGE.md) file
2. Review error messages carefully
3. Check OpenCV documentation: https://docs.opencv.org/
4. Open an issue on GitHub with detailed error information
