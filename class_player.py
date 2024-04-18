import table
import basa
import tkinter as tk
import random


class Player():
    def __init__(self, nick, password):
        self._nick = nick  # name of person
        self._password = password  # password
        self._character = 0  # name of character
        self.set_of_cards = []  # set of cards
        self.set_of_words = []  # set of cards
        self._play = True  # if can play
        self.cells = {}  # cels with color
        for i in range(1, 24):
            for j in range(1, 7):
                self.cells[i, j] = "grey"
        self.exist = []
        self.answer = []
        self.question_ = []
        self._question = False
        self._suggestion = False
        self._guessed = False
        self.given_card = ''
        self._place = 0  # where is the character
        self.dices = 0

    @property
    def password(self):
        return self._password

    @property
    def nick(self):
        return self._nick

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, number):
        self._character = number

    @property
    def play(self):
        return self._play

    @play.setter
    def play(self, bol):
        self._character = bol

    @property
    def guess(self):
        return self._guessed

    @guess.setter
    def guess(self, bol):
        self._guessed = bol

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, bol):
        self._question = bol

    @property
    def suggest(self):
        return self._suggestion

    @suggest.setter
    def suggest(self, bol):
        self._suggestion = bol

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, number):
        self._place = number


people = list(basa.People.keys())
tools = list(basa.Tools.keys())
places = list(basa.Places.keys())


