import fitz
import os
import time, threading
# from tqdm import tqdm
import progressbar
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter.ttk import Progressbar
import tkinter.ttk as ttk


def start():
    d = file_name
    # d = str(input('Перетащите файл в окно: ')).replace("\"", "")
    pdf_document = fitz.open(d)

    bar = progressbar.ProgressBar(len(pdf_document)).start()

    for current_page in range(len(pdf_document)):
        for image in pdf_document.getPageImageList(current_page):
            xref = image[0]
            pix = fitz.Pixmap(pdf_document, xref)

            if not os.path.isdir(f'img'):
                os.mkdir(f'img')

            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            # pix1.writeImage(f"img/page%s-%s.jpg" % (current_page, xref))
            pix1.writePNG(f"img/page%s-%s.png" % (current_page, xref))
            bar.update(current_page)
            progress['value'] += current_page
    console.configure(state='normal')  # enable insert
    console.insert(END, 'ГОТОВО!')
    console.yview(END)  # autoscroll
    console.configure(state='disabled')  # disable editing
    os.startfile(f"{os.path.abspath(os.curdir)}\\img")
    quit()


def ask():
    global file_name
    file_name = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
    print(file_name)
    threading.Thread(target=start).start()
    pass


window = Tk()
window.title("Поиск картинок в PDF-файле")
window.geometry('500x250')


progress = Progressbar(window, orient=HORIZONTAL, length=400, mode='determinate')
progress.pack(pady=10)
Button(window, text='Выбрать файл', command=ask, font=("Arial Bold", 20)).pack(pady=10)


"""
lbl = Label(window, text="Выберете файл:", font=("Arial Bold", 30))
lbl.grid(column=0, row=0)
"""

"""
b2 = Button(text="Выбрать файл", command=ask, font=("Arial Bold", 20))
b2.grid(row=1, column=0, sticky=S)
"""

console = scrolledtext.ScrolledText(window, state='disable', width=20, height=10, font=("Arial Bold", 70))
console.pack(pady=10)

window.mainloop()



