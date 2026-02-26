import cv2
import argparse
import os
import sys


def get_model_path(filename):
    """Get the absolute path to a model file with proper handling for spaces."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(os.path.dirname(current_dir), 'models')
    model_path = os.path.join(models_dir, filename)
    
    # Normalize path to handle spaces and special characters
    model_path = os.path.normpath(model_path)
    
    return model_path


def load_models():
    """Load all required deep learning models."""
    try:
        face_proto = get_model_path('opencv_face_detector.pbtxt')
        face_model = get_model_path('opencv_face_detector_uint8.pb')
        age_proto = get_model_path('age_deploy.prototxt')
        age_model = get_model_path('age_net.caffemodel')
        gender_proto = get_model_path('gender_deploy.prototxt')
        gender_model = get_model_path('gender_net.caffemodel')
        
        # Verify all model files exist
        required_files = [face_proto, face_model, age_proto, age_model, gender_proto, gender_model]
        missing_files = []
        corrupted_files = []
        
        for file_path in required_files:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
            elif os.path.getsize(file_path) == 0:
                corrupted_files.append(file_path)
        
        if missing_files:
            print("ERROR: Missing model files:")
            for f in missing_files:
                print(f"  - {f}")
            print("\nPlease ensure all model files are in the 'models/' directory.")
            sys.exit(1)
        
        if corrupted_files:
            print("ERROR: Corrupted model files (0 bytes):")
            for f in corrupted_files:
                print(f"  - {f}")
            print("\nModel files appear to be empty or corrupted.")
            print("Please re-download the model files from the repository.")
            sys.exit(1)
        
        print("Loading models...")
        face_net = cv2.dnn.readNet(face_model, face_proto)
        age_net = cv2.dnn.readNet(age_model, age_proto)
        gender_net = cv2.dnn.readNet(gender_model, gender_proto)
        
        print("Models loaded successfully!")
        return face_net, age_net, gender_net
    except Exception as e:
        print(f"Error loading models: {e}")
        print("\nTroubleshooting tips:")
        print("1. Ensure all model files are in the 'models/' folder")
        print("2. Check that model files are not corrupted (should be several MB)")
        print("3. Verify the path contains no special characters")
        print("4. Try moving the project to a path without spaces")
        sys.exit(1)


def highlight_face(net, frame, conf_threshold=0.7):
    """Detect faces in the frame and return bounding boxes."""
    try:
        frame_opencv_dnn = frame.copy()
        frame_height = frame_opencv_dnn.shape[0]
        frame_width = frame_opencv_dnn.shape[1]
        
        blob = cv2.dnn.blobFromImage(
            frame_opencv_dnn, 1.0, (300, 300), [104, 117, 123], True, False
        )
        
        net.setInput(blob)
        detections = net.forward()
        face_boxes = []
        
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                x1 = int(detections[0, 0, i, 3] * frame_width)
                y1 = int(detections[0, 0, i, 4] * frame_height)
                x2 = int(detections[0, 0, i, 5] * frame_width)
                y2 = int(detections[0, 0, i, 6] * frame_height)
                face_boxes.append([x1, y1, x2, y2])
                cv2.rectangle(
                    frame_opencv_dnn,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    int(round(frame_height / 150)),
                    8,
                )
        
        return frame_opencv_dnn, face_boxes
    except Exception as e:
        print(f"Error detecting faces: {e}")
        return frame, []


def predict_age_gender(age_net, gender_net, face, model_mean_values):
    """Predict age and gender for a detected face."""
    try:
        blob = cv2.dnn.blobFromImage(
            face, 1.0, (227, 227), model_mean_values, swapRB=False
        )
        
        gender_net.setInput(blob)
        gender_preds = gender_net.forward()
        gender = gender_list[gender_preds[0].argmax()]
        
        age_net.setInput(blob)
        age_preds = age_net.forward()
        age = age_list[age_preds[0].argmax()]
        
        return gender, age
    except Exception as e:
        print(f"Error predicting age/gender: {e}")
        return None, None


def main():
    parser = argparse.ArgumentParser(description='Detect faces and predict age and gender')
    parser.add_argument('--image', type=str, help='Path to input image file')
    parser.add_argument('--confidence', type=float, default=0.7, help='Confidence threshold for face detection (default: 0.7)')
    
    args = parser.parse_args()
    
    try:
        face_net, age_net, gender_net = load_models()
        
        if args.image:
            if not os.path.exists(args.image):
                print(f"Error: Image file not found: {args.image}")
                sys.exit(1)
            video = cv2.VideoCapture(args.image)
        else:
            video = cv2.VideoCapture(0)
        
        if not video.isOpened():
            print("Error: Could not open video source")
            sys.exit(1)
        
        padding = 20
        
        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            has_frame, frame = video.read()
            if not has_frame:
                cv2.waitKey()
                break
            
            result_img, face_boxes = highlight_face(face_net, frame, args.confidence)
            
            if not face_boxes:
                print("No face detected")
            
            for face_box in face_boxes:
                face = frame[
                    max(0, face_box[1] - padding): min(face_box[3] + padding, frame.shape[0] - 1),
                    max(0, face_box[0] - padding): min(face_box[2] + padding, frame.shape[1] - 1),
                ]
                
                gender, age = predict_age_gender(age_net, gender_net, face, model_mean_values)
                
                if gender and age:
                    print(f"Gender: {gender}, Age: {age[1:-1]} years")
                    cv2.putText(
                        result_img,
                        f"{gender}, {age}",
                        (face_box[0], face_box[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 255, 255),
                        2,
                        cv2.LINE_AA,
                    )
            
            cv2.imshow("Persona Predictor - Age and Gender Detection", result_img)
        
        video.release()
        cv2.destroyAllWindows()
    
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    model_mean_values = (78.4263377603, 87.7689143744, 114.895847746)
    age_list = [
        "(0-2)",
        "(4-6)",
        "(8-12)",
        "(15-20)",
        "(20-25)",
        "(30-40)",
        "(40-50)",
        "(60-100)",
    ]
    gender_list = ["Male", "Female"]
    
    main()
