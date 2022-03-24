import PyPDF2

def merge_pdfs(PDFsList: list,FileName: str):
    merger = PyPDF2.PdfFileMerger()
    for pdf in PDFsList:
        merger.append(pdf)
    merger.write(f'./BasePDFs/{FileName}.pdf')

PDFsList = ['./BasePDFs/BlankPDF.pdf','./BasePDFs/MarcaAgua.pdf']

merge_pdfs(PDFsList,'MergedPDFs')