from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top Image
        img_top = Image.open(r"C:\MiniProject\img\images.jpeg")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # Train Button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", 
                      font=("times new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        # Bottom Image
        img_bottom = Image.open(r"C:\MiniProject\img\f11.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = r"C:\MiniProject\image_metadata\data"

        # Validate directory
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"The directory '{data_dir}' does not exist.")
            return
        
        # Supported image formats
        valid_extensions = ('.jpg', '.jpeg', '.png')
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.lower().endswith(valid_extensions)]

        faces = []
        ids = []

        for image_path in path:
            try:
                file_name = os.path.split(image_path)[1]
                file_parts = file_name.split('.')
                
                if len(file_parts) > 1 and file_parts[1].isdigit():
                    id = int(file_parts[1])
                    img = Image.open(image_path).convert('L')  # Convert to grayscale
                    image_np = np.array(img, 'uint8')

                    faces.append(image_np)
                    ids.append(id)

                    # Optional: Display training images
                    # Uncomment the next two lines to visualize
                    # cv2.imshow("Training", image_np)
                    # cv2.waitKey(1)
                else:
                    print(f"Skipping file: {file_name} (Invalid ID format)")

            except Exception as e:
                print(f"Error processing file {image_path}: {str(e)}")

        if len(faces) == 0:
            messagebox.showerror("Error", "No valid images found for training.")
            return

        ids = np.array(ids)

        # Train the classifier
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)

            # Save the model
            model_path = r"C:\MiniProject\classifier.xml"
            clf.write(model_path)
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", f"Training completed successfully. Model saved at {model_path}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during training: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

