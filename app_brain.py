from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image, ImageFont, ImageDraw
import os


class AppBrain:

    def __init__(self, main_img_x, main_img_y):
        self.main_img_x = main_img_x
        self.main_img_y = main_img_y
        self.main_file_name = ""

        self.filename = None
        self.image = None
        self.mark = None
        self.image_label = None
        self.new_img = None
        self.watermark = None
        self.current_img = None

    def get_path_file(self):
        self.filename = filedialog.askopenfilename(initialdir="images_to_mark", title="Select A File", filetypes=(("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("All FIles", "*.*")), )
        return self.filename

    def open_file(self):
        try:
            self.image = ImageTk.PhotoImage(Image.open(self.get_path_file()).resize((self.main_img_x, self.main_img_y)))
            self.main_file_name = self.filename
            self.image_label = Label(image=self.image)
            self.image_label.pack(pady=20)
        except AttributeError:
            pass

    def add_text(self, user_text, entry_field):
        try:
            self.current_img = Image.open(self.filename)
            text_font = ImageFont.truetype("arial.ttf", 64)

            edit_img = ImageDraw.Draw(self.current_img)
            edit_img.text((0, 550), user_text, fill=("white"), font=text_font)

            # Only for image preview
            img_copy_path = self.main_file_name.split(".")[0] + "_copy." + self.main_file_name.split(".")[1]
            self.current_img.save(img_copy_path)
            self.show_new_img(img_copy_path)
            os.remove(img_copy_path)
            if user_text != "":
                entry_field.delete(0, END)

        except AttributeError:
            entry_field.delete(0, END)
            messagebox.showinfo("Information", "First upload your image.")

    def add_mark(self):
        try:
            self.current_img = Image.open(self.filename)
            self.watermark = Image.open(self.get_path_file()).resize((self.main_img_x, self.main_img_y))
            self.current_img.paste(self.watermark, (100, 150), self.watermark)

            # Only for image preview
            img_copy_path = self.main_file_name.split(".")[0] + "_copy." + self.main_file_name.split(".")[1]
            self.current_img.save(img_copy_path)
            self.show_new_img(img_copy_path)
            os.remove(img_copy_path)

        except AttributeError:
            messagebox.showinfo("Information", "First upload your image.")

    def show_new_img(self, img_to_show):
        self.new_img = ImageTk.PhotoImage(Image.open(f"{img_to_show}").resize((self.main_img_x, self.main_img_y)))
        self.image_label.config(image=self.new_img)

    def save_file(self):
        try:
            if self.current_img:
                path = filedialog.asksaveasfilename(defaultextension=".*", initialdir="edited_img", title="Save File", filetypes=(("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("All FIles", "*.*")))
                self.current_img.save(path)
            else:
                messagebox.showinfo("Information", "First add watermark to your image.")
        except ValueError:
            pass
