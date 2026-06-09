import tkinter as tk
import random

root = tk.Tk()
root.title("Тест")
root.geometry("600x600")

selected_answer = tk.IntVar()

#Храненилище вопросов и их ответов в СЛУЧАЙНОМ пордке :)
current_question = random.choice([
    {
    'text': 'Кому можно разглашать пароль от своего рабочего компьютера?',
    'answers': ['Никому', 'Только отделу ИБиИТ', 'Всем'],
    'correct': 1
    },

    {
    'text': 'Кому можно?',
    'answers': ['Мне','Им'],
    'correct': 0
    }
])

#Переменные для храниения значений
question_text = current_question['text']
all_answers = current_question['answers']
correct_index = current_question['correct']

#Логика на нахождение вопроса из файла "Question"
'''
with open ('Questions', 'r', encoding='utf-8') as file:
    question = file.readlines()
    for line in question:
        if not line.startswith('№') and line.strip() != '':
            questions.append(line)
'''

#Вывод вопроса
lbl_questions = tk.Label(root, text=question_text)
lbl_questions.grid(row=0, column=0, columnspan=2, pady=50)

#Логика на создание кнопки
for idx, ans_text in enumerate(all_answers):
    radio = tk.Radiobutton(root, text=ans_text, value=idx, variable=selected_answer)
    radio.grid(row=idx + 1, column=0, pady=10, sticky=tk.W)

#Логика на поверку ответа
def check_answer():
    if selected_answer.get() == correct_index:
        lbl_result.config(text='Ответ правильный!')
    else:
        lbl_result.config(text='Ответ неправильный!')

#Кнопка для проверки
btn = tk.Button(root, text='Ответить', command=check_answer)
btn.grid(row=5, column=0, pady=20)

#Скрытый Label который отображает правильность ответа при его проверки
lbl_result = tk.Label(root, text='')
lbl_result.grid(row=6, column=0, pady=10)

root.mainloop()