from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Kamu bisa menambahkan logika list file dari folder di sini
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
