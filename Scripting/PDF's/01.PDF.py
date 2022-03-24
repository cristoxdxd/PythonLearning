import PyPDF2 as pdf

File = './BasePDFs/PDFUnido.pdf'

with open(File, 'rb') as  myFile:
    print(myFile)
    print(type(myFile))

    PDFFile = pdf.PdfFileReader(myFile)
    print(PDFFile)
    print(type(PDFFile))

    print(f'Pages number of {File}: {PDFFile.getNumPages()}')

    page = PDFFile.getPage(0)
    print(page)
    print(type(page))

    PDFWriter = pdf.PdfFileWriter()
    PDFWriter.addPage(page)
    PDFWriter.addBlankPage()

    with open('./BasePDFs/BlankPDF.pdf','wb') as Outputpdf:
        PDFWriter.write(Outputpdf)
