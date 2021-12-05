#Задание 3 (сравнение ответов)
from brain_3 import Brain

brain = Brain()
prompt = "Что вас интересует?"

question = ""
while question != "хватит":
    print(prompt, end = ' ')
    answer = brain.think(input())
    print(answer)
