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

@app.route('/download',methods=['POST'])
def merge_pdfs(pdf_files, output_file):
    # Create a PDF merger object
    merger = PyPDF2.PdfMerger()

    # Add each PDF file to the merger
    for pdf_file in pdf_files:
        merger.append(pdf_file)

    # Write the merged PDF to the output file
    with open(output_file, 'wb') as f:
        merger.write(f)
        
# Example usage
pdf_files = [""]
output_file = 'merged.pdf'
merge_pdfs(pdf_files, output_file)





if __name__ == '__main__':
	app.run(debug=True)





# Import the required libraries
# import smtplib

# Define the function to merge PDF documents
