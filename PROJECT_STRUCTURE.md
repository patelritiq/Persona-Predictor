# Project Structure - Persona Predictor

Complete overview of the reorganized Persona Predictor project structure.

---

## Directory Layout

```
Persona Predictor/
├── src/
│   └── predictor.py                    # Main inference program
│
├── models/
│   ├── opencv_face_detector.pbtxt      # Face detection architecture
│   ├── opencv_face_detector_uint8.pb   # Face detection weights
│   ├── age_deploy.prototxt             # Age prediction architecture
│   ├── age_net.caffemodel              # Age prediction weights
│   ├── gender_deploy.prototxt          # Gender classification architecture
│   ├── gender_net.caffemodel           # Gender classification weights
│   └── .gitkeep                        # Ensures folder is tracked by git
│
├── docs/
│   ├── SETUP.md                        # Installation and setup guide
│   ├── USAGE.md                        # Usage examples and advanced options
│   ├── MODELS.md                       # Model architecture and information
│   ├── DOWNLOAD_MODELS.md
│
├── .gitignore                          # Git ignore rules
├── LICENSE                             # MIT License
├── README.md                           # Main project documentation
├── requirements.txt                    # Python dependencies
└── PROJECT_STRUCTURE.md                # This file
```

---

## Folder Descriptions

### `src/` - Source Code
Contains the main Python application.

**Files:**
- `predictor.py` - Main inference program with:
  - Model loading with error handling
  - Face detection
  - Age and gender prediction
  - Real-time video/image processing
  - Command-line argument parsing

**Key Features:**
- Dynamic model path resolution
- Comprehensive error handling
- Support for webcam and image input
- Configurable confidence threshold

### `models/` - Pre-trained Models
Contains all pre-trained Caffe deep learning models.

**Files:**
- Face detection model (2 files)
- Age prediction model (2 files)
- Gender classification model (2 files)

**Total Size:** ~250MB

**Note:** Models are not included in git repository due to size. Download separately if needed.

### `docs/` - Documentation
Comprehensive documentation for setup, usage, and technical details.

**Files:**
- `SETUP.md` - Installation guide with troubleshooting
- `USAGE.md` - Usage examples and best practices
- `MODELS.md` - Technical model information
- `PROJECT_STRUCTURE.md` - This file

### Root Level Files

**Configuration Files:**
- `.gitignore` - Specifies files to ignore in git
- `requirements.txt` - Python package dependencies
- `LICENSE` - MIT License

**Documentation:**
- `README.md` - Main project documentation
- `PROJECT_STRUCTURE.md` - This file

---

## File Descriptions

### `src/predictor.py`

**Purpose:** Main inference program

**Key Functions:**
- `get_model_path(filename)` - Resolves model file paths
- `load_models()` - Loads all three pre-trained models
- `highlight_face(net, frame, conf_threshold)` - Detects faces
- `predict_age_gender(age_net, gender_net, face, model_mean_values)` - Predicts age/gender
- `main()` - Main program logic

**Command-line Arguments:**
- `--image` - Path to input image (optional)
- `--confidence` - Detection confidence threshold (default: 0.7)

**Usage:**
```bash
python src/predictor.py                    # Webcam
python src/predictor.py --image photo.jpg  # Image file
python src/predictor.py --confidence 0.8   # Custom threshold
```

### `requirements.txt`

**Purpose:** Specifies Python package dependencies

**Contents:**
```
opencv-python==4.8.1.78
numpy==1.24.3
```

**Installation:**
```bash
pip install -r requirements.txt
```

### `.gitignore`

**Purpose:** Specifies files to exclude from git repository

**Includes:**
- Python cache files (`__pycache__/`, `*.pyc`)
- Virtual environment folders
- IDE configuration files
- Log files
- OS-specific files

### `LICENSE`

**Purpose:** MIT License for the project

**Allows:**
- Commercial use
- Modification
- Distribution
- Private use

**Requires:**
- License and copyright notice

---

## Model Files Explanation

### Face Detection Models
- `opencv_face_detector.pbtxt` - Architecture definition
- `opencv_face_detector_uint8.pb` - Pre-trained weights (quantized)
- **Purpose:** Detect faces in images/video
- **Size:** ~10MB total

