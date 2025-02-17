from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/letter', methods=['POST'])
def password():
    key = request.form['password']
    if key == '1234':
        return render_template('letter.html')
    else:
        return redirect(url_for('home'))

@app.route('/vid')
def vid():
    return render_template('vid.html')

@app.route('/next2')
def next2():
    return render_template('next2.html')

if __name__ == '__main__':
    app.run(debug = True)