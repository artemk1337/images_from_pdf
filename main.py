import fitz
import os


d = str(input('Перетащите файл в окно: '))
pdf_document = fitz.open(d)
f = d.split('\\')
s = ''
if len(f) < 2:
    s = './'
else:
    for i in range(len(f) - 1):
        s += f[i] + str('\\')
print(s)
for current_page in range(len(pdf_document)):
    for image in pdf_document.getPageImageList(current_page):
        xref = image[0]
        pix = fitz.Pixmap(pdf_document, xref)

        if not os.path.isdir(f'{s}/img'):
            os.mkdir(f'{s}/img')

        if pix.n < 5:        # this is GRAY or RGB
            pix.writePNG(f"{s}/img/page%s-%s.png" % (current_page, xref))
        else:                # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG(f"{s}/img/page%s-%s.png" % (current_page, xref))


