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
    
# Create the input fields and labels
label_num1 = tk.Label(window, text="Number 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_operator = tk.Label(window, text="Operator:")
label_operator.pack()
operators = ['add', 'subtract', 'multiply', 'divide', 'pow', 'sqrt', 'sin', 'cos', 'tan']
dropdown_operator = tk.StringVar(window)
dropdown_operator.set(operators[0])
operator_menu = tk.OptionMenu(window, dropdown_operator, *operators)
operator_menu.pack()

label_num2 = tk.Label(window, text="Number 2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create the calculate button
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.pack()

# Create the result label
label_result = tk.Label(window)
label_result.pack()


    window.mainloop()

if __name__ == '__main__':
    run_flask_app()
    run_calculator_gui()
