from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def head():
    return render_template('index.html',number=12)
@app.route('/burcu')
def burcu():
    var1=30
    var2=3
    return render_template('burcu.html',num1=var1,num2=var2,multiplication=var1 * var2)
if __name__=='__main__':
    app.run(debug = True)