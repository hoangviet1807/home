from flask import Flask, render_template,url_for
app = Flask(__name__, template_folder='templates', static_folder='image')

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route('/employeeadmin', methods=['GET','POST'])
def employeeadmin():
    return render_template('employeeadmin.html')


@app.route('/missionadmin', methods=['GET','POST'])
def missionadmin():
    return render_template('missionadmin.html')


app.run(debug=True)