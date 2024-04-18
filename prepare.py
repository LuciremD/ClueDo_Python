import class_player
import basa
# import table
import random
import sys
import getpass

Players = []  # pointers to players
Order = []  # order for questions
Exist = []  # what characters exist
help_1 = []  # for dices
ANSWER = []  # answer
ANSWER_ = []  # answer
chosen = []  # chosen charactres


sys.stdout.write("Поздравляем, вы хозяин игры!\n"
                 "Перед началом игры необхожимо выполнить несколько шагов.\n"
                 "Во-первыхб пожалуйста, введите количество игроков.\n"
                 "(Напишите числа или 2, или 3, или 6): ")
sys.stdout.flush()
basa.AMOUNT_OF_PLAYERS = int(input())
sys.stdout.write("\033[F\033[K\033[F\033[K\033[F\033[K\033[F\033[K")


sys.stdout.write("Спасибо! Теперь следующий шаг.\n"
                 "Пожалуйста выберите ник и создайте пароль,"
                 "чтобы я был уверен, что играете именно вы.\n")
for i in range(basa.AMOUNT_OF_PLAYERS):
    sys.stdout.write("Пожалуйста, напишите ваш ник: ")
    sys.stdout.flush()
    nickname = input()
    sys.stdout.write(f'Спасибо, {nickname}, пожалуйста, придумайте пароль: ')
    sys.stdout.flush()
    password = input()
    sys.stdout.write("\033[F\033[K\033[F\033[K")
    Players.append(class_player.Player(nickname, password))
    if i == 0:
        sys.stdout.write("Отлично, следующий игрок!\n")
        sys.stdout.flush()
    elif i == basa.AMOUNT_OF_PLAYERS - 1:
        sys.stdout.write("\033[F\033[K\033[F\033[K\033[F\033[K")

help_str = 'пожалуйста, нажмите "ENTER", чтобы ход перешел к следующему игроку'
sys.stdout.write("Отлично, следующий шаг! Давайте определимся "
                 "в каком порядке вы будуте ходить.\n"
                 "Для этого вам необходимо бросить два кубика.\n")
sys.stdout.flush()
for i in range(basa.AMOUNT_OF_PLAYERS):
    k = 0
    sys.stdout.write(f'{Players[i].nick}, пожалуйста, введите пароль: ')
    sys.stdout.flush()
    k += 1
    smth = getpass.getpass('')
    while (smth != Players[i].password):
        sys.stdout.write(f'{Players[i].nick}, пожалуйста, попробуйте снова: ')
        sys.stdout.flush()
        k += 1
        smth = getpass.getpass('')
    sys.stdout.write("Пожалуйтса, напишите 'D' или'd', чтобы бросить кубик: ")
    sys.stdout.flush()
    k += 1
    inp = input()
    while inp != 'D' and inp != 'd':
        sys.stdout.write("Пожалуйста, попробуйте еще раз: ")
        sys.stdout.flush()
        k += 1
        inp = input()
    num1, num2 = random.randint(1, 6), random.randint(1, 6)
    tl = num1 + num2
    while tl in help_1:
        num1, num2 = random.randint(1, 6), random.randint(1, 6)
        tl = num1 + num2
    sys.stdout.write(f'На кубиках выпало {num1} и {num2}. В сумме: {tl}\n')
    sys.stdout.flush()
    k += 1
    Players[i].dices = tl
    help_1.append(tl)
    sys.stdout.write(f'{Players[i].nick}, {help_str}!')
    sys.stdout.flush()
    k += 1
    ent = input()
    while (ent.endswith('\n')):
        sys.stdout.write(f'{Players[i].nick}, пожалуйста, попробуйте снова: ')
        sys.stdout.flush()
        k += 1
        ent = input()
    for j in range(k):
        sys.stdout.write("\033[F\033[K")
sys.stdout.write("\033[F\033[K\033[F\033[K")

help_1.sort(reverse=True)
for i in help_1:
    for j in range(basa.AMOUNT_OF_PLAYERS):
        if Players[j].dices == i:
            Order.append(j)

sys.stdout.write("Поздравляю, мы почти закончили!\n"
                 "Сейчас, последний шаг. Вам необходимо выбрать персонажа.\n"
                 "Вы будете выбирать их в порядке, в котором будете ходить.\n")
sys.stdout.flush()

