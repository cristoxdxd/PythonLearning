import PyPDF2

PDFFile = PyPDF2.PdfFileReader((open('./BasePDFs/PDFUnido.pdf','rb')))
PDFMarcaAgua = PyPDF2.PdfFileReader((open('./BasePDFs/MarcaAgua.pdf','rb')))

MarcaAguaPage = PDFMarcaAgua.getPage(0)
