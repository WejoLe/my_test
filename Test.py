import tkinter as tk
import random
import json

root = tk.Tk()
root.title("Тест")
root.geometry("600x600")

selected_answer = tk.IntVar()
selected_answer.set(-1)

question_number = 0

save_radio = []
save_TF = []

#Логика на нахождение вопроса из файла "Question"
with open ('questions.json', 'r', encoding='utf-8') as file:
    question = json.load(file)

random.shuffle(question)
current_question = question[question_number]

#Переменные для храниения значений
question_text = current_question['text']
all_answers = current_question['answers']
correct_index = current_question['correct']

number = len(question_text)

#Вывод вопроса
lbl_questions = tk.Label(root, text=f'Вопрос {question_number + 1}\n\n {question_text}')
lbl_questions.grid(row=0, column=0, columnspan=2, pady=50)

#Логика на создание кнопки
for idx, ans_text in enumerate(all_answers):
    radio = tk.Radiobutton(root, text=ans_text, value=idx, variable=selected_answer)
    radio.grid(row=idx + 1, column=0, pady=10, sticky=tk.W)

    save_radio.append(radio)

#Переключает вопросы и ответы
def show_question():
    global question_number
    question_number += 1

    new_current_question = question[question_number]
    quest = new_current_question['text']
    #cor = new_current_question['corrent']

    lbl_questions.config(text=f'Вопрос {question_number + 1}\n\n {quest}')

    for idx, radio in enumerate(save_radio):
        radio.config(text=new_current_question['answers'][idx])

    selected_answer.set(-1)

#Логика на поверку ответа
def check_answer():
    if selected_answer.set(-1) != selected_answer.get():
        print('Ошибка')
    else:
        print('Круто')

    if selected_answer.get() == correct_index:
        save_TF.append(True)
    else:
        save_TF.append(False)

    print(save_TF)
    return show_question()

#Чтение сколько вопросов в хранилище
Go = len(all_answers)

#Кнопка для проверки
btn = tk.Button(root, text='Ответить', command=check_answer)
btn.grid(row=Go + 2, column=0, pady=20)

root.mainloop()