### Age Prediction Models
- `age_deploy.prototxt` - Architecture definition
- `age_net.caffemodel` - Pre-trained weights
- **Purpose:** Predict age range from face
- **Size:** ~50MB total
- **Output:** 8 age categories

### Gender Classification Models
- `gender_deploy.prototxt` - Architecture definition
- `gender_net.caffemodel` - Pre-trained weights
- **Purpose:** Classify gender from face
- **Size:** ~50MB total
- **Output:** Male or Female

---

## Reorganization Changes

### What Changed

**Before:**
```
Persona Predictor/
├── Persona Predictor/
│   ├── inferenceprogram.py
│   ├── age_deploy.prototxt
│   ├── age_net.caffemodel
│   ├── gender_deploy.prototxt
│   ├── gender_net.caffemodel
│   ├── opencv_face_detector_uint8.pb
│   └── opencv_face_detector.pbtxt
├── README.md
└── LICENSE
```

**After:**
```
Persona Predictor/
├── src/
│   └── predictor.py (improved with error handling)
├── models/
│   ├── age_deploy.prototxt
│   ├── age_net.caffemodel
│   ├── gender_deploy.prototxt
│   ├── gender_net.caffemodel
│   ├── opencv_face_detector_uint8.pb
│   └── opencv_face_detector.pbtxt
├── docs/
│   ├── SETUP.md
│   ├── USAGE.md
│   └── MODELS.md
├── README.md (enhanced)
├── requirements.txt (new)
├── .gitignore (new)
└── LICENSE
```

### Code Changes

**Model Path Resolution:**
- Old: Hardcoded paths in same directory
- New: Dynamic path resolution using `get_model_path()`

**Error Handling:**
- Old: Minimal error handling
- New: Comprehensive try-catch blocks

**Model Loading:**
- Old: Direct model loading
- New: Validation of model file existence

**Command-line Arguments:**
- Old: Only `--image` parameter
- New: Added `--confidence` parameter

---

## How to Use This Structure

### For Development
1. Edit code in `src/predictor.py`
2. Models are automatically found in `models/` folder
3. No need to change file paths

### For Distribution
1. Include all folders and files
2. Users run: `pip install -r requirements.txt`
3. Users run: `python src/predictor.py`

### For Documentation
1. Setup: Read `docs/SETUP.md`
2. Usage: Read `docs/USAGE.md`
3. Models: Read `docs/MODELS.md`
4. Overview: Read `README.md`

---

## Benefits of This Structure

1. **Separation of Concerns**
   - Code in `src/`
   - Models in `models/`
   - Documentation in `docs/`

2. **Scalability**
   - Easy to add more models
   - Easy to add more scripts
   - Easy to add more documentation

3. **Maintainability**
   - Clear organization
   - Easy to find files
   - Professional structure

4. **Portability**
   - Works on Windows, macOS, Linux
   - Dynamic path resolution
   - No hardcoded paths

5. **Documentation**
   - Comprehensive guides
   - Multiple documentation files
   - Clear structure

---

## Adding New Features

### Add New Script
1. Create file in `src/` folder
2. Use `get_model_path()` for model access
3. Update `README.md` with usage

### Add New Model
1. Place model files in `models/` folder
2. Update `predictor.py` to load new model
3. Update `docs/MODELS.md` with details

### Add New Documentation
1. Create `.md` file in `docs/` folder
2. Link from `README.md`
3. Follow existing format

---

## File Size Reference

| Component | Size |
|-----------|------|
| Source code | <50KB |
| Models | ~250MB |
| Documentation | ~500KB |
| Total | ~250MB |

---

## Next Steps

1. Read `README.md` for project overview
2. Read `docs/SETUP.md` for installation
3. Read `docs/USAGE.md` for usage examples
4. Read `docs/MODELS.md` for technical details
5. Run `python src/predictor.py` to test

---

## Questions?

Refer to:
- `docs/SETUP.md` - Installation issues
- `docs/USAGE.md` - Usage questions
- `docs/MODELS.md` - Technical questions
- `README.md` - General information
