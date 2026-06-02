import tkinter as tk
import random

root = tk.Tk()
root.title("Тест")
root.geometry("600x600")

selected_answer = tk.IntVar()

questions = []

with open ('Questions', 'r', encoding='utf-8') as file:
    question = file.readlines()
    for line in question:
        if not line.startswith('№') and line.strip() != '':
            questions.append(line)

lbl_questions = tk.Label(root, text=f'{random.choice()}')
lbl_questions.grid(row=0, column=0, columnspan=2, pady=50)

radio1 = tk.Radiobutton(root, text="Никому", value=1, variable=selected_answer)
radio1.grid(row=1, column=0, pady=10, sticky=tk.W)

radio2 = tk.Radiobutton(root, text="Только отделу ИБиИТ", value=2, variable=selected_answer)
radio2.grid(row=2, column=0, pady=10, sticky=tk.W)

radio3 = tk.Radiobutton(root, text="Непосредственному начальнику", value=3, variable=selected_answer)
radio3.grid(row=3, column=0, pady=10, sticky=tk.W)

radio4 = tk.Radiobutton(root, text="Всем", value=4, variable=selected_answer)
radio4.grid(row=4, column=0, pady=10, sticky=tk.W)

def check_answer():
    if selected_answer.get() == 1:
        lbl_result.config(text='Ответ правильный!')
    else:
        lbl_result.config(text='Ответ неправильный!')

btn = tk.Button(root, text='Ответить', command=check_answer)
btn.grid(row=5, column=0, pady=20)

lbl_result = tk.Label(root, text='')
lbl_result.grid(row=6, column=0, pady=10)

root.mainloop()