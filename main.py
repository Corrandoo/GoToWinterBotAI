import random
#23OQQVCJ my key
#field[0][0] = левый верхний угол
#field[x_size - 1][0] = правый верхний угол
#field[0][y_size - 1] = левый нижний угол
#field[x_size - 1][y_size - 1] = правый нижний угол

def make_choice(x,y,field):
    x_size = len(field)
    y_size = len(field[0])
    isAttackRight = False #ЕСТЬ ЛИ АТАКА СПРАВА
    isAttackLeft = False #ЕСТЬ ЛИ АТАКА СЛЕВА
    isAttackUp = False #ЕСТЬ ЛИ АТАКА СВЕРХУ
    isAttackDown = False #ЕСТЬ ЛИ АТАКА СНИЗУ
    isUNastyHarder = False #СИЛЬНЕЕ ЛИ ВЕРХНИЙ ПРОТИВНИК
    isDNastyHarder = False #СИЛЬНЕЕ ЛИ НИЖНИЙ ПРОТИВНИК
    isLNastyHarder = False #СИЛЬНЕЕ ЛИ ЛЕВЫЙ ПРОТИВНИК
    isRNastyHarder = False #СИЛЬНЕЕ ЛИ ПРАВЫЙ ПРОТИВНИК

    for i in range(0, x - 1):
        if field[i][y] != 0 and field[i][y]['history'] == "fire_right":
            isAttackLeft = True
    for i in range(x + 1, x_size - 1):
        if field[i][y] != 0 and field[i][y]['history'] == "fire_left":
            isAttackRight = True
    for i in range(0, y - 1):
        if field[x][i] != 0 and field[x][i]['history'] == "fire_down":
            isAttackUp = True
    for i in range(y + 1, y_size - 1):
        if field[x][i] != 0 and field[x][i]['history'] == "fire_up":
            isAttackDown = True


    for i in range(0, x - 1):
        if field[i][y] != 0:
            return "fire_left"
    for i in range(x + 1, x_size - 1):
        if field[i][y] != 0:
            return "fire_right"
    for i in range(0, y - 1):
        if field[x][i] != 0:
            return "fire_up"
    for i in range(y + 1, y_size - 1):
        if field[x][i] != 0:
            return "fire_down"

    return random.choice(["go_left", "go_down"])