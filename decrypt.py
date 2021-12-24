import pikepdf


pdf_file = "eStatement9511IN_2021-11-23_17_23.pdf"
pass_word = 'LOKE180874'

with pikepdf.open(pdf_file, password=pass_word) as pdf:
    pdf.save('output.pdf')
