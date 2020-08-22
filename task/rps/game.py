import random
import math


class Game:
    def __init__(self):
        self.user_option = None
        self.compu_option = None
        self.user_name = None
        self.score = 0
        self.options = ['rock', 'paper', 'scissors']
        self.beats = None
        self.defeated_by = None

    def loose(self):
        print(f'Sorry, but the computer chose {self.compu_option}')

    def win(self):
        print(f'Well done. The computer chose {self.compu_option} and failed')

    def draw(self):
        print(f'There is a draw ({self.compu_option})')

    def game_outcome(self):
        if self.user_option == self.compu_option:
            self.draw()
            self.score += 50
        elif self.user_option in self.defeated_by:
            self.win()
            self.score += 100
        else:
            self.loose()

    def new_options(self):
        position = self.options.index(self.compu_option)
        after_lst = self.options[position:]
        before_lst = self.options[:position]
        final_lst = after_lst + before_lst
        if len(final_lst) % 2 == 0:
            half = len(final_lst) / 2
        elif len(final_lst) % 2 == 1:
            half = math.ceil(len(final_lst) / 2)
        self.defeated_by = final_lst[:half]
        self.beats = final_lst[half:]

    def name_and_score(self):
        self.user_name = input('Enter your name: ')
        print(f'Hello, {self.user_name}')
        file = open('rating.txt', 'r')
        for line in file:
            if self.user_name in line:
                self.score = int(line.split()[1])
                break
            else:
                self.score = 0
        file.close()

    def lst_options(self):
        lst = input().split(',')
        if len(lst) > 1:
            self.options = lst
        print("Okay, let's start")

    def play(self):
        self.name_and_score()
        self.lst_options()
        while True:
            self.user_option = input()
            self.compu_option = random.choice(self.options)  # It returns a random key
            self.new_options()
            if self.user_option == '!exit':
                print('Bye!')
                break
            elif self.user_option in self.options:
                self.game_outcome()
            elif self.user_option == '!rating':
                print(f'Your rating: {self.score}')
            else:
                print('Invalid input')


game = Game()
game.play()
