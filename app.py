from flask import Flask, render_template, request, send_file
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        names = request.form['names']
        names = names.strip()  # Remove leading/trailing whitespace
        names = '\n'.join(names.splitlines())
        with open('names.txt', 'w') as file:
            file.write(names)
        return render_template('index.html', file_generated=True, names=names)
    else:
        with open('names.txt', 'r') as file:
            names = file.read()
        return render_template('index.html', names=names)

@app.route('/download')
def download():
    # Generate the PDF file using your existing script
    subprocess.run(['python', 'pdfScript.py'])

    # Move the generated PDF file to a location accessible by the web server
    return send_file('generatedPDF.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)


