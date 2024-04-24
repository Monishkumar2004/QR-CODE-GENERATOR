from tkinter import *
from PIL import ImageTk, Image
import io
import pyqrcode
# pip install pypng

root = Tk()

def generate_qr():
    link_name = link_name_entry.get()
    file_name = link_name + ".png"
    link = link_entry.get()
    url = pyqrcode.create(link)
    url.png(file_name, scale=7)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image= image)
    image_label.image = image
    canvas.create_window(250,450, window = image_label)

canvas = Canvas(root, width=500, height=600)
canvas.pack()

header = Label(root, text= "QR Code Generator", fg="orange red", font=("Courier", 30))
canvas.create_window(250,50, window=header)

link_name = Label(root, text="Link Name", font= ("Courier", 15), fg= "tomato")
link_label = Label(root, text="Link", font= ("Courier", 15), fg= "tomato")
canvas.create_window(250,150, window=link_name)
canvas.create_window(250,250, window=link_label)

link_name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(250, 180, window= link_name_entry)
canvas.create_window(250, 280, window= link_entry)

button = Button(root, text= "Generate", font= ("Courier", 20), fg="red", command= generate_qr)
canvas.create_window(250, 320, window= button)

root.mainloop()

