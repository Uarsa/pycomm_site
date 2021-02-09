from flask import Flask, render_template, request, redirect
import datetime


UPLOAD_FOLDER = "files/questionnaires/"
ALLOWED_EXTENSIONS = {'txt', }


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        date = datetime.datetime.now().strftime('%d.%m.%Y %R')
        data = name + "\n" + email + "\n" + date
        f = open(UPLOAD_FOLDER + email + ".txt", "w", encoding="utf-8")
        f.write(data)
        f.close()

        return redirect('form1.html')
    else:
        return render_template('index.html')


@app.route('/form1.html', methods=['POST', 'GET'])
def form1():
    if request.method == "POST":
        knowledge = request.form['knowledge']
        yourself = request.form['yourself']
        filename = "test"
        f = open(UPLOAD_FOLDER + filename + ".txt", "w", encoding="utf-8")
        f.write(knowledge + "\n \n" + yourself)
        f.close()

        return redirect('form2.html')
    else:
        return render_template('form1.html')


@app.route('/form2.html', methods=['POST', 'GET'])
def form2():
    if request.method == "POST":
        pass

        return redirect('form2.html')
    else:
        return render_template('form2.html')


if __name__ == '__main__':
    app.run(debug=True)

