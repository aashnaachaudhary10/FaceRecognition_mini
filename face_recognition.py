from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import mysql.connector

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # First Image
        img_top = Image.open(r"C:\MiniProject\img\Screenshot (18).png")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # Second Image
        img_bottom = Image.open(r"C:\MiniProject\img\Screenshot (19).png")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", font=("times new roman", 19, "bold"), bg="dark green", fg="white", command=self.face_recog)
        b1_1.place(x=370, y=650, width=200, height=40)

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

                # Predict ID and Confidence
                id,predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                # Debugging Outputs
                print(f"Predicted ID: {id}, Confidence: {confidence}%")

                conn = mysql.connector.connect(host="localhost", username="root", password="itsjiya@12345", database="facerecognition")
                my_cursor = conn.cursor()

                # Fetch details from the database
                my_cursor.execute("SELECT name FROM student WHERE StudentId=%s", (id,))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("SELECT Roll FROM student WHERE StudentId=%s", (id,))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("SELECT Dep FROM student WHERE StudentId=%s", (id,))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                # Display Name, Roll, and Department
                if confidence > 50:  # Confidence threshold
                    cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), clf)
            return img

        # Load Haar Cascade file
        faceCascade = cv2.CascadeClassifier(r"C:\MiniProject\image_metadata\haarcascade_frontalface_default.xml")
        if faceCascade.empty():
            messagebox.showerror("Error", "Haar Cascade XML file not found!")
            return

        # Load trained model
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\MiniProject\classifier.xml")

        # Open webcam
        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Unable to access webcam!")
            return

        while True:
            ret, frame = video_cap.read()
            if not ret:
                print("Failed to grab frame!")
                break

            img = recognize(frame, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
