from distutils.log import debug
from fileinput import filename
import subprocess
from flask import Flask, send_file, render_template, request, flash, redirect
import os
from werkzeug.utils import secure_filename
import sys
from glob import glob
from io import BytesIO
from zipfile import ZipFile


sys.path.append('model/createobjects.py')

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
            f.filename="freshers.xlsx"
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template("success.html", name=f.filename+" successfully uploaded")  

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
            #do pairing by reading files from uploads.
            filename = secure_filename(f.filename)
            f.filename="continuing.xlsx"
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            path1 = 'controller/uploads/freshers.xlsx'
            path2 = 'controller/uploads/continuing.xlsx'

            isFile1 = os.path.isfile(path1)
            isFile2 = os.path.isfile(path2)

            if isFile1==True:
                if isFile2 == True:
                    os.chdir('model/')
                    subprocess.run(['python3', 'edges.py'])

    return render_template("progress.html", message= "Successful pairing!", name=f.filename+" successfully uploaded"+',')  

@app.route("/download",  methods = ['GET', 'POST'])
def download():
    return render_template("download.html")

@app.route('/download_files')
def download_files():
    target = 'controller/downloads'

    stream = BytesIO()
    with ZipFile(stream, 'w') as zf:
        for file in glob(os.path.join(target, '*.xlsx')):
            zf.write(file, os.path.basename(file))
            print(f'Added file {file} to zip file')
        print(f'Zip file contains {len(zf.namelist())} files')
    stream.seek(0)

    print(f'stream contains {len(stream.getvalue())} bytes')
    print(f'stream contents: {stream.getvalue()}')
    
    return send_file(
        stream,
        as_attachment=True,
        download_name='Buddy-up.zip'
    )
    
if __name__ == "__main__":
    app.run(debug=True)