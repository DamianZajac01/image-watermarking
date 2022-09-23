from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from app_brain import AppBrain

FONT_NAME = 'Helvetica'

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class UserInterface:

    def __init__(self, app_brain: AppBrain):
        self.app = app_brain

        self.root_tk = customtkinter.CTk()
        self.root_tk.title("Image Watermarking")
        self.root_tk.iconbitmap("images/app_icon.ico")
        self.root_tk.geometry("720x700")

        self.add_folder_img = ImageTk.PhotoImage(Image.open("images/add-folder.png").resize((20, 20), Image.ANTIALIAS))
        self.add_mark_img = ImageTk.PhotoImage(Image.open("images/add-mark.png").resize((20, 20), Image.ANTIALIAS))

        self.label_upper = customtkinter.CTkLabel(master=self.root_tk, text="Welcome to Image Watermarking", text_font=(FONT_NAME, 16))
        self.label_upper.pack(pady=30)

        self.btn_folder = customtkinter.CTkButton(master=self.root_tk, image=self.add_folder_img, text="Add File", width=190, height=40, compound="left", command=self.open_file)
        self.btn_folder.pack()

        self.btn_mark = customtkinter.CTkButton(master=self.root_tk, image=self.add_mark_img, text="Add Mark", width=190, height=40, compound="left", fg_color="#D35B58", hover_color="#ff3333", command=self.add_mark)
        self.btn_mark.pack(pady=20)

        self.label_frame = customtkinter.CTkFrame(master=self.root_tk, corner_radius=10)
        self.label_frame.pack(pady=20)

        self.entry = customtkinter.CTkEntry(self.label_frame, width=400, height=40, border_width=1, placeholder_text="Enter Text", text_color="silver")
        self.entry.grid(column=0, row=0, padx=10, pady=10)

        self.btn_text = customtkinter.CTkButton(self.label_frame, text="Add Text", command=self.add_text)
        self.btn_text.grid(column=1, row=0, padx=10, pady=10)

        self.btn_save = customtkinter.CTkButton(master=self.root_tk, image=self.add_folder_img, text="Save File",
                                                width=190, height=40, compound="left", fg_color="#28a428",
                                                hover_color="#196719", command=self.save_file)
        self.btn_save.pack()

        self.root_tk.mainloop()

    def open_file(self):
        self.app.open_file()

    def add_text(self):
        self.app.add_text(self.entry.get(), self.entry)

    def add_mark(self):
        self.app.add_mark()

    def save_file(self):
        self.app.save_file()
