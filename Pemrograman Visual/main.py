import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
import customtkinter as ctk
from PIL import ImageTk,Image
import os
import datetime

class Main:
    def __init__(self, root, username, tipe_akun):
        ctk.set_appearance_mode("light")
        self.root = root
        self.root.title("Aplikasi Sewa Laptop")
        self.root.geometry("800x600")

        self.main = ctk.CTkFrame(self.root, width=800, height=600, fg_color='#517F9C')
        self.main.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        frame1 = ctk.CTkFrame(self.main, width=800, height=150, fg_color='#7AB2B2', corner_radius=1)
        frame1.place(relx=0.5, rely=0, anchor=ctk.CENTER)
        logo = ctk.CTkImage(dark_image=Image.open("./assets/logo.png"), size=(150, 50))
        button2= ctk.CTkButton(frame1, image=logo, text=" ", fg_color='#7AB2B2', hover_color='#7AB2B2', command=self.home)
        button2.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)
        
        self.frame2 = ctk.CTkFrame(self.main, width=800, height=50, fg_color='#EEF7FF', corner_radius=1)
        self.frame2.place(relx=0.5, rely=0.15, anchor    =ctk.CENTER)
        self.btnSewa = ctk.CTkButton(self.frame2, text="Sewa Laptop", font=('Montserrat',15), fg_color='#4D869C', corner_radius=15, command=self.open_sewa, text_color_disabled='#4D869C', state='normal')
        self.btnSewa.place(relx=0.25, rely=0.5, anchor=ctk.CENTER)
        self.btnTabel = ctk.CTkButton(self.frame2, text="Tabel Laptop", font=('Montserrat',15), fg_color='#4D869C', corner_radius=15, command=self.open_tabel, text_color_disabled='#4D869C', state='normal')
        self.btnTabel.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.btnRiwayat = ctk.CTkButton(self.frame2, text="Riwayat Sewa Laptop", font=('Montserrat',15), fg_color='#4D869C', corner_radius=15, command=self.open_riwayat, text_color_disabled='#4D869C', state='normal')
        self.btnRiwayat.place(relx=0.75, rely=0.5, anchor=ctk.CENTER)
        
        self.frame3 = ctk.CTkFrame(self.main, width=800, height=500, corner_radius=1)
        self.frame3.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
        img_upj = ctk.CTkImage(dark_image=Image.open("./assets/upj.png"), size=(800, 500))
        upj = ctk.CTkLabel(self.frame3, image=img_upj, text="")
        upj.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        btnLogout = ctk.CTkButton(upj, text="Keluar", font=('Montserrat',15), fg_color='#FFFFFF', corner_radius=1, text_color='#4D869C', hover_color='#EEF7FF', command=self.logout)
        btnLogout.place(relx=0.9, rely=0.9, anchor=ctk.CENTER)

        self.user = username
        self.tipe_akun = tipe_akun

        #print(self.tipe_akun)

    def open_sewa(self):
        self.frame3.destroy()
        self.frame3 = ctk.CTkFrame(self.main, width=800, height=500, corner_radius=1, fg_color='#4D869C')
        self.frame3.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        self.btnSewa.configure(fg_color='#CACFD2', state='disabled')
        self.btnTabel.configure(fg_color='#4D869C', state='normal')
        self.btnRiwayat.configure(fg_color='#4D869C', state='normal')

        lblMain = ctk.CTkLabel(self.frame3, text="Form Sewa Laptop", font=('Montserrat',30), text_color='#FFFFFF')
        lblMain.place(x=10, y=10)
        my_image = ctk.CTkImage(dark_image=Image.open("./assets/Laptop.png"), size=(30, 30))
        image_label1 = ctk.CTkLabel(self.frame3, image=my_image, text="")
        image_label1.place(x=265, y=15)
        
        lblKodeLaptop = ctk.CTkLabel(self.frame3, text="Kode Laptop:", font=('Montserrat',15), text_color='#FFFFFF')
        lblKodeLaptop.place(x=10, y=60)
        kode = self.ambil_kode()
        self.comboKodeLaptop = ctk.CTkComboBox(self.frame3, font=('Montserrat',15),values=kode, width=150, variable=self.selected_kode, command=self.update_info)
        self.comboKodeLaptop.place(x=120, y=60)
        self.comboKodeLaptop.set("Pilih Kode Laptop")

        lblJenisLaptop1 = ctk.CTkLabel(self.frame3, text="Jenis Laptop:", font=('Montserrat',15), text_color='#FFFFFF')
        lblJenisLaptop1.place(x=10, y=90)
        self.lblJenisLaptop2 = ctk.CTkLabel(self.frame3, text="", font=('Montserrat',15), text_color='#FFFFFF')
        self.lblJenisLaptop2.place(x=120, y=90)

        lblHargaSewa1 = ctk.CTkLabel(self.frame3, text="Harga Sewa:", font=('Montserrat',15), text_color='#FFFFFF')
        lblHargaSewa1.place(x=10, y=120)
        self.lblHargaSewa2 = ctk.CTkLabel(self.frame3, text="", font=('Montserrat',15), text_color='#FFFFFF')
        self.lblHargaSewa2.place(x=120, y=120)

        btnTambah = ctk.CTkButton(self.frame3, text="Sewa", font=('Montserrat',15), fg_color='#FFFFFF', text_color='#4D869C', command=self.sewa_laptop)
        btnTambah.place(x=10, y=150)

        lblTabel = ctk.CTkLabel(self.frame3, text="Tabel sewa yang berlangsung", font=('Montserrat',30), text_color='#FFFFFF')
        lblTabel.place(x=10, y=200)

        self.create_table_list()

        btnAkhiri = ctk.CTkButton(self.frame3, text="Akhiri Sewa", font=('Montserrat',15), fg_color='#FFFFFF', text_color='#4D869C', command=self.akhiri_sewa)
        btnAkhiri.place(x=625, y=430)

    def open_tabel(self):
        self.frame3.destroy()
        self.frame3 = ctk.CTkFrame(self.main, width=800, height=500, corner_radius=1, fg_color='#4D869C')
        self.frame3.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        self.btnSewa.configure(fg_color='#4D869C', state='normal')
        self.btnTabel.configure(fg_color='#CACFD2', state='disabled')
        self.btnRiwayat.configure(fg_color='#4D869C', state='normal')

        lblMain = ctk.CTkLabel(self.frame3, text="Tabel Laptop", font=('Montserrat',30), text_color='#FFFFFF')
        lblMain.place(x=300, y=40)
        my_image = ctk.CTkImage(dark_image=Image.open("./assets/Laptop.png"), size=(30, 30))
        image_label2 = ctk.CTkLabel(self.frame3, image=my_image, text="")
        image_label2.place(x=480, y=45)

        self.create_table()

        btnTambah = ctk.CTkButton(self.frame3, text="Tambah Laptop", font=('Montserrat',20), fg_color='#FFFFFF', text_color='#4D869C', command=self.tambah_laptop)
        btnTambah.place(x=100, y=450)

        btnHapus = ctk.CTkButton(self.frame3, text="Hapus Laptop", font=('Montserrat',20), fg_color='#FFFFFF', text_color='#4D869C', command=self.hapus_laptop)
        btnHapus.place(x=550, y=450)

    def open_riwayat(self):
        self.frame3.destroy()
        self.frame3 = ctk.CTkFrame(self.main, width=800, height=500, corner_radius=1, fg_color='#4D869C')
        self.frame3.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        self.btnSewa.configure(fg_color='#4D869C', state='normal')
        self.btnTabel.configure(fg_color='#4D869C', state='normal')
        self.btnRiwayat.configure(fg_color='#CACFD2', state='disabled')

        lblMain = ctk.CTkLabel(self.frame3, text="Riwayat Sewa Laptop", font=('Montserrat',30), text_color='#FFFFFF')
        lblMain.place(x=10, y=100)

        my_image3 = ctk.CTkImage(dark_image=Image.open("./assets/history.png"), size=(30, 30))
        image_label3 = ctk.CTkLabel(self.frame3, image=my_image3, text="")
        image_label3.place(x=310, y=105)

        self.table_riwayat()

    def home(self):
        self.frame3.destroy()
        self.frame3 = ctk.CTkFrame(self.main, width=800, height=500, corner_radius=1)
        self.frame3.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        self.btnSewa.configure(fg_color='#4D869C', state='normal')
        self.btnTabel.configure(fg_color='#4D869C', state='normal')
        self.btnRiwayat.configure(fg_color='#4D869C', state='normal')

        img_upj = ctk.CTkImage(dark_image=Image.open("./assets/upj.png"), size=(800, 500))
        upj = ctk.CTkLabel(self.frame3, image=img_upj, text="")
        upj.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        btnLogout = ctk.CTkButton(upj, text="Logout", font=('Montserrat',15), fg_color='#FFFFFF', corner_radius=1, text_color='#4D869C', hover_color='#EEF7FF', command=self.logout)
        btnLogout.place(relx=0.9, rely=0.9, anchor=ctk.CENTER)


    def create_table(self):
        self.tree = ttk.Treeview(self.frame3, show='headings' )
        self.tree['columns'] = ('Kode Laptop','Jenis Laptop', 'Status', 'Harga Sewa')
        self.tree.column('Kode Laptop', width=50, anchor=tk.CENTER)
        self.tree.column('Jenis Laptop', anchor=tk.CENTER)
        self.tree.column('Status', anchor=tk.CENTER)
        self.tree.column('Harga Sewa', anchor=tk.CENTER)
        self.tree.heading('Kode Laptop', text='Kode')
        self.tree.heading('Jenis Laptop', text='Jenis Laptop')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Harga Sewa', text='Harga Sewa')

        data = Database.get_laptops()
        if data:
            for (kode_laptop, jenis_laptop, status, harga_sewa) in data:
                self.tree.insert('', 'end', values=(kode_laptop, harga_sewa, status, jenis_laptop))

        self.tree.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def tambah_laptop(self):
        if self.tipe_akun.lower() != 'admin':
            messagebox.showerror("Access Denied", "Anda tidak memiliki izin untuk menambah laptop.")
            return
            
        top = tk.Toplevel(self.root)
        top.configure(bg='#517F9C')
        top.title("Tambah Laptop")
        top.geometry("400x300")

        lblMain = ctk.CTkLabel(top, text="Tambah Laptop", font=('Montserrat', 20), text_color='#FFFFFF')
        lblMain.pack(pady=10)

        lblKode = ctk.CTkLabel(top, text="Kode Laptop:", font=('Montserrat', 15), text_color='#FFFFFF')
        lblKode.place(x=10, y=50)
        self.kode_entry = ctk.CTkEntry(top, font=('Montserrat', 12))
        self.kode_entry.place(x=150, y=50)

        lblJenis = ctk.CTkLabel(top, text="Jenis Laptop:", font=('Montserrat', 15), text_color='#FFFFFF')
        lblJenis.place(x=10, y=100)
        self.jenis_entry = ctk.CTkEntry(top, font=('Montserrat', 12))
        self.jenis_entry.place(x=150, y=100)

        lblHarga = ctk.CTkLabel(top, text="Harga Sewa:", font=('Montserrat', 15), text_color='#FFFFFF')
        lblHarga.place(x=10, y=150)
        self.harga_entry = ctk.CTkEntry(top, font=('Montserrat', 12))
        self.harga_entry.place(x=150, y=150)

        btnSubmit = ctk.CTkButton(top, text="Tambah", font=('Montserrat', 15), fg_color='#FFFFFF', text_color='#4D869C', command=self.submit_laptop)
        btnSubmit.place(x=50, y=250)

        btnClose = ctk.CTkButton(top, text="Batal", font=('Montserrat', 15), fg_color='#FFFFFF', text_color='#4D869C', command=top.destroy)
        btnClose.place(x=200, y=250)

    def hapus_laptop(self):
        if self.tipe_akun.lower() != 'admin':
            messagebox.showerror("Access Denied", "Anda tidak memiliki izin untuk menghapus laptop.")
            return

        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih laptop yang akan dihapus.")
            return

        confirmation = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus laptop ini?")
        if confirmation:
            # Hapus laptop dari database
            kode_laptop = self.tree.item(selected_item)['values'][0]
            if Database.delete_laptop(kode_laptop):
                self.tree.delete(selected_item)
                messagebox.showinfo("Info", "Laptop berhasil dihapus.")
            else:
                messagebox.showerror("Error", "Gagal menghapus laptop.")

    def submit_laptop(self):
        kode_laptop = self.kode_entry.get()
        jenis_laptop = self.jenis_entry.get()
        harga_sewa = self.harga_entry.get()

        if not (kode_laptop and jenis_laptop and harga_sewa):
            messagebox.showwarning("Error", "Semua kolom harus diisi.")
            return

        if Database.add_laptop(kode_laptop, jenis_laptop, harga_sewa):
            messagebox.showinfo("Info", "Laptop berhasil ditambahkan.")
            self.refresh_table_laptop()
            self.kode_entry.delete(0, ctk.END) 
            self.jenis_entry.delete(0, ctk.END)  
            self.harga_entry.delete(0, ctk.END)
        else:
            messagebox.showerror("Error", "Gagal menambahkan laptop.")

    def refresh_table_laptop(self):
        # Hapus semua entri saat ini dari tabel
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Perbarui tabel dengan data terbaru dari database
        data = Database.get_laptops()
        if data:
            for (kode_laptop, jenis_laptop, status, harga_sewa) in data:
                self.tree.insert('', 'end', values=(kode_laptop, harga_sewa, status, jenis_laptop))

    def update_info(self, selected_kode):
        jenis = Database.get_jenis(selected_kode)
        self.lblJenisLaptop2.configure(text=jenis)

        harga = Database.get_harga(selected_kode)
        self.lblHargaSewa2.configure(text=harga)

    def create_table_list(self):
        self.tree = ttk.Treeview(self.frame3, show='headings' )
        self.tree['columns'] = ('Id Sewa','Kode Laptop','Jenis Laptop', 'Harga Sewa/Jam', 'Jam Mulai', 'Tanggal')
        self.tree.column('Id Sewa', width=50, anchor=tk.CENTER)
        self.tree.column('Kode Laptop', width=50, anchor=tk.CENTER)
        self.tree.column('Jenis Laptop', width=100, anchor=tk.CENTER)
        self.tree.column('Harga Sewa/Jam', width=100, anchor=tk.CENTER)
        self.tree.column('Jam Mulai', width=100, anchor=tk.CENTER)
        self.tree.column('Tanggal', anchor=tk.CENTER)
        self.tree.heading('Id Sewa', text='Id Sewa')
        self.tree.heading('Kode Laptop', text='Kode')
        self.tree.heading('Jenis Laptop', text='Jenis Laptop')
        self.tree.heading('Harga Sewa/Jam', text='Harga Sewa/Jam')
        self.tree.heading('Jam Mulai', text='Jam Mulai')
        self.tree.heading('Tanggal', text='Tanggal')

        data = Database.get_list()
        if data:
            for (id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_mulai, created_at) in data:
                self.tree.insert('', 'end', values=(id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_mulai, created_at))

        self.tree.place(x=10, y=240)

    def sewa_laptop(self):
        kode_laptop = self.selected_kode.get()
        jenis = self.lblJenisLaptop2.cget("text")
        if not jenis:
            messagebox.showwarning("Peringatan", "Silakan pilih kode laptop terlebih dahulu.")
            return
        harga = self.lblHargaSewa2.cget("text")

        if Database.sewa_laptop(kode_laptop, jenis, harga, self.user):
            messagebox.showinfo("Sukses", "Laptop berhasil disewa!")
            self.refresh_table_sewa()
            
            # Hapus item terpilih dari daftar nilai ComboBox
            Database.update_status_aktif(kode_laptop)

            # Update Combobox
            kode = self.ambil_kode()
            self.comboKodeLaptop.configure(values=kode)
            self.comboKodeLaptop.set("Pilih Kode Laptop")
            self.lblJenisLaptop2.configure(text="")
            self.lblHargaSewa2.configure(text="")
        else:
            messagebox.showerror("Error", "Gagal menyewa laptop.")

    def akhiri_sewa(self):
        selected_item = self.tree.selection()
        
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih laptop yang akan diakhiri sewanya.")
            return
        id_sewa = self.tree.item(selected_item)['values'][0]

        confirmation = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin mengakhiri sewa laptop ini?")
        if confirmation:
            # Akhiri sewa laptop dan dapatkan waktu mulai dan akhir sewa
            kode_laptop = self.tree.item(selected_item)['values'][1]  # Ambil kode laptop dari item terpilih
            # Mengambil waktu saat ini
            waktu_sekarang = datetime.datetime.now()

            # Mengambil jam saat ini
            jam_sekarang = waktu_sekarang.hour
            p_jam_akhir = waktu_sekarang.strftime("%H:%M:%S")

            jam_mulai, jam_akhir = Database.akhiri_sewa(id_sewa)
            p_jam_mulai = jam_mulai
            

            if jam_mulai is not None and jam_akhir is not None:
                messagebox.showinfo("Info", "Sewa laptop berhasil diakhiri.")
                self.refresh_table_sewa()
                Database.update_status_null(kode_laptop)

                jam_mulai = int(jam_mulai.split(':')[0])
                jam_akhir = int(jam_sekarang)

                jam = jam_akhir - jam_mulai

                selisih = 1
                if jam > 0:
                    selisih += jam

                harga_sewa = Database.get_harga(kode_laptop)

                total_harga = selisih * harga_sewa
                Database.update_harga(total_harga, id_sewa)
                info_message = f"Total harga yang harus dibayar: Rp. {total_harga}\nBerhasil diakhiri dengan jam awal {p_jam_mulai} dan jam akhir {p_jam_akhir}"
            
                messagebox.showinfo("Info", info_message) 

                kode = self.ambil_kode()
                self.comboKodeLaptop.configure(values=kode)

                num_stars = 5
                self.top_level = tk.Toplevel(self.root)
                self.top_level.title("Star Rating")
                self.top_level.geometry("300x200")
                self.top_level.configure(bg="#344C64")
                self.create_widgets(num_stars)
            else:
                messagebox.showerror("Error", "Gagal mengakhiri sewa laptop.")

    def refresh_table_sewa(self):
        # Hapus semua entri saat ini dari tabel
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Perbarui tabel dengan data terbaru dari database
        data = Database.get_list()
        if data:
            for (id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_mulai, created_at) in data:
                self.tree.insert('', 'end', values=(id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_mulai, created_at))

    def table_riwayat(self):
        self.tree = ttk.Treeview(self.frame3, show='headings' )
        self.tree['columns'] = ('Id Sewa','Kode Laptop','Jenis Laptop', 'Harga Sewa/Jam', 'Jam Mulai', 'Jam Akhir', 'Tanggal', 'Total Harga')
        self.tree.column('Id Sewa', width=50, anchor=tk.CENTER)
        self.tree.column('Kode Laptop', width=50, anchor=tk.CENTER)
        self.tree.column('Jenis Laptop', width=100, anchor=tk.CENTER)
        self.tree.column('Harga Sewa/Jam', width=100, anchor=tk.CENTER)
        self.tree.column('Jam Mulai', width=100, anchor=tk.CENTER)
        self.tree.column('Jam Akhir', width=100, anchor=tk.CENTER)
        self.tree.column('Tanggal', anchor=tk.CENTER)
        self.tree.column('Total Harga', width=100, anchor=tk.CENTER)
        self.tree.heading('Id Sewa', text='Id Sewa')
        self.tree.heading('Kode Laptop', text='Kode')
        self.tree.heading('Jenis Laptop', text='Jenis Laptop')
        self.tree.heading('Harga Sewa/Jam', text='Harga Sewa/Jam')
        self.tree.heading('Jam Mulai', text='Jam Mulai')
        self.tree.heading('Jam Akhir', text='Jam Akhir')
        self.tree.heading('Tanggal', text='Tanggal')
        self.tree.heading('Total Harga', text='Total Harga')

        data = Database.riwayat(self.user)
        if data:
            for (id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_mulai, jam_akhir, created_at, total_harga, user) in data:
                self.tree.insert('', 'end', values=(id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_akhir, created_at, total_harga, jam_mulai))

        self.tree.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def ambil_kode(self):
        kode = Database.get_kode()
        self.kode_strings = [code[0] for code in kode]
        self.selected_kode = ctk.StringVar()
        return self.kode_strings
    
    def logout(self):
        frame = ctk.CTkFrame(self.main, width=450, height=200, corner_radius=1, fg_color='#344C64')
        frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        l2 = ctk.CTkLabel(frame, text="Anda yakin ingin", font=('Montserrat', 20), text_color='#EEF7FF')
        l2.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
        l3 = ctk.CTkLabel(frame, text="ingin keluar dari aplikasi?", font=('Montserrat', 20), text_color='#EEF7FF')
        l3.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)
        btnTidak = ctk.CTkButton(frame, text="Tidak", width=100, text_color='#000000', corner_radius=1, fg_color='#FF9090', command=frame.destroy)
        btnTidak.place(x=130, y=120)
        btnYa = ctk.CTkButton(frame, text="Ya", width=50, text_color='#000000', corner_radius=1, fg_color='#B7B7B7', command=self.open_login)
        btnYa.place(x=250, y=120)

    def open_login(self):
        self.root.destroy()
        from login import Login
        login_root = ctk.CTk()
        app = Login(login_root)
        login_root.mainloop()

    def create_widgets(self, num_stars):
        stars = []
        current_rating = [0]  # Menggunakan list untuk menyimpan rating

        def set_rating(rating):
            current_rating[0] = rating
            highlight_stars(rating)

        def highlight_stars(rating):
            for i, star in enumerate(stars):
                if i < rating:
                    star.config(text='★')
                else:
                    star.config(text='☆')

        for i in range(num_stars):
            star = tk.Label(self.top_level, text='☆', font=('Montserrat', 30), cursor="hand2", bg='#344C64', fg='yellow')
            star.grid(row=0, column=i, sticky="NESW")
            star.bind("<Button-1>", lambda e, idx=i: set_rating(idx + 1))
            star.bind("<Enter>", lambda e, idx=i: highlight_stars(idx + 1))
            star.bind("<Leave>", lambda e: highlight_stars(current_rating[0]))
            stars.append(star)

        submit_button = ctk.CTkButton(self.top_level, text="Selesai", fg_color='#FFFFFF', text_color='#4D869C', command=self.top_level.destroy)
        submit_button.place(relx=0.5, rely=0.85, anchor=ctk.CENTER)

        lbl1 = ctk.CTkLabel(self.top_level, text="Apakah Anda suka dengan", font=('Montserrat',20))
        lbl1.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)
        lbl2 = ctk.CTkLabel(self.top_level, text="aplikasi Sewa Laptop", font=('Montserrat',20))
        lbl2.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)
        lbl3 = ctk.CTkLabel(self.top_level, text="Kasih rating untuk laptop", font=('Montserrat',10))
        lbl3.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)


# root = ctk.CTk()
# app = Main(root)
# root.mainloop()
