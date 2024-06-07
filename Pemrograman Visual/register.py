import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
import customtkinter as ctk
from PIL import ImageTk,Image
import os

class Register:
    def __init__(self, root):
        ctk.set_appearance_mode("light")
        self.root = root
        self.root.geometry("800x600")
        self.root.title('Daftar')

        self.bg = ctk.CTkFrame(root, width=800, height=600, fg_color='#517F9C')
        self.bg.place(x=0, y=0)

        my_image = ctk.CTkImage(dark_image=Image.open("./assets/login.png"), size=(800, 300))
        image_label1 = ctk.CTkLabel(self.bg, image=my_image, text="")
        image_label1.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

        self.frame = ctk.CTkFrame(self.root, width=320, height=360, fg_color='#FFFFFF', border_width=10, corner_radius=6, border_color='#CDE8E5')
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        lblMain = ctk.CTkLabel(master=self.frame, text="Daftar Akun", font=('Montserrat',20))
        lblMain.place(x=50, y=65)

        self.entryUsername = ctk.CTkEntry(master=self.frame, width=220, placeholder_text="Nama Pengguna", font=('Montserrat',13))
        self.entryUsername.place(x=50, y=110)

        self.entryPassword = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Kata Sandi', show="*", font=('Montserrat',13))
        self.entryPassword.place(x=50, y=165)

        self.entryName = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Nama Anda', font=('Montserrat',13))
        self.entryName.place(x=50, y=220)

        btnRegister = ctk.CTkButton(master=self.frame, width=220, text="Daftar", corner_radius=6, border_width=3, fg_color='#7AB2B2', border_color='#7AB2B2', font=('Montserrat',13), command=self.register)
        btnRegister.place(x=50, y=280)

        btnBack = ctk.CTkButton(master=self.frame, width=50, text="Kembali", corner_radius=6, border_width=3, fg_color='#7AB2B2', border_color='#7AB2B2', font=('Montserrat',13), command=self.back)
        btnBack.place(x=20, y=20)

    def register(self):
        username = self.entryUsername.get()
        password = self.entryPassword.get()
        name = self.entryName.get()
        if not username or not password:
            messagebox.showerror("Error", "Nama pengguna atau kata sandi tidak boleh kosong")
            return


        if Database.register(username, password, name):
            print("Registration Successful")
            messagebox.showinfo("Daftar Akun", "Daftar Akun Berhasil")
            self.back()
        else:
            messagebox.showerror("Error", "Nama pengguna sudah dipakai")

    def back(self):
        self.root.destroy()
        from login import Login
        login_root = ctk.CTk()
        app = Login(login_root)
        login_root.mainloop()


# root = ctk.CTk()
# app = Register(root)
# root.mainloop()
