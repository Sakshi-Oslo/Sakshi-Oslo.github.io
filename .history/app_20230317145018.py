#importing flask
from flask import Flask, request, send_file, render_template
#importing libraries to read and merge pdf
from PyPDF2 import PdfMerger, PdfReader

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
#rendering html template
def main():
 return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded files
        files = request.files.getlist('files')
        
        # Merge the files
        merger = PdfMerger()
        for file in files:
            pdf = PdfReader(file)
            merger.append(pdf)
        output = 'merged.pdf'
        merger.write(output)
        
        # Download the merged file
        return send_file(output, as_attachment=True)
     if files == '':
        return "Please Upload Files"
    return

if __name__ == '__main__':
    app.run(debug=True)
