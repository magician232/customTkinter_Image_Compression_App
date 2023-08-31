import cv2
import os
from PIL import Image

import tkinter as tk
from tkinter import Label, messagebox

root = tk.Tk()


root.geometry("450x200")


sourcePath = tk.StringVar()
destpath = tk.StringVar()


def loadfile(sourcefolder, dest_folder):
    random = 5
    for filename in os.listdir(sourcefolder):
        img = Image.open(os.path.join(sourcefolder, filename))
        width = img.width
        height = img.height

        img = img.resize((int(width / 4), int(height / 4)), Image.ANTIALIAS)

        random += 1
        name = os.path.join(dest_folder, filename)
        img.save(name, optimize=True, quality=95)



def compress():
    s_name = sourcePath.get()
    d_name = destpath.get()
    try:
        loadfile(s_name, d_name)
        messagebox.showinfo("Compression", "Compression completed")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    sourcePath.set("")
    destpath.set("")



name_label = tk.Label(root, text='Source Folder Path', font=('calibre', 10, 'bold'))


name_entry = tk.Entry(root, textvariable=sourcePath, font=('calibre', 10, 'normal'))


passw_label = tk.Label(root, text='Destination folder path', font=('calibre', 10, 'bold'))


passw_entry = tk.Entry(root, textvariable=destpath, font=('calibre', 10, 'normal'))

sub_btn = tk.Button(root, text='Compress', command=compress)


name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)


root.mainloop()