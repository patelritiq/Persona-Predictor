# Model Information - Persona Predictor

Technical details about the pre-trained models used in Persona Predictor.

---

## Overview

Persona Predictor uses three pre-trained Caffe deep learning models:

1. **Face Detection Model** - Detects faces in images/video
2. **Age Prediction Model** - Predicts age range from face
3. **Gender Classification Model** - Classifies gender from face

---

## 1. Face Detection Model

### Purpose
Detects human faces in images and video frames, returning bounding boxes with confidence scores.

### Files
- `opencv_face_detector.pbtxt` - Model architecture (text format)
- `opencv_face_detector_uint8.pb` - Pre-trained weights (quantized)

### Architecture
- Based on SSD (Single Shot MultiBox Detector)
- Input size: 300x300 pixels
- Output: Bounding boxes with confidence scores

### Input Specifications
- Image size: 300x300 pixels (auto-resized)
- Color space: BGR (OpenCV default)
- Mean subtraction: [104, 117, 123]

### Output
- Bounding boxes: (x1, y1, x2, y2) coordinates
- Confidence scores: 0.0 to 1.0
- Multiple detections per frame supported

### Performance
- Detection speed: ~50-100ms per frame
- Accuracy: ~95% on frontal faces
- Works best with: Clear, frontal faces in good lighting

### Limitations
- Struggles with extreme angles
- Sensitive to lighting conditions
- May miss partially visible faces
- False positives in poor lighting

---

## 2. Age Prediction Model

### Purpose
Predicts age range from a detected face image.

### Files
- `age_deploy.prototxt` - Model architecture
- `age_net.caffemodel` - Pre-trained weights

### Architecture
- Based on CNN (Convolutional Neural Network)
- Input size: 227x227 pixels
- Output: 8 age categories

### Age Categories

| Index | Range | Typical Age |
|-------|-------|------------|
| 0 | (0-2) | Infants |
| 1 | (4-6) | Preschool |
| 2 | (8-12) | Elementary |
| 3 | (15-20) | Teenagers |
| 4 | (20-25) | Young Adults |
| 5 | (30-40) | Adults |
| 6 | (40-50) | Middle-aged |
| 7 | (60-100) | Seniors |

### Input Specifications
- Image size: 227x227 pixels (auto-resized)
- Color space: BGR
- Mean subtraction: (78.43, 87.77, 114.90)

### Output
- Probability distribution across 8 age categories
- Predicted category: Highest probability

### Performance
- Inference speed: ~20-30ms per face
- Accuracy: ~70-80% on diverse datasets
- Works best with: Clear face images, frontal view

### Limitations
- Categorical predictions (not exact age)
- Accuracy varies with ethnicity and gender
- Sensitive to lighting and image quality
- May struggle with extreme ages
- Pre-trained on specific demographic data

---

## 3. Gender Classification Model

### Purpose
Classifies gender (Male/Female) from a detected face image.

### Files
- `gender_deploy.prototxt` - Model architecture
- `gender_net.caffemodel` - Pre-trained weights

### Architecture
- Based on CNN (Convolutional Neural Network)
- Input size: 227x227 pixels
- Output: 2 gender categories

### Gender Categories

| Index | Category |
|-------|----------|
| 0 | Male |
| 1 | Female |

### Input Specifications
- Image size: 227x227 pixels (auto-resized)
- Color space: BGR
- Mean subtraction: (78.43, 87.77, 114.90)

### Output
- Probability distribution across 2 gender categories
- Predicted category: Highest probability

### Performance
- Inference speed: ~20-30ms per face
- Accuracy: ~85-95% on diverse datasets
- Works best with: Clear face images, frontal view

### Limitations
- Binary classification (Male/Female only)
- Accuracy varies with facial features
- May not reflect actual gender identity
- Sensitive to lighting and makeup
- Pre-trained on specific demographic data

---

## Model Training Data

### Face Detection Model
- Trained on: WIDER Face dataset
- Images: ~393,703 images
- Faces: ~1,393,703 labeled faces
- Variations: Multiple scales, angles, lighting conditions

### Age & Gender Models
- Trained on: IMDB-WIKI dataset
- Images: ~500,000+ images
- Age range: 0-100 years
- Diversity: Multiple ethnicities, lighting conditions

---

## Caffe Framework

### What is Caffe?
- Deep learning framework developed by Berkeley AI Research
- Optimized for computer vision tasks
- Efficient inference on CPU and GPU

