from flask import Flask, render_template, request, send_file
import pdfkit

app = Flask(__name__)

# Specify the path to the wkhtmltopdf executable on your Windows system
config = pdfkit.configuration(wkhtmltopdf="wkhtmltopdf.exe")

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/convert', methods=['POST'])
def convert():
    html_file = request.files['html_file']

    if html_file:
        pdf_file = 'output.pdf'
        html_file.save('input.html')

        pdfkit.from_file('input.html', pdf_file, configuration=config)

        return send_file(pdf_file, as_attachment=True)
    else:
        return "No HTML file uploaded."

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
