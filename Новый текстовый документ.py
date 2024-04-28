from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, \
    QGroupBox
from random import choice

questions = [
                {'question':'Какой народности не существует?', 
                'answer1':'Смурфы',
                'answer2':'Ненцы',
                'answer3':'Нанайцы',
                'answer4':'Буряты',
                'correct':'Смурфы'
                },
                {'question':'Кaк обозначается медь?', 
                'answer1':'Cu',
                'answer2':'Au',
                'answer3':'Ag',
                'answer4':'O',
                'correct':'Cu'
                }
]

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.setFixedSize(250, 200)

question = QLabel('?')
group_answers = QGroupBox('Выберите ответ')
# Create radio buttons for answers
ans_1 = QRadioButton('')
ans_2 = QRadioButton('')
ans_3 = QRadioButton('')
ans_4 = QRadioButton('')
# Place radio buttons in group box
ans_layout1 = QVBoxLayout()
ans_layout1.setSpacing(20)
ans_layout1.addWidget(ans_1, alignment=Qt.AlignCenter)
ans_layout1.addWidget(ans_2, alignment=Qt.AlignCenter)

ans_layout2 = QVBoxLayout()
ans_layout2.setSpacing(20)
ans_layout2.addWidget(ans_3, alignment=Qt.AlignCenter)
ans_layout2.addWidget(ans_4, alignment=Qt.AlignCenter)
ans_layout = QHBoxLayout()
ans_layout.addLayout(ans_layout1)
ans_layout.addLayout(ans_layout2)
group_answers.setLayout(ans_layout)


def show_result():
    if button.text() == 'Ответить':
        for ans in (ans_1, ans_2, ans_3, ans_4):
            if ans.isChecked():
                button.setText('Следующий вопрос')
                answer_group.show()
                group_answers.hide()
                if ans.text() == window.correct:
                    is_correct.setStyleSheet('color: #339900;')
                    is_correct.setText('Правильно!')
                else:
                    is_correct.setStyleSheet('color: #FF0000;')
                    is_correct.setText('Неправильно... :-(')
    else:
        set_question()
        answer_group.hide()
        group_answers.show()
        button.setText('Ответить')


button = QPushButton('Ответить')
button.clicked.connect(show_result)

answer_group = QGroupBox('Правильный ответ:')
is_correct = QLabel('Правильно')
answer_line = QVBoxLayout()
answer_line.addWidget(is_correct, alignment=Qt.AlignCenter)
answer_group.setLayout(answer_line)
answer_group.hide()

line = QVBoxLayout()
line.addWidget(question, alignment=Qt.AlignCenter)
line.addWidget(group_answers, alignment=Qt.AlignCenter)
line.addWidget(answer_group, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
line.setSpacing(20)

window.setLayout(line)
window.show()


def set_question():
    text_question, a1, a2, a3, a4, correct = choice(questions).values()
    question.setText(text_question)
    ans_1.setText(a1)
    ans_2.setText(a2)
    ans_3.setText(a3)
    ans_4.setText(a4)
    window.correct = correct


set_question()

app.exec_()
