# Download Models - Persona Predictor

Guide to downloading the pre-trained model files required for Persona Predictor.

---

## Why Download Models?

The model files are large binary files (~250MB total) and are not included in the GitHub repository. You need to download them separately and place them in the `models/` folder.

---

## Model Files Required

You need to download 6 files:

| File | Size | Purpose |
|------|------|---------|
| `opencv_face_detector.pbtxt` | ~50KB | Face detection architecture |
| `opencv_face_detector_uint8.pb` | ~2.7MB | Face detection weights |
| `age_deploy.prototxt` | ~50KB | Age prediction architecture |
| `age_net.caffemodel` | ~50MB | Age prediction weights |
| `gender_deploy.prototxt` | ~50KB | Gender classification architecture |
| `gender_net.caffemodel` | ~50MB | Gender classification weights |

**Total Size:** ~250MB

---

## Download Methods

### Method 1: Download from Official Sources (Recommended)

#### Face Detection Model
Download from OpenCV repository:
- `opencv_face_detector.pbtxt`: https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/opencv_face_detector.pbtxt
- `opencv_face_detector_uint8.pb`: https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/opencv_face_detector_uint8.pb

**Steps:**
1. Right-click each link
2. Select "Save Link As..."
3. Save to `Persona Predictor/models/` folder
4. Verify file size matches (should be ~2.7MB for .pb file)

#### Age & Gender Models
Download from Caffe Model Zoo:
- `age_deploy.prototxt`: https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/age_deploy.prototxt
- `age_net.caffemodel`: https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/age_net.caffemodel
- `gender_deploy.prototxt`: https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/gender_deploy.prototxt
- `gender_net.caffemodel`: https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/gender_net.caffemodel

**Steps:**
1. Right-click each link
2. Select "Save Link As..."
3. Save to `Persona Predictor/models/` folder
4. Verify file sizes (should be ~50MB for .caffemodel files)

---

### Method 2: Using Command Line (Windows PowerShell)

```powershell
# Create models folder if it doesn't exist
New-Item -ItemType Directory -Path "Persona Predictor\models" -Force

# Download Face Detection Model
$urls = @(
    "https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/opencv_face_detector.pbtxt",
    "https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/opencv_face_detector_uint8.pb",
    "https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/age_deploy.prototxt",
    "https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/age_net.caffemodel",
    "https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/gender_deploy.prototxt",
    "https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/gender_net.caffemodel"
)

$filenames = @(
    "opencv_face_detector.pbtxt",
    "opencv_face_detector_uint8.pb",
    "age_deploy.prototxt",
    "age_net.caffemodel",
    "gender_deploy.prototxt",
    "gender_net.caffemodel"
)

for ($i = 0; $i -lt $urls.Length; $i++) {
    $url = $urls[$i]
    $filename = $filenames[$i]
    $filepath = "Persona Predictor\models\$filename"
    
    Write-Host "Downloading $filename..."
    Invoke-WebRequest -Uri $url -OutFile $filepath
    
    $size = (Get-Item $filepath).Length / 1MB
    Write-Host "Downloaded: $filename ($([math]::Round($size, 2)) MB)"
}

Write-Host "All models downloaded successfully!"
```

---

### Method 3: Using Command Line (macOS/Linux)

```bash
# Create models folder if it doesn't exist
mkdir -p "Persona Predictor/models"

# Download Face Detection Model
wget -O "Persona Predictor/models/opencv_face_detector.pbtxt" \
  "https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/opencv_face_detector.pbtxt"

wget -O "Persona Predictor/models/opencv_face_detector_uint8.pb" \
  "https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/opencv_face_detector_uint8.pb"

# Download Age & Gender Models
wget -O "Persona Predictor/models/age_deploy.prototxt" \
  "https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/age_deploy.prototxt"

wget -O "Persona Predictor/models/age_net.caffemodel" \
  "https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/age_net.caffemodel"

wget -O "Persona Predictor/models/gender_deploy.prototxt" \
  "https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/gender_deploy.prototxt"

wget -O "Persona Predictor/models/gender_net.caffemodel" \
  "https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/gender_net.caffemodel"

echo "All models downloaded successfully!"
```

---

## Verify Downloaded Files

### Check File Sizes

