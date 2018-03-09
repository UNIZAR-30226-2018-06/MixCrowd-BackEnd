import os
from flask import Flask, render_template, request

UPLOAD_FOLDER = "/Users/pedroramonedafranco/PycharmProjects/mixcrowd/uploads"
ALLOWED_EXTENSIONS = set(['mp3'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/prueba')
def upload_html():
    return render_template('prueba1.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def mezclar():
    os.system("ffmpeg -i " + UPLOAD_FOLDER + "/nombre1.mp3 -i " + UPLOAD_FOLDER +
              "/nombre2.mp3 -filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 " +
              UPLOAD_FOLDER + "/mezcla.mp3")


@app.route('/prueba_uploader', methods=['GET', 'POST'], endpoint='func1')
def upload_file():
    if request.method == 'POST':
        filename1 = "nombre1.mp3"
        filename2 = "nombre2.mp3"
        f1 = request.files['file1']
        f2 = request.files['file2']
        if allowed_file(f1.filename) and allowed_file(f2.filename):
            f1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            f2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
            return 'files uploaded successfully'
        else:
            return 'Alguno de los archivos subidos no tiene la extensión mp3.'
    elif request.method == 'GET':
        mezclar()
        os.system("mv " + UPLOAD_FOLDER +
                  "/mezcla.mp3 /Users/pedroramonedafranco/PycharmProjects/mixcrowd/static/mezcla1.mp3")
        return ''' <audio controls>
                         <source src="http://localhost:5000/static/mezcla1.mp3" type="audio/mpeg">
                        </audio> '''


if __name__ == '__main__':
    app.run(debug=True)
