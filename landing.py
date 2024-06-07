import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
import customtkinter as ctk
from PIL import ImageTk,Image
import os
from login import Login


class Landing:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Sewa Laptop")
        self.root.geometry("800x600")

        self.frame = ctk.CTkFrame(self.root, width=800, height=600)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        my_image = ctk.CTkImage(dark_image=Image.open("./assets/logo.png"), size=(450, 200))
        image_label1 = ctk.CTkLabel(self.frame, image=my_image, text="")
        image_label1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        btnNext = ctk.CTkButton(self.frame, text="Next", font=('Montserrat',15), fg_color='#FFFFFF', text_color='#7AB2B2', hover_color='#4D869C', command=self.next_page)
        btnNext.place(x=650, y=550)

    def next_page(self):
            self.frame.destroy()
            self.frame = ctk.CTkFrame(self.root, width=800, height=600)
            self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
            my_image = ctk.CTkImage(dark_image=Image.open("./assets/laptop landing.png"), size=(450, 200))
            image_label1 = ctk.CTkLabel(self.frame, image=my_image, text="")
            image_label1.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

            lbl1 = ctk.CTkLabel(self.frame, text="Sewa laptop dengan mudah", font=('Montserrat',50))
            lbl1.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

            lbl2 = ctk.CTkLabel(self.frame, text="Kelola penyewaan laptop Anda dengan mudah dengan sistem", font=('Montserrat',20))
            lbl2.place(relx=0.5, rely=0.17, anchor=ctk.CENTER)

            lbl3 = ctk.CTkLabel(self.frame, text="manajemen penyewaan kami yang intuitif. Temukan laptop yang", font=('Montserrat',20))
            lbl3.place(relx=0.5, rely=0.21, anchor=ctk.CENTER)

            lbl4 = ctk.CTkLabel(self.frame, text="tepat untuk kebutuhan Anda, nikmati periode penyewaan yang ", font=('Montserrat',20))
            lbl4.place(relx=0.5, rely=0.251, anchor=ctk.CENTER)

            lbl5 = ctk.CTkLabel(self.frame, text="fleksibel, dan permudah pengalaman teknologi Anda.", font=('Montserrat',20))
            lbl5.place(relx=0.5, rely=0.29, anchor=ctk.CENTER)

            btnNext = ctk.CTkButton(self.frame, text="Next", font=('Montserrat',15), fg_color='#FFFFFF', text_color='#7AB2B2', hover_color='#4D869C', command=self.open_login)
            btnNext.place(x=650, y=550)

    def open_login(self):
        self.root.destroy()
        login_root = ctk.CTk()
        app = Login(login_root)
        login_root.mainloop()

            
ctk.set_appearance_mode("light")
root = ctk.CTk()
app = Landing(root)
root.mainloop()