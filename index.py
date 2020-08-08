import os               
from zipfile import ZipFile
import shutil
from flask import Flask , request, render_template
from werkzeug.utils import secure_filename

app= Flask (__name__)

@app.route('/')
def inicio():
    return render_template ("inicio.html")

@app.route('/archivos')
def archivos():
    return render_template ("archivos.html")

app.config['UPLOAD_FOLDER'] = './subidos'
app.config['DOWNLOAD_FOLDER'] = './Descargas'

@app.route("/uploader", methods=['POST'])
def uploader():
    if request.method == 'POST':
        f= request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if os.path.exists("Descargas") == True:
            if len(os.listdir(os.getcwd()+'\\Descargas')) == 0:
                print("carpeta vacia")
        else:
            os.mkdir ("Descargas")

        rutaSubidos= os.getcwd()+'\\subidos'
        rutaDescargas = os.getcwd()+'\\Descargas'
        archivo = open(rutaSubidos+'\\'+ filename,'r')
        
        myzip = ZipFile("archivo.zip",'w')
        myzip.write (rutaSubidos+'\\'+filename, os.path.basename(filename)) #busco el archivo en la carpeta subidos
        myzip.close()
        print("zip creado")
        archivo.close()

        shutil.move("archivo.zip", rutaDescargas)
        print("archivo fue enviado a descargas")

        with ZipFile(rutaDescargas+'\\archivo.zip','r') as myzip:
            myzip.extractall()

        return 'subido exitosamente'
    

if __name__ == "__main__":
    app.run(debug=True)