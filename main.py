import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from gtts import gTTS
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tensorflow as tf
from tensorflow import keras

from predictmodel import PredictPic


class ImageAndTextToVoiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image and Text to Voice App")
        self.image_label = tk.Label(self.root, text="Image will be displayed here")
        self.image_label.pack(pady=10)
        self.root.geometry("1000x580+200+80")
        self.root.resizable(False,False)
        self.style = ttk.Style()
        self.root.configure(bg="#f9dbbd")
        self.upload_button = ttk.Button(self.root, text="Upload Image",bootstyle=(SUCCESS,OUTLINE),command=self.upload_and_display_image)
        self.upload_button.pack(pady=5)
        self.generate_button = ttk.Button(self.root, text="Generate Voice",bootstyle=(PRIMARY,OUTLINE), command=self.generate_voice)
        self.generate_button.pack(pady=5)
        self.text_label = tk.Label(self.root, text="Enter text for voice:")
        self.image_path = None
        self.image = None
    def upload_and_display_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
        if self.image_path:
            self.image = Image.open(self.image_path)
            self.image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        else:
            self.image_label.config(text="No image selected")
    def generate_voice(self):
        custom_text = PredictPic(self.image_path)
        print(self.image_path)
        if custom_text:
            self.text_to_voice(custom_text)
        else:
            print("Enter text to generate voice.")

    def text_to_voice(self, text):
        if text:
            tts = gTTS(text, lang="en")
            tts.save("output.mp3")
            os.system("start output.mp3")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageAndTextToVoiceApp(root)
    root.mainloop()