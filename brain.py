cheat_sheet = ''
def was_asked(memory, q):
    global cheat_sheet
    for question, answer in memory:
        if question == q:
            return 1
    return 0

def old_answer():
    global cheat_sheet
    rez, cheat_sheet = cheat_sheet, ''
    return rez

if __name__ == '__main__':
    memory = [
        ('Ты умеешь говорить', 'да'),
        ('Ты умеешь говорить', 'нет')
    ]
    q = 'Ты умеешь говорить'

    print(q, was_asked(memory, q))
    print(q, old_answer(memory, q))
    print(q, old_answer(memory, q))