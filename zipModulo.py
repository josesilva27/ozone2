import os               
from zipfile import ZipFile

def empaquetar(rutaArchivo,baseName):
    myzip = ZipFile("archivo.zip",'w')
    myzip.write (rutaArchivo, baseName) #busco el archivo en la carpeta subidos
    myzip.close()
    print("zip creado")

def desempaquetar(rutaComprimido):
    with ZipFile(rutaComprimido+'\\archivo.zip','r') as myzip:           #extrae el archivo
            myzip.extractall('Descargas')

def empaquetar2(rutaArchivo,baseName):
    zf = ZipFile("myzipfile.zip", "w")
    for dirname, subdirs, files in os.walk(rutaArchivo):
        #zf.write(os.path.basename(dirname))
        for file in files:
            zf.write(os.path.join(dirname, file),arcname=file)
    zf.close()
    print("zip creado")

def desempaquetar2(rutaComprimido):
    with ZipFile(rutaComprimido+'\\myzipfile.zip','r') as myzip:           #extrae el archivo
            myzip.extractall('Descargas')
