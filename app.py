import os
from flask import Flask, request, render_template, abort
from fabweb import fab

app = Flask (__name__)
UPLOAD_FOLDER = 'Uploads'

app=Flask(__name__)
app.config['DATA_FOLDER']='Uploads'
files = [f for f in os.listdir(app.config['DATA_FOLDER'])]



@app.route('/', methods=['GET'])
def fich():
    return render_template('subida_fich.html', files=files)
@app.route('/estadisticas', methods=['POST'])
def estad():
    filename = request.form.get('filename')
    filepath = os.path.join(app.config['DATA_FOLDER'], filename)
    if not os.path.exists(filepath):
        abort(404)
    if filename in files:
        with open(filepath, 'r') as estadif:
            f = fab()
            cuartos, teams = f.tanper(estadif)
        return render_template('estadisticas.html', cuartos=cuartos, teams=teams, files=files)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404

if __name__=="__main__":
    app.run()