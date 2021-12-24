import fitz   # PyMuPDF
import io
from PIL import Image
import os


file = "1710.05006.pdf"
image_dir = './image'


def extracting_images():

    # open the file
    pdf_file = fitz.open(file)
    len_pdf = len(pdf_file)
    # iterate over PDF pages
    for page_index in range(len_pdf):
        # get the page itself

        page = pdf_file[page_index]
        image_list = page.getImageList()
        # printing number of images found in this page
        if image_list:
            print(
                f"[+] Found {len(image_list)} images in page {page_index}"
                )
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(page.getImageList(), start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))

            # save it to local disk
            file_name = f"image{page_index+1}_{image_index}.{image_ext}"
            filePath = os.path.join(image_dir, file_name)

            image.save(open(filePath, "wb"))


extracting_images()
