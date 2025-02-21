# Persona Predictor

The Persona Predictor is a Python program that detects faces in images or video streams and predicts the age and gender of the detected faces using OpenCV's deep learning capabilities.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Usage

To run the program, use the following command:

```bash
python inferenceprogram.py --image <path_to_image>
```

If you want to use the webcam, simply run:

```bash
python inferenceprogram.py
```

## Models

The program requires the following model files to be present in the same directory:

- `opencv_face_detector.pbtxt`
- `opencv_face_detector_uint8.pb`
- `age_deploy.prototxt`
- `age_net.caffemodel`
- `gender_deploy.prototxt`
- `gender_net.caffemodel`

Make sure to download these models and place them in the project directory.

## Example

Run the program with an image:

```bash
python inferenceprogram.py --image example.jpg
```

This will display the detected faces along with their predicted age and gender.
