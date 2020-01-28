import fitz
import os


d = str(input('Перетащите файл в окно: '))
pdf_document = fitz.open(d)
for current_page in range(len(pdf_document)):
    for image in pdf_document.getPageImageList(current_page):
        xref = image[0]
        pix = fitz.Pixmap(pdf_document, xref)

        if not os.path.isdir(f'img'):
            os.mkdir(f'img')

        if pix.n < 5:        # this is GRAY or RGB
            pix.writePNG(f"img/page%s-%s.jpg" % (current_page, xref))
        else:                # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG(f"img/page%s-%s.jpg" % (current_page, xref))


