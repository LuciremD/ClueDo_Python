import tkinter

colors = ["red", "green", "yellow", "blue", "grey"]
index = 0


def change(button):
    global index
    color = colors[index]
    index = (index + 1) % len(colors)
    button.config(bg=color)


def Table(player):
    def make_lambda(i, j):
        return lambda: change(but[i, j])

    X = 15
    rt = tkinter.Tk()
    rt.title("Table")
    but = {}
    for i in range(24):
        for j in range(7):
            if i == 0:
                if (j == 0):
                    b = tkinter.Label(rt, text='Карты', width=X,
                                      height=1, font=("Arial", 14))
                elif (j == 1):
                    b = tkinter.Label(rt, text='Мистер Мастард', width=X,
                                      height=1, font=("Arial", 14))
                elif (j == 2):
                    b = tkinter.Label(rt, text='Мистер Плам', width=X,
                                      height=1, font=("Arial", 14))
                elif (j == 3):
                    b = tkinter.Label(rt, text='Мистер Грин', width=X,
                                      height=1, font=("Arial", 14))
                elif (j == 4):
                    b = tkinter.Label(rt, text='Леди Пикок', width=X,
                                      height=1, font=("Arial", 14))
                elif (j == 5):
                    b = tkinter.Label(rt, text='Леди Уайт', width=X,
                                      height=1, font=("Arial", 14))
                elif (j == 6):
                    b = tkinter.Label(rt, text='Леди Скарлет', width=X,
                                      height=1, font=("Arial", 14))
                b.grid(row=i, column=j)
            elif i == 7 or i == 14:
                b = tkinter.Label(rt, bg='black', width=X, height=1)
                b.grid(row=i, column=j)
            else:
                if j in player.exist or j == 0:
                    if j == 0:
                        if (i == 1):
                            str_ = 'Мистер Мастард'
                            b = tkinter.Label(rt, text=str_, width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 2):
                            b = tkinter.Label(rt, text='Мистер Плам', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 3):
                            b = tkinter.Label(rt, text='Мистер Грин', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 4):
                            b = tkinter.Label(rt, text='Леди Пикок', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 5):
                            b = tkinter.Label(rt, text='Леди Уайт', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 6):
                            b = tkinter.Label(rt, text='Леди Скарлет', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 8):
                            b = tkinter.Label(rt, text='Кинжал', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 9):
                            b = tkinter.Label(rt, text='Гаечный ключ', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 10):
                            b = tkinter.Label(rt, text='Подсвечник', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 11):
                            b = tkinter.Label(rt, text='Револьвер', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 12):
                            b = tkinter.Label(rt, text='Веревка', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 13):
                            str_ = 'Свинцовая труба'
                            b = tkinter.Label(rt, text=str_, width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 15):
                            b = tkinter.Label(rt, text='Кухня', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 16):
                            b = tkinter.Label(rt, text='Столовая', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 17):
                            b = tkinter.Label(rt, text='Гостиная', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 18):
                            b = tkinter.Label(rt, text='Задний двор', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 19):
                            b = tkinter.Label(rt, text='Гараж', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 20):
                            b = tkinter.Label(rt, text='Бильярдная', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 21):
                            b = tkinter.Label(rt, text='Спалья', width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 22):
                            str_ = 'Ванная комната'
                            b = tkinter.Label(rt, text=str_, width=X,
                                              height=1, font=("Arial", 14))
                        elif (i == 23):
                            b = tkinter.Label(rt, text='Кабинет', width=X,
                                              height=1, font=("Arial", 14))
                        b.grid(row=i, column=j)
                    else:
                        l_ = tkinter.Button(rt, width=X, height=1, bg='white',
                                            command=make_lambda(i, j))
                        but[i, j] = l_
                        l_.grid(row=i, column=j)
    for i, j in but:
        color = player.cells[i, j]
        but[i, j].config(bg=color)
