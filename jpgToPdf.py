from PIL import Image
from os import listdir, path, remove
from PyPDF2 import PdfFileReader, PdfFileMerger


nomePdf = str(input('Nome para salvar o pdf: '))
todosArquivos = listdir()
apenasJpg = []
pdfs = []

for indice in range(0, len(todosArquivos) ):
    
    if todosArquivos[indice].lower().endswith('.jpg'):
        apenasJpg.append(todosArquivos[indice])# Adiciona apenas .jpg

apenasJpg.sort() # Organiza a lista em ordem Alfanumérica

for jpg in apenasJpg:
    imagem = Image.open(jpg)

    if imagem.mode == "RGBA": # Converte imagens RGBA para RGB
        imagem = imagem.convert("RGB")
        
    novoPdf = jpg.replace('.jpg', '.pdf')
    pdfs.append(novoPdf)

    if not path.exists(novoPdf):
        imagem.save(novoPdf, "PDF", resolution=100.0)

if not path.exists(nomePdf+'.pdf'):
    pdfs.sort() # Organiza a lista em ordem Alfanumérica
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(PdfFileReader(path.join(pdf), 'rb'))
    merger.write(path.join(nomePdf+'.pdf'))

for Pdf in pdfs: # Apaga as imagens convertida em .pdf
    remove(Pdf)




