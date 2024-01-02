from flask import Flask, render_template, request
import math
import tkinter as tk

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operator = request.form['operator']
    result = None

    if operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    elif operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error: Division by zero'
    elif operator == 'pow':
        result = num1 ** num2
    elif operator == 'sqrt':
        result = math.sqrt(num1)
    elif operator == 'sin':
        result = math.sin(num1)
    elif operator == 'cos':
        result = math.cos(num1)
    elif operator == 'tan':
        result = math.tan(num1)

    return render_template('index.html', result=result)

def run_flask_app():
    app.run()

def run_calculator_gui():
    def calculate():
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = dropdown_operator.get()

        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Error: Division by zero'
        elif operator == 'pow':
            result = num1 ** num2
        elif operator == 'sqrt':
            result = math.sqrt(num1)
        elif operator == 'sin':
            result = math.sin(num1)
        elif operator == 'cos':
            result = math.cos(num1)
        elif operator == 'tan':
            result = math.tan(num1)

        label_result.config(text="Result: " + str(result))

    window = tk.Tk()
    window.title("Calculator")
    # ... GUI code ...

    window.mainloop()

if __name__ == '__main__':
    run_flask_app()
    run_calculator_gui()
