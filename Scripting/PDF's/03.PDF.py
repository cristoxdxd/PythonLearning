import PyPDF2

PDFFile = PyPDF2.PdfFileReader((open('./BasePDFs/PDFUnido.pdf','rb')))
PDFMarcaAgua = PyPDF2.PdfFileReader((open('./BasePDFs/MarcaAgua.pdf','rb')))

MarcaAguaPage = PDFMarcaAgua.getPage(0)
output = PyPDF2.PdfFileWriter()

for pageNumber in range(PDFFile.getNumPages()):
    page = PDFFile.getPage(pageNumber)
    page.mergePage(MarcaAguaPage)
    output.addPage(page)
with open('./BasePDFs/resultadoFinal.pdf','wb') as archivoFinal:
    output.write(archivoFinal)