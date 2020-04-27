import sys
import PyPDF2

pdf = sys.argv[1]
watermark = sys.argv[2]

with open(f'{pdf}', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    n = reader.getNumPages()
    output = PyPDF2.PdfFileWriter()

    with open(f'{watermark}', 'rb') as file2:
        wtr = PyPDF2.PdfFileReader(file2)

        i = 0
        while (i < n):

            page = reader.getPage(i)
            page.mergePage(wtr.getPage(0))

            output.addPage(page)

            i += 1

            with open('completed.pdf', 'wb') as new_file:
                output.write(new_file)



