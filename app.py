from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('index.html', result=None)

@app.route('/calculate')
def calculate():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        op = request.args.get('operation')

        if op == '+':
            result = num1 + num2
        if op == '-':
            result = num1 - num2
        if op == '*':
            result = num1 * num2
        if op == '/':
            if num2 == 0:
                return render_template('index.html', result="Error: Cannot divide by zero")
            result = num1 / num2
        return render_template('index.html', result=result)

    except:
        return render_template('index.html', result="Error: Invalid input")

if __name__ == '__main__':
    app.run(debug=True)