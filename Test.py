import tkinter as tk
import random
import json

root = tk.Tk()
root.title("Тест")
root.geometry("600x600")

selected_answer = tk.IntVar()
selected_answer.set(-1)

#Логика на нахождение вопроса из файла "Question"
with open ('questions.json', 'r', encoding='utf-8') as file:
    question = json.load(file)

corrent_question = random.choice(question)

#Переменные для храниения значений
question_text = corrent_question['text']
all_answers = corrent_question['answers']
correct_index = corrent_question['correct']
question_number = 0

#Вывод вопроса
lbl_questions = tk.Label(root, text=f'Вопрос\n\n {question_text}')
lbl_questions.grid(row=0, column=0, columnspan=2, pady=50)

#Логика на создание кнопки
for idx, ans_text in enumerate(all_answers):
    radio = tk.Radiobutton(root, text=ans_text, value=idx, variable=selected_answer)
    radio.grid(row=idx + 1, column=0, pady=10, sticky=tk.W)

def load_next_question():
    global question_number
    question_number += 1
    new_question_r = random.choice(question)

    question_text = new_question_r['text']
    all_answers = new_question_r['answers']
    correct_index = new_question_r['correct']
    
    lbl_questions.config(text=f'Вопрос {question_number + 1}\n\n {question_text}')
    radio.grid_forget

#Логика на поверку ответа
'''
def check_answer():
    if selected_answer.get() == correct_index:
        lbl_result.config(text='Ответ правильный!')
    else:
        lbl_result.config(text='Ответ неправильный!')

    selected_answer.set(-1)
'''

#Чтение сколько вопросов в хранилище
Go = len(all_answers)

#Кнопка для проверки
btn = tk.Button(root, text='Ответить', command=load_next_question)
btn.grid(row=Go + 2, column=0, pady=20)

#Скрытый Label который отображает правильность ответа при его проверки
lbl_result = tk.Label(root, text='')
lbl_result.grid(row=Go + 3, column=0, pady=10)

root.mainloop()