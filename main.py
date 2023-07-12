'''
Created by Mark Rogers
For use at Mars VIC site only
'''
from tkinter import *
from PIL import ImageTk, Image
import os
import time

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='red')
        self.root.config(cursor='none')
        self.root.bind('<Escape>', lambda e: self.root.destroy())
        self.root.resizable(False, False)
        self.index = 0
        self.image_list = []
        self.last_modified = None
        self.image_directory = r'assets'

    def create_frames(self):
        self.frame1 = Frame(self.root, bg='black')
        self.frame1.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

        self.frame2 = Frame(self.root, bg='blue')
        self.frame2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)

        self.frame3 = Frame(self.root, bg='red')
        self.frame3.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)

        self.frame4 = Frame(self.root, bg='green')
        self.frame4.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

        self.update_image_list()
        self.start_loop()

    def update_image_list(self):
        current_modified = os.path.getmtime(self.image_directory)
        if self.last_modified != current_modified:
            self.last_modified = current_modified
            self.frame1_images = self.get_images(r'assets\one')
            self.frame2_images = self.get_images(r'assets\two')
            self.frame3_images = self.get_images(r'assets\three')
            self.frame4_images = self.get_images(r'assets\four')

    def get_images(self, path):
        image_list = []
        extensions = ['bmp', 'gif', 'jpeg', 'jpg', 'png', 'ppm', 'tiff', 'xbm']
        for filename in os.listdir(path):
            img_name = filename.split('.')[-1].lower()
            if img_name.endswith(tuple(extensions)):
                image_list.append(os.path.join(path, filename))
        return image_list

    def start_loop(self):
        self.fill_frame_delay(self.frame1, self.frame1_images)
        self.fill_frame_delay(self.frame2, self.frame2_images)
        self.fill_frame_delay(self.frame3, self.frame3_images)
        self.fill_frame_delay(self.frame4, self.frame4_images)

    def fill_frame_delay(self, frame, image_list):
        frame.after(15000, lambda: self.fill_frame(frame, image_list))

    def fill_frame(self, frame, image_list):
        for widget in frame.winfo_children():
            widget.destroy()

        try:
            if self.index >= len(image_list):
                self.index = 0

            image = Image.open(image_list[self.index])
            image = image.resize((frame.winfo_width(), frame.winfo_height()), Image.LANCZOS)
            photo_image = ImageTk.PhotoImage(image)

        except IndexError:
            image = Image.open(r'assets\default.png')
            image = image.resize((frame.winfo_width(), frame.winfo_height()), Image.LANCZOS)
            photo_image = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo_image)
        label.image = photo_image
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.pack_propagate(0)
        label.pack(fill=BOTH, expand=1)

        self.index += 1
        print(self.index)

if __name__ == '__main__':
    root = Tk()
    app = MainWindow(root)
    app.create_frames()
    root.mainloop()