class Choice(Player):
    def __init__(self, player):
        self._player = player
        self.master = tk.Tk()
        self.master.title("My App")
        self.master.geometry("550x200+350+700")
        self.people_ = tk.StringVar()
        self.tool_ = tk.StringVar()
        self.place_ = tk.StringVar()
        self.value = 0
        self.my_button = tk.Button(self.master, text="Roll the dices",
                                   command=self.on_button_click,
                                   font=("Arial", 14))
        self.my_button.pack()
        self.master.mainloop()

    def on_button_click(self):
        self.my_button.pack_forget()
        num1, num2 = random.randint(1, 6), random.randint(1, 6)
        tl = num1 + num2
        self.button_for_table = tk.Button(self.master, text='Table',
                                          font=("Arial", 14), command=self.Tab)
        self.button_for_table.pack()
        self.label_for_result = tk.Label(self.master,
                                         text=f'The dices rolled {num1} and ' +
                                         f'{num2}. In total: {tl}\n',
                                         font=("Arial", 14))
        self.label_for_result.pack()
        help_str = f'You are in the {self._player.place}\n'
        if self._player.place > 0 and self._player.place < 10:
            help_str = f'You are in the {basa.Places_[self._player.place]}\n'
        help_str += "Now, choose from these cells\n"
        self.label_for_cells = tk.Label(self.master, font=("Arial", 14),
                                        text=help_str)
        self.label_for_cells.pack()
        self.entry = tk.Entry(self.master, font=("Arial", 14))
        self.entry.pack()
        self.enter_button = tk.Button(self.master, text="Enter",
                                      font=("Arial", 14),
                                      command=self.on_enter_button_click)
        self.enter_button.pack()

    def on_enter_button_click(self):
        self._player.place = self.entry.get()
        self.label_for_result.pack_forget()
        self.label_for_cells.pack_forget()
        self.entry.pack_forget()
        self.enter_button.pack_forget()
        self.value = int(self.entry.get())
        if self.value > 0 and self.value < 10:
            self._player.question = True
            self._player.place = self.value
            self.task = tk.Label(self.master, text="Chose suspect and tool",
                                 font=("Arial", 14))
            self.task.pack()
            self.people = tk.OptionMenu(self.master, self.people_, *people)
            self.people.pack()
            self.tool = tk.OptionMenu(self.master, self.tool_, *tools)
            self.tool.pack()
            self.ask_button = tk.Button(self.master, text="Ask Question",
                                        command=self.on_ask_button_click,
                                        font=("Arial", 14))
            self.ask_button.pack()
        elif self.value == 0:
            self._player.place = 0
            self.task = tk.Label(self.master, text="Do you want to make a" +
                                 "suggestion?\n" + "Press 'YES', if you want" +
                                 '.\nPress "NO" and the turn passes to' +
                                 'the next player', font=("Arial", 14))
            self.task.pack()
            self.yes_button = tk.Button(self.master, text="YES",
                                        command=self.make_suggestion,
                                        font=("Arial", 14))
            self.yes_button.pack(side=tk.LEFT, padx=100)
            self.no_button = tk.Button(self.master, text="NO",
                                       command=self.next_player,
                                       font=("Arial", 14))
            self.no_button.pack(side=tk.RIGHT, padx=100)
        else:
            self._player.place = self.value
            self.label3 = tk.Label(self.master, text="You are not in the room"
                                   + "\nSo its next player's turn\n",
                                   font=("Arial", 14))
            self.label3.pack()
            self.button_next = tk.Button(self.master, text='Next player',
                                         font=("Arial", 14),
                                         command=self.next_player)
            self.button_next.pack()

    def make_suggestion(self):
        self.task.pack_forget()
        self.no_button.pack_forget()
        self.yes_button.pack_forget()
        self._player.suggest = True
        self.task = tk.Label(self.master, text="Chose suspect, tool and place",
                             font=("Arial", 14))
        self.task.pack()
        self.people = tk.OptionMenu(self.master, self.people_, *people)
        self.people.pack()
        self.tool = tk.OptionMenu(self.master, self.tool_, *tools)
        self.tool.pack()
        self.place = tk.OptionMenu(self.master, self.place_, *places)
        self.place.pack()
        self.ask_button = tk.Button(self.master, text="Ask Question",
                                    command=self.check_suggest,
                                    font=("Arial", 14))
        self.ask_button.pack()

    def check_suggest(self):
        self.people.pack_forget()
        self.tool.pack_forget()
        self.place.pack_forget()
        self.task.pack_forget()
        self.ask_button.pack_forget()
        print(self._player.answer)
        print(self.people_.get(), self.tool_.get(), self.place_.get())
        print(*self._player.answer)
        if (self.people_.get() == self._player.answer[0] and
           self.tool_.get() == self._player.answer[1] - 21 and
           self.place_.get() == self._player.answer[2] - 11):
            self._player.guess = True
            help_str = "Congrats, you are right!"
            self.result = tk.Label(self.master, text=help_str,
                                   font=("Arial", 14))
            self.result.pack()
        else:
            self._player.guess = False
            help_str = "Oh no! It seems like you made wrong suggestion!\n"
            help_str1 = "You lost your ability to ask questions"
            self.result = tk.Label(self.master, text=help_str + help_str1,
                                   font=("Arial", 14))
            self.result.pack()
        self._player.suggest = True

    def on_ask_button_click(self):
        self.label_sure = tk.Label(self.master, text="Are you sure?",
                                   font=("Arial", 14))
        self.label_sure.pack()
        self.yes_button = tk.Button(self.master, text="Yes",
                                    font=("Arial", 14),
                                    command=self.on_yes_button_click)
        self.yes_button.pack()

    def on_yes_button_click(self):
        self.label_sure.pack_forget()
        self.yes_button.pack_forget()
        self.people.pack_forget()
        self.tool.pack_forget()
        self.ask_button.pack_forget()
        self.task.pack_forget()
        self.label_question = tk.Label(self.master, text='You suggestion is:\n'
                                       + f'\n{self.people_.get()} commited a '
                                       + f'murder with {self.tool_.get()} in '
                                       + f'the {basa.Places_[self.value]}\n',
                                       font=("Arial", 14))
        self.label_question.pack()
        self._player.question_ = [self.people_.get(), self.tool_.get(),
                                  basa.Places_[self.value]]
        self.button_next = tk.Button(self.master, text='Get answer',
                                     font=("Arial", 14),
                                     command=self.next_player)
        self.button_next.pack()

    def next_player(self):
        self.master.destroy()

    def Tab(self):
        table.Table(self._player)


class PasswordWindow(Player):
    def __init__(self, player):
        self._player = player
        Nick = self._player.nick
        self.password_window = tk.Tk()
        self.password_window.title("Enter Password")
        self.password_window.config(bg="grey")
        password_frame = tk.Frame(self.password_window, bg="gray")
        password_label = tk.Label(password_frame,
                                  text=f'{Nick}, enter password!',
                                  font=("Arial", 16), bg="gray")
        password_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.try_label = tk.Label(password_frame, text="Try Again",
                                  font=("Arial", 16), fg="red", bg="gray")
        self.try_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.try_label.grid_remove()

        self.password_entry = tk.Entry(password_frame, show="*",
                                       font=("Arial", 14))
        self.password_entry.grid(row=5, column=0, padx=10, pady=10)
        self.password_entry.focus()

        password_button = tk.Button(password_frame, text="Enter",
                                    font=("Arial", 14),
                                    command=self.check_password)
        password_button.grid(row=5, column=1, padx=10, pady=10)

        password_frame.pack(side=tk.TOP)
        self.password_window.mainloop()

    def check_password(self):
        if self.password_entry.get() == self._player.password:
            self.password_window.destroy()
            Choice(self._player)

        else:
            self.try_label.grid()
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus()


