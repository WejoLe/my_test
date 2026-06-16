import tkinter as tk
import random
import json

root = tk.Tk()
root.title("Тест")
root.geometry("600x600")

selected_answer = tk.IntVar()
selected_answer.set(-1)

question_number = 0

#Логика на нахождение вопроса из файла "Question"
with open ('questions.json', 'r', encoding='utf-8') as file:
    question = json.load(file)

random.shuffle(question)
current_question = question[question_number]

#Переменные для храниения значений
question_text = current_question['text']
all_answers = current_question['answers']
correct_index = current_question['correct']

#Вывод вопроса
lbl_questions = tk.Label(root, text=f'Вопрос {question_number + 1}\n\n {question_text}')
lbl_questions.grid(row=0, column=0, columnspan=2, pady=50)

#Логика на создание кнопки
for idx, ans_text in enumerate(all_answers):
    radio = tk.Radiobutton(root, text=ans_text, value=idx, variable=selected_answer)
    radio.grid(row=idx + 1, column=0, pady=10, sticky=tk.W)

def load_next_question():
    global question_number

    question_number += 1

    new_current_question = question[question_number]
    quest = new_current_question['text']
    ans = current_question['answers']

    lbl_questions.config(text=f'Вопрос {question_number + 1}\n\n {quest}')


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