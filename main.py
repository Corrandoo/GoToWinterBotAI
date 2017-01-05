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
    isEnemyU = False #ЕСТЬ ЛИ ПРОТИВНИК СВЕРХУ
    isEnemyD = False #ЕСТЬ ЛИ ПРОТИВНИК СНИЗУ
    isEnemyL = False #ЕСТЬ ЛИ ПРОТИВНИК СЛЕВА
    isEnemyR = False #ЕСТЬ ЛИ ПРОТИВНИК СПРАВА

    for i in range(0, x - 1):
        try:
            if field[i][y] != 0 and field[i][y]['history'][-1] == "fire_right":
                isAttackLeft = True
        except:
            pass
        if field[i][y] != 0 and field[i][y]['life'] >= field[x][y]['life']:
            isLNastyHarder = True
    for i in range(x + 1, x_size - 1):
        try:
            if field[i][y] != 0 and field[i][y]['history'][-1] == "fire_left":
                isAttackRight = True
        except:
            pass
        if field[i][y] != 0 and field[i][y]['life'] >= field[x][y]['life']:
            isRNastyHarder = True
    for i in range(0, y - 1):
        try:
            if field[x][i] != 0 and field[x][i]['history'][-1] == "fire_down":
                isAttackUp = True
        except:
            pass
        if field[x][i] != 0 and field[x][i]['life'] >= field[x][y]['life']:
            isUNastyHarder = True
    for i in range(y + 1, y_size - 1):
        try:
            if field[x][i] != 0 and field[x][i]['history'][-1] == "fire_up":
                isAttackDown = True
        except:
            pass
        if field[x][i] != 0 and field[x][i]['life'] >= field[x][y]['life']:
            isDNastyHarder = True

    for i in range(0, x - 1):
        if field[i][y] != 0:
            isEnemyL = True
    for i in range(x + 1, x_size - 1):
        if field[i][y] != 0:
            isEnemyR = True
    for i in range(0, y - 1):
        if field[x][i] != 0:
            isEnemyU = True
    for i in range(y + 1, y_size - 1):
        if field[x][i] != 0:
            isEnemyD = True

    if isAttackRight == True and isAttackLeft == True:
        return random.choice(["go_up", "go_down"])
    elif isAttackDown == True and isAttackUp == True:
        return random.choice(["go_left", "go_right"])
    elif isAttackUp == True and isAttackRight == True:
        return random.choice(["go_left", "go_down"])
    elif isAttackUp == True and isAttackLeft == True:
        return random.choice(["go_right", "go_down"])
    elif isAttackDown == True and isAttackLeft == True:
        return random.choice(["go_right", "go_down"])
    elif isAttackDown == True and isAttackRight == True:
        return random.choice(["go_up", "go_left"])

    if isEnemyD == True and isDNastyHarder == False:
        return "fire_down"
    if isEnemyL == True and isLNastyHarder == False:
        return "fire_left"
    if isEnemyR == True and isRNastyHarder == False:
        return "fire_right"
    if isEnemyU == True and isUNastyHarder == False:
        return "fire_up"

    return random.choice(["go_left", "go_down", "go_up", "go_right"])