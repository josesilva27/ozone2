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
    zf = zipfile.ZipFile("myzipfile.zip", "w")
    for dirname, subdirs, files in os.walk(rutaArchivo):
        zf.write(dirname,baseName)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()