# Usage Guide - Persona Predictor

Complete usage examples and advanced options for Persona Predictor.

---

## Basic Usage

### Run with Webcam (Default)

```bash
python src/predictor.py
```

This will:
1. Open your default webcam
2. Display real-time video with face detection
3. Show age and gender predictions for detected faces
4. Print predictions to console

**Exit:** Press `q` to quit

---

## Advanced Usage

### Run with Image File

```bash
python src/predictor.py --image path/to/image.jpg
```

Supported formats: JPG, PNG, BMP, TIFF

**Example:**
```bash
python src/predictor.py --image sample.jpg
```

### Adjust Confidence Threshold

```bash
python src/predictor.py --confidence 0.8
```

**Confidence Threshold Explanation:**
- Range: 0.0 to 1.0
- Default: 0.7
- Higher values: Fewer detections, higher confidence
- Lower values: More detections, including uncertain ones

**Examples:**
```bash
# Strict detection (only very confident faces)
python src/predictor.py --confidence 0.9

# Loose detection (includes uncertain faces)
python src/predictor.py --confidence 0.5

# Image with loose threshold
python src/predictor.py --image photo.jpg --confidence 0.6
```

---

## Output Explanation

### Console Output

```
Gender: Male, Age: (20-25) years
Gender: Female, Age: (30-40) years
No face detected
```

### Visual Output

- **Green Bounding Box**: Detected face
- **Yellow Text**: Gender and age prediction
- **Format**: "Gender, (Age Range)"

---

## Use Cases

### 1. Retail Analytics

Analyze customer demographics:

```bash
# Process store camera feed
python src/predictor.py
```

Use predictions to:
- Understand customer demographics
- Optimize product placement
- Target marketing campaigns

### 2. Event Management

Manage seating arrangements:

```bash
# Process event photos
python src/predictor.py --image event_photo.jpg
```

Use predictions to:
- Separate seating by gender
- Arrange age-appropriate sections
- Plan accessibility accommodations

### 3. Entertainment

Adapt experiences based on demographics:

```bash
# Real-time demographic analysis
python src/predictor.py
```

Use predictions to:
- Customize game difficulty by age
- Recommend age-appropriate content
- Personalize entertainment experience

### 4. Accessibility

Create inclusive experiences:

```bash
# Analyze audience composition
python src/predictor.py --image audience.jpg
```

Use predictions to:
- Identify accessibility needs
- Plan inclusive features
- Ensure diverse representation

---

## Tips and Best Practices

### For Best Results

1. **Lighting**: Ensure good, even lighting
2. **Face Position**: Position face directly toward camera
3. **Distance**: Keep face 1-2 meters from camera
4. **Angle**: Minimize head tilt for better accuracy
5. **Clarity**: Avoid blurry or obscured faces

### Confidence Threshold Selection

| Threshold | Use Case | Characteristics |
|-----------|----------|-----------------|
| 0.9+ | Strict security | Only very confident detections |
| 0.7-0.8 | General use | Balanced accuracy and coverage |
| 0.5-0.7 | Loose detection | Includes uncertain faces |
| <0.5 | Experimental | Many false positives |

### Performance Optimization

1. **Reduce Input Resolution**: Faster processing
2. **Increase Confidence**: Fewer detections = faster
3. **Close Other Apps**: More CPU available
4. **Use GPU**: If available (advanced setup)

---

## Batch Processing

### Process Multiple Images

Create a Python script `batch_process.py`:

```python
import os
import subprocess

image_dir = "images/"
for image_file in os.listdir(image_dir):
    if image_file.endswith(('.jpg', '.png', '.bmp')):
        image_path = os.path.join(image_dir, image_file)
        print(f"\nProcessing: {image_file}")
        subprocess.run(['python', 'src/predictor.py', '--image', image_path])
```

Run:
```bash
python batch_process.py
```

---

## Keyboard Controls

| Key | Action |
|-----|--------|
| `q` | Quit the program |
| `ESC` | Quit the program (alternative) |

---

## Common Scenarios

### Scenario 1: Analyze Store Customers

```bash
# Real-time analysis
python src/predictor.py

# Record observations:
# - Peak age groups
# - Gender distribution
# - Busy hours
```

### Scenario 2: Process Event Photos

```bash
# Analyze single photo
python src/predictor.py --image event.jpg

# Analyze multiple photos
for file in photos/*.jpg; do
    python src/predictor.py --image "$file"
done
```

### Scenario 3: Adjust for Difficult Lighting

```bash
# Lower confidence for poor lighting
python src/predictor.py --confidence 0.5

# Or process image file
python src/predictor.py --image dark_photo.jpg --confidence 0.6
```

### Scenario 4: Strict Face Detection

```bash
# Only detect very clear faces
python src/predictor.py --confidence 0.9
```

---

## Interpreting Results

### Age Ranges

The system predicts one of 8 age ranges:

| Range | Typical Age |
|-------|------------|
| (0-2) | Infants |
| (4-6) | Preschool |
| (8-12) | Elementary |
| (15-20) | Teenagers |
| (20-25) | Young Adults |
| (30-40) | Adults |
| (40-50) | Middle-aged |
| (60-100) | Seniors |

### Gender Classification

- **Male**: Predicted as male
- **Female**: Predicted as female

Note: These are statistical predictions based on facial features and may not reflect actual gender identity.

---

## Limitations to Remember

1. **Age Ranges**: Predictions are categorical, not exact ages
2. **Accuracy**: Varies with lighting, angle, and facial features
3. **Bias**: Pre-trained models may have inherent biases
4. **Privacy**: Always obtain consent before analyzing faces
5. **Reliability**: Not suitable for critical applications

---

## Troubleshooting During Usage

### No Faces Detected

**Try:**
1. Improve lighting
2. Move closer to camera
3. Lower confidence threshold:
   ```bash
   python src/predictor.py --confidence 0.5
   ```

### Incorrect Predictions

**Possible Causes:**
- Poor lighting
- Extreme face angles
- Partial face visibility
- Model limitations

**Note:** Age and gender predictions are probabilistic and may not always be accurate.

### Program Crashes

**Try:**
1. Restart the program
2. Check model files exist
3. Update OpenCV:
   ```bash
   pip install --upgrade opencv-python
   ```

---

## Advanced Topics

### Modifying Confidence Threshold in Code

Edit `src/predictor.py`:

```python
# Change default confidence
parser.add_argument('--confidence', type=float, default=0.8)
```

### Changing Age/Gender Categories

Edit `src/predictor.py`:

```python
age_list = [
    "(0-2)",
    "(4-6)",
    # ... modify as needed
]
```

### Adjusting Bounding Box Color

Edit `src/predictor.py`:

```python
# Change from (0, 255, 0) green to other colors
# BGR format: (Blue, Green, Red)
cv2.rectangle(..., (0, 0, 255), ...)  # Red
cv2.rectangle(..., (255, 0, 0), ...)  # Blue
```

---

## Next Steps

1. Explore different confidence thresholds
2. Test with various images and videos
3. Try different use cases
4. Read [MODELS.md](MODELS.md) for technical details
5. Modify code for custom applications

---

## Getting Help

If you encounter issues:
1. Check [SETUP.md](SETUP.md) for installation help
2. Review error messages carefully
3. Try adjusting confidence threshold
4. Check lighting and face positioning
5. Open an issue on GitHub with details
