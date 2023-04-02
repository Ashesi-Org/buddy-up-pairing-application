from distutils.log import debug
from fileinput import filename
from flask import Flask, render_template, request, flash, redirect
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'controller/uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'csv'}

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method=='POST':
        return render_template("home.html") #from progress page.
    else:
        return render_template("home.html")

@app.route('/success', methods = ['GET', 'POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            # f.save(secure_filename(f.filename))
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template("success.html", name=f.filename+" successfully uploaded"+',')  

@app.route("/progress", methods = ['GET', 'POST'])
def progress():
    if request.method == 'POST':
        f = request.files['file']
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            # f.save(secure_filename(f.filename))
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template("progress.html", name=f.filename+" successfully uploaded"+',')  

@app.route("/download")
def download():
    return render_template("download.html")
    
if __name__ == "__main__":
    app.run(debug=True)