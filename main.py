"""A GUI app for adding watermark to pictures."""

import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import PIL
from PIL import Image, ImageTk

WATERMARK_PATH = "smiley.png"


def add_picture() -> None:
    """Saves a watermarked picture."""
    filename = filedialog.askopenfilename(initialdir='.',
                                          title='Select a picture',
                                          filetypes=(("Picture files",
                                                      ("*.blp", "*.bmp", "*.dds", "*.dib", "*.eps", "*.gif", "*.icns",
                                                       "*.ico", "*.im", "*.jpeg", "*.jpg", "*.j2k", "*.j2p", "*.jpx",
                                                       "*.msp", "*.pcx", "*.png", "*.ppm", "*.sgi", "*.spi", "*.tga",
                                                       "*.tiff", "*.webp", "*.xbm")),
                                                     ("All files", "*.*")))
    file, extension = os.path.splitext(filename)
    outfile = file + "_wm.png"
    try:
        image = Image.open(filename)
    except PIL.UnidentifiedImageError:
        messagebox.showerror(title='Error', message='Please select a valid image.')
    else:
        image = image.convert("RGBA")
        image.paste(resized_mark, (0, 0), resized_mark)
        image.save(outfile, format='png')
        messagebox.showinfo(title='Success', message=f'File saved to {outfile}')

    return None


# Window
window = Tk()
window.title("Add watermark")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(window, width=600, height=400, highlightthickness=0)
mark = Image.open(WATERMARK_PATH)
resized_mark = mark.resize((128, 128), Image.ANTIALIAS)
resized_mark = resized_mark.convert("RGBA")
new_mark = ImageTk.PhotoImage(resized_mark)
canvas.create_image(300, 200, image=new_mark, anchor=CENTER)
canvas.grid(column=0, row=0)

# Buttons
add_picture_button = Button()
add_picture_button.config(text='Add watermark to a picture', command=add_picture)
add_picture_button.grid(column=0, row=1)

window.mainloop()