### Model Format
- `.prototxt` files: Model architecture in text format
- `.caffemodel` files: Pre-trained weights in binary format

### Advantages
- Fast inference
- Lightweight models
- Good for production deployment
- Wide community support

---

## Model Performance Metrics

### Face Detection
- **Precision**: ~95%
- **Recall**: ~90%
- **FPS**: 15-30 (depends on hardware)

### Age Prediction
- **Accuracy**: ~70-80%
- **Mean Absolute Error**: ±5-10 years
- **FPS**: 30-50 per face

### Gender Classification
- **Accuracy**: ~85-95%
- **Precision**: ~90%
- **Recall**: ~90%
- **FPS**: 30-50 per face

---

## Known Biases and Limitations

### Age Prediction
- Better accuracy for ages 20-60
- Less accurate for very young and very old
- Accuracy varies by ethnicity
- Affected by makeup and facial hair
- Categorical predictions (not exact)

### Gender Classification
- Binary classification only
- May not reflect actual gender identity
- Accuracy varies by facial features
- Affected by makeup and styling
- Pre-trained on specific demographic data

### Face Detection
- Better with frontal faces
- Struggles with extreme angles
- Sensitive to lighting
- May miss partially visible faces
- False positives in cluttered backgrounds

---

## Improving Model Performance

### Input Quality
1. **Lighting**: Ensure even, bright lighting
2. **Face Position**: Keep face frontal and centered
3. **Distance**: Optimal 1-2 meters from camera
4. **Resolution**: Higher resolution = better accuracy

### Confidence Threshold
- Adjust `--confidence` parameter
- Higher threshold: Fewer false positives
- Lower threshold: More detections

### Preprocessing
- Crop face region tightly
- Normalize lighting
- Enhance contrast if needed

---

## Model Limitations Summary

| Aspect | Limitation |
|--------|-----------|
| Age | Categorical, not exact; ±5-10 year error |
| Gender | Binary only; may not reflect identity |
| Face Detection | Struggles with angles >45°; lighting sensitive |
| Accuracy | Varies by ethnicity, age, gender |
| Speed | ~50-100ms per frame on CPU |
| Bias | Pre-trained on specific demographic data |

---

## Future Model Improvements

1. **Ensemble Methods**: Combine multiple models
2. **Fine-tuning**: Adapt to specific use cases
3. **Newer Architectures**: Use modern deep learning models
4. **Multi-task Learning**: Joint age/gender/emotion prediction
5. **Fairness**: Reduce demographic bias
6. **Efficiency**: Optimize for mobile/edge devices

---

## References

### Datasets
- WIDER Face: http://shuoyang1213.me/WIDERFACE/
- IMDB-WIKI: https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/

### Papers
- SSD: Single Shot MultiBox Detector
- Age and Gender Classification using Convolutional Neural Networks

### Frameworks
- Caffe: http://caffe.berkeleyvision.org/
- OpenCV DNN: https://docs.opencv.org/master/d6/d0f/group__dnn.html

---

## Technical Specifications

### System Requirements for Models
- Disk space: ~250MB (all models)
- RAM: 2GB minimum
- CPU: Any modern processor
- GPU: Optional (CUDA for acceleration)

### Model File Sizes
- Face detector: ~10MB
- Age model: ~50MB
- Gender model: ~50MB
- Total: ~110MB

### Inference Requirements
- OpenCV 4.0+
- NumPy
- Python 3.6+

---

## Troubleshooting Model Issues

### Issue: Poor Detection Quality

**Causes:**
- Low lighting
- Extreme face angles
- Low image resolution
- Confidence threshold too high

**Solutions:**
1. Improve lighting conditions
2. Position face frontally
3. Use higher resolution input
4. Lower confidence threshold

### Issue: Incorrect Age/Gender Predictions

**Causes:**
- Model limitations
- Demographic bias
- Poor input quality
- Extreme facial features

**Solutions:**
1. Improve input image quality
2. Ensure frontal face position
3. Understand model limitations
4. Use multiple predictions for averaging

### Issue: Slow Inference

**Causes:**
- CPU-only processing
- High resolution input
- Multiple faces per frame
- System resource constraints

**Solutions:**
1. Reduce input resolution
2. Increase confidence threshold
3. Close other applications
4. Use GPU acceleration (if available)

---

## Additional Resources

- OpenCV Documentation: https://docs.opencv.org/
- Caffe Documentation: http://caffe.berkeleyvision.org/
- Deep Learning Basics: https://www.deeplearningbook.org/
