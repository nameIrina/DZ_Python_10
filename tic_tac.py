from tkinter import *
import random

root = Tk()
root.title('Крестики-Нолики')
root.geometry('350x350')

games = Canvas(root, width=400, height=400)
games.place(x=30, y=30)
condition = [None] * 9
win = None
combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


for i in range(0, 9):
    x = i // 3 * 100
    y = i % 3 * 100
    games.create_rectangle(x, y, x + 100, y + 100, 
                           width=3,
                           outline='gray',
                           fill='white',
                           activefill='gray')

def add_x(column, row):
    x = 10 + 100 * column
    y = 10 + 100 * row
    games.create_line(x, y, x + 80, y + 80, width=8, fill='green')
    games.create_line(x, y + 80, x + 80, y, width=8, fill='green')

def add_o(column, row):
    x = 10 + 100 * column
    y = 10 + 100 * row
    games.create_oval(x, y, x + 80, y + 80, width=8, outline='red')

def click(event):
    colum = event.x // 100
    row = event.y // 100
    index = colum + row * 3
    if condition[index] is None:
        condition[index] = 'x'
        add_x(colum, row)
        if winner():
            end_game()
        else:
            bot_move()
            if winner():
                end_game()  
def bot_move():
    empty_indexes = []
    for index, el in enumerate(condition):
        if el is None:
            empty_indexes.append(index)
        if empty_indexes:
            index = random.choice(empty_indexes)
            condition[index] = 'o'
            colum = index % 3
            row = index // 3
            add_o(colum, row)
def winner():
    global win
    variants = []
    for i in combinations:
        variants.append([condition[i[0]], condition[i[1]], condition[i[2]]])
    if ['x'] * 3 in variants:
        creat_win_line()
        win = 'Твоя ПОБЕДА!'
    elif ['o'] * 3 in variants:
        creat_win_line()
        win = 'БОТ Выиграл'
    elif None not in condition:
        win = 'По рукам'
    return win

def creat_win_line():
    for i in combinations:
        win_line = (condition[i[0]], condition[i[1]], condition[i[2]])
        if win_line.count('x') == 3 or win_line.count('o') == 3:
            index_start = i[0]
            index_end = i[2]
            games.create_line((index_start % 3) * 100 + 50, (index_start // 3) * 100 + 50,
                                (index_end % 3) * 100 + 50, (index_end // 3) * 100 + 50, width=10, fill='violet')
            games.update()
            break

def end_game():
    print(f'Игра окончена {win}')
games.bind('<Button-1>', click)
root.mainloop()