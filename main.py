import tkinter
from tkinter import *
import settings
import util
import game_logic
import random

def play():
    min_value = 0
    max_value = 9
    play = random.randint(min_value, max_value)
    return play

def coba():
    jumlah_pemain = int(jumlah_pemain_var.get())
    main = 'y'
    turn = 3
    player_scores = [0 for i in range(jumlah_pemain)]
    for i in range(jumlah_pemain):
        while main == 'y' and turn > 0:           # TkInter tbl play
            game = [play() for d in range(3)]
            for a in range(3):
                if a == 2:
                    print(game[a])
                else:
                    print(game[a], end='')  # layar

            if game[0] == game[1] == game[2]:
                if game[0] == game[1] == game[2] == 7:
                    player_scores[i] += 25
                else:
                    player_scores[i] += 10
            elif game[0] == game[1] or game[0] == game[2] or game[1] == game[2]:
                player_scores[i] += 5
            else:
                player_scores[i] += 0
            main = input('Apakah anda ingin melanjutkan permainan ?(y/n): ')
            if main == 'y':
                turn -= 1

        main = 'y'
        turn = 5
        q = 0
        print(f'score = {player_scores[i]}')
    return player_scores[i]

root = Tk()
root.config(background='grey')
root.geometry(f'{settings.width}x{settings.height}')
root.title('Minesweeper')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=util.width_prcnt(100),
    height=util.height_prcnt(20)
)
top_frame.place(x=0, y=0)
left_frame = Frame(
    root,
    bg='black',
    width=util.width_prcnt(12.5),
    height=util.height_prcnt(80)
)
left_frame.place(x=0, y=util.height_prcnt(20))

main_frame = Frame(
    root,
    bg='black',
    width=util.width_prcnt(87.5),
    height=util.height_prcnt(80)
)
main_frame.place(x=util.width_prcnt(12.5),
                 y=util.height_prcnt(20)
                 )

jumlah_pemain_var = tkinter.StringVar(root)
jumlah_pemain_var.set("1")
jumlah_pemain_options = ["1", "2", "3"]
jumlah_pemain_dropdown = tkinter.OptionMenu(root, jumlah_pemain_var, *jumlah_pemain_options)
jumlah_pemain_dropdown.place(x=util.width_prcnt(0), y=util.height_prcnt(0))


coba_button = tkinter.Button(root, text="lanjut", command=coba)
coba_button.place(x=util.width_prcnt(90), y=util.height_prcnt(80))




giliran_label = tkinter.Label(root, text="giliran pemain:")
giliran_label.place(x=util.width_prcnt(60), y=util.height_prcnt(0))
root.mainloop()
