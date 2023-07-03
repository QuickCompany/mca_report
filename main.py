from flask import Flask, render_template , request
from AOC.read_aoc_xml import aoc_form
import os

app = Flask(__name__)


if not os.path.exists("file"):
    os.makedirs("file")


@app.route('/mgt7',methods=['GET' , 'POST'])
def MGT7():
    File = request.files['file']
    print(File)

    return "200"

@app.route('/aoc',methods=['GET' , 'POST'])
def aoc():
    File = request.files['file']
    name = File.filename
    cin = request.form['cin']
    if not os.path.exists(cin):
        os.makedirs(cin)

    File.save(f'{cin}/{name}')


    if "aoc" in name.lower():
        return aoc_form(cin,name)

    return "200"

if __name__ == '__main__':
    app.run(debug=True , port = 8097 , host = "0.0.0.0")
