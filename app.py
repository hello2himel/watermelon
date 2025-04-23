import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource (for dev and for PyInstaller) """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def on_close(window, image_label, text_label):
    image_label.config(image=seeds_img)
    text_label.config(text="You can't make the watermelon go extinct.")

    # Spawn windows first
    for _ in range(2):
        spawn_new_window()

    # Then show the message box after a tiny delay
    window.after(100, lambda: messagebox.showinfo("Warning!", "When you destroy a watermelon, you spread its seeds."))

def spawn_new_window():
    new_win = tk.Toplevel()
    new_win.title("Watermelon")
    new_win.geometry("300x300")

    img_label = tk.Label(new_win, image=watermelon_img)
    img_label.pack(pady=10)

    txt_label = tk.Label(new_win, text="Let the watermelon live.")
    txt_label.pack()

    new_win.protocol("WM_DELETE_WINDOW", lambda: on_close(new_win, img_label, txt_label))

# Create root window first
root = tk.Tk()
root.title("Watermelon")
root.geometry("300x300")

# Load images after root is created
watermelon_img = ImageTk.PhotoImage(Image.open(resource_path("res/watermelon.png")).resize((200, 200)))
seeds_img = ImageTk.PhotoImage(Image.open(resource_path("res/seeds.png")).resize((200, 200)))


main_img = tk.Label(root, image=watermelon_img)
main_img.pack(pady=10)

main_text = tk.Label(root, text="Let the watermelon live.")
main_text.pack()

root.protocol("WM_DELETE_WINDOW", lambda: on_close(root, main_img, main_text))
root.mainloop()
