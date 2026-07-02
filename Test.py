import tkinter as tk
import random
import json
from tkinter.messagebox import showwarning

root = tk.Tk()
root.title("Тест")
root.geometry("600x600")
root.eval('tk::PlaceWindow . center')


selected_answer = tk.IntVar()
selected_answer.set(-1)

question_number = 0
max_questions = 15

#Массив для кнопок что бы потом изменить их текст
save_radio = []

#Массив для True & False
save_TF = []

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
correct_index = current_question['correct']

#Реализует перемешанный порядок кнопок
'''
random.shuffle(all_answers)
'''

#Вывод вопроса
lbl_questions = tk.Label(root, text=f'Вопрос {question_number + 1}\n\n {question_text}')
lbl_questions.grid(row=0, column=0, columnspan=2, pady=50)

#Логика на создание кнопки
for idx, ans_text in enumerate(all_answers):
    radio = tk.Radiobutton(root, text=ans_text, value=idx, variable=selected_answer)
    radio.grid(row=idx + 1, column=0, pady=10, sticky=tk.W)

    save_radio.append(radio)

def next_question():
    global question_number, question_text, all_answers, correct_index, current_question
    question_number += 1

    current_question = question[question_number]

    question_text = current_question['text']
    all_answers = current_question['answers']
    correct_index = current_question['correct']

    correct_count = sum(save_TF)
    total_count = len(save_TF)


    #Условие по остановке теста и удаление лишних объектов
    if question_number != max_questions:
        return show_question()
    else:
        lbl_questions.config(text=f'Тест пройден! Правильных ответов: {correct_count} из {total_count} вопросов')
        btn.destroy()
        for i in save_radio:
            i.destroy()


def result():
    ...

    return result
    
#Переключает вопросы и ответы
def show_question():

    #Вывод нового вопроса
    lbl_questions.config(text=f'Вопрос {question_number + 1}\n\n {question_text}')

    #Вывод нового ответа
    for idx, radio in enumerate(save_radio):
        radio.config(text=all_answers[idx])

    #Утсановка значения для того что бы следующий вопрос не был тоже выбран как и предыдущий
    selected_answer.set(-1)

#Функция на вывод всплывающего окна
def open_warning():
    showwarning(title='Предупреждение', message='Выберете вариант ответа')

#Логика на поверку ответа
def check_answer():

    #Условие на то что бы пользовтель не мог пройти дальше пока не выберет овтет
    if selected_answer.get() == -1:
        return open_warning()

    #Условие добавления Правильного или Неправильного вопроса
    if selected_answer.get() == correct_index:
        save_TF.append(True)
    else:
        save_TF.append(False)

    return next_question()

#Кнопка для проверки
btn = tk.Button(root, text='Ответить', command=check_answer)
btn.grid(row=6, column=0, pady=20)

root.mainloop()