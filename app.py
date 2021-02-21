from flask import Flask, render_template, request, redirect, url_for
import datetime
import os


UPLOAD_FOLDER = "files/questionnaires/"
ALLOWED_EXTENSIONS = {'txt', 'py', }


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
filename = ""


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        date = datetime.datetime.now().strftime('%d.%m.%Y %R')
        global filename
        filename = email.split(".")[0]
        data = name + "\n" + email + "\n" + date
        f = open(UPLOAD_FOLDER + filename + "_bio.txt", "w", encoding="utf-8")
        f.write(data)
        f.close()

        return redirect('questionnaire.html')
    else:
        return render_template('index.html')


@app.route('/questionnaire.html', methods=['POST', 'GET'])
def form1():
    if request.method == "POST":
        knowledge = request.form['knowledge']
        yourself = request.form['yourself']
        global filename
        f = open(UPLOAD_FOLDER + filename + "_bio.txt", "a", encoding="utf-8")
        f.write("\nИспользовать:\n" + knowledge + "\nО себе:\n" + yourself)
        f.close()

        return redirect('tasks.html')
    else:
        return render_template('questionnaire.html')


@app.route('/tasks.html', methods=['POST', 'GET'])
def form2():
    if request.method == "POST":
        global filename
        filename = filename.split(".")[0] + "_"
        task_1 = request.files["task1"]
        if task_1:
            task_1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename + task_1.filename))
        task_2 = request.files["task2"]
        if task_2:
            task_2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename + task_2.filename))
        task_3 = request.files["task3"]
        if task_3:
            task_3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename + task_3.filename))

        return redirect('success.html')
    else:
        return render_template('tasks.html')


@app.route('/success.html')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)


