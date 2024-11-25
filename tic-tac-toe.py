
#функция печати
def print_arr():
    print (' ',0, 1, 2)
    for i in range(3): print(i, *array[i])

#функция проверки позиции
def choose_position():
    print("Выберите, Столбец и Строку, куда поставить ",element)
    try:
        a, b = [int(z) for z in input().split()]
    except ValueError:
        print("Ошибка в данных, попробуй еще раз")
        choose_position()
    else:
        if (a >= 0 and a < 3) and (b >= 0 and b < 3):
            if array[b][a] == '-':
                print("Вы выбрали столбец", a, "и строку", b)
                array[b][a] = element
                return array
            else: 
                print("Позиция занята")
                choose_position()
        else:
            print("Позиция вне диапазона")
            choose_position()

def check_win(arr):
    #проверяем диагональ, их всего 2
    if (arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2]) or (arr[0][2] == arr[1][1] and arr[1][1] == arr[2][0]):
        return arr[1][1]
    else:
        for i in range(3):
            #сверяем строки/столбцы
            if (arr[i][0] == arr[i][1] and arr[i][0] == arr[i][2]):
                return arr[i][0] 
            if (arr[0][i] == arr[1][i] and arr[0][i] == arr[2][i]):
                return arr[0][i]    



array = [['-']*3 for j in range(3)]
print_arr()
#итератор хода
pos = 0
while True:
    element = "x" if pos%2 == 0 else "o"
    choose_position()
    print_arr()
    pos += 1
    if pos > 4:
        z = check_win(array)
        if z is not None:
            print("Выиграл игрок", z)
            break
    if pos > 8:
        print("Ничья")
        break