for i in range(basa.AMOUNT_OF_PLAYERS):
    N = Players[Order[i]].nick
    k = 0
    sys.stdout.write(f'{N}, пожалуйста, введите пароль: ')
    sys.stdout.flush()
    k += 1
    smth = getpass.getpass('')
    while (smth != Players[Order[i]].password):
        help_str_ = 'пожалуйста, попробуйте снова: '
        sys.stdout.write(f'{Players[Order[i]].nick}, ' + help_str_)
        sys.stdout.flush()
        k += 1
        smth = getpass.getpass('')
    aop = basa.AMOUNT_OF_PLAYERS
    sys.stdout.write('Выберите из следующих персонажей:\n')
    sys.stdout.flush()
    k += 1
    keys = list(basa.People.keys())
    for j in range(6):
        if j not in chosen:
            sys.stdout.write(f'{j + 1} {keys[j]}\n')
            sys.stdout.flush()
            k += 1
    sys.stdout.write(f'{N}, пожалуйста, выберите одного из этих персонажей.\n')
    sys.stdout.flush()
    k += 1
    sys.stdout.write('Когда сделаете выбор, введите номер персонажа: ')
    sys.stdout.flush()
    k += 1
    inp = int(input())
    while inp - 1 in chosen or inp >= 7 or inp <= 0:
        hp_str_ = "Вы не можете выбрать этого персонажа, попробуйте еще раз: "
        sys.stdout.write(hp_str_)
        sys.stdout.flush()
        k += 1
        inp = int(input())
    Players[Order[i]].character = inp
    Exist.append(inp)
    chosen.append(inp - 1)
    sys.stdout.write(f'Отлично, {N}, вы сделали свой выбор.\n')
    sys.stdout.flush()
    k += 1
    sys.stdout.write(f'Теперь вы {keys[inp - 1]}.\n')
    sys.stdout.flush()
    k += 1
    sys.stdout.write(f'{N}, {help_str}')
    sys.stdout.flush()
    k += 1
    ent = input()
    while (ent.endswith('\n')):
        help_str_ = 'пожалуйста, попробуйте снова: '
        sys.stdout.write(f'{Players[Order[i]].nick}, ' + help_str_)
        sys.stdout.flush()
        k += 1
        ent = input()
    for j in range(k):
        sys.stdout.write("\033[F\033[K")
sys.stdout.write("\033[F\033[K\033[F\033[K\033[F\033[K")

people_keys = list(basa.People.keys())
tools_keys = list(basa.People.keys())
places_keys = list(basa.People.keys())
all_keys = list(basa.All_cards.keys())

ANSWER_.append(random.choice(people_keys))
ANSWER_.append(random.choice(tools_keys))
ANSWER_.append(random.choice(places_keys))

for i in Players:
    i.answer = ANSWER_
for i in Players:
    i.exist = Exist
Remain_cards = []
for i in all_keys:
    if i not in ANSWER_:
        Remain_cards.append(i)
random.shuffle(Remain_cards)
cards = basa.Amount_of_cards[basa.AMOUNT_OF_PLAYERS]
for i in range(basa.AMOUNT_OF_PLAYERS):
    Players[i].set_of_cards = Remain_cards[(i)*cards:(i + 1)*cards].copy()
    print(Players[i].set_of_cards)
    for j in basa.All_cards:
        Players[i].cells[basa.All_cards[j], Players[i].character] = "white"
        if j not in Players[i].set_of_cards:
            Players[i].cells[basa.All_cards[j], Players[i].character] = "red"
        else:
            Players[i].cells[basa.All_cards[j], Players[i].character] = "green"
    for j in Players[i].set_of_cards:
        for k in Exist:
            if k != Players[i].character:
                Players[i].cells[basa.All_cards[j], k] = "green"

someone_right = False
while not someone_right:
    for i in range(0, basa.AMOUNT_OF_PLAYERS):
        i_i = Order[i]
        if Players[i_i].play:
            class_player.PasswordWindow(Players[i_i])
            if Players[i_i].suggest and Players[i_i].guess:
                someone_right = True
                break
            elif Players[i_i].suggest and not Players[i_i].guess:
                Players[i_i].play = False
            elif Players[i_i].question:
                should_answer = True
                for j in range(i + 1, i + basa.AMOUNT_OF_PLAYERS):
                    j_j = Order[j % basa.AMOUNT_OF_PLAYERS]
                    aop = basa.AMOUNT_OF_PLAYERS
                    if should_answer:
                        class_player.Password_window_Answer(
                            Players[j_j], Players[i_i].question_, Players[i_i])
                        sm = Players[j_j].character
                        if Players[i_i].given_card != '':
                            should_answer = False
                            num = basa.All_cards[Players[i_i].given_card]
                            Players[i_i].cells[num, sm] = "green"
                        else:
                            for k in Order:
                                if k != j % basa.AMOUNT_OF_PLAYERS:
                                    for el in Players[i_i].question_:
                                        num = basa.All_cards(el)
                                        Players[k].cells[num, sm] = "red"
