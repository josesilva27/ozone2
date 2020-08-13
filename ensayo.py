import os               
from zipfile import ZipFile
import shutil
from flask import Flask , request, render_template
from werkzeug.utils import secure_filename
from zipModulo import empaquetar, desempaquetar,empaquetar2,desempaquetar2

rutaSubidos= os.getcwd()+'\\subidos'
rutaDescargas = os.getcwd()+'\\Descargas'

empaquetar2(rutaSubidos,os.path.basename(rutaSubidos))   #llamo al modulo
shutil.move("myzipfile.zip", rutaDescargas)

#falta acomodar 
"""
archivito = open(rutaDescargas+'\\'+'myzipfile.zip','w')

desempaquetar2(rutaDescargas)                                #llamo al modulo

archivito.close()
"""
