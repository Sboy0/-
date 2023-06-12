import tkinter as tk



def add_digit(digit):
    value = calc.get() + str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, value)


def add_operation(operation):
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value)

def add_operation(operation):
        value = calc.get()
        if value[-1] in '-+/*√Y^ᵡ':
            value = value[:-1]
            calc.delete(0, tk.END)
            calc.insert(0, value+operation)

def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_operation(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=lambda :add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=lambda :add_digit(operation))


win = tk.Tk()

win.geometry(f"240x270+100+200")
win['bg'] = '#33ffe6'
win.title('калькулятор')

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.grid(row=0, column=0, columnspan=3, stick='we', padx=5)

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=2.5,pady=2.5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=2.5,pady=2.5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=2.5,pady=2.5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=2.5,pady=2.5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=2.5,pady=2.5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=2.5,pady=2.5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=2.5,pady=2.5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=2.5,pady=2.5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=2.5,pady=2.5)
make_digit_button('0').grid(row=4, column=1, stick='wens', padx=2.5,pady=2.5)


make_operation_button("+").grid(row=0, column=3, stick='wens', padx=2.5,pady=2.5)
make_operation_button("-").grid(row=1, column=3, stick='wens', padx=2.5,pady=2.5)
make_operation_button("/").grid(row=2, column=3, stick='wens', padx=2.5,pady=2.5)
make_operation_button("*").grid(row=3, column=3, stick='wens', padx=2.5,pady=2.5)
make_operation_button("√").grid(row=4, column=3, stick='wens', padx=2.5,pady=2.5)
make_operation_button("=").grid(row=4, column=2, stick='wens', padx=2.5,pady=2.5)
make_operation_button("Y^ᵡ").grid(row=5, column=3, stick='wens', padx=2.5,pady=2.5)

win.grid_columnconfigure(0, minsize=50)
win.grid_columnconfigure(1, minsize=50)
win.grid_columnconfigure(2, minsize=50)
win.grid_columnconfigure(3, minsize=50)

win.grid_rowconfigure(0, minsize=30)
win.grid_rowconfigure(1, minsize=30)
win.grid_rowconfigure(2, minsize=30)
win.grid_rowconfigure(3, minsize=30)


win.mainloop()