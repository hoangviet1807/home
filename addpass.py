from flask import Flask, render_template,url_for, request
app = Flask(__name__,template_folder='templates',static_folder='image')

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('addpass.html')

app.run(debug=True)