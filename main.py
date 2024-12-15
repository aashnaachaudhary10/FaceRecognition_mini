from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import student  # Assuming the student class is imported from another file
import os
from train import Train
from face_recognition import Face_Recognition


class face_recognition_system:
    def __init__(self, root):  
        self.root = root  
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System") 
         
        # Add images for labels and buttons
        img = Image.open(r"C:\MiniProject\img\f4.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
        img1 = Image.open(r"C:\MiniProject\img\face2.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)
        
        img2 = Image.open(r"C:\MiniProject\img\f3.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=550, height=130)
        
        img3 = Image.open(r"C:\MiniProject\img\bg.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Adding buttons for each functionality
        img4 = Image.open(r"C:\MiniProject\img\f5.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        
        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)
        
        img5=Image.open(r"C:\MiniProject\img\f6.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        
        
        img6=Image.open(r"C:\MiniProject\img\f7.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        
        
        
        
        img7=Image.open(r"C:\MiniProject\img\f8.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        
        
        img8=Image.open(r"C:\MiniProject\img\f9.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        
        
        
        img9=Image.open(r"C:\MiniProject\img\f10.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        
        
        
        img10=Image.open(r"C:\MiniProject\img\f11.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10= ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        
        
        
        img11=Image.open(r"C:\MiniProject\img\f12.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11= ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
    
    
    
    def open_img(self):
        os.startfile(r"C:\MiniProject\image_metadata\data")
        
    
    
    
        
        # Repeat similar code for other buttons as needed (face detection, attendance, etc.)
        # Omitted for brevity...

    # Define the student_details method at the class level
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)  # Assuming 'student' is a class that you have imported

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window) 

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window) 



# Main loop to run the program
if __name__ == "__main__":  
    root = Tk()  
    obj = face_recognition_system(root)  
    root.mainloop()
