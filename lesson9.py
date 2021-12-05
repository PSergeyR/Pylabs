from random import randint
from brain import was_asked, old_answer
memory = []
prompt = "Что Вас интересует?"
answers = ("Да", "Нет")
question = ""
while question != "хватит": #Надо предусмотреть выход
    print(prompt, end = ' ')
    question = input()
    if was_asked(memory, question):
        print(old_answer())
    else:
        answer = answers[randint(0, len(answers) - 1)]
        print(answer)
        memory += [(question, answer)]
