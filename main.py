#=================== 1. ИНИЦИАЛИЗАЦИЯ (GUI + переменные) =================== 

import tkinter as tk
import random
import json
from tkinter.messagebox import showwarning

root = tk.Tk()
root.title("Мой тест на Python — версия 1.0")
root.geometry("600x650")
root.eval('tk::PlaceWindow . center')
root.configure(bg = '#f0f4f8')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)


selected_answer = tk.IntVar(); selected_answer.set(-1)

question_number = 0
max_questions = 15

#Массив для кнопок что бы потом изменить их текст
save_radio = []

#Массив для True & False
save_TF = []

#===================== 2. ЗАГРУЗКА ДАННЫХ ===================== 

#Логика на нахождение вопроса из файла "Question"
with open ('questions.json', 'r', encoding='utf-8') as file:
    question = json.load(file)

#Задаём значение перемешивания в массиве
random.shuffle(question)

#Получаем случайный 1й вопрос
current_question = question[question_number]

#Переменные для храниения значений
question_text = current_question['text']
all_answers = current_question['answers']

random.shuffle(all_answers)

#=================== 3. СОЗДАНИЕ ИНТЕРФЕЙСА (кнопки, лейблы) =================== 

#Вывод номера вопроса
lbl_num = tk.Label(root, text=f'Вопрос {question_number + 1}',
font=('Helvetica', 14),
wraplength=600,
justify = tk.CENTER,
bg = '#f0f4f8',
fg='#777777')
lbl_num.grid(row=0, column=0, columnspan=2, pady=[50, 10])

#Вывод вопроса
lbl_questions = tk.Label(root, text=f'{question_text}',
font=('Helvetica', 16, 'bold'),
wraplength=600,
justify = tk.CENTER,
bg = '#f0f4f8')
lbl_questions.grid(row=1, column=0, columnspan=2, pady=[0, 50])

#Логика на создание кнопки
for idx, ans_text in enumerate(all_answers):
    radio = tk.Radiobutton(root, text=ans_text['text'], value=idx, variable=selected_answer,
    indicatoron=0,
    selectcolor="#2f8acb",
    width=42,
    pady=12,
    relief = tk.FLAT,
    bg = '#ffffff')
    radio.grid(row=1 + idx + 1, column=0, pady=10, columnspan=2)

    save_radio.append(radio)

#================================================= 4. ФУНКЦИИ (логика) ================================================= 

def next_question():
    global question_number, question_text, all_answers, current_question
    question_number += 1

    #Условие по остановке теста и удаление лишних объектов
    if question_number >= max_questions:
        lbl_questions.config(text=f'Тест пройден! Правильных ответов: {sum(save_TF)} из {len(save_TF)} вопросов \n\n Процент правильных ответов: {result():.2f}%')
        btn.destroy()
        for i in save_radio:
            i.grid_forget()
        return

    #Получаем случайные вопросы
    current_question = question[question_number]

    #Указываем значения
    question_text = current_question['text']
    all_answers = current_question['answers']
    
    show_question()

#Функция подсчёта процента для ответа
def result():

    correct_count = sum(save_TF)
    total_count = len(save_TF)

    res = (correct_count / total_count) * 100

    return res
    
#Переключает вопросы и ответы
def show_question():
    global all_answers

    all_answers = current_question['answers'][:] #Делаем копию
    random.shuffle(all_answers) # Исразу перемешиваем её

    #Вывод нового номера вопроса
    lbl_num.config(text=f'Вопрос {question_number + 1}')

    #Вывод нового вопроса
    lbl_questions.config(text=f'{question_text}')

    #Вывод нового ответа
    for idx, radio in enumerate(save_radio):
        radio.config(text=all_answers[idx]['text'])

    #Утсановка значения для того что бы следующий вопрос не был тоже выбран как и предыдущий
    selected_answer.set(-1)

#Функция на вывод всплывающего окна
def open_warning():
    showwarning(title='Предупреждение', message='Выберите вариант ответа')

#Логика на поверку ответа
def check_answer():

    #Условие на то что бы пользовтель не мог пройти дальше пока не выберет овтет
    if selected_answer.get() == -1:
        return open_warning()

    idx = selected_answer.get()
    chosen_answer = all_answers[idx]

    #Условие добавления Правильного или Неправильного вопроса
    if chosen_answer['is_correct']:
        save_TF.append(True)
    else:
        save_TF.append(False)

    return next_question()

#Кнопка для проверки
btn = tk.Button(root, text='Ответить', command=check_answer, padx=20, pady=10)
btn.grid(row=6, column=0, pady=20, columnspan=2)

root.mainloop()