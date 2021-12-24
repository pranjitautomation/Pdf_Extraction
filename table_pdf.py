import camelot as cam

table = cam.read_pdf("output.pdf", pages='1', flavor='stream')


table.export('next.csv', f='csv', compress=False)  # Extracting all the tables


table[1].to_csv('output.csv')  # Extracting a  particular tables
