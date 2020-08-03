import os               
import zipfile
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

@app.route("/uploader", methods=['POST'])
def uploader():
    if request.method == 'POST':
        f= request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return 'subido exitosamente'

if __name__ == "__main__":
    app.run(debug=True)