class Answer(Player):
    def __init__(self, player_from, question, player_to):
        self._question = question
        self._pl_from = player_from
        self._pl_to = player_to
        self.com = set(self._question).intersection(
            set(self._pl_from.set_of_cards))
        self.com = list(self.com)
        self.master = tk.Tk()
        self.master.title("Enter Password")
        self.master.config(bg="grey")
        if len(self.com) == 0:
            self.label_var1 = tk.Label(self.master, text="You don't " +
                                       "have any of those cards",
                                       font=("Arial", 14))
            self.label_var1.pack()
            self.button_var1 = tk.Button(self.master, text="Next player",
                                         font=("Arial", 14),
                                         command=self.next_player1)
            self.button_var1.pack()
        elif len(self.com) == 1:
            help_str = f'You have only one card: {self.com[0]}'
            self.label_var2 = tk.Label(self.master, text=help_str,
                                       font=("Arial", 14))
            self.label_var2.pack()
            help_str = "Show this card"
            self.button_va2 = tk.Button(self.master, text=help_str,
                                        font=("Arial", 14),
                                        command=self.next_player2)
            self.button_va2.pack()
        elif len(self.com) == 2:
            help_str = f'You have two cards: {self.com[0], self.com[1]}'
            self.label_vari3 = tk.Label(self.master, text=help_str,
                                        font=("Arial", 14))
            self.label_vari3.pack()
            self.yes_button = tk.Button(self.master, text=f'{self.com[0]}',
                                        command=self.next_player2,
                                        font=("Arial", 14))
            self.yes_button.pack(side=tk.LEFT, padx=100)
            self.not_button = tk.Button(self.master, text=f'{self.com[1]}',
                                        command=self.next_player3,
                                        font=("Arial", 14))
            self.not_button.pack(side=tk.RIGHT, padx=100)
        else:
            str = 'You have three cards:'
            hel = f' {self.com[0]}, {self.com[1]}, {self.com[2]}'
            self.label_vari4 = tk.Label(self.master, text=str + hel,
                                        font=("Arial", 14))
            self.label_vari4.pack()
            self.yes_button = tk.Button(self.master, text=f'{self.com[0]}',
                                        command=self.next_player2,
                                        font=("Arial", 14))
            self.yes_button.pack(side=tk.LEFT, padx=50)
            self.som_button = tk.Button(self.master, text=f'{self.com[1]}',
                                        command=self.next_player3,
                                        font=("Arial", 14))
            self.som_button.pack(side=tk.LEFT, padx=100)
            self.not_button = tk.Button(self.master, text=f'{self.com[2]}',
                                        command=self.next_player4,
                                        font=("Arial", 14))
            self.not_button.pack(side=tk.RIGHT, padx=50)

    def next_player1(self):
        self.master.destroy()

    def next_player2(self):
        self.master.destroy()
        self._pl_to.given_card = self.com[0]

    def next_player3(self):
        self.master.destroy()
        self._pl_to.given_card = self.com[1]

    def next_player4(self):
        self.master.destroy()
        self._pl_to.given_card = self.com[2]


class Password_window_Answer(Player):
    def __init__(self, player_from, question, player_to):
        self._question = question
        self._player_from = player_from
        self._player_to = player_to
        Nick = self._player_from.nick
        self.password_window = tk.Tk()
        self.password_window.title("Enter Password")
        self.password_window.config(bg="grey")
        password_frame = tk.Frame(self.password_window, bg="gray")
        password_label = tk.Label(password_frame,
                                  text=f'{Nick}, enter password!',
                                  font=("Arial", 16), bg="gray")
        password_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.try_label = tk.Label(password_frame, text="Try Again",
                                  font=("Arial", 16), fg="red", bg="gray")
        self.try_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.try_label.grid_remove()

        self.password_entry = tk.Entry(password_frame, show="*",
                                       font=("Arial", 14))
        self.password_entry.grid(row=5, column=0, padx=10, pady=10)
        self.password_entry.focus()

        password_button = tk.Button(password_frame, text="Enter",
                                    font=("Arial", 14),
                                    command=self.check_password)
        password_button.grid(row=5, column=1, padx=10, pady=10)

        password_frame.pack(side=tk.TOP)
        self.password_window.mainloop()

    def check_password(self):
        if self.password_entry.get() == self._player_from.password:
            self.password_window.destroy()
            Answer(self._player_from, self._question, self._player_to)
            tk.mainloop()

        else:
            self.try_label.grid()
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus()
