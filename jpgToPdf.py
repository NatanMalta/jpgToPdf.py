from PIL import Image
from os import listdir, path, remove
from PyPDF2 import PdfFileReader, PdfFileMerger


nomePdf = str(input('Nome para salvar o pdf: '))
apenasJpg = [f for f in listdir() if f.lower().endswith("jpg")] # Lista apenas arquivos .jpg
apenasJpg.sort()
pdfs = [] 

for jpg in apenasJpg: 
    imagem = Image.open(jpg)

    if imagem.mode == "RGBA": # Converte imagens RGBA para RGB
        imagem = imagem.convert("RGB")
        
    novoPdf = jpg.replace('.jpg', '.pdf') # Substitui .jpg para .pdf
    pdfs.append(novoPdf) # Adiciona na lista o nome do .pdf

    if not path.exists(novoPdf): # Se não existir ele salva o .pdf
        imagem.save(novoPdf, "PDF", resolution=100.0)

if not path.exists(nomePdf+'.pdf'):
    pdfs.sort() # Organiza a lista em ordem Alfanumérica
    merger = PdfFileMerger()
    
    for pdf in pdfs:
        merger.append(PdfFileReader(path.join(pdf), 'rb'))
    merger.write(path.join(nomePdf+'.pdf'))

for Pdf in pdfs: # Apaga as imagens convertida em .pdf
    remove(Pdf)
