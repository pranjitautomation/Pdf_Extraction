from PIL import Image
import pytesseract
from pdf2image import convert_from_path

PDF_file = "app.pdf"

path_teseract = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = path_teseract


def extracting_text():

    # Opening pages from path of pdf
    pages = convert_from_path(
        PDF_file, 500,
        poppler_path=r"C:\\Users\\hp\\Downloads\\poppler-0.68.0\\bin"
        )

    image_counter = 1

    for page in pages:
        # Saving pages as image
        filename = "page_"+str(image_counter)+".jpg"
        page.save(filename, 'JPEG')

        image_counter = image_counter + 1

    filelimit = image_counter-1

    outfile = "out_text.txt"

    f = open(outfile, "a")

    for i in range(1, filelimit + 1):

        filename = "page_"+str(i)+".jpg"

        # Taking Text from images
        text = str(((pytesseract.image_to_string(Image.open(filename)))))

        text = text.replace('-\n', '')

        f.write(text)

    f.close()


extracting_text()
