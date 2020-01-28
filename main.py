import fitz
import os
from tqdm import tqdm


d = str(input('Перетащите файл в окно: '))
pdf_document = fitz.open(d)
for current_page in tqdm(range(len(pdf_document))):
    for image in pdf_document.getPageImageList(current_page):
        xref = image[0]
        pix = fitz.Pixmap(pdf_document, xref)

        if not os.path.isdir(f'img'):
            os.mkdir(f'img')

        pix1 = fitz.Pixmap(fitz.csRGB, pix)
        # pix1.writeImage(f"img/page%s-%s.jpg" % (current_page, xref))
        pix1.writePNG(f"img/page%s-%s.png" % (current_page, xref))


