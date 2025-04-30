import customtkinter as ctk
from PIL import Image
import os

def load_image(image_path:str, size:tuple)->ctk.CTkImage:
        """Function to load and resize an image. Returns None if the image not found."""
        try:
            if os.path.exists(image_path):
                return ctk.CTkImage(light_image=Image.open(image_path),
                                    dark_image=Image.open(image_path),
                                    size=size)
            else:
                print (f"[Warning]: Image not found at {image_path}")
                return None
        except Exception as e:
            print(f"[Error]: Failed to load image {image_path}: {e}")
            return None

     