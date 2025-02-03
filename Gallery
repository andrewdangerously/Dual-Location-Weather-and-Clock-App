import os
import random
import sys
from tkinter import Tk, Label
from PIL import Image, ImageTk

# Path to the image folder
image_folder = '/opt/gallery/images'

def get_images():
    try:
        images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if not images:
            print("No images found in the folder!")
        return images
    except Exception as e:
        print(f"Error reading images: {e}")
        return []

def resize_image(img, width, height):
    img_width, img_height = img.size
    aspect_ratio = img_width / img_height
    if img_width > img_height:
        new_width = width
        new_height = int(width / aspect_ratio)
    else:
        new_height = height
        new_width = int(height * aspect_ratio)
    return img.resize((new_width, new_height), Image.Resampling.LANCZOS)

def update_image():
    images = get_images()
    if images:
        image = random.choice(images)
        print(f"Displaying image: {image}")
        try:
            img_path = os.path.join(image_folder, image)
            img = Image.open(img_path)

            # Resize the image to fit the window size while maintaining aspect ratio
            img = resize_image(img, window_width, window_height)
            img = ImageTk.PhotoImage(img)

            # Update label
            label.config(image=img)
            label.image = img  # Keep a reference to avoid garbage collection
        except Exception as e:
            print(f"Error loading image: {e}")
    else:
        print("No images to display.")

    root.after(15000, update_image)

def show_window():
    root.deiconify()  # Restore the window

root = Tk()
root.title("Photo Gallery")  # Set the title (visible in the taskbar)

# Check if the '--minimized' flag is passed
if '--minimized' in sys.argv:
    root.iconify()  # Minimize the window on startup

# Timer to restore the window after 5 seconds (adjust as needed)
root.after(5000, show_window)

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Define taskbar height at the top (adjust as needed)
taskbar_height = 40  # Assuming the taskbar is about 40 pixels high

# Adjust window size and position to avoid overlapping the taskbar
window_width = screen_width
window_height = screen_height - taskbar_height
root.geometry(f"{window_width}x{window_height}+0+{taskbar_height}")

# Create image label
label = Label(root)
label.place(relwidth=1, relheight=1)

# Start the image rotation
update_image()

root.mainloop()
