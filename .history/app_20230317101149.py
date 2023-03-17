from flask import *
# import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import PyPDF2
app = Flask(__name__)


@app.route('/')
def main():
	return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
	if request.method == 'POST':

		# Get the list of files from webpage
		files = request.files.getlist("file")

		# Iterate for each file in the files List, and Save them
		for file in files:
			file.save(file.filename)
		return "<h1>Files Uploaded Successfully!</h1>"

# @app.route('/download',methods=['POST'])
# def merge_pdfs(pdf_files, output_file):
#     # Create a PDF merger object
#     merger = PyPDF2.PdfMerger()

#     # Add each PDF file to the merger
#     for pdf_file in pdf_files:
#         merger.append(pdf_file)

#     # Write the merged PDF to the output file
#     with open(output_file, 'wb') as f:
#         merger.write(f)
        
# # Example usage
# pdf_files = [""]
# output_file = 'merged.pdf'
# merge_pdfs(pdf_files, output_file)





if __name__ == '__main__':
	app.run(debug=True)

# import os
# from flask import Flask, request, redirect, url_for, render_template, send_from_directory
# from werkzeug.utils import secure_filename
# from PyPDF2 import PdfFileReader, PdfFileWriter

# app = Flask(__name__)

# # UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
# ALLOWED_EXTENSIONS = {'pdf'}
# @app.route('/', methods=['GET', 'POST'])
# def index():
#    if request.method == 'POST':
#        if 'file' not in request.files:
#            print('No file attached in request')
#            return redirect(request.url)
#        file = request.files['file']
#        if file.filename == '':
#            print('No file selected')
#            return redirect(request.url)
#        if file and allowed_file(file.filename):
#            filename = secure_filename(file.filename)
#            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
#            return redirect(url_for('uploaded_file', filename=filename))
#    return render_template('index.html')
# def allowed_file(filename):
#    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'

# app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# def process_file(path, filename):
#    remove_watermark(path, filename)

# def remove_watermark(path, filename):
#    input_file = PdfFileReader(open(path, 'rb'))
#    output = PdfFileWriter()
#    for page_number in range(input_file.getNumPages()):
#        page = input_file.getPage(page_number)
#        page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x(), 20)
#        output.addPage(page)
#    output_stream = open(app.config['DOWNLOAD_FOLDER'] + filename, 'wb')
#    output.write(output_stream)

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)