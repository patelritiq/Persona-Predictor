# Persona Predictor 🎭

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A real-time face detection and age-gender prediction system built with OpenCV and deep learning. Detects faces in images or video streams and predicts age ranges and gender with pre-trained Caffe models.

---

## Project Statistics 📊

- **8 age categories** (0-2, 4-6, 8-12, 15-20, 20-25, 30-40, 40-50, 60-100)
- **2 gender classifications** (Male, Female)
- **3 pre-trained deep learning models** (Face detection, Age prediction, Gender prediction)
- **Real-time processing** on webcam and image inputs
- **Tested on diverse demographics** with consistent accuracy

---

## Project Overview 🎯

Persona Predictor is a computer vision learning project built during college to understand face detection and demographic prediction using deep learning. It demonstrates practical implementation of OpenCV's DNN module with pre-trained Caffe models for real-time age and gender inference.

### Development Context
- Built as a hands-on learning project for computer vision and machine learning
- Focused on understanding face detection algorithms and neural network inference
- Demonstrates practical application of pre-trained models
- Foundation for understanding demographic analysis systems

### What I Learned
- Face detection using OpenCV's DNN module
- Working with pre-trained Caffe models
- Real-time video processing and frame manipulation
- Bounding box detection and confidence thresholding
- Age and gender classification using deep learning

---

## Key Features ✨

- Real-time face detection with confidence thresholding
- Age prediction across 8 age ranges
- Gender classification (Male/Female)
- Support for both image and webcam input
- Bounding box visualization with predictions
- Configurable confidence threshold for detection
- Error handling and model validation
- Dynamic model path resolution

---

## Real-World Applications 🚀

- **Retail Analytics**: Analyze customer demographics for targeted marketing
- **Event Management**: Separate seating or stands based on age and gender demographics
- **Entertainment**: Gaming and interactive experiences with demographic adaptation
- **Accessibility**: Assist in creating inclusive experiences based on user demographics
- **Crowd Analytics**: Understand audience composition at events and venues

---

## Technology Stack 🛠️

- **Python 3.8+**
- **OpenCV 4.8+** - Computer vision and DNN module
- **NumPy** - Numerical computations
- **Caffe Models** - Pre-trained deep learning models

---

## Project Structure 📁

For detailed model information, see [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

---

## Quick Start 🚀

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pateltitiq/Persona-Predictor.git
   cd Persona-Predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify model files are in the `models/` directory:
   ```
   models/
   ├── opencv_face_detector.pbtxt
   ├── opencv_face_detector_uint8.pb
   ├── age_deploy.prototxt
   ├── age_net.caffemodel
   ├── gender_deploy.prototxt
   └── gender_net.caffemodel
   ```

### Usage

**Run with webcam (default):**
```bash
python src/predictor.py
```

**Run with image file:**
```bash
python src/predictor.py --image path/to/image.jpg
```

**Run with custom confidence threshold:**
```bash
python src/predictor.py --confidence 0.8
```

**Exit the program:**
Press `q` to quit

---

## Model Information 📚

The system uses three pre-trained Caffe models:

1. **Face Detection Model**
   - Detects faces in images/video frames
   - Returns bounding boxes with confidence scores
   - Files: `opencv_face_detector.pbtxt`, `opencv_face_detector_uint8.pb`

2. **Age Prediction Model**
   - Predicts age range from detected face
   - 8 age categories: (0-2), (4-6), (8-12), (15-20), (20-25), (30-40), (40-50), (60-100)
   - Files: `age_deploy.prototxt`, `age_net.caffemodel`

3. **Gender Classification Model**
   - Classifies gender as Male or Female
   - Files: `gender_deploy.prototxt`, `gender_net.caffemodel`

For detailed model information, see [MODELS.md](docs/MODELS.md)

---

## Performance Characteristics ⚡

- **Real-time Processing**: Processes video at ~15-30 FPS (depends on hardware)
- **Accuracy**: Tested on diverse demographics with consistent predictions
- **Confidence Threshold**: Default 0.7 (adjustable via `--confidence` flag)
- **Face Detection**: Detects multiple faces per frame
- **Latency**: ~50-100ms per frame on standard hardware

---

## Limitations ⚠️

- Age predictions are categorical ranges, not exact ages
- Accuracy varies with lighting conditions and face angles
- Not suitable for security or surveillance applications
- Requires clear, frontal face views for best results
- Pre-trained models have inherent biases
- Single-threaded processing (no GPU acceleration in base version)

---

## Troubleshooting 🔧

**Issue**: "Model file not found" error
- **Solution**: Ensure all model files are in the `models/` directory

**Issue**: Webcam not opening
- **Solution**: Check if another application is using the webcam, or specify a different camera index

**Issue**: No faces detected
- **Solution**: Ensure good lighting, face is clearly visible, and confidence threshold is appropriate

**Issue**: ImportError for OpenCV
- **Solution**: Run `pip install -r requirements.txt` to install dependencies

For more troubleshooting, see [SETUP.md](docs/SETUP.md)

---

## Future Enhancements 🔮

- [ ] GPU acceleration support (CUDA)
- [ ] Multi-threading for faster processing
- [ ] Emotion detection
- [ ] Face recognition and identification
- [ ] Ethnicity classification
- [ ] Web interface for easy access
- [ ] REST API for integration
- [ ] Performance metrics and benchmarking
- [ ] Support for multiple face detection backends

---

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author 👨‍💻

**Ritik Pratap Singh Patel**  
Computer Vision & Machine Learning Enthusiast

*Built with passion to learn and understand computer vision* 🎥

---

## Documentation 📖

- [SETUP.md](docs/SETUP.md) - Detailed setup and installation guide
- [USAGE.md](docs/USAGE.md) - Usage examples and advanced options
- [MODELS.md](docs/MODELS.md) - Model architecture and information
- [DOWNLOAD_MODELS.md](docs/DOWNLOAD_MODELS.md) - Instructions to download models

## Acknowledgments 🙏

This project was developed during college as a learning exercise in computer vision and deep learning. Models are based on pre-trained Caffe networks for face detection, age prediction, and gender classification.