**Windows PowerShell:**
```powershell
Get-ChildItem "Persona Predictor\models" -File | ForEach-Object {
    $size = $_.Length / 1MB
    Write-Host "$($_.Name): $([math]::Round($size, 2)) MB"
}
```

**macOS/Linux:**
```bash
ls -lh "Persona Predictor/models/"
```

### Expected File Sizes

| File | Expected Size |
|------|---------------|
| `opencv_face_detector.pbtxt` | ~50KB |
| `opencv_face_detector_uint8.pb` | ~2.7MB |
| `age_deploy.prototxt` | ~50KB |
| `age_net.caffemodel` | ~50MB |
| `gender_deploy.prototxt` | ~50KB |
| `gender_net.caffemodel` | ~50MB |

**Total:** ~250MB

### Verify All Files Present

**Windows PowerShell:**
```powershell
$required = @(
    "opencv_face_detector.pbtxt",
    "opencv_face_detector_uint8.pb",
    "age_deploy.prototxt",
    "age_net.caffemodel",
    "gender_deploy.prototxt",
    "gender_net.caffemodel"
)

$missing = @()
foreach ($file in $required) {
    if (-not (Test-Path "Persona Predictor\models\$file")) {
        $missing += $file
    }
}

if ($missing.Count -eq 0) {
    Write-Host "All model files present!" -ForegroundColor Green
} else {
    Write-Host "Missing files:" -ForegroundColor Red
    $missing | ForEach-Object { Write-Host "  - $_" }
}
```

---

## Troubleshooting Download Issues

### Issue: Downloaded File is HTML (Not Binary)

**Cause:** Using "Save Link As" on GitHub web interface instead of raw link

**Solution:**
1. Use the raw GitHub links provided above
2. Or use command-line download methods
3. Check file size - HTML files are only a few KB

### Issue: Download Interrupted

**Solution:**
1. Delete the incomplete file
2. Try downloading again
3. Use a download manager for large files

### Issue: Slow Download Speed

**Solution:**
1. Try downloading at different time
2. Use a VPN if GitHub is slow in your region
3. Download files one at a time
4. Use a download manager

### Issue: "Permission Denied" Error

**Solution:**
1. Ensure `models/` folder exists and is writable
2. Check folder permissions
3. Run command as administrator (Windows)
4. Use `sudo` (macOS/Linux)

---

## After Downloading

1. Verify all files are in `Persona Predictor/models/` folder
2. Check file sizes match expected values
3. Run the program:
   ```bash
   python src/predictor.py
   ```

---

## Alternative: Pre-packaged Download

If you have difficulty downloading individual files, you can:

1. Download a pre-packaged version from releases (if available)
2. Extract to `Persona Predictor/models/` folder
3. Run the program

---

## Model Sources

### Face Detection
- **Source:** OpenCV 3rdparty repository
- **License:** BSD 3-Clause
- **Repository:** https://github.com/opencv/opencv_3rdparty

### Age & Gender Classification
- **Source:** Caffe Model Zoo (Gil Levi & Tal Hassner)
- **License:** Creative Commons Attribution 4.0
- **Paper:** "Age and Gender Classification using Convolutional Neural Networks"
- **Repository:** https://github.com/GilLevi/AgeGenderDeepLearning

---

## FAQ

**Q: Why are models not included in the repository?**
A: Model files are large (~250MB) and GitHub has size limits. They're downloaded separately.

**Q: Can I use different models?**
A: Yes, but you'll need to modify the code to load different model architectures.

**Q: Are these models free to use?**
A: Yes, they're available under open licenses (BSD, Creative Commons).

**Q: How often do I need to download models?**
A: Only once. After downloading, they're reused for all runs.

**Q: Can I share downloaded models?**
A: Check the license terms. Generally, yes, but include attribution.

---

## Next Steps

1. Download all 6 model files
2. Place them in `Persona Predictor/models/` folder
3. Verify file sizes
4. Run `python src/predictor.py`
5. Read [USAGE.md](USAGE.md) for usage examples

---

## Getting Help

If you encounter issues:
1. Check file sizes match expected values
2. Verify all 6 files are present
3. Try re-downloading corrupted files
4. Check [SETUP.md](SETUP.md) for other troubleshooting
5. Open an issue on GitHub with details
