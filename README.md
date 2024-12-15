# Face Recognition System

This project implements a face recognition system using OpenCV, Haar cascades, and a custom-trained LBPH face recognizer. It is integrated with a MySQL database to fetch and display user details such as name, roll number, and department based on the recognized face.

## Folder Structure
```
image_metadata/          # Contains Haar cascade files for face detection
img/                     # Contains images used in the GUI
.gitignore               # Lists files and directories to ignore in Git
LICENSE                  # License file
README.md                # Project documentation
classifier.xml           # Trained model for face recognition
face_recognition.py      # Face recognition implementation
file.txt                 # Placeholder or additional file
main.py                  # Main script to launch the system
student.py               # Handles student-related functionalities
train.py                 # Handles training of the face recognition model
face_recognition_database.sql     # SQL script to set up the database
```

## Features
- **Real-time Face Recognition**: Detect and recognize faces from a live webcam feed.
- **Database Integration**: Fetch user details from a MySQL database.
- **GUI Integration**: User-friendly graphical interface built using Tkinter.
- **Custom Training**: Train the LBPH recognizer using labeled datasets.

## Requirements
### Python Libraries
- `opencv-python`
- `Pillow`
- `mysql-connector-python`
- `tkinter` (built-in with Python)
- `numpy`

Install the dependencies using:
```bash
pip install opencv-python Pillow mysql-connector-python numpy
```

### MySQL Setup
- Import the provided `face_recognition_database.sql` file into your MySQL database to set up the required structure and initial data.
  ```bash
  mysql -u <username> -p facerecognition < face_recognition_database.sql
  ```

### Files
- `classifier.xml`: Contains the trained LBPH model.
- `haarcascade_frontalface_default.xml`: Haar cascade file for face detection.

## How to Run
### Step 1: Add Students and Images
1. Open the `student.py` script to add student details and their images.
   ```bash
   python student.py
   ```
2. Ensure images for each student are correctly labeled and stored.

### Step 2: Train the Model
1. Use the `train.py` script to train the face recognizer:
   ```bash
   python train.py
   ```
2. Ensure the trained model (`classifier.xml`) is generated in the root directory.

### Step 3: Run the Face Recognition System
1. Launch the main application:
   ```bash
   python main.py
   ```
2. The system will open a GUI with options to initiate face recognition.

### Step 4: Perform Face Recognition
1. Use the `face_recognition.py` script to start the face recognition process.
   ```bash
   python face_recognition.py
   ```
2. The system will detect faces and display the recognized details or mark the face as "Unknown."

## Code Highlights
### GUI Layout
The main GUI is designed using Tkinter with two sections for images and a button to trigger face recognition.
```python
self.root.geometry("1530x790+0+0")
title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="black")
```

### Face Detection and Recognition
Haar cascades are used for face detection, and LBPH recognizer predicts the ID.
```python
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
```

### Database Integration
Fetch user details based on the recognized ID:
```python
my_cursor.execute("SELECT name FROM student WHERE StudentId=%s", (id,))
```

## Future Enhancements
- Add support for multiple datasets and user roles.
- Enhance accuracy with deep learning-based models like FaceNet.
- Implement attendance tracking.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author
- **Aashnaa Chaudhary**

