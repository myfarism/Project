import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
import customtkinter as ctk
from PIL import ImageTk,Image
import os
from register import Register
from main import Main

class Login:
    def __init__(self, root):
        ctk.set_appearance_mode("light")
        self.root = root
        self.root.geometry("800x600")
        self.root.title('Masuk')

        self.bg = ctk.CTkFrame(root, width=800, height=600, fg_color='#517F9C')
        self.bg.place(x=0, y=0)

        my_image = ctk.CTkImage(dark_image=Image.open("./assets/login.png"), size=(800, 300))
        image_label1 = ctk.CTkLabel(self.bg, image=my_image, text="")
        image_label1.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

        self.frame = ctk.CTkFrame(self.root, width=320, height=360, fg_color='#FFFFFF', border_width=10, corner_radius=6, border_color='#CDE8E5')
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        lblMain = ctk.CTkLabel(master=self.frame, text="MASUK", font=('Montserrat',20))
        lblMain.place(x=50, y=45)

        self.entryUsername = ctk.CTkEntry(master=self.frame, width=220, placeholder_text="Nama Pengguna", font=('Montserrat',13))
        self.entryUsername.place(x=50, y=110)

        self.entryPassword = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Kata Sandi', show="*", font=('Montserrat',13))
        self.entryPassword.place(x=50, y=165)

        btnLogin = ctk.CTkButton(master=self.frame, width=220, text="Masuk", corner_radius=6, border_width=3, fg_color='#7AB2B2', border_color='#7AB2B2', font=('Montserrat',13), command=self.login)
        btnLogin.place(x=50, y=240)

        btnRegister = ctk.CTkButton(master=self.frame, width=220, text="Daftar Akun", corner_radius=6, border_width=3, fg_color='#7AB2B2', border_color='#7AB2B2', font=('Montserrat',13), command=self.open_register_window)
        btnRegister.place(x=50, y=290)

    def login(self):
        username = self.entryUsername.get()
        password = self.entryPassword.get()

        if not username or not password:
            messagebox.showerror("Error", "Nama pengguna atau kata sandi tidak boleh kosong")
            return

        tipe_akun = Database.check_credentials(username, password)
        if tipe_akun:
            # print("Masuk Ber")
            self.root.destroy()
            main_root = ctk.CTk()
            app = Main(main_root, username, tipe_akun)
            main_root.mainloop()
            # Do something after successful login
        else:
            messagebox.showerror("Error", "Nama pengguna atau kata sandi salah")

    def open_register_window(self):
        self.root.destroy()
        register_root = ctk.CTk()
        app = Register(register_root)
        register_root.mainloop()


# root = ctk.CTk()
# app = Login(root)
# root.mainloop()
