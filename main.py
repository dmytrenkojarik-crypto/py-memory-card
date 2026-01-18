from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QRadioButton,
    QGroupBox, QLabel, QVBoxLayout,QHBoxLayout,QButtonGroup
)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        
question_list = []
q1 = Question("chomu dorivnue P", "3.1415", "3", "4.51", "9.28")
q2 = Question("skilky bude 27 * 3 ", "81", "80", "30", "59")
q3 = Question("chomu dorivnue priskorena volneho padina", "9.8", "9", "12.7","6.3")

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card")

btn_ok = QPushButton("vidpovid")
lb_question = QLabel("ckladne zapitana")
radioGroupBox = QGroupBox("varianty vidpovidei")

rbtn_1 = QRadioButton("1")
rbtn_2 = QRadioButton("2")
rbtn_3 = QRadioButton("3")
rbtn_4 = QRadioButton("4")

layout_ans1 = QHBoxLayout()

layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radioGroupBox.setLayout(layout_ans1)

ansGroupBox = QGroupBox("rezultat")
lb_result = QLabel("pravilno")
lb_correct = QLabel("pravilna vidpovid")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, 0,(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct,  2, Qt.AlignHCenter)
ansGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question,  0, Qt.AlignCenter)

layout_line2.addWidget(radioGroupBox)
layout_line2.addWidget(ansGroupBox)

ansGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, 2)
layout_card.addLayout(layout_line2, 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


window.setLayout(layout_card)
window.resize(700, 500)
window.show()

radioGroup = QButtonGroup()
radioGroup.addButton(rbtn_1)
radioGroup.addButton(rbtn_2)
radioGroup.addButton(rbtn_3)
radioGroup.addButton(rbtn_4)

def show_result():
    radioGroupBox.hide()
    ansGroupBox.show()
    btn_ok.setText("nastupne zapitana")

def show_question():
    ansGroupBox.hide()
    radioGroupBox.show()
    btn_ok.setText("vidpovid")
    radioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radioGroup.setExclusive(True)  
    
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(result):
    lb_result.setText(result)
    show_result()
    
def check_answer():
    if answers[0].isChecked():
        show_correct("pravilno")
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked()or answers[3].isChecked():
            show_correct("ne pravilno")
                
def next_question():
    window.total += 1
    
    cur_question = randint(0, len(question_list)- 1)
    q = question_list[cur_question]
    ask(q)       
         
def click_ok():
    if btn_ok.text() == "vidpovid":
        check_answer()
        print("vasha statistika:")
        print("vsoho vidpovidei", window.total)
        print("pravilnych vidpovidei",window.score)
        print("vash reiting", (window.score / window.total * 100), "%")
    else:
        next_question()
          
window.cur_question = -1


window.total = 0
window.score = 0

btn_ok.clicked.connect(click_ok)
next_question  ()              
                
app.exec_()

